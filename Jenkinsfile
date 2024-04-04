pipeline {
    agent { label 'linux' }

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
                sh 'python3 -m venv venv'  //Create virtual environment
                sh 'source venv/bin/activate'  // Activate virtual environment
                script {
                    // Install dependencies from requirements.txt
                    sh 'pip install -r requirements.txt'
                    
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
        //stage('Static code Analysis') {
            //steps {
                //sh 'pylint flask_sql1.py tests/*.py'
            //}
        //}

        //stage('build docker image') {
          //  steps {
            //    sh 'docker build -t python_flask1 .'
              //  anchore name: 'python_flask1'
            //}
        //}
        
        //Create Docker image stages
        stage('Integration Test') {
            steps {
                sh 'minikube start --driver=docker'
                sh 'kubectl delete pod flask-app'
                sh 'kubectl apply -f intigration.yaml'

                // Wait for deployment to be ready
                sh 'kubectl get deployment'
                sh 'kubectl get pods'
                sh 'sleep 50'
                //sh 'kubectl wait --for=condition=Running pod/flask-app --timeout=100s'
                sh 'kubectl get pods'

                // Get a list of pods with the appropriate label
               // sh 'kubectl get pods -l app=flask-app -o name'.split('\n').each { podName ->
                    sh "kubectl exec flask-app -- bash -c 'echo \"Executing command in flask-app\"; ls -l;python3 inti_test.py'"
                //}
                // Run integration tests against the deployed application
                sh 'python3 tests/uni_test.py'

                sh 'kubectl delete -f intigration.yaml'
            }
        }
        //stage ('Image Scan with Anchor'){
            //steps {
                //anchore name: 'python_flask1'
            //}
        //}
    }
    post {
        always {
            emailext (
                subject: "Pipeline Status: ${currentBuild.result}",
                body: """<html>
                            <body>
                                <p>Build Status: ${currentBuild.result}</p>
                                <p>Build Number: ${currentBuild.number}</p>
                                <p>check the <a href-"${env.Build_Url}">console output</a>.</p>
                            </body>
                        </html>""",
                to: "prajwalpm27@gmail.com",
                from: "demojenkins21@outlook.com",
                replyTo: "demojenkins21@outlook.com",
                mimeType: "text/html"
            )
        }
    }
}
