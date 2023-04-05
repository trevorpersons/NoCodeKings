import requests

# Define the API endpoint URL
url = "https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=d2b1cf9beb66264ece3054788678d1b4"

# Send a GET request to the API endpoint
response = requests.get(url)

# Check if the API returned a successful response (status code 200)
if response.status_code == 200:
    # Parse the JSON response and extract the data dictionary
    data = response.json()

    # Print the data dictionary and its keys
    print(type(data))
    
    
else:
    # If the API returned an error response, print the status code and message
    print("Error: %d - %s" % (response.status_code, response.text))

