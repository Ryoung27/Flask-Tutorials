#Import Flask
from flask import Flask

#Create an app function
app = Flask(__name__)

#Create a route for you app
@app.route("/")

#Define what this route does.
def hello():
    return "Hello World!"
#Run the app
if __name__ == "__main__":
    app.run()