from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'San Francisco',
    'salary': '$150,000',
  },
  {
    'id': 3,
    'title': 'Machine Learning Engineer',
    'location': 'Remote',
  }
]

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)
  
  
@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS, company_name="Jovian")

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
