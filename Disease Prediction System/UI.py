import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
st.set_page_config(
    page_title="Health Guardian",
    page_icon="🩺",
    layout="wide",
)







diabetes_model = pickle.load(open(
    'C:\\Users\\DELL\\Desktop\\Bar Coders\\Multiple-Disease-Prediction-ML\\diabetes_model.sav', 'rb'))

heart_disease_model =  pickle.load(open(
    'C:\\Users\\DELL\\Desktop\\Bar Coders\\Multiple-Disease-Prediction-ML\\heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(
    'C:\\Users\\DELL\\Desktop\\Bar Coders\\Multiple-Disease-Prediction-ML\\parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open(
    'C:\\Users\\DELL\\Desktop\\Bar Coders\\Multiple-Disease-Prediction-ML\\breast_cancer_model.sav', 'rb'))



#  sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Home','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction','Contact Specialists','About Us'],
                           icons=['house','activity', 'heart', 'person', '','phone','hospital'],
                           default_index=0)
    
if (selected == 'Home'):

    # page title
    st.title('HEALTH GUARDIAN')
    st.text('Our Disease Prediction System (DPS) leverages Machine learning on diverse medical data to provide personalized risk  \nassessments for various diseases, enabling early interventions.')
    st.image('./landing.jpg')



# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP RAP')

    with col2:
        PPQ = st.text_input('MDVP PPQ')

    with col3:
        DDP = st.text_input('Jitter DDP')

    with col4:
        Shimmer = st.text_input('MDVP Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer APQ5')

    with col3:
        APQ = st.text_input('MDVP APQ')

    with col4:
        DDA = st.text_input('Shimmer DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):

    # page title
    st.title('Breast Cancer Prediction using ML')

    # getting the input data from the user
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        radius_mean = st.text_input('Radius mean')

    with col2:
        texture_mean = st.text_input('Texture mean')

    with col3:
        perimeter_mean = st.text_input('Perimeter mean')

    with col4:
        area_mean = st.text_input('Area mean')

    with col5:
        smoothness_mean = st.text_input('Smoothness mean')

    with col6:
        compactness_mean = st.text_input('Compactness mean')

    with col1:
        concavity_mean = st.text_input('Concavity mean')

    with col2:
        concave_points_mean = st.text_input('Concave points mean')

    with col3:
        symmetry_mean = st.text_input('Symmetry mean')

    with col4:
        fractal_dimension_mean = st.text_input('Fractal dimension mean')

    with col5:
        radius_se = st.text_input('Radius se')

    with col6:
        texture_se = st.text_input('Texture se')

    with col1:
        perimeter_se = st.text_input('Perimeter se')

    with col2:
        area_se = st.text_input('Area se')

    with col3:
        smoothness_se = st.text_input('Smoothness se')

    with col4:
        compactness_se = st.text_input('Compactness se')

    with col5:
        concavity_se = st.text_input('Concavity se')

    with col6:
        concave_points_se = st.text_input('Concave points se')

    with col1:
        symmetry_se = st.text_input('Symmetry se')

    with col2:
        fractal_dimension_se = st.text_input('Fractal dimension se')

    with col3:
        radius_worst = st.text_input('Radius worst')

    with col4:
        texture_worst = st.text_input('Texture worst')

    with col5:
        perimeter_worst = st.text_input('Perimeter worst')

    with col6:
        area_worst = st.text_input('Area worst')

    with col1:
        smoothness_worst = st.text_input('Smoothness worst')

    with col2:
        compactness_worst = st.text_input('Compactness worst')

    with col3:
        concavity_worst = st.text_input('Concavity worst ')

    with col4:
        concave_points_worst = st.text_input('Concave points worst')

    with col5:
        symmetry_worst = st.text_input('Symmetry worst')

    with col6:
        fractal_dimension_worst = st.text_input('Fractal dimension worst')

    # code for Prediction
    breast_diagnosis = ''

    # creating a button for Prediction

    if st.button('Breast Cancer Test Result'):
        breast_prediction = breast_cancer_model.predict(
            [[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se, radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])

        if (breast_prediction[0] == 1):
            breast_diagnosis = 'The Breast cancer is Malignant'
        else:
            breast_diagnosis = 'The Breast Cancer is Benign'

    st.success(breast_diagnosis)


    
    

if (selected == 'Contact Specialists'):
    # Add a title to the home page
      st.title("Doctor's Information")
      col1, col2= st.columns([1, 2])
      with col1:
          st.image("doctor male.png", use_column_width=True)

      with col2:
          st.header("Doctor Name : Dr. Rajendiran N") 
          st.subheader("Diabetes Specialist Doctor")
          st.write("38 Yrs Experience")
          st.subheader("Contact Information")
          st.write("Email: dr.rajendra@gmail.com")
          st.write("Phone: +91 7345677221")
        
      
      
      
      st.write("   ")
      st.write("   ")
      
      with col1:
          st.image("doctor female.png", use_column_width=True)

      with col2:
          st.header("Doctor Name: Dr. Manjula Ranganathan. M")
          st.subheader("Breast Cancer Specialist Doctor")
          st.write("10 Yrs Experience")
          st.subheader("Contact Information")
          st.write("Email: manjula12@gmail.com")
          st.write("Phone: +91 8341573458")


if (selected == 'About Us'):
    st.subheader("Welcome to Health Guardian !!")
    st.subheader("Our Mission")
    st.write("At Health Guardian, our mission is to empower individuals to take control of their health and well-being. We believe that proactive healthcare can lead to longer, healthier lives. With this goal in mind, we've developed a cutting-edge disease prediction model using Python and Streamlit to provide you with a seamless and informative healthcare experience.")

# Team Section
    st.subheader("Our Team")
    st.write("Our dedicated team comprises a diverse set of professionals, including healthcare experts, data scientists, and software engineers. Together, we're committed to bridging the gap between healthcare and technology to create a brighter and healthier future.")

# Why Choose Health Guardian Section
    st.subheader("Why Choose Health Guardian")
    st.write("- *Precision*: Our disease prediction model leverages the latest advancements in machine learning to deliver precise and reliable health assessments.")
    st.write("- *User-Centric*: We've designed our platform with you in mind. Health Guardian is built on Streamlit, ensuring a user-friendly interface that makes healthcare accessible to all.")
    st.write("- *Privacy First*: Your data privacy is a priority for us. We adhere to strict data protection standards, ensuring that your information remains confidential and secure.")
    st.write("- *Innovation*: We continuously strive for improvement. Expect regular updates and enhancements as we stay at the forefront of healthcare technology.")

# How Health Guardian Works Section
    st.subheader("How Health Guardian Works")
    st.write("Health Guardian analyzes your health data to provide valuable insights into your well-being. By inputting relevant information, you gain insights into your risk for various medical conditions. It's your companion in early detection and proactive health management.")

# Get Started Section
    st.subheader("Get Started with Health Guardian")
    st.write("We invite you to explore Health Guardian and start your journey toward better health. Your well-being matters, and Health Guardian is here to guide and support you every step of the way.")

# Thank You Section
    st.write("Thank you for choosing Health Guardian as your healthcare partner.")
    