from django.shortcuts import render, redirect
from send_image_app.forms import ImageForm
import pytorch_lightning as pl
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from torchvision.models import resnet18
from sklearn.metrics import accuracy_score
from torcheval.metrics.functional import multiclass_accuracy



def image_upload(request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_name = request.FILES['image']
            img_url = f'media/documents/{img_name}'

        return predict_image(request, img_name, img_url)
    else:
        form = ImageForm()
    return render(request, 'index2.html' , {'form': form}) 

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from PIL import Image
import io
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms


# 学習済みモデルのパス

model_path = 'send_image_app/a_model/model_horse_sleep.pth'

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv = nn.Conv2d(3, 3, 3, padding=1)
        self.bn = nn.BatchNorm2d(3)
        self.fc = nn.Linear(37632, 2)

    def forward(self, x):
        x = self.conv(x)
        x = F.relu(x)
        x = self.bn(x)
        x = F.max_pool2d(x, 2, 2)
        x = x.view(-1, 37632)
        x = self.fc(x)
        return x


@csrf_exempt
def predict_image(request, image, img_url):
    image.seek(0)  # ファイルの先頭に戻す
    img = Image.open(io.BytesIO(image.read())).convert('RGB')
    print(img)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    img = transform(img).unsqueeze(0)
    
    model = Net()
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    
    with torch.no_grad():
        output = model(img)
    print("Transformed image tensor shape:", img.shape)
    
    output = model(img)
    print("Model output:", output)
    predicted_class = torch.argmax(output).item()
    
    img_name = request.FILES['image']
    img_url = 'media/documents/{}'.format(img_name)
    
    
    predicted_class = torch.argmax(output).item()
    print(predicted_class)
    if predicted_class == 0:
        prediction = "異常です（お腹を見てます）"
    elif predicted_class == 1:
        prediction = "正常です"
    else:
        prediction = "Unknown"
        


        
    return render(request, 'result.html', {'prediction': prediction , 'img_url': img_url, })


