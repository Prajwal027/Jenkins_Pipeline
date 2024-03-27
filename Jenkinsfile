pipeline {
    agent { label 'linux' }  //Run on any available agent

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
                sh 'minikube start --driver=docker'
                // Deploy application to Kubernetes cluster
                sh 'kubectl apply -f intigration.yaml'
                
                // Wait for deployment to be ready
                sh 'kubectl wait --for=condition=available --timeout=300s deployment/flask-app-deployment'
                
                // Run integration tests against the deployed application
                sh 'python3 tests/uni_test.py'
                
                // Clean up the deployed resources
                sh 'kubectl delete -f intigration.yaml'
            }
        }
    }
}
