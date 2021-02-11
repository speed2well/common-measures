from flask import Flask, request
# from pprint import pprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

	data = request.form
	data = repr(data)

	# data = 'request.data'

	# if request.method == "POST":
	# 	data = request.form.get("veryvar")
	# else:
	# 	data = request.form["veryvar"]

	return '''<html><h1>Form</h1>
		<form action="" method="post">
		<input name='veryvar' />
		<input name='veryvar111' />
		<button type="submit" class="btn btn-primary">Send</button>
		</form>
		''' + str(data) + '</html>'