from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    name = 'Samanvita'
    data = [15, 'Female', '9th Grade']
    subj = {'phy':78, 'math':80, 'chem':65, 'computers':95}
    # Connecting to a template (html file)
    return render_template('02-template-variables.html', name=name, data=data, subj=subj)

@app.route('/information')
def info():
    return '<h1>Information about students!</h1>'

@app.route('/student/Harshit')
def puppy(name):
    # Page for an individual puppy.
    return '<h1>This is a page for {}<h1>'.format(name)



if __name__ == '__main__':
    app.run(debug=True)