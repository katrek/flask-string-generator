from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def pw_gen(n=12):
    return ''.join(random.choice('!@#$%^&*(' + string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(int(n)))

@app.route('/', methods=['GET', 'POST'])
def index():
    n = request.form.get('n') or '12'
    if int(n) < 8 or int(n) > 16:
        return 'This page does not exist', 404
    password = pw_gen(n)
    length_options = [str(x) for x in range(8, 17)]
    content = {'password' : password, 'n' : n, 'nums' : length_options}
    return render_template('index.html', **content)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
