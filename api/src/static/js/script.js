// js/script.js
document.addEventListener('DOMContentLoaded', () => {
    const emailForm = document.getElementById('email-form');
    const emailTextInput = document.getElementById('email-text');
    const analyzeBtn = document.getElementById('analyze-btn');
    
    const resultsContainer = document.getElementById('results-container');
    const statusMessage = document.getElementById('status-message');
    const resultContent = document.getElementById('result-content');
    const resultCategory = document.getElementById('result-category');
    const resultSuggestion = document.getElementById('result-suggestion');


    emailForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const emailText = emailTextInput.value;
        if (!emailText.trim()) {
            alert('Por favor, insira o texto de um email para analisar.');
            return;
        }

        analyzeBtn.disabled = true;
        statusMessage.textContent = 'Analisando... Por favor, aguarde.';
        resultsContainer.classList.remove('hidden');
        resultContent.classList.add('hidden');

        try {

            const response = await fetch('/classificar', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email_text: emailText }),
            });

            if (!response.ok) {
                throw new Error(`Erro no servidor: ${response.statusText}`);
            }

            const data = await response.json();


            statusMessage.textContent = '';
            resultCategory.textContent = data.categoria;
            
            resultSuggestion.textContent = data.sugestao_resposta; 
            
            resultContent.classList.remove('hidden');

        } catch (error) {
            statusMessage.textContent = `Erro: ${error.message}`;
            statusMessage.style.color = 'red';
        } finally {
            analyzeBtn.disabled = false;
        }
    });
});