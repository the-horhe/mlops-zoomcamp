import mlflow
import pickle

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment("mage-nyc-taxi-experiment")

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    lr, dv = data

    with mlflow.start_run():
        mlflow.sklearn.log_model(lr, artifact_path="models")
        with open("dv.bin", "wb") as f:
            pickle.dump(dv, f)
        mlflow.log_artifacts("dv.bin", artifact_path="models/dv")
    
    print("Done")
