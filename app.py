# Import the Flask and requests modules
from flask import Flask, request, make_response
import requests
import os

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the GET request
@app.route("/")
def hello_world():
    # Return a "Hello World" message
    return "Hello World"

# Define a route for the POST request
@app.route("/upload", methods=["POST"])
def upload_file():
    # Access request data
    request_data = request.data
    request_headers = request.headers
    request_args = request.args
    request_form = request.form
    request_files = request.files

    # Print request data for debugging
    print("Received request data:")
    print(f"Request method: {request.method}")
    print(f"Request URL: {request.url}")
    print(f"Request headers: {request_headers}")
    print(f"Request args: {request_args}")
    print(f"Request form data: {request_form}")
    print(f"Request body: {request_data}")
    print(f"Request files: {request_files}")

    uploaded_file = request_files['file']
    if uploaded_file:  # Check if a file was provided
        folder_path = 'audios'
        file_path = os.path.join(folder_path, uploaded_file.filename)  # Define the target file path
        uploaded_file.save(file_path)  # Save the uploaded file to the specified folder
        return 'File uploaded and saved successfully.'
    return 'No file provided in the request.'


    # Get the mp3 file from the request
    # file = request.files.get("audio")
    # Check if the file is valid
    # if file and file.filename.endswith(".mp3"):
    #     # Save the file to a local directory
    #     file.save("uploads/" + file.filename)
    #     # Return a "ok" message with HTTP status 200
    #      return make_response("ok", 200)
    # else:
    #     # Return a "bad request" message with HTTP status 400
    #     return make_response("bad request", 400)

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
