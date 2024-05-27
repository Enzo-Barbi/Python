from flask import Flask, jsonify
from pesquisa import Pesquisa

app = Flask(__name__)

@app.route('/google', methods=['POST'])
def get_dados():
    dados = Pesquisa.main()
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
