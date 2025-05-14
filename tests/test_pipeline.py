import pytest
from scripts.pipeline import run_pipeline
from utils.label_map import label_map
from scripts.translate import translate_signs

# Test the complete pipeline functionality
def test_run_pipeline():
    # Sample input sign label for pipeline processing
    test_label = "headache"
    
    # Expected result after the pipeline completes
    expected_translation = label_map[test_label]
    
    # Run the pipeline for the given test label
    result = run_pipeline(test_label)
    
    # Check that the result is the correct translation for the sign
    assert result == expected_translation, f"Pipeline failed for {test_label}. Expected: {expected_translation}, but got: {result}"

# Test that the pipeline gracefully handles an invalid label
def test_run_pipeline_invalid_label():
    invalid_label = "unknown_sign"
    
    # Run the pipeline for the invalid label
    result = run_pipeline(invalid_label)
    
    # Assert that the result is None, as the label doesn't exist in the translation map
    assert result is None, f"Pipeline failed for invalid label '{invalid_label}'. Expected None, but got: {result}"

# Test that the pipeline processes multiple labels correctly
def test_run_pipeline_multiple_labels():
    test_labels = ["headache", "fever", "cough", "cold", "chest_pain", "vomiting"]
    expected_translations = [label_map[label] for label in test_labels]
    
    # Run the pipeline for multiple labels and check if results match the expected translations
    for i, label in enumerate(test_labels):
        result = run_pipeline(label)
        assert result == expected_translations[i], f"Pipeline failed for {label}. Expected: {expected_translations[i]}, but got: {result}"

# Test that the pipeline does not return an empty translation for valid labels
def test_run_pipeline_non_empty_result():
    test_labels = ["headache", "fever", "cough", "cold", "chest_pain"]
    
    for label in test_labels:
        result = run_pipeline(label)
        assert len(result) > 0, f"Pipeline result for {label} is empty."

# Test the performance of the pipeline (optional)
def test_run_pipeline_performance():
    import time
    
    test_label = "headache"
    
    # Start the timer
    start_time = time.time()
    
    # Run the pipeline
    result = run_pipeline(test_label)
    
    # End the timer
    end_time = time.time()
    
    # Check if the pipeline runs in a reasonable time (e.g., less than 1 second)
    assert end_time - start_time < 1, f"Pipeline took too long to process. Duration: {end_time - start_time} seconds."

