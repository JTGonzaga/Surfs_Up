#import dependencies
from flask import Flask

# Create new Flask instance
app = Flask(__name__)
# Create Flase routes
@app.route('/')
# Create function for flask
def hello_world():
    return 'Hello world'
    