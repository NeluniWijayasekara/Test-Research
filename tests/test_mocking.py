import pytest
from unittest import mock
from utils import helpers
import numpy as np

def test_draw_label_mock_image_write():
    # Mocking the cv2.imwrite function to simulate saving an image without actually doing it
    with mock.patch("cv2.imwrite") as mock_imwrite:
        img = np.zeros((100, 200, 3), dtype=np.uint8)
        result = helpers.draw_label(img.copy(), "Test Label", position=(10, 50))
        
        # Simulate saving the image (mocked version)
        result = helpers.draw_label(img.copy(), "Test Label", position=(10, 50), save_path="test_image.jpg")
        
        # Check that cv2.imwrite was called once
        mock_imwrite.assert_called_once_with("test_image.jpg", result)

def test_preprocess_image_mock_resize():
    # Mocking the cv2.resize function to simulate image resizing
    with mock.patch("cv2.resize") as mock_resize:
        img = np.ones((800, 600, 3), dtype=np.uint8) * 255
        mock_resize.return_value = np.ones((640, 640, 3), dtype=np.uint8) * 255
        
        processed = helpers.preprocess_image(img.copy())
        
        # Assert that resize was called with the right size
        mock_resize.assert_called_once_with(img.copy(), (640, 640))
        assert processed.shape == (640, 640, 3)

def test_postprocess_predictions_mock_filtering():
    # Mocking the actual filtering logic in postprocess_predictions
    with mock.patch("utils.helpers.filter_predictions") as mock_filter:
        predictions = [
            [10, 10, 100, 100, 0.8, "label1"],
            [20, 20, 150, 150, 0.3, "label2"]
        ]
        
        # Simulating filtered predictions
        mock_filter.return_value = [
            [10, 10, 100, 100, 0.8, "label1"]
        ]
        
        filtered = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
        
        # Check that the filtering method was called with the correct parameters
        mock_filter.assert_called_once_with(predictions, confidence_threshold=0.5)
        assert len(filtered) == 1
        assert filtered[0][-1] == "label1"

def test_postprocess_predictions_mock_no_confidence_field():
    # Mocking behavior where the predictions don't contain confidence field
    with mock.patch("utils.helpers.filter_predictions") as mock_filter:
        predictions = [
            [10, 10, 100, 100, "label1"]
        ]
        
        # Simulate that no confidence score is returned
        mock_filter.return_value = []
        
        filtered = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
        
        # Ensure the mock method was called correctly
        mock_filter.assert_called_once_with(predictions, confidence_threshold=0.5)
        assert len(filtered) == 0

def test_draw_label_mock_invalid_font():
    # Mocking the font scaling method in draw_label
    with mock.patch("cv2.putText") as mock_putText:
        img = np.zeros((100, 200, 3), dtype=np.uint8)
        
        # Simulate an invalid font that raises an error
        mock_putText.side_effect = Exception("Font error")
        
        with pytest.raises(Exception):
            helpers.draw_label(img.copy(), "Test Label", position=(10, 50))

def test_preprocess_image_mock_invalid_input():
    # Mocking a situation where preprocess_image gets invalid input
    with mock.patch("utils.helpers.preprocess_image") as mock_preprocess:
        img = "invalid_image"  # Invalid input
        
        mock_preprocess.side_effect = ValueError("Invalid image input")
        
        with pytest.raises(ValueError, match="Invalid image input"):
            helpers.preprocess_image(img)

def test_postprocess_predictions_mock_with_empty_list():
    # Mocking the behavior when an empty list of predictions is passed
    with mock.patch("utils.helpers.filter_predictions") as mock_filter:
        predictions = []
        
        # Simulate no predictions are available
        mock_filter.return_value = []
        
        filtered = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
        
        # Ensure the mock method was called correctly
        mock_filter.assert_called_once_with(predictions, confidence_threshold=0.5)
        assert len(filtered) == 0
