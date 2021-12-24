from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('itemlist.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploaded', filename)

if __name__ == '__main__':
    app.run(debug=True)