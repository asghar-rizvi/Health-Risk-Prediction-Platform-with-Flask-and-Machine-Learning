const selectImage = document.querySelector('.select-button');
const inputFile = document.querySelector('#file');
const imgArea = document.querySelector('.img-container');
const container = document.querySelector('.container');
const resultDiv = document.querySelector('.result');

var resultContainer = document.querySelector('.result-cont p'); 
// Add event listener for image selection
selectImage.addEventListener('click', function () {
    inputFile.click();
});

inputFile.addEventListener('change', function () {
    const image = this.files[0];
    if (image.size < 2000000) {
        const reader = new FileReader();
        reader.onload = () => {
            const allImg = imgArea.querySelectorAll('img');
            allImg.forEach(item => item.remove());
            const imgUrl = reader.result;
            const img = document.createElement('img');
            img.src = imgUrl;
            imgArea.appendChild(img);
            imgArea.classList.add('active');
            imgArea.dataset.img = image.name;
        };
        reader.readAsDataURL(image);

        // Submit the image to Flask
        const formData = new FormData();
        formData.append('image', image);

        fetch('http://127.0.0.1:5000/api/predict_pneumonia', {
            method: 'POST',
            body: formData,
        })
			
            .then(response => response.json())
            .then(data => {
				setTimeout(() => {
					resultContainer.innerHTML = data.prediction;
				}, 500); 
				resultContainer.classList.remove('fade-out');
				resultContainer.classList.add('fade-in');
            })

            .catch(error => {
                console.error('Error:', error);
				resultContainer.innerHTML = 'An error occurred. Please try again.';
            });
    } else {
        alert("Image size more than 2MB");
    }
});

