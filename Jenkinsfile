pipeline{ 
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    environment {
        registry = "almogchn/randomnum"
        registryCredential = 'docker_hub'
        dockerImage = ''
    }
    stages{
        stage('Cloning Git') {
            steps {
                script { 
                    properties([pipelineTriggers([pollSCM('30 * * * *')])])
                }
                git 'https://github.com/AlmogChn/randomnum.git'
            }
        }
        stage('run random app') {
            steps{
                script{
                    sh ' nohup python main.py &'
                }
            }
        }
        stage ('build image'){
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('push image') {
            steps {
                script {
                    docker.withRegistry('', registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
         stage('set version') {
            steps {
                sh "echo IMAGE_TAG=${BUILD_NUMBER} > .env"
            }
        }  
        stage ('docker compose'){
            steps{
                sh 'docker-compose up -d'
            }
        }
       stage('Deploy HELM chart'){
            steps{
                  sh 'helm install helm helm --set image.repository=almogchn/randomnum:${BUILD_NUMBER}'
            }
        } 
    }   
    post {
        always {
            sh "docker rmi $registry:$BUILD_NUMBER"
        }
    }
    
}
