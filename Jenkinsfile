pipeline {
    agent { label 'linux' }  // Run on any available agent

    stages {
        // Checkout stage
        stage('Checkout') {
            steps {
                git branch: 'master', 
                   url: 'https://github.com/Prajwal027/Jenkins_Pipeline.git'
            }
        }

        // Build stage
        stage('Build') {
            steps {
                sh 'python3 -m venv venv'  // Create virtual environment
                sh 'source venv/bin/activate'  // Activate virtual environment
                script {
                    // Install dependencies from requirements.txt
                    sh 'pip install -r requirements.txt'
                    //sh 'python3 flask_sql1.py'
                }
            }
        }

        // Test stage
        stage('Test') {
            steps {
            // Run unit tests with python3 using unittest module
                    sh 'python3 tests/uni_test.py'  
                    sh 'python3 tests/uni_test_edit.py'
                    sh 'python3 tests/uni_test_delete.py'
                    //sh 'python3 flask_sql1.py'
                  }
             }

        // Static Code Analysis stage
        stage('Static code Analysis') {
            steps {
                sh 'pylint flask_sql1.py tests/*.py'
            }
        }
        
        //Create Docker image stages
        stage('Integration Test') {
            steps {
                stage('Integration Test') {
                withCredentials([usernamePassword(credentialsId: 'jenkins-token', usernameVariable: 'JENKINS_USERNAME', passwordVariable: 'JENKINS_PASSWORD')]) {
    
                sh 'kubectl get pods --token $TOKEN'
                sh """
                kubectl apply -f intigration.yaml --token $TOKEN
                """

                //sh "kubectl apply -f intigration.yaml"
                // Deploy the application using the integration.yaml definition
                //sh 'kubectl apply -f intigration.yaml'

                // Run integration tests against the deployed application
                // (Replace with your actual test script)
                sh 'python3 tests/*.py'

                // Clean up the deployed resources
                sh 'kubectl delete -f integration.yaml'
                }
                }
            }
        }
    }
}
