def call(String imageName, String dockerHubRepo) {
        
         withCredentials([
        usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USERNAME',
        )
    ])
      {  
        sh """
            docker tag ${imageName} \$DOCKER_USERNAME/${dockerHubRepo}:latest

            docker push \$DOCKER_USERNAME/${dockerHubRepo}:latest

            docker logout
        """
      }
}