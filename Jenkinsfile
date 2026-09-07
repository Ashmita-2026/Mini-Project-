pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh '''
                    python3 -m venv .jenkins-venv
                    .jenkins-venv/bin/pip install -r app/requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '.jenkins-venv/bin/pytest app/tests'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t service-health-dashboard:latest .'
            }
        }

        stage('Tag') {
            steps {
                sh 'docker tag service-health-dashboard:latest service-health-dashboard:${BUILD_NUMBER}'
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                    docker run -d --name health-check \
                        -p 5001:5000 \
                        -e APP_ENV=jenkins \
                        -e APP_VERSION=${BUILD_NUMBER} \
                        service-health-dashboard:${BUILD_NUMBER}

                    sleep 5

                    curl --fail http://localhost:5001/health

                    docker stop health-check
                    docker rm health-check
                '''
            }
        }
    }
}