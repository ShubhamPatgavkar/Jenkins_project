def call(String imageName){
     sh "docker scout cves ${imageName}"
}

// Docker Scout is to Scan Images