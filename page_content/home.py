import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h2>丁然</h2>
        <p>市场营销硕士<br>
        香港中文大学<br>
        香港新界大埔区山塘路8号天钻7座7H<br>
        <a href="mailto:13779598117@163.com">13779598117@163.com</p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image1.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        I am a recent master's graduate in Data Science from the University of XYZ, eager to apply my knowledge and skills in a professional setting. During my academic journey, I developed a strong foundation in statistical analysis, machine learning, and data visualization.

        As part of my master's program, I completed several projects that involved working with real-world datasets and applying various data science techniques. These projects allowed me to gain hands-on experience in data preprocessing, exploratory data analysis, model building, and evaluation.

        I am passionate about leveraging data to drive insights and make informed decisions. I am a quick learner, a collaborative team player, and possess strong problem-solving skills. I am excited to contribute my skills and grow as a data science professional in a dynamic and challenging environment.
        """
    )

    st.markdown(
        """
        ### Skills
        - Programming Languages: Python, R
        - Data Analysis: Pandas, NumPy, Matplotlib, Seaborn
        - Machine Learning: Scikit-learn, TensorFlow, Keras
        - Database: SQL, MongoDB
        - Data Visualization: Tableau, Power BI
        - Statistical Analysis: Hypothesis Testing, Regression Analysis
        - Communication: Presentation Skills, Technical Writing
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 