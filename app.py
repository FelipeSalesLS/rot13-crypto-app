from flask import Flask, render_template, request, jsonify
import codecs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criptografar', methods=['POST'])
def criptografar():
    data = request.get_json()
    mensagem = data.get('mensagem', '')
    
    if not mensagem:
        return jsonify({'erro': 'Por favor, digite uma mensagem'}), 400
    
    mensagem_criptografada = codecs.encode(mensagem, 'rot_13')
    return jsonify({'resultado': mensagem_criptografada})

@app.route('/descriptografar', methods=['POST'])
def descriptografar():
    data = request.get_json()
    mensagem = data.get('mensagem', '')
    
    if not mensagem:
        return jsonify({'erro': 'Por favor, cole uma mensagem criptografada'}), 400
    
    mensagem_descriptografada = codecs.encode(mensagem, 'rot_13')
    return jsonify({'resultado': mensagem_descriptografada})

if __name__ == '__main__':
    app.run(debug=True)
