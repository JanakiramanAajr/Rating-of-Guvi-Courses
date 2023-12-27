# Imports
import streamlit as st
from PIL import Image
import pandas as pd
from streamlit_option_menu import option_menu
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pickle

# List of algorithm for Regression
reg_algo = {'DecisionTreeRegressor': r"D:\Guvi project\DecisionTreeRegressor.sav",
            'RandomForestRegressor': r"D:\Guvi project\RandomForestRegressor.sav",
            'AdaBoostRegressor': r"D:\Guvi project\AdaBoostRegressor.sav",
            'GradientBoostingRegressor': r"D:\Guvi project\GradientBoostingRegressor.sav",
            'ExtraTreesRegressor': r"D:\Guvi project\ExtraTreesRegressor.sav",
            'HistGradientBoostingRegressor': r"D:\Guvi project\HistGradientBoostingRegressor.sav",
            'SVR': r"D:\Guvi project\SVR.sav"}

# Page configuration
st.set_page_config(layout="wide", page_icon=Image.open(r"D:\Guvi project\guvi logo.png"),
                   page_title="Rating of Guvi Courses.")
selected = option_menu(None, ["Home", "To_find_rating","About_Guvi"], icons=["house", "pencil-square ","gear"],default_index=0,
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"}})
# Selecting Home Menu
if selected == 'Home':
    # Open the image
    image = Image.open(r"D:\Guvi project\guvi.png")

    # Resize the image to the desired dimensions
    new_width = 300  # Set your desired width
    new_height = 200  # Set your desired height
    resized_image = image.resize((new_width, new_height))
    # Display the resized image
    st.image(resized_image, caption="Guvi")
    st.title('Rating of Guvi Courses')

# Selecting Regression dependent variable Selling price
if selected == 'To_find_rating':
    # Selecting Test percentage i.e. 10% to 40%
    st.subheader('Selecting Test percentage 10% to 40%')
    test_size = st.slider('Test percentage', 0.10, 0.40, 0.15)
    st.write('Selected Test Size : ', round(test_size * 100,2), '%')
    # Regression cleaned files
    df = pd.read_csv(r"D:\Guvi project\cleaned guvi data.csv")
    y = df['Rating']
    x = df.drop(['Rating', 'published_timestamp'], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)



    algo = st.selectbox('Select after selecting Algorithm Predict_Algorithm button for test ', list(reg_algo.keys()))
    if algo:
        st.write('Selected Algorithm : ', algo)
        load_mod = pickle.load(open(reg_algo[algo], 'rb'))
    if st.button('Predict_Algorithm'):
        y_pred = load_mod.predict(x_test)
        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        st.write('Predicted Algorithm Test')
        st.write('Mean Absolute Error (MSE):', mae)
        st.write('Mean Squared Error (MSE):', mse)
        st.write('Root Mean Squared Error (RMSE):', rmse)
        st.write('R-squared (R2):', r2)
    st.write('*****************')
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        st.subheader('Price')
        st.write('Select the Price')
        price = st.slider('Price', 0, 200,0)
        st.write('Price : ', price)
        st.subheader('Number of Subscribers')
        num_subscribers = st.number_input('Enter the number',value=125.0)
        st.write('Number of Subscribers :', num_subscribers)
        st.subheader('Number of Reviews')
        num_reviews = st.number_input('Enter the number', value=125.0, key='unique_key_for_num_reviews')
        st.write('Number of Reviews :', num_reviews)
        st.subheader('Number of Lectures')
        num_lectures = st.number_input('Enter the number', value=10.0)
        st.write('Number of Lectures :', num_lectures)
    with col2:
        st.subheader('Level')
        level = st.radio('Select the level', [0.0, 1.0, 2.0, 3.0], index=0)
        if level == 0.0:
            level0 = 'All Levels'
        elif level == 1.0:
            level0 = 'Beginner Level'
        elif level == 2.0:
            level0 = 'Expert Level'
        else:
            level0 = 'Intermediate Level'
        st.write('Level :',level0)
        st.subheader('Content Duration')
        content_duration = st.number_input('Enter the number',value= 10.0, key='unique_key_for_content_duration')
        st.write('Content Duration :', content_duration)
        st.subheader('Subject')
        subject = st.radio('select the Subject',[0.0, 1.0, 2.0, 3.0],index=0)
        if subject == 0.0:
            subj = 'Business Finance'
        elif subject == 1.0:
            subj = 'Graphic Design'
        elif subject == 3.0:
            subj = 'Musical Instruments'
        else:
            subj = 'Web Development'
        st.write('Subject :', subj)
    with col3:
        st.subheader('Prediction Unknown Data')
        st.write("""Selecting Prediction Button to Predicting the unknown data from the previous selection.
                """)
        if st.button('Predict'):
            prid_data = np.array([[price, num_subscribers, num_reviews, num_lectures, level, content_duration, subject]])
            given_predict = load_mod.predict(prid_data)
            st.write('The predicted Rating : ',given_predict)
if selected == 'About_Guvi':
    col1, col2, col3 = st.columns([2, 2, 2])
    # Open the image
    with col2:
        image = Image.open(r"D:\Guvi project\guvi.png",)
        st.image(image)
    st.subheader("Introduction:")
    st.write('  1. GUVI (an acronym for Grab Your Vernacular Imprint)is an IIT Madras and IIM Ahmedabad incubated company based in Chennai,India.')
    st.write('  2. It was founded by ex-PayPal engineers Arun Prakash,Sridevi Arun Prakash, and SP Balamurugan in 2014.')
    st.write('''    3. GUVI offers free and paid learning courses on various IT and tech domains in Indian vernacular languages such as 
            Tamil, Telugu, Hindi, Kannada, Bengali, and English.
            GUVI's mission is "to make technical education available to
            all in their native languages".''')
    st.write('''    4. In 2022, Indian Information Technology and Consulting Service giant HCL acquired 
    a majority stake in the vernacular edtech company that provides diverse professional and certificate tech courses to 
    students, graduates, and working professionals who wish to upskill themselves.''')
    st.subheader('History:')
    st.write("""    1. The founder trio comprising Arun Prakash, Sridevi Arun Prakash, 
            and SP Balamurugan, started GUVI as a volunteering initiative in the 
            form of a YouTube channel back in 2011 while they were working for PayPal.""")
    st.write(''' 2. They used to post videos, tutorials, and practice material explaining technical 
            terminologies and concepts in vernacular languages like 
            Tamil, Telugu, and Marathi. The founders’ primary goal was to bring tech 
            closer to the learners not fluent in English.''')
    st.write('''    3. It all started when GUVI’s CEO and founder, 
            Arun Prakash went to attend an alumni meet at his college where 
            he got the chance to meet and interact with the current batch of students. 
            During the interaction, the students seemed to lack basic technical knowledge.''')
    st.write('''    4. So, Arun started teaching and explaining those tech concepts in the student’s 
            native language. They seemed to grasp the concepts and understand them very well.''')
    st.write('''    5. This made Arun realize the gaping skill gap in college students because of 
            the high dependency on English for tech education. He then discussed his 
            concern with Sridevi and Balamurugan.''')
    st.write("""    6. Then they decided to put out and teach technical skills to students in 
            vernacular language to bridge the gap in tech education caused 
            by the language barrier.Arun started to upload his videos in vernacular 
            language explaining tech concepts.""")
    st.write('''    7. Initially, the response was low and it didn’t get enough attention. 
            Still, they stayed put and kept creating more videos. 
            Soon, after almost 6 months from inception, they were able to 
            gain a stable audience through their unique approach to spreading tech knowledge. 
            They started receiving good engagement from various tier-2 and tier-3 
            learners as well as international viewers.''')
    st.write('''    8. With time, their YouTube channel had already garnered millions of views 
            and 5000+ subscribers.''')
    st.write('''    9. Given the demand and growing popularity, GUVI was finally started as a 
            private limited company as GUVI Geeks Network Private Limited. 
            Sridevi quit her job followed by S.P. Balamurugan to start working full time for GUVI. 
            Meanwhile, Arun Prakash continued working at PayPal to support GUVI and fund its expenses. 
            He too eventually quit his job in 2015 and came to work for GUVI full-time.''')
    st.write("""    10. After a while,given the potential, the company was then incubated by IIT-Madras 
            at IIT-Madras Research Park in Chennai, Tamil Nadu. In 2019, GUVI got co-incubated by 
            CIIE of IIM Ahmedabad too.""")