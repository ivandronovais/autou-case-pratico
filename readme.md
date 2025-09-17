# Classificador de Emails com IA 📧✨

![Status do Projeto](https://img.shields.io/badge/status-concluído-green)

## 📝 Descrição

Este projeto é uma aplicação web desenvolvida como parte de um desafio técnico. A aplicação utiliza inteligência artificial para analisar o conteúdo de emails, classificando-os em duas categorias predefinidas:
 - **Produtivo**: emails que exigem uma ação ou resposta específica, como solicitações de suporte técnico, atualização sobre casos em aberto ou dúvidas sobre o sistema
 - **Improdutivo**: emails que não necessitam de uma ação imediata, como mensagens de felicitações ou agradecimentos

Com base nisso, foi feito a escolha de um modelo de I.A que atendesse a **3 critérios** fundamentais:
- **Suporte ao idioma português:** Necessário pois os emails recebidos serão em português
- **Bom Desempenho:** O modelo deve ter um equilibrio entre possuir uma boa quantidade de parâmetros e realizar a classificação de forma rápida
- **Tamanho do arquivo:** O aquivo não deve ser muito pesado, pois enfrentará alguns problemas ao fazer o deploy

Com base nisso, foi utilizado o modelo pré-treinado **DistilBERT base multilingual (cased)**, disponível no HuggingFace. Após isso, os passos foram o seguintes:
- **Criação de um pequeno dataset com emails já classificados**: Dataset com emails rotulados como "produtivo" ou "improdutivo"
- **Treinamento:** O modelo possui um conhecimento geral do idioma, como regras gramaticais, contexto e nuances. Porém, para essa tarefa em específico, ele não foi treinado. 
    - **Fine-tuning** é o processo de pegar um modelo pré-treinado e continuar seu treinamento com um conjunto de dados menor e específico para uma nova tarefa, no caso, o dataset com os emails já classificados.
    - Durante o Fine-tuning, o modelo **ajusta** seus **pesos** para minimizar o erro na classificação dos seus exemplos. Ele aprende os padrões de palavras, frases e contextos necessários para a classificação.
- **O Resultado é um modelo especializado:** Após isso, o DistilBERT não é mais um modelo genérico. Ele se tornou um especialista em classificar emails como `Produtivo` ou `Improdutivo` baseados no nosso contexto! 

## 🚀 Link para a Aplicação

Você pode testar a aplicação online no seguinte link:

**Acesse a aplicação online aqui!** `https://autou-case-pratico.onrender.com/`

## 📸 Screenshot / GIF
![Video demonstração do classificador de emails](https://github.com/user-attachments/assets/d5db42fe-d8cd-48ed-bf62-296b9866c265)




## ✨ Funcionalidades

- **Classificação de Emails:** Categoriza o texto de um email como `Produtivo` ou `Improdutivo`.
- **Sugestão de Resposta:** Gera uma resposta automática contextual com base na classificação.
- **Múltiplas Formas de Entrada:** O usuário pode colar o texto do email diretamente em uma área de texto ou fazer o upload de arquivos `.txt` e `.pdf`.
- **Interface Web Simples:** Uma interface limpa e intuitiva para facilitar a interação do usuário.

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

* **Frontend:**
    * HTML5
    * CSS3
    * JavaScript (ES6+)

* **Backend:**
    * **Python 3.13**
    * **Flask:** Micro-framework web para a criação da API.
    * **PyPDF2:** Biblioteca para extração de texto de arquivos PDF.

* **Inteligência Artificial:**
    * **DistilBERT base multilingual (cased):** Modelo base utilizado para as tarefas de classificação de texto .

## ⚙️ Como Rodar o Projeto Localmente

Para executar este projeto na sua máquina local, siga os passos abaixo.

### Pré-requisitos

* Python 3.10 ou superior
* Git (para clonar o repositório)
### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/ivandronovais/autou-case-pratico.git
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd autou-case-pratico
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\activate

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências do projeto:**
  
    ```bash
    pip install -r requirements.txt
    ```

### Executando a Aplicação

1.  **Inicie o servidor Flask:**
    ```bash
    flask --app api/src/app.py run
    ```

2.  **Abra seu navegador** e acesse o seguinte endereço:
    ```
    http://127.0.0.1:5000/
    ```

Pronto! A aplicação estará rodando localmente na sua máquina.

## 👨‍💻 Autor

Desenvolvido por **Ivandro Novais**.

* **LinkedIn:** `https://www.linkedin.com/in/ivandronovais/`
* **GitHub:** `https://github.com/ivandronovais`

