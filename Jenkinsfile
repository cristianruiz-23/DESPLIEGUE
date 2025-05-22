pipeline {
    agent any

    environment {
        REMOTE_HOST = "ruiz@172.18.187.111"
        PROJECT_PATH = "/home/ruiz/AplicativoOptativa/mi_app"
    }

    stages {
        stage('Clonar proyecto') {
            steps {
                git 'https://github.com/JorgeAAV-Official/AplicativoOptativa.git'
            }
        }

        stage('Desplegar en servidor remoto') {
            steps {
                sshagent(credentials: ['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']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no $REMOTE_HOST '
                            cd $PROJECT_PATH &&
                            git pull &&
                            docker-compose down &&
                            docker-compose up -d --build
                        '
                    '''
                }
            }
        }
    }
}
