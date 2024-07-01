from django.shortcuts import render, redirect
from send_image_app.forms import ImageForm
import pytorch_lightning as pl
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import cv2

from django.shortcuts import render
from videoset.forms import VideoForm
from videoset.models import Video

cap = cv2.VideoCapture(0)

cap.release()
cv2.destroyAllWindows()

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = VideoForm()
    
    videos = Video.objects.all()
    print(videos,form)
    return render(request, 'upload_video.html', {'form': form, 'videos': videos})

# while True:
#     # 1フレームずつ取得する。
#     ret, frame = cap.read()
#     key = cv2.waitKey(1) & 0xFF
#     # img = cv2.imread(frame)
#     cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     objects = cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=3)
    
#     for(x, y, w, h) in objects:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 200), thickness=3)
        
#     # result.jpgを出力
#     cv2.imwrite("result.png", frame)
#     cv2.imshow('image', frame)
    
#     # qキーが押されたらループを終了する
#     if key == ord('q'):
#         break


