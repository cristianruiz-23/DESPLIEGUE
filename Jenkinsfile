pipeline {
    agent { label 'Agent1' }  // Ejecuta el pipeline en el agente con etiqueta 'agent1'

    environment {
        REMOTE_HOST = "ruiz@172.18.187.111"
        PROJECT_PATH = "/home/ruiz/AplicativoOptativa/mi_app"
    }

    stages {
        stage('Clonar proyecto') {
            steps {
                git 'https://github.com/cristianruiz-23/DESPLIEGUE.git'
            }
        }

        stage('Desplegar en servidor remoto') {
            steps {
                sshagent(credentials: ['ruiz-ssh-key']) {
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
