from fastapi import FastAPI, Depends
from pydantic import BaseModel
from tensorflow.keras.models import load_model
import joblib
import numpy as np
from sqlalchemy.orm import Session
import database, models

# Initialize FastAPI
app = FastAPI()

# Create Database Tables
models.Base.metadata.create_all(bind=database.engine)

# Load Model & Tokenizer
model = load_model("Research/sentiment_model.h5")
tokenizer = joblib.load("Research/tokenizer.pkl")

# Pydantic Schema for Input
class ReviewRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: ReviewRequest, db: Session = Depends(database.get_db)):
    # Tokenize and pad input
    sequence = tokenizer.texts_to_sequences([request.text])
    sequence = np.array(sequence, dtype=object)  # Convert to NumPy array
    padded_sequence = np.zeros((1, 62))  # Ensure fixed length of 62
    padded_sequence[:, :len(sequence[0])] = sequence[0]

    # Make prediction
    prediction = model.predict(padded_sequence)[0][0]
    sentiment = "positive" if prediction > 0.5 else "negative"
    confidence = float(prediction) if sentiment == "positive" else float(1 - prediction)

    # Save to Database
    db_review = models.Review(text=request.text, sentiment=sentiment, confidence=confidence)
    db.add(db_review)
    db.commit()

    return {"text": request.text, "sentiment": sentiment, "confidence": confidence}

@app.get("/")
def home():
    return {"message": "Amazon Product Sentiment Analysis API"}
