pipeline {
    agent any

    tools {
        maven 'Maven 3.8.1'   // Nom configuré dans Jenkins > Manage Jenkins > Global Tool Configuration
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Checking out...'
                git url: 'https://github.com/abidenabik/syst_devops_besse.git', branch: 'sys_devops'
            }
        }

        stage('Build') {
            steps {
                echo '🔧 Building project...'
                sh 'mvn clean install -DskipTests'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running automated tests...'
                sh 'mvn test'
            }

            post {
                always {
                    junit '**/target/surefire-reports/*.xml'
                }
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying app...'
                sh 'docker build -t simple-api .'
                sh 'docker run -d -p 8080:8080 simple-api'
            }
        }
    }

    post {
        always {
            echo '📌 Pipeline finished.'
        }
        success {
            echo '✅ All stages passed.'
        }
        failure {
            echo '❌ A stage failed.'
        }
    }
}
