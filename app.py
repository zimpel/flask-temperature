#56:29
from flask import Flask, request, render_template

app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'berlin',
    'gehalt': '120000'
  },
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'berlin',
    'gehalt': '120000'
  },
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'berlin',
    'gehalt': '120000'
  },
  {
    'id': 1,
    'title': 'data analyst',
    'location': 'berlin',
    'gehalt': '120000'
  },
]


@app.route("/")
def hello_zimpel():
  return render_template('home.html', jobs=JOBS, company_name='Zimpel')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
