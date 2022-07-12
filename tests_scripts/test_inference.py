import io
import torch
from PIL import Image

# Model
#model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True)
model = torch.hub.load("ultralytics/yolov5", "custom", path = r"C:\Users\prava\Desktop\Flask\yolov5\datasets\today\best.pt", force_reload=True)

# img = Image.open("zidane.jpg")  # PIL image direct open

# Read from bytes as we do in app
with open("1.jpg", "rb") as file:
    img_bytes = file.read()
img = Image.open(io.BytesIO(img_bytes))

results = model(img, size=640)  # includes NMS

print(results.pandas().xyxy[0])
