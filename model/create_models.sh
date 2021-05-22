#!/bin/bash
generateDS='/home/mf/envs/wnapi2/bin/generateDS'
base_host='http://wn:8080'
gateway=$base_host'/merchant/gateway.xsd'
rest=$base_host'/merchant/terminal/application.wadl/xsd0.xsd'
boarding=$base_host'/merchant/boarding/application.wadl/xsd0.xsd'
gds_args='--use-getter-setter=new --no-dates --no-versions -f -o'

wget $gateway -O gateway.xsd
wget $rest -O rest.xsd
wget $boarding -O boarding.xsd

sed -i -e 's/name="50"/name="A50"/g' rest.xsd
sed -i -e 's/name="5F20"/name="A5F20"/g' rest.xsd
sed -i -e 's/name="9F06"/name="A9F06"/g' rest.xsd
sed -i -e 's/name="9F26"/name="A9F26"/g' rest.xsd

$generateDS --user-methods=rest_user_methods --export="etree literal" $gds_args rest.py rest.xsd
$generateDS --user-methods=boarding_user_methods --export="etree literal" $gds_args boarding.py boarding.xsd
$generateDS --user-methods=gateway_user_methods --export="etree literal"  $gds_args gateway.py gateway.xsd