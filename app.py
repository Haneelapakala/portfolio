

import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image
import requests

st.set_page_config(layout="wide")
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
image = Image.open('pic.jpg') 
lottie_url = load_lottie_url("https://lottie.host/0c1681fb-be3d-41a9-a7ff-34dc62a7cc00/FJDEziS74b.json")
lottie_contact = load_lottie_url("https://lottie.host/17b287ce-cdda-4e32-8332-669e99cb6ecc/fWQkoX38oH.json")
lottie_Auto = load_lottie_url("https://lottie.host/b7c22a23-d0be-4789-b937-69f56b270b31/azRRDr4od3.json")
lottie_cyber = load_lottie_url("https://lottie.host/1f3e40a9-cccf-4a2e-b579-593c161a62af/oB3NUJ63sD.json")
lottie_cancer = load_lottie_url("https://lottie.host/1069f626-6944-4619-ae46-55f2cb0a314e/5F5eB4W7nI.json")
lottie_Chatbot = load_lottie_url("https://lottie.host/1adade21-2016-46af-8fdd-528c28bc6721/geW1l6x5pd.json")
lottie_sentiment = load_lottie_url("https://lottie.host/1d5412d0-0740-4441-b6ba-d75134deb657/AkXR9HT9EK.json")
lottie_qa = load_lottie_url("https://lottie.host/adddee58-687c-48e9-a78c-844be18b8857/6dfo9OLIQz.json")
lottie_blog = load_lottie_url("https://lottie.host/a1ffcf82-6fbd-467f-8595-fd7b210db647/mfZ9GjqBBu.json")
lottie_newsresearch = load_lottie_url("https://lottie.host/1e1fc41e-53df-4f62-9200-a7da5a3bc8b4/8tpjMFJMfb.json")
lottie_linkedin = load_lottie_url("https://lottie.host/ba1892ee-ed64-432a-ad04-4fc25435435b/zA5wtkxal0.json")
lottie_email = load_lottie_url("https://lottie.host/858252e7-bdce-4ace-a3a0-d86d1d28aa28/gnHmk0Ip0V.json")
lottie_phn = load_lottie_url("https://lottie.host/d216b690-b992-459c-9d99-6b373c3e06fb/JpXSt0i0eG.json")




# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown
with st.container():
        colu1, colu2 = st.columns(2)
        with colu1:
            st.write("##")
            st.subheader("Hey Guys  :wave:")
            st.title("Haneela Pakala")
            # st.write(""" Haneela Pakala""")
            # st.write("[Read More](https://www.linkedin.com/in/haneelapakala/)")
        with colu2:
            st.image(image, width = 200)
with st.container(): 
        colu3, colu4, colu5 = st.columns([0.5,0.6,0.5])
        
        with colu3:
            st_lottie(lottie_linkedin,  height=100, width =100)
            
        with colu4:
            st_lottie(lottie_email,  height=100, width =100)
       
        with colu5:
            st_lottie(lottie_phn,  height=100, width =100)
        
with st.container(): 
        column, colu6, colu7, colu8 = st.columns([0.03,0.5,0.8,0.6])
        with column:
            pass
        
        
        with colu6:
            st.write("[Linkedin](https://www.linkedin.com/in/haneelapakala/)")
            
      
        with colu7:
            st.write("pakalahaneelareddy@gmail.com")
       
        with colu8:
            st.write("+1 (945)209-1823")


st.write("___")
with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects'],
        icons = ['person' , 'code-slash'],
        orientation = 'horizontal'
    )
    
if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Haneela Pakala")
            st.title("Graduate from Texas A&M University - Commerce")
            st.subheader("""
            Education: 
            MASTER OF SCIENCE (M.S.) IN COMPUTER SCIENCE at Texas A&M University-Commerce Aug  2022 to May 2024
            

        """)
        with col2:
            st_lottie(lottie_url)
    st.write("___")

    with st.container():
        col4, col3= st.columns([9, 0.1])
            
        with col4:
            st.title("Expereince:")
            st.subheader("""
            Artificial Intelligence Intern at Radical AI – New York,  USA        March 2024 – Present""")
            st.write("•	Designed and deployed AI applications using cutting-edge frameworks (OpenAI Assistant API, Google Gemini), honed prompt engineering skills, and optimized data for generative AI models.")
            st.write("•	Contributed to innovative projects (ReX, Sky, Kai) in personalized education, career coaching, and AI-powered teaching assistance, showcasing breadth in AI applications. ")
            st.write("___")
            st.subheader("""
            Machine Learning Intern at BEPEC SOLUTION - Bangalore, India          Mar 2023 - Mar 2024""")
            st.write("•Developed sentiment analysis engine using Python, NLTK and Scikit-learn to classify emotions and opinions in employee feedback reviews for manager performance.")
            st.write("•	Lead the design and development of MLops pipline using Sagemaker, MLFlow and S3 .") 
            st.write("•	Employed AWS cloud, Python, SQL and CI/CD pipeline for developing the desired model by research and quantitative analysis .")
            st.write("•	Trained a LLM model (GPT-3) on a dataset covering 80% of customer support tickets to automate 70% of common inquiries, resulting in a notable 45% reduction in response time and a significant 35% increase in customer satisfaction.") 
            st.write("___")
            st.subheader("""
            Application Development Associate:  ACCENTURE - [Hyderabad, India]  """)                                                                   (Jan 2021 – Aug 2022)  """)
            st.write(" • Developed ETL pipelines and Big Query scripts for seamless data transformation and knowledge extraction, enhancing project efficiencies. Accelerated unit testing using Google Cloud Platform and Python, ensuring robustness of codebase.")
            st.write("•	Debugged complex code (C#, Python), optimized SQL queries, and streamlined CI/CD pipelines to improve system performance and reliability for a client website.")
            st.write("•	Implemented predictive modeling with logistic regression and decision trees, achieving 85% accuracy on test datasets. Integrated automated anomaly detection to identify data irregularities and ensure data quality throughout the pipeline.")
            st.write("•	Developed data visualizations in Power BI, communicating complex findings and trends to stakeholders effectively.")

            

        with col3:
            pass
            
if selected == "Projects":

    with st.container():
        st.header("My Projects")
        st.write("##")
        col5, col6  = st.columns((1,2))
        with col5:
            st_lottie(lottie_Chatbot, height = 150)
            # st.image(image)
        with col6:
            st.subheader("Chatbot-for-Ecommerce-using-PALM")
            st.write("Built a chatbot for E-commerce using PALM, Langchain")
            st.markdown("[Visit Github Repo](https://github.com/Haneelapakala/chatbot-using-Palm)")

    with st.container():
        st.write("##")
        col6, col7  = st.columns((1,2))
        with col6:
            st_lottie(lottie_sentiment, height = 150)
            # st.image(image)
        with col7:
            st.subheader("Linkedin_analysis")
            st.write("Built a Sentiment Analysis of LinkedIn Messages")
            st.markdown("[Visit Github Repo](https://github.com/Haneelapakala/linkedin_analysis)")

    with st.container():
        st.write("##")
        col8, col9  = st.columns((1,2))
        with col8:
            st_lottie(lottie_newsresearch, height = 150)
            # st.image(image)
        with col9:
            st.subheader("Sentiment Analysis ")
            st.write("Built a Sentiment Analysis Using BERT")
            #st.markdown("[Visit Github Repo](https://github.com/Haneelapakala/BERT)")

    with st.container():
        st.write("##")
        col10, col11  = st.columns((1,2))
        with col10:
            st_lottie(lottie_qa, height = 150)
            # st.image(image)
        with col11:
            st.subheader("Conversational-Q-A-Chatbot")
            st.write("Built a Conversational Q-A  Chatbot using OpenAI")
            #st.markdown("[Visit Github Repo](https://github.com/prem8667/Conversational-Q-A-Chatbot)")

    with st.container():
        st.write("##")
        col12, col13  = st.columns((1,2))
        with col12:
            st_lottie(lottie_blog, height = 150)
            # st.image(image)
        with col13:
            st.subheader("Blog-Generation-Using-Langchain")
            st.write("Built a Blog generation webpage using Langchain")
            #st.markdown("[Visit Github Repo](https://github.com/prem8667/Blog-Generation-Using-Langchain)")

    

    with st.container():
        st.write("##")
        col14, col15  = st.columns((1,2))
        with col14:
            st_lottie(lottie_Auto, height = 150)
            # st.image(image)
        with col15:
            st.subheader("Automobile Price prediction")
            st.write("Predicted prices of automobile usinh different ML algorithms")
            #st.markdown("[Visit Github Repo](https://github.com/prem8667/Automobile-Price-Prediction)")
    with st.container():
        
        st.write("##")
        col16, col17  = st.columns((1,2))
        with col16:
            st_lottie(lottie_cancer, height = 150)

        with col17:
            st.subheader("Cancer Prediction")
            st.write("Predicted Cancer using Logistic KNN and Decision-Tree")
            #st.markdown("[Visit Github Repo](https://github.com/prem8667/Cancer-prediction-using-Logistic-KNN-and-Decision-Tree)")
    with st.container():
        
        st.write("##")
        col18, col19  = st.columns((1,2))
        with col18:
            st_lottie(lottie_cyber, height = 150)

        with col19:
            st.subheader("Attack Detection Using Autoencoders")
            st.write("Anomoly detection using Autoencoders")
            #st.markdown("[Visit Github Repo](https://github.com/prem8667/Anomaly-detection-using-Autoencoders)")





