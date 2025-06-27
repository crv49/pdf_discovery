from ultralytics import YOLO

# DO NOT RUN CODE AGAIN - MODEL TRAINED

# Load a pretrained YOLO11n model
model = YOLO("yolo11n.yaml")

# Train the model on the COCO8 dataset for 100 epochs
train_results = model.train(
    data="config.yaml",  # Path to dataset configuration file
    epochs=30,  # Number of training epochs
    imgsz=640,  # Image size for training
)

# # Evaluate the model's performance on the validation set
# metrics = model.val()

# # Perform object detection on an image
# results = model("path/to/image.jpg")  # Predict on an image
# results[0].show()  # Display results

# # Export the model to ONNX format for deployment
# path = model.export(format="onnx")  # Returns the path to the exported model