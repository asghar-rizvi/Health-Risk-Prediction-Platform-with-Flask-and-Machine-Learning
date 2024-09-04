function onClickedPredictLiverDisease(event) {
    event.preventDefault(); 

    console.log("Predict Liver Disease button clicked");

    const resultContainer = document.querySelector('.result-cont p');

    var age = parseFloat(document.getElementById("age").value);
    var gender = document.getElementById("gender").value;
    var alamineAminotransferase = parseFloat(document.getElementById("alamine_aminotransferase").value);
    var aspartateAminotransferase = parseFloat(document.getElementById("aspartate_aminotransferase").value);
    var totalProteins = parseFloat(document.getElementById("total_proteins").value);
    var albumin = parseFloat(document.getElementById("albumin").value);
    var albuminAndGlobulinRatio = parseFloat(document.getElementById("albumin_and_globulin_ratio").value);

    resultContainer.classList.remove('fade-in');
    resultContainer.classList.add('fade-out');

    var url = "http://127.0.0.1:5000/api/predict_liver_disease";

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            Age: age,
            Gender: gender,
            Alamine_Aminotransferase: alamineAminotransferase,
            Aspartate_Aminotransferase: aspartateAminotransferase,
            Total_Protiens: totalProteins,
            Albumin: albumin,
            Albumin_and_Globulin_Ratio: albuminAndGlobulinRatio
        }).toString()
    })
    .then(response => response.json())
    .then(data => {

        setTimeout(() => {
         
            if (data.prediction === 1) {
                resultContainer.innerHTML = "Liver Disease Detected";
            } else if (data.prediction === 0) {
                resultContainer.innerHTML = "No Liver Disease";
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
            resultContainer.innerHTML = "<h2>Error: Unable to fetch prediction.</h2>";
            resultContainer.classList.remove('fade-out');
            resultContainer.classList.add('fade-in');
        }, 500); 
    });
}
document.getElementById('predict').addEventListener('click', onClickedPredictLiverDisease);
