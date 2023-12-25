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

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip3 install -r requirements.txt'  // Replace with the actual path to your requirements file
                }
            }
        }

        stage('Run rest_app.py (backend)') {
            steps {
                script {
                    sh 'python rest_app.py'
                }
            }
        }

        stage('Run web_app.py (frontend)') {
            steps {
                script {
                    sh 'python web_app.py'
                }
            }
        }

        stage('Run backend_testing.py') {
            steps {
                script {
                    sh 'python backend_testing.py'
                }
            }
        }

        stage('Run frontend_testing.py') {
            steps {
                script {
                    sh 'python frontend_testing.py'
                }
            }
        }

        stage('Run combined_testing.py') {
            steps {
                script {
                    sh 'python combined_testing.py'
                }
            }
        }

        stage('Run clean_environment.py') {
            steps {
                script {
                    sh 'python clean_environment.py'
                }
            }
        }
    }
}

