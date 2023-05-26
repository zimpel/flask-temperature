#56:29
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_zimpel():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
