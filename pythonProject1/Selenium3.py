from flask import Flask, request

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello():
    return "Hello, World!"

# Define a route for the /cars URL with GET and POST methods
@app.route('/cars', methods=["GET", "POST"])
def cars():
    if request.method == "GET":
        return "mazda, chevrolet, citroen, toyota"
    elif request.method == "POST":
        return "creating new car"

# Define a route for the /motors URL with GET and POST methods
@app.route('/motors', methods=["GET", "POST"])
def motors():
    if request.method == "GET":
        return "yamaha, kawasaki, honda, bmw"
    elif request.method == "POST":
        return "creating new motor"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)