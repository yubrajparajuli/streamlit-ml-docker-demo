# Streamlit ML + Docker Demo

A simple machine learning project built to learn Streamlit and Docker.

---

## Tech Stack

- Python
- Scikit-learn
- Streamlit
- Docker

---

## Run Locally


pip install -r requirements.txt
python train_model.py
streamlit run main.py

---

## Run with Docker

docker build -t streamlit-demo .  
docker run -p 8501:8501 streamlit-demo
