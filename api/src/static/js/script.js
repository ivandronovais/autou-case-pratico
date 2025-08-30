// js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const emailForm = document.getElementById('email-form');
    const emailTextInput = document.getElementById('email-text');
    const emailFileInput = document.getElementById('email-file');
    const analyzeBtn = document.getElementById('analyze-btn');

    const resultsContainer = document.getElementById('results-container');
    const statusMessage = document.getElementById('status-message');
    const resultContent = document.getElementById('result-content');
    const resultCategory = document.getElementById('result-category');
    const resultSuggestion = document.getElementById('result-suggestion');


    emailForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const emailFile = emailFileInput.files[0];
        const emailText = emailTextInput.value;
        if (!emailText.trim() && !emailFile) {
            alert('Por favor, insira o texto de um email para analisar.');
            return;
        }

        analyzeBtn.disabled = true;
        statusMessage.textContent = 'Analisando... Por favor, aguarde.';
        resultsContainer.classList.remove('hidden');
        resultContent.classList.add('hidden');

        try {
            let response;
            if (emailFile) {
                // Se um arquivo foi selecionado, preparamos os dados de forma diferente
                const formData = new FormData();
                formData.append('email_file', emailFile);

                // E enviamos para a nova rota /upload
                response = await fetch('/upload', {
                    method: 'POST',
                    body: formData, // FormData não precisa de headers
                });

            } else {
                response = await fetch('/classificar', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email_text: emailText }),
                });
            }
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `Erro no servidor: ${response.statusText}`);
            }
            const data = await response.json();

            statusMessage.textContent = '';
            resultCategory.textContent = `${data.categoria} (${data.confianca})`;
            resultSuggestion.textContent = data.sugestao_resposta;

            resultContent.classList.remove('hidden');
        } catch (error) {
            statusMessage.textContent = `Erro: ${error.message}`;
            statusMessage.style.color = 'red';
        } finally {
            analyzeBtn.disabled = false;
        }

        // try {
        //     const response = await fetch('/classificar', {
        //         method: 'POST',
        //         headers: { 'Content-Type': 'application/json' },
        //         body: JSON.stringify({ email_text: emailText }),
        //     });

        //     if (!response.ok) {
        //         throw new Error(`Erro no servidor: ${response.statusText}`);
        //     }

        //     const data = await response.json();


        //     statusMessage.textContent = '';
        //     resultCategory.textContent = data.categoria;

        //     resultSuggestion.textContent = data.sugestao_resposta; 

        //     resultContent.classList.remove('hidden');

        // } catch (error) {
        //     statusMessage.textContent = `Erro: ${error.message}`;
        //     statusMessage.style.color = 'red';
        // } finally {
        //     analyzeBtn.disabled = false;
        // }
    });
});