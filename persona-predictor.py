#Importing Neccessary libraries
import pandas as pd
import streamlit as st
from models import logistics
import matplotlib.pyplot as plt
from models.logistics import scaler
import plotly.express as px
import plotly.graph_objects as go

# Initialize the current page
if "page" not in st.session_state:
    st.session_state.page = "form"  # default page

# Navigation logic
def go_to_results():
    # You can run your model here before navigating
    predicted_class, confidence = logistics.predict_with_confidence(user_input)
    st.session_state.prediction = predicted_class
    st.session_state.confidence = confidence
    st.session_state.page = "results"
    st.session_state.user_input = user_input
    st.rerun()

#Setting website look
st.set_page_config(page_title="Persona Predictor", page_icon="🧠", layout="wide")

#Pages
if st.session_state.page == "form":

    st.markdown(
        """
        <p style='text-align: center; color: pink; margin-bottom: -30px; font-weight: bold; font-size: 72px;'>
            Persona Predictor.
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <p style='text-align: center; margin-top: 0px; font-size: 18px; color: light;'>
            <i>Be yourself and answer honestly to find out your personality type.</i>
        </p>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<hr></hr>", unsafe_allow_html=True)

    left, center, right = st.columns([1, 2, 1])
    #Slider and questions builder
    def render_slider_question(title: str, subtitle: str, key: str):
        st.markdown(
            f"<h5 style='text-align: center;margin-bottom: -30px;'>{title}</h3>",
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <p style='text-align: center; margin-top: 5px; font-size: 16px; color: lightgray; margin-bottom: -40px;'>
                <i>{subtitle}</i>
            </p>
            """,
            unsafe_allow_html=True
        )
        value = st.slider("", min_value=0.0, max_value=10.0, step=0.1, format="%.0f", key=key)
        st.markdown("<div style='height:25px;'></div>", unsafe_allow_html=True)
        return value
    
    #Render the questionare and the sliders
    with center:

        #Category: Cognitive and Emotional Traits
        st.markdown(
            f"<h3 style='text-align: center;margin-bottom: -30px;font-weight: bold;'><i>🧠 Cognitive & Emotional Traits:</i></h3>",
            unsafe_allow_html=True
        )
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

        with st.container(border=True):
            deep_reflection = render_slider_question(
                "How often do you engage in deep or introspective thinking?",
                "(0 = Never, 10 = Very frequently)",
                "deep_reflection"
            )

            creativity = render_slider_question(
                "How often do you think creatively or outside the box?",
                "(0 = Never, 10 = Very often)",
                "creativity"
            )

            curiosity = render_slider_question(
                "How interested are you in learning or exploring new things?",
                "(0 = Not at all, 10 = Extremely interested)",
                "curiosity"
            )

            emotional_stability = render_slider_question(
                "How well do you stay calm and balanced under stress?",
                "(0 = Very reactive, 10 = Very calm)",
                "emotional_stability"
            )
            
            stress_handling = render_slider_question(
                "How well do you manage stress?",
                "(0 = Crumbles under pressure, 10 = Handles stress well)",
                "stress_handling"
            )

            decision_speed = render_slider_question(
                "How quickly do you make decisions?",
                "(0 = Very slowly, 10 = Very quickly)",
                "decision_speed"
            )
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
        
        #Category: Social Behavior & Interaction
        st.markdown(
            f"<h3 style='text-align: center;margin-bottom: -30px;font-weight: bold;'><i>👥 Social Behavior & Interaction:</i></h3>",
            unsafe_allow_html=True
        )
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
        with st.container(border=True):
            social_energy = render_slider_question(
                "Tendency to gain energy from social interaction",
                "(0 = Not at all, 10 = A lot)",
                "social_energy"
            )

            alone_time_preference = render_slider_question(
                "How comfortable are you being alone?",
                "(0 = Not at all, 10 = Extremely comfortable)",
                "alone_time"
            )

            talkativeness = render_slider_question(
                "Tendency to talk a lot in conversations.",
                "(0 = Very quiet, 10 = Very talkative)",
                "talkativeness"
            )

            group_comfort = render_slider_question(
                "How comfortable do you feel in group settings/environments?",
                "(0 = Not at all, 10 = Very comfortable)",
                "group_comfort"
            )

            party_liking = render_slider_question(
                "How much do you enjoy parties and social events?",
                "(0 = Not at all, 10 = Very Much)",
                "party_liking"
            )

            listening_skill = render_slider_question(
                "How good are you at actively listening to others?",
                "(0 = Not at all, 10 = Very good)",
                "listening_skill"
            )
            
            empathy = render_slider_question(
                "How well do you understand others’ emotions?",
                "(0 = Not at all, 10 = Extremely well)",
                "empathy"
            )
            
            friendliness = render_slider_question(
                "How socially warm and approachable do you consider yourself?",
                "(0 = Very reserved, 10 = Very friendly)",
                "friendliness"
            )
            
            public_speaking_comfort = render_slider_question(
                "How comfortable are you with public speaking?",
                "(0 = Not at all, 10 = Very comfortable)",
                "public_speaking_comfort"
            )
            
            leadership = render_slider_question(
                "How comfortable are you with leading others?",
                "(0 = Not at all, 10 = Very comfortable)",
                "leadership"
            )
            
            work_style_collaborative = render_slider_question(
                "Do you prefer working alone or in a team?",
                "(0 = Strong preference for solo work, 10 = Strong preference for teamwork)",
                "work_style_collaborative"
            )   
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)   
        
        #Category: Lifestyle & Preferences
        st.markdown(
            f"<h3 style='text-align: center;margin-bottom: -30px;font-weight: bold;'><i>🎯 Lifestyle & Preferences:</i></h3>",
            unsafe_allow_html=True
        )
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)   

        with st.container(border=True):
            routine_preference = render_slider_question(
                "Do you prefer routine or spontaneity?",
                "(0 = Strong preference for routine, 10 = Strong preference for spontaneity)",
                "routine_preference"
            )

            excitement_seeking = render_slider_question(
                "How strong is your desire for new and stimulating experiences?",
                "(0 = None at all, 10 = Very strong)",
                "excitement_seeking"
            )

            risk_taking = render_slider_question(
                "How willing are you to take risks?",
                "(0 = Not at all, 10 = Very willling)",
                "risk_taking"
            )

            adventurousness = render_slider_question(
                "How willing are you to try new and risky activities?",
                "(0 = Not willing, 10 = Very willing)",
                "adventurousness"
            )

            travel_desire = render_slider_question(
                "How interested are you in traveling and exploring new places",
                "(0 = Not interested, 10 = Very interested)",
                "travel_desire"
            )

            sports_interest = render_slider_question(
                "How interested are you in sports or physical activities?",
                "(0 = No interest, 10 = Very high interest)",
                "sports_interest"
            )

            reading_habit = render_slider_question(
                "How often do you read books or articles",
                "(0 = Never, 10 = Daily or often)",
                "reading_habit"
            )

            online_social_usage = render_slider_question(
                "How much time do you spend on social media and online interactions?",
                "(0 = Rarely or never, 10 = Very frequently)",
                "online_social_usage"
            )

            gadget_usage = render_slider_question(
                "How often do you use gadgets or tech devices?",
                "(0 = Very rarely, 10 = All the time)",
                "gadget_usage"
            )
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
        
        #Category: Organizational Traits
        st.markdown(
            f"<h3 style='text-align: center;margin-bottom: -30px;font-weight: bold;'><i>📦 Organizational Traits:</i></h3>",
            unsafe_allow_html=True
        )
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

        with st.container(border=True):
            organization = render_slider_question(
                "Tendency to prefer order and organization",
                "(0 = Not at all, 10 = Very strong)",
                "organization"
            )

            planning = render_slider_question(
                "How often do you plan ahead?",
                "(0 = Never plans, 10 = Always plans)",
                "planning"
            )

            spontaneity = render_slider_question(
                "How often do you act on impulse or without planning?",
                "(0 = Never impulsive, 10 = Very impulsive)",
                "spontaneity"
            )
        st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

        # CSS styling for the button
        st.markdown("""
            <style>
            div.stButton > button {
                font-size: 22px;
                padding: 14px 28px;
                background-color: #ff4b4b;
                color: white;
                border-radius: 10px;
                border: 2px solid #ff4b4b;
                transition: all 0.3s ease;
                width: 200px; /* Optional: Fix width for symmetry */
            }

            div.stButton > button:hover {
                background-color: transparent;
                color: #ff4b4b;
                border: 2px solid #ff4b4b;
            }
            </style>
        """, unsafe_allow_html=True)

        left, center, right = st.columns([1, 1, 1])
        with center:
            if st.button("🚀 Predict"):
                user_input = pd.DataFrame({
                    'social_energy': [social_energy],
                    'alone_time_preference': [alone_time_preference],
                    'talkativeness': [talkativeness],
                    'deep_reflection': [deep_reflection],
                    'group_comfort': [group_comfort],
                    'party_liking': [party_liking],
                    'listening_skill': [listening_skill],
                    'empathy': [empathy],
                    'creativity': [creativity],
                    'organization': [organization],
                    'leadership': [leadership],
                    'risk_taking': [risk_taking],
                    'public_speaking_comfort': [public_speaking_comfort],
                    'curiosity': [curiosity],
                    'routine_preference': [routine_preference],
                    'excitement_seeking': [excitement_seeking],
                    'friendliness': [friendliness],
                    'emotional_stability': [emotional_stability],
                    'planning': [planning],
                    'spontaneity': [spontaneity],
                    'adventurousness': [adventurousness],
                    'reading_habit': [reading_habit],
                    'sports_interest': [sports_interest],
                    'online_social_usage': [online_social_usage],
                    'travel_desire': [travel_desire],
                    'gadget_usage': [gadget_usage],
                    'work_style_collaborative': [work_style_collaborative],
                    'decision_speed': [decision_speed],
                    'stress_handling': [stress_handling]
                })
                st.session_state.user_input = user_input
                go_to_results()

elif st.session_state.page == "results":
    theme_color = {
        'Introvert': '#5DADE2',
        'Ambivert': '#A569BD',
        'Extrovert': '#F5B041'
    }[st.session_state.prediction]
    
    import plotly.express as px

    st.markdown(
        """
        <p style='text-align: center; color: pink; margin-bottom: -30px; font-weight: bold; font-size: 72px;'>
            🧠 Prediction result:
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
            f"<h3 style='text-align: center;margin-bottom: 30px;font-weight: bold;'><i>You are {st.session_state.confidence}% an...</i></h3>",
            unsafe_allow_html=True
    )

    left, center, right = st.columns([1, 2, 1])  
    with st.container(border=True):
        st.markdown(
                f"<h1 style='text-align: center; margin-bottom: 20px; font-weight: bold; color: {theme_color};'>{st.session_state.prediction}</h1>",
                unsafe_allow_html=True
        )
    st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)

    st.markdown(
        f"<h5 style='text-align: center;margin-bottom: -10px;'>📃 Description:</h3>",
        unsafe_allow_html=True
    )

    if st.session_state.prediction == 'Introvert':
        st.markdown(
            """
            <blockquote style='margin: 0 auto; width: fit-content; border-left: 4px solid #ccc; padding-left: 1em;'>
                <p style='text-align: center; margin: 0;'>
                    Prefers solitary environments and deep thinking. Gains energy from spending time alone.
                </p>
            </blockquote>
            """,
            unsafe_allow_html=True
        )
    elif st.session_state.prediction == 'Ambivert':
        st.markdown(
            """
            <blockquote style='margin: 0 auto; width: fit-content; border-left: 4px solid #ccc; padding-left: 1em;'>
                <p style='text-align: center; margin: 0;'>
                    A balanced mix of introversion and extroversion. Can enjoy social interaction and alone time equally.
                </p>
            </blockquote>
            """,
            unsafe_allow_html=True
        )
    elif st.session_state.prediction == 'Extrovert':
        st.markdown(
            """
            <blockquote style='margin: 0 auto; width: fit-content; border-left: 4px solid #ccc; padding-left: 1em;'>
                <p style='text-align: center; margin: 0;'>
                    Energized by social interactions and external stimulation. Often talkative, outgoing, and enthusiastic.
                </p>
            </blockquote>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:50px;'></div>", unsafe_allow_html=True)
    
    st.markdown(
        f"<h5 style='text-align: center;margin-bottom: -10px;'>🔍 Traits:</h3>",
        unsafe_allow_html=True
    )

    if st.session_state.prediction == 'Introvert':
        st.markdown(
            """
            <div style='display: flex; justify-content: center; align-items: center; height: 100%;'>
                <ul style='text-align: left; list-style-position: inside;'>
                    <li>Enjoys solitude</li>
                    <li>Deep thinker</li>
                    <li>Good listener</li>
                    <li>Avoids social crowds</li>
                    <li>Highly introspective</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif st.session_state.prediction == 'Ambivert':
        st.markdown(
            """
            <div style='display: flex; justify-content: center; align-items: center; height: 100%;'>
                <ul style='text-align: left; list-style-position: inside;'>
                    <li>Flexible in social situations</li>
                    <li>Balanced energy levels</li>
                    <li>Can adapt to different environments</li>
                    <li>Comfortable in groups and alone</li>
                    <li>Intuitive communicator</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    elif st.session_state.prediction == 'Extrovert':
        st.markdown(
            """
            <div style='display: flex; justify-content: center; align-items: center; height: 100%;'>
                <ul style='text-align: left; list-style-position: inside;'>
                    <li>Outgoing and expressive</li>
                    <li>Enjoys being around people</li>
                    <li>Thinks out loud</li>
                    <li>Comfortable in group settings.</li>
                    <li>Energetic and talkative</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("<hr></hr>", unsafe_allow_html=True)
    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

    # Radar Chart
    input_df = st.session_state.user_input.copy()
    normalized_input = input_df / 10.0  # assuming scale is 0-10
    
    fig = px.line_polar(
        normalized_input.T.reset_index(),
        r=normalized_input.T.iloc[:, 0],
        theta=normalized_input.T.index,
        line_close=True,
        title="",
        )
    st.markdown(
        f"<i><h3 style='text-align: center;margin-bottom: -40px;font-weight: bold;'>Your personality trait profile:</h3></i>",
        unsafe_allow_html=True
    )
    st.plotly_chart(fig, use_container_width=True)

    #Feature Importance
    importance = logistics.logreg.coef_[0]
    features = st.session_state.user_input.columns

    # Sort by importance
    sorted_idx = importance.argsort()[::-1][:10]  # Top 10
    top_features = [features[i] for i in sorted_idx]
    top_values = [importance[i] for i in sorted_idx]

    fig, ax = plt.subplots()
    ax.barh(top_features[::-1], top_values[::-1], color='#FF6F61')
    ax.set_xlabel("Importance")
    ax.set_title("Features that contribute the most in swaying the prediction:")
    
    col1, col2, col3, col4, col5 = st.columns([1,1,4,1,1])
    with col3:
        st.pyplot(fig)

        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)

        st.markdown(
        f"<i><h3 style='text-align: center;margin-bottom: -60px;font-weight: bold;'>🔍 How was this prediction made?</h3></i>",
        unsafe_allow_html=True
        )
        st.markdown(
            """
            ###
            The prediction is based on how your trait scores align with patterns learned from a wide range of personality profiles. 

            Each of your answers contributed to a numerical representation of your personality, which was evaluated by a machine learning model trained to recognize personality types based on these patterns.

            The model identified key traits — such as your level of social energy, emotional stability, and preference for routine or spontaneity — and used them to estimate the most likely personality type that fits your profile.

            The bar chart shown above highlights the traits that had the strongest influence on the final prediction.
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    # Back button
    if st.button("Back"):
        st.session_state.page = "form"
        st.rerun()