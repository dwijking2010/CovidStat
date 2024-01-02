#import flask library
from flask import Flask,render_template,request
#initialize flask
app = Flask(__name__)
#route your webpage
@app.route("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()
	return render_template("index.html",count = visitors_count)

# Render HTML with count variable
@app.route('/',methods = ['POST'])
#route your webpage
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()
	text = request.form['text']
	corona_data= 'https://covidstats-sdbd.onrender.com/?country='+text
	return render_template("index.html",image = corona_data, count = visitors_count)
    
    
	#complete the code
if __name__=="__main__":
	app.run()
#add code for executing flask