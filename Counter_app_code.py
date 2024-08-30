from flask import Flask , render_template_string

db = {'number': 0}



app = Flask(__name__)

Amit_HTML = '''

<link rel="stylesheet" href="./static/counter_styles.css">
<span>{{number}}</span>

<div>
<form action='/increment'>
<button>+</button>
</form>

<form action='/decrement'>
<button>-</button>
</form>
</div>
'''
@app.route('/')
def home():
  return render_template_string(Amit_HTML , number = db['number'])

@app.route('/increment')
def increment():
  db['number'] += 1
  print(db['number'])
  return render_template_string(Amit_HTML , number = db['number'])

@app.route('/decrement')
def decrement():
  db['number'] -= 1
  print(db['number'])
  return render_template_string(Amit_HTML , number = db['number'])

app.run(host='0.0.0.0', port=81)