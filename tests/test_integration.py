import pytest
import numpy as np
from utils import helpers
from scripts import pipeline
import cv2

def test_integration_draw_label_and_preprocess_image():
    # Test the integration of draw_label and preprocess_image
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    
    # Apply draw_label
    labeled_img = helpers.draw_label(img.copy(), "Test Label", position=(10, 50))
    
    # Apply preprocess_image
    processed_img = helpers.preprocess_image(labeled_img)
    
    # Check that the processed image has the correct shape
    assert processed_img.shape == (640, 640, 3)
    
    # Check that the image is altered by draw_label
    assert not np.array_equal(processed_img, img)

def test_integration_postprocess_predictions_with_pipeline():
    # Test integration of postprocess_predictions and pipeline
    predictions = [
        [10, 10, 100, 100, 0.8, "label1"],
        [20, 20, 150, 150, 0.3, "label2"]
    ]
    
    # Run the pipeline's prediction post-processing
    processed_predictions = pipeline.process_predictions(predictions, confidence_threshold=0.5)
    
    # Check that the output is correctly filtered
    assert len(processed_predictions) == 1
    assert processed_predictions[0][-1] == "label1"

def test_integration_pipeline_with_realistic_data():
    # Test integration of the pipeline with realistic data
    img = np.ones((800, 600, 3), dtype=np.uint8) * 255
    labels = ["label1", "label2"]
    
    # Apply preprocessing
    preprocessed_img = helpers.preprocess_image(img.copy())
    
    # Simulate post-processing (mock predictions)
    predictions = [
        [10, 10, 100, 100, 0.9, "label1"],
        [20, 20, 150, 150, 0.4, "label2"]
    ]
    
    # Process predictions
    processed_predictions = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
    
    # Verify that the processed predictions contain only high confidence entries
    assert len(processed_predictions) == 1
    assert processed_predictions[0][-1] == "label1"
    
    # Simulate drawing labels on image (mocking for testing integration)
    for prediction in processed_predictions:
        preprocessed_img = helpers.draw_label(preprocessed_img, prediction[-1], position=(prediction[0], prediction[1]))
    
    # Final check that the image has been altered
    assert not np.array_equal(preprocessed_img, img)

def test_integration_end_to_end_pipeline():
    # Simulate an end-to-end test involving preprocess, prediction, and draw_label integration
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    
    # Simulate preprocessing the image (resize to 640x640)
    preprocessed_img = helpers.preprocess_image(img)
    assert preprocessed_img.shape == (640, 640, 3)
    
    # Simulate generating predictions (mock predictions)
    predictions = [
        [10, 10, 100, 100, 0.9, "label1"],
        [20, 20, 150, 150, 0.6, "label2"]
    ]
    
    # Simulate post-processing predictions with a threshold of 0.5
    filtered_predictions = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
    assert len(filtered_predictions) == 2  # Both predictions should be included
    
    # Draw the labels on the image
    for prediction in filtered_predictions:
        preprocessed_img = helpers.draw_label(preprocessed_img, prediction[-1], position=(prediction[0], prediction[1]))
    
    # Check if the image has been changed by label drawing
    assert not np.array_equal(preprocessed_img, img)

def test_integration_pipeline_with_invalid_data():
    # Test the entire pipeline with invalid data and handle exceptions
    img = "invalid_image"
    
    with pytest.raises(ValueError, match="Invalid image input"):
        preprocessed_img = helpers.preprocess_image(img)
        
    predictions = [
        [10, 10, 100, 100, "label1"]
    ]
    
    with pytest.raises(ValueError, match="Invalid prediction format"):
        processed_predictions = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
        
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    with pytest.raises(Exception, match="Font error"):
        helpers.draw_label(img, "Test Label", position=(10, 50))
