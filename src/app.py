from flask import Flask, request, jsonify,render_template, redirect, url_for, flash, session
from models import kidney_util, liver_util,heart_util, diabetes_util, CNN
from data import make_database as database
import bcrypt
import re
import os

app = Flask(__name__,template_folder='../HTML',static_folder='../static')

app.secret_key = 'your_secret_key_here'

database.create_database()
database.create_table()

@app.route('/homepage')
def home():
    return render_template('index.html')



@app.route('/model')
def model_page():
    return render_template('model.html')



@app.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            if any(char.isdigit() for char in name):
                raise ValueError('Name should not contain numbers')

            if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                raise ValueError('Invalid email format. Email should contain exactly one "@" and end with ".com".')

            record = database.search_by_email(email)
            if record:
                raise ValueError('Email Already Taken')

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            database.insert_values(name, email, hashed_password)
            flash('Account Successfully Created', 'success')
            return redirect(url_for('sign_up'))
        except ValueError as e:
            flash(str(e), 'error')

    return render_template('signup.html')


@app.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            # Validate email format
            if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                raise ValueError('Invalid email format. Email should contain exactly one "@" and end with ".com".')

            # Check if email is registered
            record = database.search_by_email(email)
            if not record:
                flash('Email Not Registered', 'error')
                return redirect(url_for('sign_in'))

            if record and bcrypt.checkpw(password.encode('utf-8'), record[0][3].encode('utf-8')):
                session['user_id'] = record[0][0]
                session['email'] = record[0][2]
                return redirect(url_for('home'))
            else:
                flash('Login Failed', 'error')
                return redirect(url_for('sign_in'))

        except ValueError as e:
            flash(str(e), 'error')

    return render_template('signup.html')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')

@app.route('/profile',methods=['GET','POST'])
def profile_page():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        try:
            if any(char.isdigit() for char in name):
                raise ValueError('Name should not contain numbers')

            if not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
                raise ValueError('Invalid email format. Email should contain exactly one "@" and end with ".com".')
            if email == session['email']:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                database.update_record(session['user_id'], name, email, hashed_password)
                success = 1
                return render_template('profile.html', name=name, email=email, success=success)
            else:
                record = database.search_by_email(email)
                if record:
                    raise ValueError('Email Already Taken')

        except ValueError as e:
            flash(str(e), 'error')

    elif 'user_id' in session:
        user_id = session['user_id']
        record = database.search_by_user_id(user_id)
        if record:
            user_id, name, email, passwd = record  # Unpack the tuple correctly
            return render_template('profile.html',
                                   name=name,
                                   email=email)
    return redirect(url_for('profile_page'))  # Redirect to sign-in if user is not logged in

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("You have been logged out successfully.",'success')
    return redirect(url_for('sign_up'))


@app.route('/heart_predict')
def heart_predict_page():
    return render_template('heart_predict.html')

@app.route('/kidney')
def kidney_page():
    return render_template('kidney.html')

@app.route('/liver')
def liver_page():
    return render_template('liver.html')

@app.route('/diabetes')
def diabetes_page():
    return render_template('diabetes.html')
@app.route('/penumonia')
def penumonia_page():
    return render_template('pneominia.html')

@app.route('/signup')
def signup_page():
    return render_template('signup.html')


@app.route('/api/predict_kidney_disease', methods=['GET','POST'])
def predict():
    data = request.form
    prediction = kidney_util.predict_kidney_disease(
        float(data['age']),
        float(data['bp']),
        float(data['sg']),
        float(data['al']),
        float(data['su']),
        int(data['rbc']),
        int(data['pc']),
        int(data['pcc']),
        int(data['ba']),
        float(data['bgr']),
        float(data['bu']),
        float(data['sc']),
        float(data['sod']),
        float(data['pot']),
        float(data['hemo']),
        float(data['pcv']),
        float(data['wc']),
        float(data['rc']),
        int(data['htn']),
        int(data['dm']),
        int(data['cad']),
        int(data['appet']),
        int(data['pe']),
        int(data['ane'])
    )
    prediction_int = int(prediction[0])
    response = jsonify({'prediction': prediction_int})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/predict_liver_disease', methods=['GET','POST'])
def predict_liver_disease():
    data = request.form
    gender_mapping = {'Male': 1, 'Female': 0}  # Assuming Male = 1, Female = 0
    prediction = liver_util.predict_liver(
        Age=float(data['Age']),
        Gender=gender_mapping[data['Gender']],  # Convert gender to numerical format
        Alamine_Aminotransferase=float(data['Alamine_Aminotransferase']),
        Aspartate_Aminotransferase=float(data['Aspartate_Aminotransferase']),
        Total_Protiens=float(data['Total_Protiens']),
        Albumin=float(data['Albumin']),
        Albumin_and_Globulin_Ratio=float(data['Albumin_and_Globulin_Ratio'])
    )
    prediction_int = int(prediction[0])
    response = jsonify({'prediction': prediction_int})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow origin from your dev server
    return response

@app.route('/api/predict_heart_disease', methods=['GET', 'POST'])
def predict_heart_disease():
    data = request.form
    sex_mapping = {'Male': 1, 'Female': 0}
    prediction = heart_util.predict_heart(
        age=float(data['age']),
        sex=sex_mapping[data['sex']],  # Convert gender to numerical format
        cp=int(data['cp']),
        trestbps=float(data['trestbps']),
        chol=float(data['chol']),
        fbs=int(data['fbs']),
        restecg=int(data['restecg']),
        thalach=float(data['thalach']),
        slope=int(data['slope']),
        ca=int(data['ca']),
        thal=int(data['thal'])
    )
    prediction_int = int(prediction[0])
    print(prediction_int)
    response = jsonify({'prediction': prediction_int})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow CORS for your dev server
    print(response)
    return response


@app.route('/api/predict_pneumonia', methods=['POST'])
def predict_pneumonia():

    if 'image' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Define the directory and file path
    temp_dir = os.path.join(os.getcwd(), "images")
    os.makedirs(temp_dir, exist_ok=True)  # Create directory if it doesn't exist
    temp_path = os.path.join(temp_dir, image.filename)

    image.save(temp_path)

    try:
        result = CNN.predict_model(temp_path)

        # Clean up the temp file
        os.remove(temp_path)
        return jsonify({'prediction': result})

    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    kidney_util.load_data()
    liver_util.load_data()
    heart_util.load_data()
    diabetes_util.load_data()
    CNN.load_model_cnn()
    app.run(debug=True)