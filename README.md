
# 📦 PredictFlowAI — ML-Driven Support & Churn Pipeline

PredictFlowAI is an end-to-end data engineering and machine learning pipeline that uses Airflow + MLflow to process product usage and support logs, and predict both support resolution time and customer churn risk.

---

## 🧠 Features
- Synthetic product usage + support log generation
- ETL pipeline with Apache Airflow
- Predictive modeling with scikit-learn
- ML tracking using MLflow
- Streamlit dashboard for prediction
- Power BI dashboard for trend monitoring

---

## 📁 Project Structure
```
predictflowai/
├── dags/                    # Airflow ETL DAG
├── data/                   # CSV files (raw, processed)
├── notebooks/              # Jupyter notebook for modeling
├── models/                 # Trained model pickle files
├── scripts/                # MLflow training script
├── app/                    # Streamlit app
├── mlflow_train_models.py  # Model logging script
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## 🛠️ Setup Instructions

### Run Streamlit App
```bash
streamlit run app/streamlit_predictflowai.py
```

### Run MLflow Tracking
```bash
mlflow ui
python mlflow_train_models.py
```

### Airflow (if dockerized)
```bash
docker-compose up airflow-init
docker-compose up
```

---

## 📊 Power BI
Includes mock file `predictflowai_dashboard_data.csv` to build:
- Avg. resolution time by category
- Churn trends by region
- Usage behavior vs churn

---

## 📦 Author
Built by a data scientist with expertise in data engineering, MLOps, and end-to-end analytics workflows.
