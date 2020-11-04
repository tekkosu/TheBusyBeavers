from ethicalEats import app

@app.route('/')
@app.route('/index')
def index():
	return "Ethical Eats"

