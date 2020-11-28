from flask import Flask, render_template
app = Flask(__name__)
@app.route('/echo/<thing>/<place>')
def echo(thing, place):
		return render_template('flask2.html', thing=thing, place=place+' 2a ver')
app.run(port=9999, debug=True)