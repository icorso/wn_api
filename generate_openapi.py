import os
import ssl
import subprocess
import urllib.request

if not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
    ssl._create_default_https_context = ssl._create_unverified_context

swagger_client_url = 'https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.25/'
swagger_client_name = 'swagger-codegen-cli-3.0.25.jar'
gds_args = '--use-getter-setter=new --no-dates --no-versions -f -o'
gds_template = '%s --user-methods=rest_user_methods --export="etree literal" %s %s %s'

scheme_name = 'openapi.yaml'
rest_scheme_url = 'https://vagrant.wntps.com/merchant/api/v1/docs/openapi.yaml'
boarding_scheme_url = 'https://vagrant.wntps.com/merchant/api/v2/boarding/openapi.yaml'
rest2_args = ["java", "-Dmodels -DmodelDocs=false -DmodelTests=false", "-jar", swagger_client_name,
              "generate", "-i", "rest_v2_" + scheme_name, "-l",  "python", "-o", "rest21", "--model-package=models"]
boarding2_args = ["java", "-Dmodels -DmodelDocs=false -DmodelTests=false", "-jar", swagger_client_name,
                  "generate", "-i", "boarding_v2_" + scheme_name, "-l", "python", "-o", "boarding21", "--model-package=models"]


if os.path.isfile(swagger_client_name):
    print('Swagger client exits, downloading skipped')
else:
    print('Swagger client doesn\'t exit, downloading now ... ' + swagger_client_url + swagger_client_name)
    with urllib.request.urlopen(swagger_client_url + swagger_client_name) \
            as response, open(swagger_client_name, 'wb') as out_file:
        data = response.read()
        out_file.write(data)

urllib.request.urlretrieve(rest_scheme_url, "rest_v2_" + scheme_name)
urllib.request.urlretrieve(boarding_scheme_url, "boarding_v2_" + scheme_name)

subprocess.Popen(rest2_args, stdout=subprocess.PIPE)
subprocess.Popen(boarding2_args, stdout=subprocess.PIPE)
