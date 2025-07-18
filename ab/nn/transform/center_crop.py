import torch
import torchvision.transforms as transforms

def transform(norm):
    return transforms.Compose([
    transforms.CenterCrop(size=48),
    transforms.Resize((64,64)),
    transforms.ToTensor(),
    transforms.Normalize(*norm)
])
