## Amazon Product Review Sentiment Analysis
Overview
This project is a machine learning-based sentiment analysis system designed to analyze Amazon product reviews and determine whether they are positive or negative. It features a FastAPI backend for model inference and a Streamlit frontend for user interaction.

Features
✅ Predict Sentiment – Classifies reviews as positive or negative
✅ Confidence Score – Displays how confident the model is in its prediction
✅ Database Storage – Saves user reviews and predictions in a PostgreSQL database
✅ Interactive UI – A Streamlit web app allows users to input reviews and see predictions
✅ FastAPI Backend – Provides a REST API for model inference

Tech Stack
🔹 Machine Learning: TensorFlow/Keras (GRU-based sentiment model)
🔹 Backend: FastAPI (Lightweight and fast API framework)
🔹 Database: PostgreSQL (Stores user reviews and predictions)
🔹 Frontend: Streamlit (User-friendly web interface)
🔹 Deployment: Uvicorn for API, Streamlit for UI

Workflow
1️⃣ User enters a product review via the Streamlit interface.
2️⃣ The text is preprocessed and tokenized using a trained tokenizer.
3️⃣ The model predicts the sentiment (positive/negative) and confidence score.
4️⃣ The result is displayed on the UI and stored in the database.


🎯 This project demonstrates a real-world use case of sentiment analysis for e-commerce applications, helping businesses and customers understand product feedback efficiently. 🚀