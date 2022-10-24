import json
import requests

serverURL = "https://sandbox.api.visa.com/cofds-web/v1/datainfo

userid = "YOUR USER ID"
password = "YOUR PASSWORD"

body = {"requestMessageId":"6da6b8b024532a2e0eacb1af58581","messageDateTime":"2019-02-35 05:25:12.327",}
header1 = {"pANs":"4072208010000000","group":"STANDARD"}

check = requests.post(serverURL,
                 verify = ('DigiCertGlobalRootCA.pem'),
				  			 cert = ('cert.pem','private_key.pem'),
								 headers = header1,
								 check = (userid, password),
								 data = body,
								 )
print(check.json())
