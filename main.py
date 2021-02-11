from flask import Flask, request
from pprint import pprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	data = pprint.pformat(request.form)
 	return "<h1>Welcome to CodingX</h1>" + data