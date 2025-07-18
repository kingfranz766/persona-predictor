## **🧠 Persona Predictor**
Persona Predictor is a web-based personality classification app built using Streamlit. It evaluates users’ responses to psychological and behavioral questions and predicts whether their personality type is Introvert, Ambivert, or Extrovert.

## **Features**
_Slider-based Questionnaire covering:_
- Cognitive & Emotional Traits
- Social Behavior & Interaction
- Lifestyle & Preferences
- Organizational Traits
 
_Machine Learning-Based Prediction_ with confidence level

_Visual Trait Breakdown_ via radar chart and feature importance bar graph

_Personality Type Explanation_ with matching traits

## **Requirements**
Make sure you have the following Python libraries installed:  
```bash
pip install streamlit pandas plotly matplotlib scikit-learn seaborn  
```

## **How to Run the App**
- Clone or download the project.
- Navigate to the project directory in your terminal.
```bash
cd YourProjectDirectory
#Example: "C:\personality-type-classifier-g9"
```
- Run the Streamlit app:
```bash
streamlit run persona_predictor.py
```
- The app will open in your web browser at:
```bash
http://localhost:8501
```

## **How It Works**
_Users answer behavioral and preference-based questions via interactive sliders._

_The answers are compiled into a Dataframe._

_The input is passed to a machine learning model (logistic regression) that:_
  - Scales the input
  - Predicts personality type
  - Computes a confidence score

_The app then displays:_
  - Your predicted personality type
  - A radar chart showing your trait profile
  - A bar chart showing the top traits influencing the result
