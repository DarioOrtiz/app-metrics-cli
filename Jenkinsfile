pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        DOCKER_IMAGE = "fastapi_app:latest"
        DOCKER_CONTAINER = "fastapi_app"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DarioOrtiz/app-metrics-cli.git'
            }
        }

        stage('Build Docker API') {
            steps {
                echo 'Construyendo imagen Docker de la API...'
                sh "docker build -t ${DOCKER_IMAGE} ./api"
            }
        }

        stage('Start API Container') {
            steps {
                echo 'Levantando contenedor Docker de la API...'
                sh "docker run -d -p 8000:8000 --name ${DOCKER_CONTAINER} ${DOCKER_IMAGE}"
                sh "sleep 5"
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Creando entorno virtual y instalando dependencias...'
                sh "python3 -m venv ${VENV_DIR}"
                sh "source ${VENV_DIR}/bin/activate && pip install --upgrade pip"
                sh "source ${VENV_DIR}/bin/activate && pip install -r requirements.txt"
                sh "source ${VENV_DIR}/bin/activate && pip install pytest requests"
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Ejecutando tests...'
                sh """
                    source ${VENV_DIR}/bin/activate
                    pytest ./tests/
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminado, limpiando contenedores...'
            sh "docker stop ${DOCKER_CONTAINER} || true"
            sh "docker rm ${DOCKER_CONTAINER} || true"
        }
        success {
            echo 'Build y tests completados correctamente.'
        }
        failure {
            echo 'Algo falló en el build o tests.'
        }
    }
}