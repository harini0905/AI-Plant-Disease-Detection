# 🌱 Plant Disease Detection Using Deep Learning and Generative AI

## 📌 Project Overview

Plant diseases are one of the major challenges affecting agricultural productivity and crop quality. Early identification of diseases helps farmers take timely preventive actions and reduce crop losses.

This project develops an **AI-powered Plant Disease Detection System** using **Deep Learning and Generative AI**. The system analyzes plant leaf images and classifies them into different disease categories using multiple deep learning models.

Four deep learning models were developed and compared:

- Custom CNN
- ResNet50
- EfficientNetB0
- MobileNetV2

The best-performing model is integrated into a **Streamlit web application** for real-time plant disease prediction.

A **Generative AI module using Hugging Face Transformers** is integrated to provide:

- Disease explanation
- Symptoms
- Possible causes
- Treatment recommendations
- Prevention methods

The final application allows users to upload a plant leaf image and receive disease prediction along with AI-generated agricultural guidance.

---

# 🎯 Objectives

- Detect plant diseases automatically from leaf images.
- Build a custom CNN model for image classification.
- Implement transfer learning models.
- Compare different deep learning architectures.
- Select the best-performing model for deployment.
- Integrate Generative AI for disease-related recommendations.
- Develop an interactive Streamlit application.

---

# 🏗️ Project Workflow

```
Leaf Image Upload
        |
        ↓
Image Preprocessing
        |
        ↓
Deep Learning Models
(CNN / ResNet50 / EfficientNetB0 / MobileNetV2)
        |
        ↓
Disease Classification
        |
        ↓
Confidence Score
        |
        ↓
Hugging Face Generative AI
        |
        ↓
Disease Explanation
Treatment & Prevention Advice
        |
        ↓
Streamlit Application
```

---

# 📂 Dataset

## Dataset Used

**New Plant Diseases Dataset (Augmented)**

The dataset contains multiple categories of healthy and diseased plant leaf images.

Dataset includes:

- Healthy leaves
- Diseased leaves
- Multiple crop categories
- Multiple disease classes

---

# 🔄 Data Preprocessing

The following preprocessing techniques were applied:

- Image resizing
- Pixel normalization
- Data augmentation
- Label encoding
- Training and validation split

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Deep Learning Framework

- TensorFlow
- Keras

## Machine Learning Libraries

- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- OpenCV

## Generative AI

- Hugging Face Transformers
- Qwen2.5-7B-Instruct

## Deployment

- Streamlit

## Development Tools

- VS Code
- Jupyter Notebook
- Google Colab

---

# 🧠 Deep Learning Models

## 1. Custom CNN Model

A Convolutional Neural Network was developed as a baseline model.

Architecture:

- Conv2D Layers
- MaxPooling Layers
- Dropout
- Flatten Layer
- Dense Layers
- Softmax Output Layer

---

## 2. ResNet50

Transfer learning model using residual connections to extract deep image features.

Advantages:

- Better feature extraction
- Handles deeper networks
- Reduces vanishing gradient problems

---

## 3. EfficientNetB0

A lightweight transfer learning architecture designed to balance:

- Accuracy
- Model size
- Computational efficiency

---

## 4. MobileNetV2

A lightweight deep learning model optimized for faster inference and deployment.

Advantages:

- Low computational cost
- Suitable for real-time applications
- Faster prediction speed

---

# 📊 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix


| Model | Accuracy |
|------|----------|
| CNN | 92.90% |
| ResNet50 | 15.55% |
| EfficientNetB0 | 2.86% |
| MobileNetV2 | 92.43% |


## Final Model Selection

Based on evaluation results:

**CNN achieved the highest accuracy and was selected as the primary deployment model.**

MobileNetV2 was also evaluated because of its lightweight architecture suitable for deployment.

---

# 🤖 Generative AI Integration

After disease classification, the predicted disease name is passed to a Hugging Face Large Language Model.

## LLM Used

**Qwen2.5-7B-Instruct**

The Generative AI module provides:

- Disease overview
- Symptoms
- Causes
- Treatment recommendations
- Prevention strategies


Example:

```
Disease: Tomato Early Blight

Overview:
A fungal disease affecting tomato plants.

Symptoms:
- Brown spots on leaves
- Yellowing of foliage

Treatment:
- Remove infected leaves
- Apply suitable fungicides

Prevention:
- Maintain proper spacing
- Avoid excess moisture
```

---

# 🚀 Streamlit Application Features

The application provides:

✅ Upload plant leaf image  
✅ Automatic disease prediction  
✅ Confidence score display  
✅ AI-generated disease explanation  
✅ Treatment recommendations  
✅ Prevention guidelines  

---

# 📁 Project Structure

```
Plant-Disease-Detection
│
├── app.py
│
├── Model Evaluation.ipynb
│
├── HuggingFace.ipynb
│
├── models
│   │
│   ├── cnn_model.keras
│   ├── resnet50_final.keras
│   ├── efficientnet_final.keras
│   └── mobilenet_final.keras
│
├── class_names.pkl
│
├── sample_images
│
├── screenshots
│   ├── home_page.png
│   ├── prediction_result.png
│   └── ai_response.png
│
├── requirements.txt
│
└── README.md
```

---

# 📸 Application Screenshots

## 1. Streamlit Home Page

(Add screenshot here)

```
screenshots/home_page.png
```

---

## 2. Leaf Image Upload and Prediction

(Add screenshot here)

```
screenshots/prediction_result.png
```

---

## 3. Generative AI Disease Explanation

(Add screenshot here)

```
screenshots/ai_response.png
```

---

# ▶️ How to Run the Project

## Step 1: Clone Repository

```bash
git clone <repository-url>
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3: Run Streamlit Application

```bash
streamlit run app.py
```

---

## Step 4: Upload Leaf Image

Upload a plant leaf image and get:

- Predicted disease
- Confidence score
- AI-generated explanation
- Treatment and prevention recommendations

---

# 📌 Results

The project successfully combines:

### Computer Vision

Deep learning models identify plant diseases from leaf images.

### Transfer Learning

Pre-trained architectures improve feature extraction and comparison.

### Generative AI

Provides human-friendly explanations and agricultural recommendations.

The system demonstrates how Artificial Intelligence can support faster plant disease identification and decision-making.

---

# 🔮 Future Enhancements

- Mobile application development
- Real-time camera-based disease detection
- Support for more plant varieties
- Multi-language farmer assistance
- Integration with agricultural databases
- Cloud deployment

---

# 👩‍💻 Author

## A Harini

Aspiring Data Scientist | Deep Learning | Generative AI | Python
