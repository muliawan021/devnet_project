from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Selamat Belajar DevNet v 1'

@app.route('/test')
def test():
    return 'ini halaman uji coba dengan menambahkan /test'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")