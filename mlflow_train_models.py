
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_absolute_error, classification_report
import pandas as pd

df = pd.read_csv("data/processed/merged_logs.csv")

# === REGRESSION TASK: Resolution Time ===
X_reg = pd.get_dummies(df[['priority', 'issue_category', 'region']], drop_first=True)
y_reg = df['resolved_in_hours']
X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)

reg_model = RandomForestRegressor(n_estimators=100, random_state=42)

with mlflow.start_run(run_name="ResolutionTime_RF"):
    reg_model.fit(X_train_r, y_train_r)
    y_pred_r = reg_model.predict(X_test_r)
    mae = mean_absolute_error(y_test_r, y_pred_r)

    mlflow.log_param("model_type", "RandomForestRegressor")
    mlflow.log_metric("mae", mae)
    mlflow.sklearn.log_model(reg_model, "resolution_model")

# === CLASSIFICATION TASK: Churn Risk ===
X_cls = df[['avg_session_length_min', 'feature_clicks', 'days_active_last_30']]
y_cls = df['churn_risk']
X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)

with mlflow.start_run(run_name="ChurnRisk_RF"):
    clf.fit(X_train_c, y_train_c)
    y_pred_c = clf.predict(X_test_c)

    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("accuracy", clf.score(X_test_c, y_test_c))
    mlflow.sklearn.log_model(clf, "churn_model")
