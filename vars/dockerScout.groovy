def call(String imageName) {

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
        """

        def status = sh(
            script: "docker scout cves ${imageName}",
            returnStatus: true
        )

        echo "Docker Scout scan completed with exit code: ${status}"

        if (status != 0) {
            echo "⚠️ Docker Scout found issues, but the pipeline will continue."
        }
    }
}