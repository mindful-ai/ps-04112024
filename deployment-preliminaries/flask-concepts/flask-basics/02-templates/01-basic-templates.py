from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # Connecting to a template (html file)
    return render_template('01-basic-template.html')

if __name__ == '__main__':
    app.run(debug=True)