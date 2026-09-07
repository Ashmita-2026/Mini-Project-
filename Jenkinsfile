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
                    docker rm -f health-check 2>/dev/null || true

                    docker run -d --name health-check \
                        -e APP_ENV=jenkins \
                        -e APP_VERSION=${BUILD_NUMBER} \
                        service-health-dashboard:${BUILD_NUMBER}

                    sleep 5

                    docker exec health-check python3 -c "import urllib.request; print(urllib.request.urlopen('http://localhost:5000/health').read().decode())"

                    docker rm -f health-check
                '''
            }
        }
    }

    post {
        always {
            sh 'docker rm -f health-check 2>/dev/null || true'
        }
    }
}