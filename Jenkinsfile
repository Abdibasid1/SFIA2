pipeline {
    agent any
    environment {
		app_version = 'v1'
		docker_creds = credentials('docker-hub-credentials')
		//DATABASE_URI = credentials('database-uri')
	}
    stages{
        stage('Build') {
            steps {
                // install docker and docker-compose
                // add jenkins to docker group
                // sudo su - jenkins, docker login
                // docker-compose build and push
                sh "docker login -u ${docker_creds_USR} -p ${docker_creds_PSW}"
                sh "docker-compose build && docker-compose push"
            
            }
        }
        stage('Deploy') {
            steps {
	    	sh "docker rm -f \$(docker ps -qa)"
                sh "bash deploy.sh"    
            }
        }
    }
}
