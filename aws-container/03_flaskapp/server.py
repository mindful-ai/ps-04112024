# Note we imported request!
from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('allinputs.html')

@app.route('/process', methods=["GET", "POST"])
def process():
    print(request.form)
    print(request.files['cert']) # File upload and save
    file = request.files['cert']
    print(file)
    file.save('downloads/cert.txt')
    return ('<h1>Thank you! {} </h1>'.format(str(request.form.get('fname'))))

@app.route('/download', methods=['GET', 'POST'])
def download():
    return send_file(r"pics/kailash.jpg")
    
if __name__ == '__main__':
    app.run()
