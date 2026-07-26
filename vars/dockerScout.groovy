def call(String imageName){
    sh """
    echo "\$DOCKER_PASSWORD" | docker login -u "\$DOCKER_USERNAME" --password-stdin
    docker scout cves ${imageName} 
    """
}

// Docker Scout is to Scan Images