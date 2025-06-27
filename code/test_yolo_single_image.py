from ultralytics import YOLO

model = YOLO("runs/detect/train3/weights/best.pt")





# Perform object detection on an image
results = model("data/test/images/arbys-2022-fdd-39.png")  # Predict on an image
results[0].show()  # Display results

# Export the model to ONNX format for deployment
path = model.export(format="onnx")  # Returns the path to the exported model