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
                //yo
            // Run unit tests with python3 using unittest module
                    sh 'python3 tests/uni_test.py'  
                    sh 'python3 tests/uni_test_edit.py'
                    sh 'python3 tests/uni_test_delete.py'
                    dir('tests') { // Change directory to tests relative to the workspace root
                      sh 'ls'
                        }
                  }
             }

        // Static Code Analysis stage
        //stage('Static code Analysis') {
            //steps {
                //sh 'pylint flask_sql1.py tests/*.py'
            //}
        //}
        stage('build docker image') {
            steps {
                sh 'docker build -t demo1 .'
                sh 'docker tag demo1 prajwal027/demo1'
                sh 'docker push prajwal027/demo1'
            }
        }

        // Integration Test and Deployment
        stage('Integration Test And Deployment') {
            steps {
                //use this cmd if minikube is not started
                //sh 'minikube start --driver=docker'
                sh 'kubectl apply -f intigration.yaml'
                sh 'kubectl get pods'
                // Wait for deployment to be ready
                sh 'sleep 80'
                sh 'kubectl get pods'
                sh "kubectl exec flask-app1 -- bash -c 'echo \"Executing command in flask-app1\"; ls -l;pip install requests;python3 inti_test.py'"
                sh 'kubectl delete -f intigration.yaml'
            }
        }
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
