from flask import Flask, request, render_template

''' наименьшее общее кратное '''

app = Flask(__name__)

#a = int(input())
#b = int(input())

#assert a > 0
#assert b > 0

def overflow_exit(i):
	if i > pow(10, 10):
		print("error")
		exit(1)
		
def multiply_list(myList):
	# Multiply elements one by one
	result = 1
	for x in myList:
		 result = result * x 
	return result
 
def comult(n):
	rlist = []
	
	while n > 1:
		i=2
		while True:
			if n % i == 0:
				rlist.append(i)
				n = n / i
				break
			i += 1
			overflow_exit(i)       
	
	# assert len(rlist) != 0 , 'нет делителей - ваще'
 
	return rlist
		
def nod(aa, bb):
	l_aa = comult(aa)
	l_bb = comult(bb)
	
	common_elements = []

	while l_aa:
		el = l_aa.pop(0)
		
		if el in l_bb:
			common_elements.append(el)
			l_bb.remove(el)
	
	return multiply_list(common_elements)

def nok(max, min):
	rdiv = 1
	i = 1
	
	while rdiv != 0:
		deg = max * i # увеличиваем большее число
		
		rdiv = deg % min
		i += 1
		
		#print(deg)
		
		if i > pow(10, 10):
			return "error"
		
	return deg

################################################################################################

@app.route('/', methods=['GET', 'POST'])
def index():

	#data = request.form
	#data = repr(data)

	a, b = 0, 0
	nod_result, nok_result = 0, 0
	error = False

	if request.method == "POST":
		try:
			a = int(request.form.get("veryvar1"))
			b = int(request.form.get("veryvar2"))
		except ValueError as e:#AttributeError:
			error = '<b>Введите целые числа:</b> ' + str(e)

	if a > 0 and b > 0:
		nok_result = nok(a, b) if a > b else nok(b, a) # меняем порядок параметров функции
		nod_result = nod(a,b)

	return render_template("index.html",
		nok_result = nok_result,
		nod_result = nod_result, a = a, b = b, e = error)

	return '''<html><h1>"Least common multiple" and "Greatest common divisor"</h1>
		<form action="" method="post">
		<input name='veryvar1' value="{2}"/>
		<input name='veryvar2' value="{3}"/>
		<button type="submit" class="btn btn-primary">Calculate</button>
		</form>
		<hr /><br />
		<p>NOK: {1}</p>
		<p>NOD: {0}</p>
		</html>'''.format(nod_result, nok_result, a, b)