/Users/dpadmin/deven/software/sonar-scanner-4.6.2.2472-macosx/bin/sonar-scanner \
  -Dsonar.projectKey=loan_dummy_app \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=188056923c014fdd7d007406af88dd4c5813c18c


#docker run --rm -e SONAR_HOST_URL="http://localhost:9000" -e SONAR_LOGIN="188056923c014fdd7d007406af88dd4c5813c18c" -v "/app:/app" sonarsource/sonar-scanner-cli


