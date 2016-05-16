from flask import Flask, request, send_from_directory
import sqlite3
import emoji
app = Flask(__name__)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>/')
def index(path):
    return send_from_directory('pages', path)

@app.route('/gen/', defaults={'num': 3})
@app.route('/gen/<int:num>/')
def generate(num):
    return emoji.generate(num)

@app.route('/gen/s/', defaults={'char': 140})
@app.route('/gen/s/<int:char>/')
def generate_sentence(char):
    return emoji.generate_sentence(char)

@app.route('/gen/c/')
def get_count():
    con = sqlite3.connect('pasta.db')
    c = con.cursor()
    c.execute("SELECT COUNT(*) FROM counter")
    count = c.fetchone()[0]
    return str(count)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=22109, debug=True)

