#!/bin/bash
wget https://github.com/Sayi/swagger-diff/releases/download/v1.2.2/swagger-diff.jar
# java swagger-diff.jar rest_v2_openapi_old.yaml rest_v2_openapi.yaml -output-mode=html
# -old
#      old api-doc location:Json file path or Http url
#  * -new
#      new api-doc location:Json file path or Http url
#    -v
#      swagger version:1.0 or 2.0
#      Default: 2.0
#    -output-mode
#      render mode: markdown or html
#      Default: markdown