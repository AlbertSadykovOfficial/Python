from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/echo/')
def echo():
		kwargs = {}
		kwargs['thing'] = request.args.get('thing')
		kwargs['place'] = request.args.get('place')+' 2c ver'
		return render_template('flask2.html', **kwargs)
app.run(port=9999, debug=True)