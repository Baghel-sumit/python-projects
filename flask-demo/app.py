# Flask App Routing


from flask import Flask, render_template, request

# create a simple flask application

app = Flask(__name__)

@app.route("/", methods=["GET"])

def welcome():
  return "<h1>Welcome to the python world.</h1>"


@app.route("/index", methods=["GET"])

def indexPage():
  return "<h1>Welcome to the python index.</h1>"

# variable rule

@app.route("/success/<int:score>", methods=["GET"])

def successPage(score):
  return f"<h1>The person has passed and the score is: {score}</h1>"


@app.route("/failure/<int:score>", methods=["GET"])

def failurePage(score):
  return f"<h1>The person has failed and the score is: {score}</h1>"

@app.route('/form', methods=["GET", "POST"])

def form():
  if request.method == 'GET':
    return render_template('form.html')
  elif request.method == 'POST':
    return render_template('postForm.html')
  else:
    return render_template('invalid.html')

def form():
  if request.method == 'GET':
    return render_template('form.html')
  elif request.method == 'POST':
    return render_template('submit.html')
  else:
    return '<h1>Invalid page</h1>'

if __name__ == "__main__":
  app.run(debug=True)