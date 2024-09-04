# Health Risk Prediction Platform with Flask and Machine Learning

## Project Overview
This project is a full-stack web application that predicts potential health risks, including heart attack risk, kidney disease likelihood, liver disease predictions, and diabetes forecasting. The application combines advanced machine learning models with a sleek and responsive frontend, providing users with accurate health predictions based on their input data.

## Features
- **Home Page**: Introduction to the platform and its health prediction capabilities.
- **User Authentication**: Secure user registration and login using Flask and MySQL.
- **Health Prediction Pages**: Interactive forms for predicting heart attack risk, kidney disease, liver disease, and diabetes.
- **Profile Management**: Users can view and manage their profiles, securely storing their data.
- **High Accuracy Models**: Machine learning models trained on extensive datasets, achieving 98% accuracy.
- **Backend Integration**: Machine learning models are integrated into the Flask backend using Pickle for real-time predictions.

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask, Python
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Database**: MySQL
- **Model Serialization**: Pickle

## Installation Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/asghar-rizvi/Health-Risk-Prediction-Platform-with-Flask-and-Machine-Learning.git
2. **Navigate to the Project Directory**:
   ```bash
   cd Health-Risk-Prediction-Platform-with-Flask-and-Machine-Learning
3. **Install Required Dependencies: Ensure you have pip installed and use it to install the necessary packages**:
     pip install -r requirements.txt
4. **Set Up the MySQL Database**:
   Create a MySQL database and user.
  Update the config.py file with your database credentials.
5. **Migrate Database: Run the migration commands to set up the database tables**:
     flask db upgrade
6. **Run the Flask Application: Start the development server** :
     flask run
## Usage
#### User Registration: Register a new account to access health prediction features.
#### Login: Securely log in to access your profile and prediction tools.
#### Health Predictions: Use the interactive forms on the prediction pages to receive instant health risk assessments.

## Model Information
The platform employs four distinct machine learning models, each trained on health-related datasets. The models are evaluated for accuracy, with the top-performing models achieving up to 98% accuracy.

## Future Enhancements
1. Adding more health prediction models.
2. Implementing real-time data visualization and analytics.
3. Enhancing user interface for improved user experience.

## Contact Information
For any inquiries or support, please reach out to:
Asghar Qamber Rizvi
Email: asgharqamberrozvi@gmail.com
GitHub: asghar-rizvi

