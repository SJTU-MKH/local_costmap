import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models



class VMLP(nn.Module):
    def __init__(self, m):
        super(VMLP, self).__init__()
        
        self.fc1 = nn.Linear(m, 64)
        self.relu1 = nn.ReLU()

        self.fc2 = nn.Linear(64, 32)
        self.relu2 = nn.ReLU()

        self.fc3 = nn.Linear(32, 32)
        self.relu3 = nn.ReLU()

    def forward(self, x):
        x = self.relu1(self.fc1(x))
        x = self.relu2(self.fc2(x))
        x = self.fc3(x)
        return x


class TerrainCNN(nn.Module):
    def __init__(self, v_size):
        super(TerrainCNN, self).__init__()

        self.resnet18 = models.resnet18(pretrained=True)
        self.vmlp = VMLP(v_size)

        self.fc = nn.Linear(32+18, 1)
        self.sigmoid = nn.Sigmoid()
    
    def forward(self, x):
        (img, velocity) = x
        img = self.resnet18(img)

        v = self.vmlp(velocity)

        x = torch.cat((img, v), dim=0)
        x = self.sigmoid(self.fc(x))

        return x




