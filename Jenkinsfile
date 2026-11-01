
pipeline {
    agent any

    environment {
        PATH = "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/opt/homebrew/opt/sonar-scanner/bin"
        IMAGE_NAME = "dvp-week12-cicd"
        CONTAINER_NAME = "dvp-week12-app"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Test Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/pip install coverage
                '''
            }
        }

        stage('Unit Tests') {
            steps {
                sh '''
                    .venv/bin/coverage run -m unittest -v test_app.py
                    .venv/bin/coverage xml
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        /opt/homebrew/opt/sonar-scanner/bin/sonar-scanner \
                          -Dsonar.host.url=http://localhost:9000
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        // Docker build, push and deployment stages will be added next.
    }
}