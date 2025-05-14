import pytest
from utils import helpers

def test_draw_label_invalid_type():
    # Pass in an invalid type for the image (e.g., string instead of ndarray)
    with pytest.raises(TypeError):
        helpers.draw_label("invalid_image", "Test Label", position=(10, 50))

def test_preprocess_image_invalid_type():
    # Pass in an invalid type (e.g., string instead of image)
    with pytest.raises(ValueError):
        helpers.preprocess_image("invalid_image")

def test_postprocess_predictions_invalid_type():
    # Pass in a non-list type for predictions
    with pytest.raises(TypeError):
        helpers.postprocess_predictions("invalid_predictions", confidence_threshold=0.5)

def test_postprocess_predictions_invalid_confidence_threshold():
    # Pass in an invalid confidence threshold (non-numeric value)
    predictions = [
        [10, 10, 100, 100, 0.8, "label1"]
    ]
    with pytest.raises(ValueError):
        helpers.postprocess_predictions(predictions, confidence_threshold="high")

def test_draw_label_position_out_of_bounds():
    # Test for label drawing with an out-of-bounds position
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        helpers.draw_label(img, "Out of Bounds", position=(2000, 1000))

def test_preprocess_image_invalid_shape():
    # Provide an image with an invalid shape (e.g., a 1D array instead of 3D)
    img = np.ones((100,), dtype=np.uint8)
    with pytest.raises(ValueError):
        helpers.preprocess_image(img)

def test_draw_label_invalid_color_type():
    # Test passing an invalid color type (not a tuple)
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    with pytest.raises(TypeError):
        helpers.draw_label(img, "Test Label", position=(10, 50), color="invalid_color")

def test_postprocess_predictions_empty_input():
    # Provide an empty list for predictions
    filtered = helpers.postprocess_predictions([], confidence_threshold=0.5)
    assert isinstance(filtered, list)
    assert len(filtered) == 0

def test_preprocess_image_empty_input():
    # Test with an empty input image (None)
    with pytest.raises(ValueError):
        helpers.preprocess_image(None)

def test_draw_label_invalid_font_size():
    # Test for invalid font size that is out of reasonable range
    img = np.zeros((100, 200, 3), dtype=np.uint8)
    with pytest.raises(ValueError):
        helpers.draw_label(img, "Test Label", position=(10, 50), font_size=-1)  # Invalid negative font size

def test_postprocess_predictions_no_confidence_field():
    # Test predictions that don't include a confidence field
    predictions = [
        [10, 10, 100, 100, "label1"]
    ]
    with pytest.raises(IndexError):  # Expecting IndexError because confidence field is missing
        helpers.postprocess_predictions(predictions, confidence_threshold=0.5)
