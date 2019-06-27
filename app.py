from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    def pw_gen(size=20, chars=string.ascii_letters + string.digits + string.punctuation):
        return ''.join(random.choice(chars) for _ in range(size))
    password = pw_gen()
    size = request.form.get('size') or '12'
    content = {'password' : password, 'size' : size}
    return render_template('index.html', **content)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
