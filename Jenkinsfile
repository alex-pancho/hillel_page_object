pipeline {
    agent any

    stages {
        stage('Clone source') {
            steps {
                git url: 'https://github.com/alex-pancho/hillel_page_object.git', branch: 'main'
            }
        }
        stage('Build and activate venv') {
            steps {
                sh 'python3 -m venv venv'
                sh '. $WORKSPACE/venv/bin/activate'
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r $WORKSPACE/requirements.txt'
            }
        }
        stage('Tests') {
            steps {
                sh 'python3 -m pytest --junitxml=$WORKSPACE/report.xml'
                junit 'report.xml'
            }
        }
    }
}
