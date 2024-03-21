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
        stage('Docker-build') {
            //when {
             //   expression { // Optional condition to trigger this stage
                    // Replace with your condition to enable, e.g., branch name check
               //     return env.BRANCH_NAME == 'integration'
                //}
            //}
            steps {
                // Build Docker image (assuming Dockerfile exists)
                sh 'docker build -t python-flask .'
                //sh 'docker kill integration-test'
                // Start a container for integration tests
                sh 'docker run -d --name integration-test2 python-flask'

                // Replace the following with your actual integration test commands
                // These commands should interact with the running container
                sh 'curl http://localhost:5000/'  // Example API call
                sh 'docker logs integration-test'  // Check container logs

                // Stop the container after tests
                sh 'docker stop integration-test'
                //sh 'docker rm integration-test'  // Remove container
            }
        }
    }
}
