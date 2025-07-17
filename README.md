## **🧠 Persona Predictor**
Persona Predictor is a web-based personality classification app built using Streamlit. It evaluates users’ responses to psychological and behavioral questions and predicts whether their personality type is Introvert, Ambivert, or Extrovert, along with a confidence score and explanation.

## **🚀 Features**
**📊 Slider-based Questionnaire covering:**
◦ Cognitive & Emotional Traits
◦ Social Behavior & Interaction
◦ Lifestyle & Preferences
◦ Organizational Traits
  
**🔮 Machine Learning-Based Prediction** with confidence level

**📌 Visual Trait Breakdown** via radar chart and feature importance bar graph

**🧾 Personality Type Explanation** with matching traits

**🔁 Page Navigation** (Form ↔ Results)

## **📦 Dependencies**
Make sure you have the following Python libraries installed:
**pip install** streamlit pandas plotly matplotlib scikit-learn seaborn  

## **▶️ How to Run the App**
1. Clone or download the project.
   
2. Navigate to the project directory in your terminal.
   
3. Run the Streamlit app:
**streamlit run** persona_predictor.py

4. The app will open in your web browser at:
**http://localhost:8501**


## **🧠 How It Works**
1. Users answer behavioral and preference-based questions via interactive sliders.

2. The answers are compiled into a feature vector.

3. The input is passed to a machine learning model (logistic regression) that:
◦ Scales the input
◦ Predicts personality type
◦ Computes a confidence score

4. The app displays:
◦ Your predicted personality type
◦ A radar chart showing your trait profile
◦ A bar chart showing the top traits influencing the result
