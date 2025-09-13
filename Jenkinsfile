pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup venv & Install deps') {
      steps {
        sh '''
          set -e
          # create virtualenv inside workspace
          python3 -m venv venv
          . venv/bin/activate
          python -m pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Restart Flask service') {
      steps {
        // restart flask service (requires sudoers permission for jenkins)
        sh 'sudo /bin/systemctl restart flask-app'
      }
    }
  }

  post {
    success {
      echo 'Flask deployed ✔'
    }
    failure {
      echo 'Deployment failed ❌'
    }
  }
}
