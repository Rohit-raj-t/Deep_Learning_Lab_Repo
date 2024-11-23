from PIL import Image, ImageDraw, ImageFont
import requests
import json

# Define the function to draw bounding boxes
def draw_bounding_boxes(image_path, response):
    # Load the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    
    # Define font (adjust path and size if necessary)
    try:
        font = ImageFont.truetype("arial.ttf", 15)
    except IOError:
        font = ImageFont.load_default()

    # Iterate over each detection in the response
    for result in response['images'][0]['results']:
        # Extract bounding box coordinates
        x1 = result['box']['x1']
        y1 = result['box']['y1']
        x2 = result['box']['x2']
        y2 = result['box']['y2']
        class_name = result['name']
        confidence = result['confidence']

        # Draw the bounding box
        draw.rectangle([(x1, y1), (x2, y2)], outline="red", width=3)
        
        # Add label with confidence score
        label = f"{class_name}: {confidence:.2f}"
        text_bbox = draw.textbbox((x1, y1), label, font=font)
        text_background = [text_bbox[0], text_bbox[1], text_bbox[2], text_bbox[3]]
        draw.rectangle(text_background, fill="red")
        draw.text((x1, y1), label, fill="white", font=font)

    # Save or display the image
    img.show()
    img.save("output_with_bboxes.jpg")

# Define the API request
url = "https://predict.ultralytics.com"
headers = {"x-api-key": "API KEY"}
data = {
    "model": "https://hub.ultralytics.com/models/OtSQgcctEkvOMxFGdklK",
    "imgsz": 640,
    "conf": 0.25,
    "iou": 0.45
}

# Open and send the image for inference
image_path = "brain.jpg"
with open(image_path, "rb") as f:
    response = requests.post(url, headers=headers, data=data, files={"file": f})
response.raise_for_status()

# Parse and use the response
response_data = response.json()
draw_bounding_boxes(image_path, response_data)
