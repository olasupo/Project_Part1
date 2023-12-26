pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                // Checkout code from your GitHub repository
                git 'https://github.com/olasupo/Project_Part1.git'
            }
        }

        stage('Run Backend') {
            steps {
                // Run rest_app.py
                sh 'python rest_app.py'
            }
        }

        stage('Run Frontend') {
            steps {
                // Run web_app.py
                sh 'python web_app.py'
            }
        }

        stage('Run Backend Testing') {
            steps {
                // Run backend_testing.py
                sh 'python backend_testing.py'
            }
        }

        stage('Run Frontend Testing') {
            steps {
                // Run frontend_testing.py
                sh 'python frontend_testing.py'
            }
        }

        stage('Run Combined Testing') {
            steps {
                // Run combined_testing.py
                sh 'python combined_testing.py'
            }
        }

        stage('Clean Environment') {
            steps {
                // Run clean_environment.py
                sh 'python clean_environment.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline successfully executed!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

