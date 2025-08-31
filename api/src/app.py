from flask import Flask, request, jsonify, render_template
from utils.read_files import ler_arquivo_pdf, ler_arquivo_txt
from werkzeug.utils import secure_filename

from transformers import pipeline
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

print("Carregando o modelo classificador...")
caminho_do_modelo = "api/src/trained_model"
classifier = pipeline("text-classification", model=caminho_do_modelo)
print("Modelo carregado!")

def arquivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf'}

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

@app.route('/upload', methods=['POST'])
def classificar_arquivo():
    if 'email_file' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    arquivo = request.files['email_file']

    if arquivo.filename == '':
        return jsonify({"error": "Nenhum arquivo selecionado"}), 400

    if arquivo and arquivo_permitido(arquivo.filename):
        nome_seguro = secure_filename(arquivo.filename)
        caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], nome_seguro)
        arquivo.save(caminho_arquivo)

        texto_extraido = ""
        if nome_seguro.lower().endswith('.txt'):
            texto_extraido = ler_arquivo_txt(caminho_arquivo)
        elif nome_seguro.lower().endswith('.pdf'):
            texto_extraido = ler_arquivo_pdf(caminho_arquivo)
        
        os.remove(caminho_arquivo)

        previsao = classifier(texto_extraido)[0]
        categoria = "Produtivo" if previsao['label'] == 'LABEL_1' else "Improdutivo"
        confianca = previsao['score']
        resposta = gerar_resposta(categoria, texto_extraido)

        return jsonify({
            "categoria": categoria,
            "confianca": f"{confianca:.2%}",
            "sugestao_resposta": resposta
        })

    return jsonify({"error": "Tipo de arquivo não permitido"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)