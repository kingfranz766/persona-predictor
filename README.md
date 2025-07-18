## **🧠 Persona Predictor**
Persona Predictor is a web-based personality classification app built using Streamlit. It evaluates users’ responses to psychological and behavioral questions and predicts whether their personality type is Introvert, Ambivert, or Extrovert, along with a confidence score and explanation.

## **Features**
**Slider-based Questionnaire covering:** 
- Cognitive & Emotional Traits
- Social Behavior & Interaction
- Lifestyle & Preferences
- Organizational Traits
 
**Machine Learning-Based Prediction** with confidence level
**Visual Trait Breakdown** via radar chart and feature importance bar graph
**Personality Type Explanation** with matching traits
**Page Navigation** (Form ↔ Results)

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
- **Users answer behavioral and preference-based questions via interactive sliders.**
- **The answers are compiled into a Dataframe.**
- **The input is passed to a machine learning model (logistic regression) that:**
  - Scales the input
  - Predicts personality type
  - Computes a confidence score
- **The app then displays:**
  - Your predicted personality type
  - A radar chart showing your trait profile
  - A bar chart showing the top traits influencing the result
