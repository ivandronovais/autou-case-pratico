# app.py
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

print("Carregando o modelo classificador...")
caminho_do_modelo = "api/src/results"
classifier = pipeline("text-classification", model=caminho_do_modelo)
print("Modelo carregado!")

def gerar_resposta(categoria):
    if categoria == "Produtivo":
        return "Recebido. Sua solicitação será processada por nossa equipe em breve."
    else:
        return "Obrigado pela sua mensagem!"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/classificar', methods=['POST'])
def classificar_email():
    dados = request.get_json()
    texto_email = dados.get('email_text', '')

    if not texto_email:
        return jsonify({"error": "Nenhum texto de email fornecido"}), 400

    previsao = classifier(texto_email)[0]
    categoria = "Produtivo" if previsao['label'] == 'LABEL_1' else "Improdutivo"
    confianca = previsao['score']
    resposta = gerar_resposta(categoria)

    return jsonify({
        "categoria": categoria,
        "confianca": f"{confianca:.2%}",
        "sugestao_resposta": resposta
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)