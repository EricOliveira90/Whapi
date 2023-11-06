# Import the Flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the GET request
@app.route("/")
def hello_world():
    # Return a "Hello World" message
    return "Hello World"

# Run the app in debug mode
if __name__ == "__main__":
    app.run(debug=True)
