from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('06-home.html')

@app.route('/puppy/<name>')
def pup_name(name):
    return render_template('06-puppy.html',name=name)



if __name__ == '__main__':
    app.run(debug=True)
