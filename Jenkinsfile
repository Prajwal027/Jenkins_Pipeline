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
                    // run the python-flask file
                    //sh 'python3 flask_sql1.py'
                }
            }
        }

        // Test stage
        stage('Test') {
            steps {
                    //Change the directory
                    //dir('tests'){
            // Run unit tests with pytest
                    sh 'python3 tests/uni_test.py'  // Assuming your tests are in uni_test.py
                    //}
                  }
             }

    }
}
