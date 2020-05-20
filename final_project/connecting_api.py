##Token Stuff needed to link to the API
consumer_ID = "91475-35c85f4e35ae67ce6c3b3e63"
request_token = "050ef980-d5be-feaa-4ea4-afb32c"
accesss_token ="70f96a8f-1ed4-1026-21db-92fe07"

##Requesting a Token (https://www.jamesfmackenzie.com/getting-started-with-the-pocket-developer-api/)
curl https://getpocket.com/v3/oauth/request --insecure -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"91475-35c85f4e35ae67ce6c3b3e63\",\"redirect_uri\":\"http://www.google.com\"}"

##STEP 3. VISIT THE POCKET WEBSITE TO AUTHORIZE YOUR APP
https://getpocket.com/auth/authorize?request_token=050ef980-d5be-feaa-4ea4-afb32c&redirect_uri=http://www.google.com


##STEP 4. CONVERT YOUR REQUEST TOKEN INTO A POCKET ACCESS TOKEN
curl https://getpocket.com/v3/oauth/authorize --insecure -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"91475-35c85f4e35ae67ce6c3b3e63\",\"code\":\"050ef980-d5be-feaa-4ea4-afb32c\"}"

##STEP 5. MAKE AUTHENTICATED REQUESTS AGAINST THE POCKET API
curl https://getpocket.com/v3/get --insecure -X POST -H "Content-Type: application/json" -H "X-Accept: application/json" -d "{\"consumer_key\":\"91475-35c85f4e35ae67ce6c3b3e63\", \"access_token\":\"70f96a8f-1ed4-1026-21db-92fe07\"}"