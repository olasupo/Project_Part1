pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '5'))
    }

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/olasupo/Project_Part1.git'
            }
        }

        stage('Run rest_app.py (backend)') {
            steps {
                script {
                    sh 'nohup python3 rest_app.py &'
                }
            }
        }

        stage('Run web_app.py (frontend)') {
            steps {
                script {
                    sh 'nohup python3 web_app.py &'
                }
            }
        }

        stage('Run backend_testing.py') {
            steps {
                script {
                    sh 'python3 backend_testing.py'
                }
            }
        }

        stage('Run frontend_testing.py') {
            steps {
                script {
                    sh 'python3 frontend_testing.py'
                }
            }
        }

        stage('Run combined_testing.py') {
            steps {
                script {
                    sh 'python3 combined_testing.py'
                }
            }
        }

        stage('Run clean_environment.py') {
            steps {
                script {
                    sh 'python3 clean_environment.py'
                }
            }
        }
    }

}
