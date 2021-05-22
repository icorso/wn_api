SET wget=c:\Tools\wget\wget.exe
SET generateDS=c:\dev\envs\wnapi_env\Scripts\generateDS.exe

SET base_host=http://wn:8080
SET gateway=%base_host%/merchant/gateway.xsd
SET rest=%base_host%/merchant/terminal/application.wadl/xsd0.xsd
SET boarding=%base_host%/merchant/boarding/application.wadl/xsd0.xsd

SET gds_args=--export="etree literal" --use-getter-setter=new --no-dates --no-versions -f -o

%wget% --no-check-certificate %gateway% -O gateway.xsd
%wget% --no-check-certificate %rest% -O rest.xsd
%wget% --no-check-certificate %boarding% -O boarding.xsd

%generateDS% --user-methods=rest_user_methods %gds_args% rest.py rest.xsd
%generateDS% --user-methods=boarding_user_methods %gds_args% boarding.py boarding.xsd
%generateDS% --user-methods=gateway_user_methods  %gds_args% gateway.py gateway.xsd
