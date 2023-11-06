# Import the requests module
import requests

# Define the URL to send the request to
url = "http://127.0.0.1:5000/"

# Send a GET request to the URL and store the response object
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful
    print("The request was successful.")
    # Print the content of the response
    print(response.content)
else:
    # The request failed
    print("The request failed.")
    # Print the status code and the reason
    print(response.status_code, response.reason)
