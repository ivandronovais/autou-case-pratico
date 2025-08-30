# app.py
from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

print("Carregando o modelo classificador...")
caminho_do_modelo = "api/src/trained_model"
classifier = pipeline("text-classification", model=caminho_do_modelo)
print("Modelo carregado!")

def gerar_resposta(categoria, texto_email):
    texto_email = texto_email.lower()
    if categoria == "Produtivo":
        if "ticket" in texto_email or "chamado" in texto_email or "suporte" in texto_email:
            return "Sua solicitação de suporte foi recebida e será analisada por nossa equipe."
        elif "reunião" in texto_email or "agenda" in texto_email:
            return "Presença confirmada. Obrigado!"
        else:
            return "Recebido. Sua solicitação será processada por nossa equipe em breve."
    elif categoria == "Improdutivo":
        if "obrigado" in texto_email or "agradecer" in texto_email or "grato" in texto_email:
            return "De nada! Ficamos felizes em ajudar."
        else:
            return "Obrigado pelo seu contato!"

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
    resposta = gerar_resposta(categoria, texto_email)

    return jsonify({
        "categoria": categoria,
        "confianca": f"{confianca:.2%}",
        "sugestao_resposta": resposta
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)