from flask import Flask, request
from pprint import pprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	data = pprint.pformat(request.form)
 	return '''<html><h1>Form</h1>
 		<from>
 		<input name='veryvar' />
 		<button />
 		</form>
 		</html>''' + data