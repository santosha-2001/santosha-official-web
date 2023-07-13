from flask import Flask, render_template, jsonify
JOBS=[
  {
    'id' :'1',
    'title':'Data Analyst',
     'location':'Bengaluru',
'salary':200000

  },
{
    'id':'2',
    'title':'Data Scientist',
     'location':'Chennai',
'salary':2500000

  },
  {
    'id':'3',
    'title':'Software Developer',
     'location':'Hydrabada',
'salary':1500000

  }
]
app = Flask(__name__)
@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)