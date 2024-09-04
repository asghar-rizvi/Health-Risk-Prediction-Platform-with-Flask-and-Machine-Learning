function onClickedPredictKidneyDisease(event) {
    event.preventDefault();

    var age = parseFloat(document.getElementById("age").value);
    var bp = parseFloat(document.getElementById("bp").value);
    var sg = parseFloat(document.getElementById("sg").value);
    var al = parseFloat(document.getElementById("al").value);
    var su = parseFloat(document.getElementById("su").value);
    var rbc = parseInt(document.getElementById("rbc").value);
    var pc = parseInt(document.getElementById("pc").value);
    var pcc = parseInt(document.getElementById("pcc").value);
    var ba = parseInt(document.getElementById("ba").value);
    var bgr = parseFloat(document.getElementById("bgr").value);
    var bu = parseFloat(document.getElementById("bu").value);
    var sc = parseFloat(document.getElementById("sc").value);
    var sod = parseFloat(document.getElementById("sod").value);
    var pot = parseFloat(document.getElementById("pot").value);
    var hemo = parseFloat(document.getElementById("hemo").value);
    var pcv = parseFloat(document.getElementById("pcv").value);
    var wc = parseFloat(document.getElementById("wc").value);
    var rc = parseFloat(document.getElementById("rc").value);
    var htn = parseInt(document.getElementById("htn").value);
    var dm = parseInt(document.getElementById("dm").value);
    var cad = parseInt(document.getElementById("cad").value);
    var appet = parseInt(document.getElementById("appet").value);
    var pe = parseInt(document.getElementById("pe").value);
    var ane = parseInt(document.getElementById("ane").value);

    var resultContainer = document.querySelector('.result-cont p'); 

    resultContainer.classList.remove('fade-in');
    resultContainer.classList.add('fade-out');

    var url = "http://127.0.0.1:5000/api/predict_kidney_disease"; 

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams({
            age: age,
            bp: bp,
            sg: sg,
            al: al,
            su: su,
            rbc: rbc,
            pc: pc,
            pcc: pcc,
            ba: ba,
            bgr: bgr,
            bu: bu,
            sc: sc,
            sod: sod,
            pot: pot,
            hemo: hemo,
            pcv: pcv,
            wc: wc,
            rc: rc,
            htn: htn,
            dm: dm,
            cad: cad,
            appet: appet,
            pe: pe,
            ane: ane
        }).toString()
    })
    .then(response => response.json()) 
    .then(data => {

        setTimeout(() => {
            if (data.prediction === 1) {
                resultContainer.innerHTML = "Kidney Disease Detected";
            } else if (data.prediction === 0) {
                resultContainer.innerHTML = "No Kidney Disease";
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

document.getElementById('predict').addEventListener('click', onClickedPredictKidneyDisease);
