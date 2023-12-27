# DemoFraudDetection
Code for demo fraud detection. </br>
Note: This version is only for local-run only. I have some problems with deploying API to Google Cloud Platform.</br>
**Running fastAPI** </br>
```
conda activate {your_env}
uvicorn main:app -reload
```
**Running Gradio app** </br>
```
conda activate {your_env}
python Interface.py
```