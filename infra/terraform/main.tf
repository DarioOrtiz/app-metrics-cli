terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 2.16.0"
    }
  }
}

provider "docker" {}

resource "docker_image" "fastapi_image" {
  name         = "fastapi_app:latest"
  build {
    context = "../../api"
  }
}

resource "docker_container" "fastapi_container" {
  name  = "fastapi_app"
  image = docker_image.fastapi_image.latest
  ports {
    internal = 8000
    external = 8000
  }
}