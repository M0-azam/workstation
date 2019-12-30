import requests

API_ENDPOINT = "http://142.93.214.20/OBD/obd.php"
  
myd = "{something:soemthing,wafesgr:wdaesrg,something:soemthing,wafesgr:wdaesrg,something:soemthing,wafesgr:wdaesrg,something:soemthing,wafesgr:wdaesrg}"
# data to be sent to api 
mydata = {'message':myd} 
  
# sending post request and saving response as response object
for i in range(0,100):
    r = requests.post(url = API_ENDPOINT, data = mydata) 
    pastebin_url = r.text 
    print("Response = "+pastebin_url) 
