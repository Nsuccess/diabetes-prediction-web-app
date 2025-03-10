import numpy as np
import pickle
import streamlit as st

# Load the trained model (make sure the model path is correct)
loaded_model = pickle.load(open(r"C:/Users/NewUserName/Desktop/work/trained_model.sav", "rb"))  # Update the path accordingly

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
      
def main():
    # Giving the title
    st.title('Diabetes Prediction Web App')
    
    # Getting input from the user, handle empty input
    Pregnancies = st.text_input('Number Of Pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction Value')
    Age = st.text_input('Age of the person')
    
    # Code for prediction
    diagnosis = ''
    
    # Check if all inputs are provided
    if st.button('Diabetes Test Result'):
        # Convert inputs to float only if they are not empty
        try:
            input_data = [
                float(Pregnancies) if Pregnancies else 0,
                float(Glucose) if Glucose else 0,
                float(BloodPressure) if BloodPressure else 0,
                float(SkinThickness) if SkinThickness else 0,
                float(Insulin) if Insulin else 0,
                float(BMI) if BMI else 0,
                float(DiabetesPedigreeFunction) if DiabetesPedigreeFunction else 0,
                float(Age) if Age else 0
            ]
            
            diagnosis = diabetes_prediction(input_data)
        except ValueError:
            diagnosis = "Please enter valid values for all fields."
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()
