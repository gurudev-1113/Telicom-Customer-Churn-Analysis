document.getElementById('churn-form').addEventListener('submit', async function(e) {
    e.preventDefault();

    const submitBtn = document.getElementById('submit-btn');
    const resultContainer = document.getElementById('result-container');
    const predictionResult = document.getElementById('prediction-result');
    const probabilityText = document.getElementById('probability-text');
    
    // Disable button and show loading state
    submitBtn.textContent = 'Predicting...';
    submitBtn.classList.add('loading');
    resultContainer.classList.add('hidden');

    // Collect form data
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());

    // Type casting
    const payload = {
        CreditScore: parseInt(data.CreditScore),
        Geography: data.Geography,
        Gender: data.Gender,
        Age: parseInt(data.Age),
        Tenure: parseInt(data.Tenure),
        Balance: parseFloat(data.Balance),
        NumOfProducts: parseInt(data.NumOfProducts),
        HasCrCard: parseInt(data.HasCrCard),
        IsActiveMember: parseInt(data.IsActiveMember),
        EstimatedSalary: parseFloat(data.EstimatedSalary),
        Complain: parseInt(data.Complain),
        SatisfactionScore: parseInt(data.SatisfactionScore),
        CardType: data.CardType,
        PointEarned: parseInt(data.PointEarned)
    };

    // Determine API URL based on environment (local vs production)
   // Determine API URL based on environment
const isLocal = 
    window.location.hostname === 'localhost' || 
    window.location.hostname === '127.0.0.1' || 
    window.location.protocol === 'file:';

const apiUrl = isLocal 
    ? 'http://127.0.0.1:8000/predict' 
    : '/predict';

    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        
        // Show result
        resultContainer.classList.remove('hidden');
        
        if (result.prediction === 1) {
            predictionResult.textContent = 'High Risk of Churn';
            predictionResult.className = 'churn-yes';
        } else {
            predictionResult.textContent = 'Low Risk of Churn';
            predictionResult.className = 'churn-no';
        }
        
        probabilityText.textContent = `Churn Probability: ${(result.probability * 100).toFixed(2)}%`;

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while making the prediction. Ensure the backend server is running.');
    } finally {
        submitBtn.textContent = 'Predict Churn';
        submitBtn.classList.remove('loading');
    }
});
