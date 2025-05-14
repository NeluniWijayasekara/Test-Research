import numpy as np
import cv2
import pytest
from utils import helpers

def test_draw_label_returns_image():
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    result = helpers.draw_label(img.copy(), "Test Label", position=(10, 50))
    assert isinstance(result, np.ndarray)
    assert result.shape == img.shape

def test_draw_label_draws_text():
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    result = helpers.draw_label(img.copy(), "Text", position=(10, 50))
    assert not np.array_equal(result, img), "Expected image to be altered by draw_label"

def test_preprocess_image_output_shape():
    img = np.ones((800, 600, 3), dtype=np.uint8) * 255
    processed = helpers.preprocess_image(img.copy())
    assert processed.shape == (640, 640, 3)

def test_preprocess_image_value_range():
    img = np.ones((800, 600, 3), dtype=np.uint8) * 255
    processed = helpers.preprocess_image(img.copy())
    assert processed.max() <= 1.0
    assert processed.min() >= 0.0

def test_postprocess_predictions_filters_by_threshold():
    predictions = [
        [10, 10, 100, 100, 0.8, "label1"],
        [20, 20, 150, 150, 0.3, "label2"]
    ]
    filtered = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
    assert len(filtered) == 1
    assert filtered[0][-1] == "label1"

def test_postprocess_predictions_returns_empty_list_for_low_scores():
    predictions = [
        [10, 10, 100, 100, 0.2, "label1"],
        [20, 20, 150, 150, 0.3, "label2"]
    ]
    filtered = helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
    assert isinstance(filtered, list)
    assert len(filtered) == 0
