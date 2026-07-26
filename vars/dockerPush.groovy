def call(String imageName, String dockerHubRepo) {
        sh """
            docker tag ${imageName} \$DOCKER_USERNAME/${dockerHubRepo}:latest

            docker push \$DOCKER_USERNAME/${dockerHubRepo}:latest

            docker logout
        """

}