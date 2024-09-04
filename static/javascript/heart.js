document.getElementById('predict').addEventListener('click', function (event) {
    event.preventDefault(); 
    const resultContainer = document.querySelector('.result-cont p');

    resultContainer.classList.remove('fade-in');
    resultContainer.classList.add('fade-out');

    const age = document.getElementById('age').value;
    const sex = document.getElementById('sex').value;
    const chestpain = document.getElementById('chestpain').value;
    const bloodpressure = document.getElementById('bloodpressure').value;
    const cholestoral = document.getElementById('cholestoral').value;
    const bloodsugar = document.getElementById('bloodsugar').value;
    const electrocardiographic = document.getElementById('electrocardiographic').value;
    const heartrate = document.getElementById('heartrate').value;
    const slope = document.getElementById('slope').value;
    const ca = document.getElementById('ca').value;
    const thal = document.getElementById('thal').value;

    const data = new FormData();
    data.append('age', age);
    data.append('sex', sex);
    data.append('cp', chestpain);
    data.append('trestbps', bloodpressure);
    data.append('chol', cholestoral);
    data.append('fbs', bloodsugar);
    data.append('restecg', electrocardiographic);
    data.append('thalach', heartrate);
    data.append('slope', slope);
    data.append('ca', ca);
    data.append('thal', thal);

    fetch('http://127.0.0.1:5000/api/predict_heart_disease', {
        method: 'POST',
        body: data,
    })
    .then(response => response.json())
    .then(data => {
        
        setTimeout(() => {
            // Update the content
            if (data.prediction === 1) {
                resultContainer.innerHTML = "Chances Of Heart Attack";
            } else if (data.prediction === 0) {
                resultContainer.innerHTML = "No Chances Of Heart Attack";
            } else {
                resultContainer.innerHTML = "<h2>Error: Unexpected Result</h2>";
            }
            
            resultContainer.classList.remove('fade-out');
            resultContainer.classList.add('fade-in');
        }, 500); 
    })
    .catch(error => {
        console.error('Error:', error);
        
        resultContainer.classList.remove('fade-in');
        resultContainer.classList.add('fade-out');
        setTimeout(() => {
            resultContainer.textContent = 'An error occurred. Please try again.';
            resultContainer.classList.remove('fade-out');
            resultContainer.classList.add('fade-in');
        }, 500); 
    });
});
