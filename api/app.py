from flask import Flask, jsonify
from crypto_api import get_coin_data

app = Flask(__name__)

@app.route('/api/coins')
def coins():
    data = get_coin_data()
    return jsonify(data)

@app.route('/api/about')
def about():
    return {"message": "CryptEdu API for learning crypto"}

if __name__ == '__main__':
    app.run(debug=True)
