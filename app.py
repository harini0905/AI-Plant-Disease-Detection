# ==========================================================
# AI PLANT DISEASE DETECTION SYSTEM
# Deep Learning + Hugging Face Generative AI
# ==========================================================


# ============================
# IMPORT LIBRARIES
# ============================

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import pickle
import os

from huggingface_hub import InferenceClient
from dotenv import load_dotenv


# ============================
# PAGE CONFIGURATION
# ============================

st.set_page_config(
    page_title="AI Plant Disease Detection",
    page_icon="🌿",
    layout="wide"
)


# ============================
# HUGGING FACE CONFIGURATION
# ============================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN is None:
    st.error("❌ Hugging Face token not found. Check your .env file")


client = InferenceClient(
    api_key=HF_TOKEN
)



# ============================
# TITLE
# ============================

st.title("🌿 AI Plant Disease Detection System")

st.write("""
Upload a plant leaf image to detect diseases using Deep Learning
and receive AI-generated treatment recommendations.
""")


# ============================
# LOAD ResNet50 MODEL
# ============================

@st.cache_resource
def load_model():

    model = tf.keras.models.load_model(
        "resnet50_best.keras"
    )

    return model



model = load_model()



# ============================
# LOAD CLASS NAMES
# ============================

@st.cache_resource
def load_class_names():

    with open(
        "class_names.pkl",
        "rb"
    ) as f:

        class_names = pickle.load(f)

    return class_names



class_names = load_class_names()


# ============================
# SIDEBAR
# ============================

st.sidebar.title("🌿 Navigation")


menu = st.sidebar.radio(
    "Select Option",
    [
        "🏠 Home",
        "🔍 Predict Disease",
        "ℹ️ About"
    ]
)



# ============================
# HOME PAGE
# ============================


if menu == "🏠 Home":

    st.success("✅ ResNet50 Model Loaded Successfully")
    st.success(f"✅ Total Disease Classes : {len(class_names)}")

    st.header(
        "Welcome to AI Plant Disease Detection System"
    )


    st.write("""
This application detects plant diseases using a ResNet50 Deep Learning
model and provides AI-generated disease explanations using
Hugging Face Large Language Models.
""")


    st.subheader("✨ Features")


    st.markdown("""
- 🌱 Upload plant leaf image
- 🧠 ResNet50-based disease classification
- 📊 Confidence score prediction
- 🤖 Hugging Face AI explanation
- 🌿 Treatment recommendations
- 🛡 Prevention tips
""")



# ============================
# PREDICTION PAGE
# ============================


elif menu == "🔍 Predict Disease":


    st.header(
        "📷 Upload Plant Leaf Image"
    )


    uploaded_file = st.file_uploader(
        "Choose Leaf Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )


    if uploaded_file:


        image = Image.open(uploaded_file)


        st.image(
            image,
            caption="Uploaded Leaf Image",
            use_container_width=True
        )


        if st.button(
            "🔍 Predict Disease"
        ):



            with st.spinner(
                "Predicting Disease..."
            ):


                # Image preprocessing

                from tensorflow.keras.applications.resnet50 import preprocess_input

                img = image.convert("RGB")
                img = img.resize((224, 224))

                img_array = np.array(img, dtype=np.float32)

                img_array = np.expand_dims(img_array, axis=0)

                img_array = preprocess_input(img_array)



                prediction = model.predict(
                    img_array
                )



                predicted_index = np.argmax(
                    prediction
                )


                predicted_disease = class_names[
                    predicted_index
                ]


                confidence = (
                    prediction[0][predicted_index]
                    *100
                )



            # ============================
            # RESULT
            # ============================


            st.success(
                "✅ Prediction Completed"
            )


            st.subheader(
                "🦠 Predicted Disease"
            )


            st.write(
                predicted_disease
            )



            st.subheader(
                "📊 Confidence Score"
            )


            st.progress(
                float(confidence/100)
            )


            st.write(
                f"Confidence: {confidence:.2f}%"
            )



            # ============================
            # HUGGING FACE RESPONSE
            # ============================


            st.subheader(
                "🤖 AI Disease Explanation"
            )


            prompt = f"""

Disease: {predicted_disease}


Explain:

1. Disease Overview
2. Symptoms
3. Causes
4. Recommended Treatment
5. Prevention Tips


Use simple farmer-friendly language.

"""



            with st.spinner(
                "Generating AI Recommendation..."
            ):


                try:


                    response = client.chat.completions.create(

                        model=
                        "Qwen/Qwen2.5-7B-Instruct",


                        messages=[

                            {
                                "role":"user",
                                "content":prompt
                            }

                        ],


                        max_tokens=500

                    )



                    ai_response = (
                        response
                        .choices[0]
                        .message
                        .content
                    )



                    st.success(
                        "✅ AI Recommendation Generated"
                    )


                    st.write(
                        ai_response
                    )



                except Exception as e:


                    st.error(
                        f"Hugging Face Error: {e}"
                    )




            # ============================
            # MODEL DETAILS
            # ============================


            st.divider()


            st.subheader(
                "📊 Model Information"
            )


            st.write("""

**Deployment Model:** ResNet50


**Models Compared:**

1. Custom CNN
2. ResNet50
3. EfficientNetB0
4. MobileNetV2


**Input Image Size:** 224 × 224


**Task:** Multi-class Plant Disease Classification

""")



            col1,col2 = st.columns(2)



            with col1:

                st.metric(
                    "Disease",
                    predicted_disease
                )


            with col2:

                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )



# ============================
# ABOUT PAGE
# ============================


elif menu == "ℹ️ About":


    st.header(
        "🌱 About Project"
    )


    st.write("""

This AI Plant Disease Detection System combines:

### Deep Learning
- CNN
- ResNet50
- EfficientNetB0
- MobileNetV2


### Generative AI
- Hugging Face Transformers
- Qwen2.5-7B-Instruct


### Deployment
- Streamlit


Workflow:

Leaf Image
↓
Image Processing
↓
ResNet50 Prediction
↓
Disease Name
↓
Hugging Face AI Explanation


""")


# ============================
# FOOTER
# ============================


st.divider()


st.caption(
"🌿 AI Plant Disease Detection System | "
"Deep Learning + Generative AI"
)