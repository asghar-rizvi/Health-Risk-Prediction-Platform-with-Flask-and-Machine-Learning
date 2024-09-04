document.getElementById('predict').addEventListener('click', function (event) {
    event.preventDefault(); 
    const resultContainer = document.querySelector('.result-cont p');

    resultContainer.classList.remove('fade-in');
    resultContainer.classList.add('fade-out');

    const gender = document.getElementById('gender').value;
    const age = document.getElementById('age').value;
    const hypertension = document.getElementById('hypertension').value;
    const heart_disease = document.getElementById('heart_disease').value;
    const bmi = document.getElementById('bmi').value;
    const HbA1c_level = document.getElementById('HbA1c_level').value;
    const blood_glucose_level = document.getElementById('blood_glucose_level').value;
    const smoking_history = document.getElementById('smoking_history').value;

    const data = new FormData();
    data.append('gender', gender);
    data.append('age', age);
    data.append('hypertension', hypertension);
    data.append('heart_disease', heart_disease);
    data.append('bmi', bmi);
    data.append('HbA1c_level', HbA1c_level);
    data.append('blood_glucose_level', blood_glucose_level);
    data.append('smoking_history', smoking_history);

    fetch('http://127.0.0.1:5000/api/predict_diabetes', {
        method: 'POST',
        body: data,
    })
    .then(response => response.json())
    .then(data => {
        setTimeout(() => {
            // Update the content
            if (data.prediction === 1) {
                resultContainer.innerHTML = "High Risk of Diabetes";
            } else if (data.prediction === 0) {
                resultContainer.innerHTML = "Low Risk of Diabetes";
            } else {
                resultContainer.innerHTML = "<h2>Error: Unexpected Result</h2>";
            }
            // Trigger the fade-in animation
            resultContainer.classList.remove('fade-out');
            resultContainer.classList.add('fade-in');
        }, 500);
    })
    .catch(error => {
        console.error('Error:', error);
        document.querySelector('.result-cont p').textContent = 'An error occurred. Please try again.';
    });
});
