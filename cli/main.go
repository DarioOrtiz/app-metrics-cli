package main

import (
    "bytes"
    "encoding/json"
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
)

type App struct {
    ID      int    `json:"id,omitempty"` 
    Name    string `json:"name"`
    Version string `json:"version"`
    Status  string `json:"status"`
}

func main() {
    if len(os.Args) < 2 {
        fmt.Println("Uso: go run main.go add-app <name> <version> <status> | list-apps | update-app <id> <name|version|status> | delete-app <id>")
        return
    }

    cmd := os.Args[1]

    switch cmd {
    case "add-app":
        if len(os.Args) != 5 {
            fmt.Println("Uso: add-app <name> <version> <status>")
            return
        }
        app := App{
            Name:    os.Args[2],
            Version: os.Args[3],
            Status:  os.Args[4],
        }
        addApp(app)

    case "list-apps":
        listApps()

    case "update-app":
        if len(os.Args) != 6 {
            fmt.Println("Uso: update-app <id> <name> <version> <status>")
            return
        }
        id := os.Args[2]
        app := App{
            Name:    os.Args[3],
            Version: os.Args[4],
            Status:  os.Args[5],
        }
        updateApp(id, app)

    case "delete-app":
        if len(os.Args) != 3 {
            fmt.Println("Uso: delete-app <id>")
            return
        }
        deleteApp(os.Args[2])

    default:
        fmt.Println("Comando desconocido:", cmd)
    }
}

func addApp(app App) {
    url := "http://127.0.0.1:8000/apps/"
    resp, err := doRequest("POST", url, app)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println(resp)
}

func listApps() {
    url := "http://127.0.0.1:8000/apps/"
    resp, err := http.Get(url)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    defer resp.Body.Close()
    body, _ := ioutil.ReadAll(resp.Body)

    var apps []App
    if err := json.Unmarshal(body, &apps); err != nil {
        fmt.Println("Error parseando respuesta:", err)
        return
    }

    fmt.Printf("%-5s %-20s %-10s %-10s\n", "ID", "Name", "Version", "Status")
    for _, app := range apps {
        fmt.Printf("%-5d %-20s %-10s %-10s\n", app.ID, app.Name, app.Version, app.Status)
    }
}

func updateApp(id string, app App) {
    url := fmt.Sprintf("http://127.0.0.1:8000/apps/%s", id)
    resp, err := doRequest("PUT", url, app)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println(resp)
}

func deleteApp(id string) {
    url := fmt.Sprintf("http://127.0.0.1:8000/apps/%s", id)
    resp, err := doRequest("DELETE", url, nil)
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println(resp)
}

func doRequest(method, url string, data interface{}) (string, error) {
    var req *http.Request
    var err error
    if data != nil {
        jsonData, _ := json.Marshal(data)
        req, err = http.NewRequest(method, url, bytes.NewBuffer(jsonData))
        req.Header.Set("Content-Type", "application/json")
    } else {
        req, err = http.NewRequest(method, url, nil)
    }
    if err != nil {
        return "", err
    }

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        return "", err
    }
    defer resp.Body.Close()
    body, _ := ioutil.ReadAll(resp.Body)
    return string(body), nil
}

func validateApp(app App) error {
    if app.Status != "active" && app.Status != "inactive" {
        return fmt.Errorf("status debe ser 'active' o 'inactive'")
    }
    matched, _ := regexp.MatchString(`^\d+\.\d+(\.\d+)?$`, app.Version)
    if !matched {
        return fmt.Errorf("version debe tener formato X.Y o X.Y.Z")
    }
    if app.Name == "" {
        return fmt.Errorf("name no puede estar vacío")
    }
    return nil
}