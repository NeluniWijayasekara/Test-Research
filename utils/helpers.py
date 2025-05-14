import cv2
import numpy as np

def draw_label(image, label, position=(50, 50), font=cv2.FONT_HERSHEY_SIMPLEX, font_scale=1, color=(0, 255, 0), thickness=2):
    """
    Draws a Sinhala label on the given image.

    Args:
        image (ndarray): The image on which the label will be drawn.
        label (str): The label text to display.
        position (tuple): Position to place the label text.
        font (int): Font type (OpenCV).
        font_scale (float): Scale factor for font size.
        color (tuple): Text color in BGR.
        thickness (int): Thickness of the text.

    Returns:
        image (ndarray): Image with the label drawn.
    """
    if image is None:
        raise ValueError("Input image is None. Cannot draw label.")
    cv2.putText(image, label, position, font, font_scale, color, thickness, cv2.LINE_AA)
    return image


def preprocess_image(image):
    """
    Preprocesses the input image to match YOLOv8 requirements.

    Args:
        image (ndarray): Input image (BGR format from OpenCV).

    Returns:
        preprocessed_image (ndarray): Resized, normalized RGB image.
    """
    if image is None:
        raise ValueError("Input image is None. Cannot preprocess.")
    image = cv2.resize(image, (640, 640))
    image = image / 255.0  # Normalize to [0, 1]
    image = image[..., ::-1]  # BGR to RGB
    return image


def postprocess_predictions(predictions, confidence_threshold=0.5):
    """
    Filters YOLOv8 predictions based on a confidence threshold.

    Args:
        predictions (list or ndarray): Raw predictions from the model. Expected format:
                                       [x, y, w, h, confidence, class_id]
        confidence_threshold (float): Minimum confidence to keep a prediction.

    Returns:
        filtered (list): Predictions that meet the threshold.
    """
    filtered = []
    if predictions is None or len(predictions) == 0:
        return filtered

    for pred in predictions:
        if len(pred) >= 6 and pred[4] >= confidence_threshold:
            filtered.append(pred)
    return filtered
