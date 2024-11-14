from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    name = 'Harshith'
    data = [15, 'Female', '9th Grade']
    subj = {'phy':78, 'math':80, 'chem':65, 'computers':95}
    # Connecting to a template (html file)
    return render_template('03-template-filters.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)