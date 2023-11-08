# Import the requests module
import requests

# Define the URL to send the request to
url = "http://127.0.0.1:5000/upload"

def hello_world():
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

def send_audio(file_path):
    # Create a dictionary to specify the file to be uploaded
    files = {'file': ('audio.mp3', open(file_path, 'rb'), 'audio/mpeg')}

    # Send the POST request with the MP3 file and additional data (if any)
    response = requests.post(url, files=files)

    # Check the response status and content
    if response.status_code == 200:
        print("POST request successful")
        print("Response content:")
        print(response.text)
    else:
        print("POST request failed with status code:", response.status_code)

send_audio("sample-3s.mp3")