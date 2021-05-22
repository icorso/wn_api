#!/bin/bash
python swagger_yaml_to_html.py < rest_v2_openapi.yaml > rest_v2_openapi.html
python swagger_yaml_to_html.py < boarding_v2_openapi.yaml > boarding_v2_openapi.html