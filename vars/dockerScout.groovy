def call(String imageName){

    withCredentials([
        usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USERNAME',
            passwordVariable: 'DOCKER_PASSWORD'
        )
    ])
    {
        sh """
            echo "\$DOCKER_PASSWORD" | docker login -u "\$DOCKER_USERNAME" --password-stdin
            docker scout cves ${imageName} 
        """
    }
}

// Docker Scout is to Scan Images