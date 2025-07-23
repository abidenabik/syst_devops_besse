


pipeline {
    agent any

  

    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Checking out...'
                git url: 'https://github.com/abidenabik/syst_devops_besse.git', branch: 'sys_devops'
            }
        }

        stage('Build') {
            steps {
                echo ' Building project...'
                sh 'mvn clean install -DskipTests'
            }
        }

        stage('Test') {
            steps {
                echo ' Running automated tests...'
                sh 'mvn test'
            }
            }
        
        stage('INtegraed Test') {
            steps {
                echo ' Building project...'
                sh 'mvn verify'
            }
        }
        

        stage('Deploy') {
            steps {
                echo '🚀 Deploying app...'
                sh 'docker build -t simple-api .'
                sh 'docker run -d  simple-api'
            }
        }
    }

    post {
        always {
            junit '**/target/surefire-reports/*.xml'
        }
        success {
            echo '✅ All stages passed.'
        }
        failure {
            echo '❌ A stage failed.'
        }
    }

}