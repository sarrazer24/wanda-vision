def load_model(model_path):
    import joblib
    return joblib.load(model_path)

def preprocess_frame(frame):
    import cv2
    # Resize frame to the required input size for the model
    resized_frame = cv2.resize(frame, (224, 224))
    # Normalize the frame
    normalized_frame = resized_frame / 255.0
    return normalized_frame