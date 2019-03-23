pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Build') {
      steps {
        sh 'python --version'
      }
    }
    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'python main.py'
          }
        }
        stage('Test Fail') {
          steps {
            sh 'python fail.py'
          }
        }
      }
    }
    stage('Test-fail') {
      steps {
        sh 'python fail.py'
      }
    }
  }
}