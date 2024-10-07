pipeline {
    agent any
    // environment {
    //     GIT_CREDENTIALS_ID = 'b943825b-5659-4d27-9fdf-b19746a0bc16' //the ID of  Jenkins credentials
    // }
    stages {
        stage('Setup Python Virtual ENV') {
            steps {
                script {
                    dir('/root/frs_cicd') {

                        if (!fileExists('CICD_Docker_k8')) {
                            sh 'mkdir CICD_Docker_k8'                            
                        }
                                                                    
                    } 
                }              

            }
        }

        stage('checkout') {
            steps {
                script {
                    dir('/root/frs_cicd/CICD_Docker_k8') {
                       git branch: 'main', credentialsId: 'b943825b-5659-4d27-9fdf-b19746a0bc16', url: 'https://github.com/WencesKipsang/CICD_Docker.git' 
                    } 
                }
            }
        }

        
        stage('Build') {
            steps {
                echo "Building"
                script {
                    dir('/root/frs_cicd/CICD_Docker_k8') {
                        sh '''
                        docker compose build --no-cache                                              
                        '''
                        echo "docker images complete"
                        // docker compose up -d 
                    } 
                }
            }
        }
        
        stage('pushing image to docker') {
            steps {
                echo "Pushing"
                script {
                    dir('/root/frs_cicd/CICD_Docker_k8') {                       
                        
                        withCredentials([usernamePassword(credentialsId: '5af99eb7-b813-4c34-829c-19c33f8544c7', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                            sh '''
                            echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                            docker tag django_app:latest $DOCKER_USER/django_app1:latest
                            docker push $DOCKER_USER/django_app1:latest
                            '''
                        }                                                                                        
                        echo "docker pushing images complete"
                    } 
                }
            }
        }
        // stage('Push Docker Image') {
        //     environment {
        //         registry = "wences3160/django_app"
        //         registryCredential = '5af99eb7-b813-4c34-829c-19c33f8544c7' 
        //     }
        //     steps {
        //         script {
        //             // Log in to Docker Hub and push the Docker image
        //             docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
        //                 def appImage = docker.image("${registry}:latest")
        //                 appImage.push('latest')
        //             }
        //             echo "Docker image ${registry}:latest pushed successfully"
        //         }
        //     }
        // }

                    // def services = ['service1', 'service2', 'service3']
                    // for (service in services) {
                    //     def imageTag = "${DOCKER_REPO}/${service}:latest"
                    //     sh """
                    //         docker tag ${service}:latest ${imageTag}
                    //         docker push ${imageTag}
                    //     """

        stage('kubernetes') {
            steps {
                echo "Pushing"
                script {
                    dir('/root/frs_cicd/CICD_Docker_k8/kubernetes') { 
                        sh '''
                        kubectl apply -k deploy/django_app:latest
                            '''                                                                                                                
                        echo "docker pushing images complete"
                    } 
                }
            }
        }

    }
    post {
        success {
            echo "Build successful"
            // You can add additional steps here, like running tests or notifications.
        }

        failure {
            echo "Build failed"
        }
    }
}