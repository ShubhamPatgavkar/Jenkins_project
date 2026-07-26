def call(String imageName){
     sh "docker scout cves ${imageName}"
}
