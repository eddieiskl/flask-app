pipeline {
    agent any

    environment {
        IMAGE_NAME = 'eddieiskl/flask-app'
        IMAGE_TAG = 'latest'
        REPO_URL = 'https://github.com/eddieiskl/flask-app.git'
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        LOCAL_SCORES_PATH = 'TheWoWCopy/Scores.txt'  // Relative path to Scores.txt within your repo
        CONTAINER_SCORES_PATH = '/app/Scores.txt'   // Path inside the Docker container
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: "${env.REPO_URL}"
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build("${env.IMAGE_NAME}:${env.IMAGE_TAG}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    def appContainer = docker.image("${env.IMAGE_NAME}:${env.IMAGE_TAG}").run(
                        "-p 8777:8777 -v ${env.WORKSPACE}/${env.LOCAL_SCORES_PATH}:${env.CONTAINER_SCORES_PATH} -d"
                    )
                    env.CONTAINER_ID = appContainer.id
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python e2e.py'
                    } catch (Exception e) {
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh "docker stop ${env.CONTAINER_ID} && docker rm ${env.CONTAINER_ID}"
                    
                    docker.withRegistry("https://${env.DOCKER_REGISTRY}", "${env.DOCKER_CREDENTIALS_ID}") {
                        docker.image("${env.IMAGE_NAME}:${env.IMAGE_TAG}").push("${env.IMAGE_TAG}")
                    }
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -af'
        }
    }
}
