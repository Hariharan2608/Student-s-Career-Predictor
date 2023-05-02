import pickle
import streamlit as st
import pandas as pd
from PIL import Image

import base64

st.set_page_config(
    page_title="Student's Career Predictor",
    page_icon="👨‍💼",
    initial_sidebar_state="expanded",
)
padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

# main_bg = "b1.jfif"
# main_bg_ext = "jpg"
# st.write(
    # f"""
    # <style>
    # .reportview-container {{
        # background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    # }}

    # </style>
    # """,
    # unsafe_allow_html=True
# )


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
</style> """, unsafe_allow_html=True)



img1 = Image.open("image/logos.png")
#img2 = Image.open("boston.png")


# side_1,side_2 = st.sidebar.columns(2)

# side_1.image(img1, use_column_width=True)
# side_2.image(img2, use_column_width=True)



st.sidebar.image(img1)
st.sidebar.write("The app results should not be taken seriously") 
        

# loading the trained model
pickle_in = open('RF_career.pkl', 'rb') 
classifier = pickle.load(pickle_in)

# defining the function which will make the prediction using the data which the user inputs 
def prediction(education,novel,indoor_game,outdoor_game,mobile,movie_type,movie_genre,newspaper,ott,social_media):  
    
    if education == '10th':
        education = 0
    elif education == '12th':
        education = 1
    elif education == 'UG':
        education = 2
    elif education == 'PG':
        education = 3
        
    if novel == 'Mysteries':
        novel = 0
    elif novel == 'Fantasy':
        novel = 1
    elif novel == 'Historical':
        novel = 3
    elif novel == 'Romance':
        novel = 2
        
    if indoor_game == 'Chess':
        indoor_game = 0
    elif indoor_game == 'Carrom Board':
        indoor_game = 1
    elif indoor_game == 'Shuttle':
        indoor_game = 2
    elif indoor_game == 'Card Games':
        indoor_game = 3
        
    if outdoor_game == 'Cricket':
        outdoor_game = 0
    elif outdoor_game == 'Football':
        outdoor_game = 1
    elif outdoor_game == 'Kabaddi':
        outdoor_game = 2
    elif outdoor_game == 'Hockey':
        outdoor_game = 3
        
    if mobile == 'Rarely':
        mobile = 0
    elif mobile == 'Occasionally':
        mobile = 1
    elif mobile == 'Frequently':
        mobile = 2
        
    if movie_type == 'Hollywood':
        movie_type = 0
    elif movie_type == 'Bollywood':
        movie_type = 1
    elif movie_type == 'Kollywood':
        movie_type = 2
    elif movie_type == 'Tollywood':
        movie_type = 3
    elif movie_type == 'Sandalwood':
        movie_type = 4
        
    if movie_genre == 'Drama':
        movie_genre = 0
    elif movie_genre == 'Action':
        movie_genre = 1
    elif movie_genre == 'Comedy':
        movie_genre = 2
    elif movie_genre == 'Science Fiction':
        movie_genre = 3
        
    if newspaper == 'Yes':
        newspaper = 0
    elif newspaper == 'No':
        newspaper = 1
    
    if ott == 'Netflix':
        ott = 0
    elif ott == 'Disney + Hotstar':
        ott = 1
    elif ott == 'Amazon Prime':
        ott = 2
    elif ott == 'Sony LIV':
        ott = 3
        
    if social_media == 'Instagram':
        social_media = 0
    elif social_media == 'Facebook':
        social_media = 1
    elif social_media == 'Twitter':
        social_media = 2
    elif social_media == 'You Tube':
        social_media = 3
    elif social_media == 'Whatsapp':
        social_media = 4
        
    prediction = classifier.predict( 
        [[education,novel,indoor_game,outdoor_game,mobile,movie_type,movie_genre,newspaper,ott,social_media]])
    return prediction


     
# front end elements of the web page 
html_temp = """ 
<div style ="background-color:#025246;padding:8px"> 
<h1 style ="font-family:Times New Roman;color:white;text-align:center;">Student's Career Predictor</h1> 
<h3 style ="font-family:Times New Roman;color:white;text-align:center;">APP created by Hariharan</h3>
</div> 
"""
  
# display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True)

col1, col2 = st.columns(2)

with col1:
   education = st.selectbox('1. What is your educational qualification?',("10th","12th","UG","PG"))
   indoor_game = st.selectbox('3. What is your favourite indoor game?',("Chess","Carrom Board","Shuttle","Card Games"))
   mobile = st.selectbox('5. How much time do you use a mobile phone?',("Rarely","Occasionally","Frequently"))
   movie_genre = st.selectbox('7. What movies genre you are interested in?',("Drama","Action","Comedy",'Science Fiction'))
   ott = st.selectbox('9. What is your favourite OTT platform?',("Netflix","Disney + Hotstar","Amazon Prime","Sony LIV"))

with col2:
   novel = st.selectbox('2. Which kind of novel do you read?',("Mysteries","Fantasy","Historical","Romance"))
   outdoor_game = st.selectbox('4. What is your favourite outdoor game?',("Cricket","Football","Kabaddi","Hockey"))
   movie_type = st.selectbox('6. Which is your favourite type of movie to watch?',("Hollywood","Bollywood","Kollywood","Tollywood","Sandalwood"))
   newspaper = st.selectbox('8. Do you read the newspaper daily?',("Yes","No"))
   social_media = st.selectbox('10. Which social media platform do you use most?',("Instagram","Facebook","Twitter","You Tube","Whatsapp"))

     
safe_html_0 ="""  
  <div style="background-color:#80ff80; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may do a Business</h2>
  </div>
"""

safe_html_1 ="""  
  <div style="background-color:#B9F80D; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may be a Chartered Accountant (CA)</h2>
  </div>
"""

safe_html_2 ="""  
  <div style="background-color:#07E1B5; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may work in Cini Industry </h2>
  </div>
"""

safe_html_3 ="""  
  <div style="background-color:#07BFE1; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may be a Driver</h2>
  </div>
"""

safe_html_4 ="""  
  <div style="background-color:#07E1CC; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may be a Employee in Manufacturing Industry</h2>
  </div>
"""

safe_html_5 ="""  
  <div style="background-color:#0780E1; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may be a Farmer</h2>
  </div>
"""

safe_html_6 ="""  
  <div style="background-color:#2307E1; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may do a Government job</h2>
  </div>
"""

safe_html_7 ="""  
  <div style="background-color:#BE07E1 ; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may work in IT Company</h2>
  </div>
"""

safe_html_8 ="""  
  <div style="background-color:#E1009D ; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may be a Professional for your job</h2>
  </div>
"""

safe_html_9 ="""  
  <div style="background-color:#E1009D ; padding:10px >
  <h2 style="color:white;text-align:center;">In future you may become a Teacher</h2>
  </div>
"""

safe_html_10 ="""  
  <div style="background-color:#E1009D ; padding:10px >
  <h2 style="color:white;text-align:center;">Youtuber 😑 </h2>
  </div>
"""   
question = []
question.append("What is your educational qualification?")
question.append("Which kind of novel do you read?")
question.append("What is your favourite indoor game?")
question.append("What is your favourite outdoor game?")
question.append("How much time do you use a mobile phone?")
question.append("Which is your favourite type of movie to watch? ")
question.append("What movies genre you are interested in? ")
question.append("Do you read the newspaper daily? ")
question.append("What is your favourite OTT platform?")
question.append("Which social media platform do you use most?")
#st.write(question)
answer = []
answer.append(education)
answer.append(novel)
answer.append(indoor_game)
answer.append(outdoor_game)
answer.append(mobile)
answer.append(movie_type)
answer.append(movie_genre)
answer.append(newspaper)
answer.append(ott)
answer.append(social_media)

df1 = pd.DataFrame({"Questions":question,"Your Answer":answer})


img3 = Image.open("image/youtuber.jfif")
img4 = Image.open("image/teacher.jfif")
img5 = Image.open("image/company.jfif")
img6 = Image.open("image/gov job.jfif")
img7 = Image.open("image/farmer.jfif")
img8 = Image.open("image/industry.jfif")
img9 = Image.open("image/driver.jfif")
img10 = Image.open("image/cini industry.jfif")
img11 = Image.open("image/ca.jfif")
img12 = Image.open("image/business.jfif")
img13 = Image.open("image/professional.jfif")



# if st.button("Show Answer"):
    # st.write(df1)
st.write(df1)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(153, 204, 255);
}
</style>""", unsafe_allow_html=True)
    
if st.button("Predict"):
    output = prediction(education,novel,indoor_game,outdoor_game,mobile,movie_type,movie_genre,newspaper,ott,social_media)

    if output == 0:
        st.markdown(safe_html_0,unsafe_allow_html=True)
        st.image(img12,width = 736)
    elif output == 1:
        st.markdown(safe_html_1,unsafe_allow_html=True)
        st.image(img11,width = 736)
    elif output == 2:
        st.markdown(safe_html_2,unsafe_allow_html=True)
        st.image(img10,width = 736)
    elif output == 3:
        st.markdown(safe_html_3,unsafe_allow_html=True)
        st.image(img9,width = 736)
    elif output == 4:
        st.markdown(safe_html_4,unsafe_allow_html=True)
        st.image(img8,width = 736)
    elif output == 5:
        st.markdown(safe_html_5,unsafe_allow_html=True)
        st.image(img7,width = 736)
    elif output == 6:
        st.markdown(safe_html_6,unsafe_allow_html=True)
        st.image(img6,width = 736)
    elif output == 7:
        st.markdown(safe_html_7,unsafe_allow_html=True)
        st.image(img5,width = 736)
    elif output == 8:
        st.markdown(safe_html_8,unsafe_allow_html=True)
        st.image(img13,width = 736)
    elif output == 9:
        st.markdown(safe_html_9,unsafe_allow_html=True)
        st.image(img4,width = 736)
    elif output == 10:
        st.markdown(safe_html_10,unsafe_allow_html=True)
        st.image(img3,width = 736)
        


# #st_card('Completed Orders', value=76.4, show_progress=True)


