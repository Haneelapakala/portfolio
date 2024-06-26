

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
            st.write("•Contributed to innovative projects (ReX, Sky, Kai) in personalized education, career coaching, and AI-powered teaching assistance, showcasing breadth in AI applications.")
            st.write("•Utilized transfer learning and fine-tuning of pre-trained models to adapt to specific educational content, ensuring high accuracy.")
            st.write("•Implemented generative AI techniques to create custom content and personalized learning paths for students, significantly improving engagement and retention rates.")
            st.write("•Developed AI-driven career coaching tools that leverage LLMs to offer personalized advice, resume building tips, and interview preparation, helping users achieve their career goals.")
            st.write("___")
            st.subheader("""
            Machine Learning Intern at BEPEC SOLUTION - Bangalore, India          Mar 2023 - Mar 2024""")
            st.write("•Identified patterns in customer feedback employed feature engineering, decision trees, linear regression. The objective was to identify patterns and build initial predictive models to enhance service delivery and customer satisfaction.")
            st.write("•Engineered and implemented advanced prompt strategies to significantly improve the quality of outputs from LLM’s.") 
            st.write("•Fine-tuned open-source LLMs using Parameter-Efficient Transfer Learning (PEFT) to achieve the desired text format.")
            st.write("•Implemented image segmentation and point localization with mask R-CNN, YOLO in OpenCV and object tracking.") 
            st.write("•Created a user-friendly Flask interface on AWS SageMaker, enhancing ultrasound image segmentation by 6%.")
            st.write("•Prototyped algorithms for 3D face model conversion from 2D images using depth information and key point access.")
            st.write("___")
            st.subheader("""
            Application Development Associate:  ACCENTURE - [Hyderabad, India]        (Jan 2021 – Aug 2022)  """)                                                                   
            st.write("•Developed ETL pipelines and Big Query scripts for seamless data transformation and knowledge extraction, enhancing project efficiencies. Accelerated unit testing using Google Cloud Platform and Python, ensuring robustness of codebase.")
            st.write("•Created a CI/CD pipeline using Azure DevOps for automating application deployment, reducing deployment time by 25%.")
            st.write("•Created and aggregated daily reports for clients by analyzing data provided by the client and from data sources improving decision making.")
            st.write("•Utilized statistical methods, metrics, quantitative methods, and strategic project plans for data collection, ensuring integrity and accuracy.")
            st.write("•Analyzed and optimized complex SQL queries for various products, reducing total execution time by 13% across all products.")
            st.write("•Engineered advanced machine learning models using python programming to forecast customer churn, resulting in a 20% decrease in customer churn and a remarkable $5 million boost in annual revenue.")
            st.write("•Employed data blending techniques in Tableau to combine data from multiple sources and create comprehensive visualizations.")

            

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
            st.subheader("Real-Time Streaming")
            st.write("Real-Time Streaming-Apache Flink ")
            #st.markdown("[Visit Github Repo](https://github.com/Haneelapakala/Real-Time-Streaming)")

    with st.container():
        st.write("##")
        col12, col13  = st.columns((1,2))
        with col12:
            st_lottie(lottie_blog, height = 150)
            # st.image(image)
        with col13:
            st.subheader("Shakespearean Text Generator")
            st.write("Generates text given a cue in the style of Shakespearean Language.")
            #st.markdown("[Visit Github Repo](https://github.com/Haneelapakala/Shakespearean-Text-Generator)")

    

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
    




