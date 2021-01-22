pipeline {
    agent any
    stages {
		app_version = 'v1'
		docker_creds = credentials('docker-hub-credentials')
		//DATABASE_URI = credentials('database-uri')
	}
        stage('Build') {
            steps {
                // install docker and docker-compose
                // add jenkins to docker group
                // sudo su - jenkins, docker login
                // docker-compose build and push
                sh "docker-compose build && docker-compose push"
            
            }
        }
        stage('Deploy') {
            steps {
	    	sh "docker rm -f \$(docker ps -qa)"
                sh "docker-compose pull && docker-compose up -d"    
            }
        }
    }
}
