pipeline {
    agent any
    stages {
        stage('Test Selenium') {
            steps {
                script {
                    dir('/Users/MacBook/PycharmProjects/SeleniumJenkins') {
                        sh 'python3 First.py'
                    }
                }
            }
        }
    }
}