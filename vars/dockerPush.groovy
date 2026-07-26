def call(String imageName, String dockerHubRepo) {

    withCredentials([
        usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USERNAME',
            passwordVariable: 'DOCKER_PASSWORD'
        )
    ]) {

        sh """
            echo "\$DOCKER_PASSWORD" | docker login \
                -u "\$DOCKER_USERNAME" \
                --password-stdin

            docker tag ${imageName} \$DOCKER_USERNAME/${dockerHubRepo}:latest

            docker push \$DOCKER_USERNAME/${dockerHubRepo}:latest

            docker logout
        """
    }
}