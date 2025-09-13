pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Restart Flask app') {
            steps {
                sh 'sudo systemctl restart flask-app'
            }
        }
    }
}
