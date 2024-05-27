from flask import Flask, jsonify
from pop_sc import PopulacaoSC

app = Flask(__name__)

@app.route('/ibge', methods=['GET'])
def get_dados():
    dados = PopulacaoSC.main()
    return jsonify(dados)

if __name__ == '__main__':
    app.run(debug=True)
