from flask import Flask
app = Flask(__name__)

# Root
@app.route('/')
def index():
    return '<h1>Student Information Center</h1>'

# Another Route
@app.route('/information')
def info():
    return '<h1>List of Enrolled Students</h1>'

# Dynamic Route
@app.route('/physics/<name>')
def puppy(name):
    # Page for an individual student
    return '<h1>This is a page for {}<h1>'.format(name)

if __name__ == '__main__':
    app.run()

    # Debug mode
    # app.run(debug=True)