from flask import Flask, render_template
import random
import string

app = Flask(__name__)

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

@app.route('/')
@app.route('/index')
def index():
    password = pw_gen()
    content = {'password' : password}
    return render_template('index.html', **content)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
