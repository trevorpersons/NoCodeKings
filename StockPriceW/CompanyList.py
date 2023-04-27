import requests

# Define the API endpoint URL
url = "https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=eaf732d59fb77c92a95fb2bafd74f126"


# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the API returned a successful response (status code 200)
if response.status_code == 200:
    # Parse the JSON response and extract the data dictionary
    data = response.json()
    index = 12
    print(len(data))
    
    
    url1 = "https://financialmodelingprep.com/api/v3/quote/"+data[index]+",FB?apikey=eaf732d59fb77c92a95fb2bafd74f126"
    response1 = requests.get(url1)
    data1 = response1.json()
    print(data1)


    
    
    
else:
    # If the API returned an error response, print the status code and message
    print("Error: %d - %s" % (response.status_code, response.text))

    

