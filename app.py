# Import the Flask and requests modules
from flask import Flask, request, make_response
import requests

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
    # Get the mp3 file from the request
    file = request.files.get("audio")
    # Check if the file is valid
    if file and file.filename.endswith(".mp3"):
        # Save the file to a local directory
        file.save("uploads/" + file.filename)
        # Return a "ok" message with HTTP status 200
        return make_response("ok", 200)
    else:
        # Return a "bad request" message with HTTP status 400
        return make_response("bad request", 400)

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
