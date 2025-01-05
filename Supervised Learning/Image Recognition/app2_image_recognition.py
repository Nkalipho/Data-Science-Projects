from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

# CIFAR-10 class names
class_names = [
    "airplane", "automobile", "bird", "cat", "deer",
    "dog", "frog", "horse", "ship", "truck"
]

# Load the trained model
model = tf.keras.models.load_model("/home/mthobisi/Desktop/Python Libs/Image_recognition.keras")

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]

    try:
        # Process the image
        image = Image.open(file).convert("RGB")  # Ensure it's in RGB mode
        image = image.resize((32, 32))  # Resize to model input size
        image_array = np.array(image).astype("float32") / 255  # Normalize
        image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension

        # Predict using the model
        prediction = model.predict(image_array)
        predicted_index = int(np.argmax(prediction))
        confidence = float(prediction[0][predicted_index])
        class_name = class_names[predicted_index]  # Get the class name

        return jsonify({"class_name": class_name, "confidence": confidence})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
