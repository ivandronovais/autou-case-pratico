from PyPDF2 import PdfReader

caminho_do_arquivo = "exemplo.txt"
def ler_arquivo_txt(caminho_do_arquivo):
    try:
        with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"

def ler_arquivo_pdf(caminho_do_arquivo):
    try:
        conteudo_total = ""
        with open(caminho_do_arquivo, 'rb') as arquivo:
            leitor_pdf = PdfReader(arquivo)
            for pagina in leitor_pdf.pages:
                conteudo_total += pagina.extract_text() or ""
        return conteudo_total
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"