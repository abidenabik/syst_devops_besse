


pipeline {
    agent any

    tools {
        maven 'Maven 3.8.1'   // Nom configuré dans Jenkins > Manage Jenkins > Global Tool Configuration
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Clonage du dépôt...'
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
                echo '🚀 Déploiement Docker...'
                sh 'docker build -t abidenabik/syst_devops_besse .'
                sh 'docker run -d -p 8080:8080 abidenabik/syst_devops_besse'
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
