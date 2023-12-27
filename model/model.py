import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.utils.data import sampler

class NeuralNetwork(nn.Module):
    def __init__(self, num_features: int):
        super().__init__()
        self.arch = nn.Sequential(
                    nn.Linear(in_features= num_features, out_features= 256),
                    nn.ReLU(),
                    nn.Dropout(0.5),
                    nn.Linear(in_features= 256, out_features= 128),
                    nn.BatchNorm1d(num_features= 128),
                    nn.Dropout(0.5),
                    nn.Linear(in_features= 128, out_features= 2),
                    nn.Sigmoid())
        
    def forward (self, x):
        return self.arch(x)
    
