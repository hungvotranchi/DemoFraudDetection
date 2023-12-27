import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
import model.model as m
import pandas as pd
import numpy as np

model = m.NeuralNetwork(29)
model.load_state_dict(torch.load("model/ModelNN-CreditFraudDetection.pt"))
model.eval()
USE_GPU = True
dtype = torch.float32
if USE_GPU and torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')


def model_pipeline(data):
    assert data.shape[1] != 29, "The input file need to have 29 attributes as defined"
    data = data.drop(columns=["id"])
    test = []
    for i in range(100):
        temp_data = data.iloc[i].drop(columns=["Class"])
        test.append([[temp_data.to_numpy()[1:-1]], np.array(0)])
    test_data = DataLoader(test, batch_size=64)
    model.eval()  # set model to evaluation mode
    result = {}
    count = 0
    with torch.no_grad():
        for i, (x, y) in enumerate(test_data):
            x_new = torch.stack(x).to(torch.float32).squeeze()
            
            #x = x.to(device=device, dtype=dtype)
            scores = model(x_new)
            _, preds = scores.max(1)
            for i in range(len(preds)):
                result[f"{count}"] = {}
                result[f"{count}"]["label_pred"] = preds[i].item()
                result[f"{count}"]["scores"] = scores[i].tolist()
                count = count + 1
    return result

    