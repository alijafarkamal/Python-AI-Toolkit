import torch
import torchvision.transforms as transforms
from PIL import Image

# Load pre-trained model
model = torch.hub.load('pytorch/vision', 'vit_b_16', pretrained=True)
model.eval()

# Load and preprocess image
image_path = "path_to_image.jpg"
img = Image.open(image_path).convert("RGB")
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
img_tensor = preprocess(img).unsqueeze(0)

# Generate caption
output = model(img_tensor)
print("Image features:", output)
