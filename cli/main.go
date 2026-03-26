package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	resp, err := http.Get("http://localhost:8000/apps/")
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	var apps []map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&apps)

	fmt.Println("Lista de aplicaciones:")
	for _, app := range apps {
		fmt.Printf("ID: %v, Name: %v, Version: %v, Status: %v\n",
			app["id"], app["name"], app["version"], app["status"])
	}
}