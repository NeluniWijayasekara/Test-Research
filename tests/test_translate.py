import pytest
from scripts.translate import translate_signs
from utils.label_map import label_map

# Test that translate_signs function returns correct translation for each sign label
def test_translate_signs():
    test_labels = [
        "headache", "fever", "cough", "cold", "chest_pain", "vomiting", "diarrhea",
        "back_pain", "joint_pain", "stomachache", "dizziness", "tiredness", "sore_throat",
        "toothache", "eye_pain"
    ]
    
    for label in test_labels:
        translated_text = translate_signs(label)
        expected_translation = label_map[label]
        assert translated_text == expected_translation, f"Translation for {label} is incorrect. Expected: {expected_translation}, but got: {translated_text}"

# Test that the translate_signs function handles unknown labels gracefully
def test_translate_signs_invalid_label():
    invalid_label = "unknown_sign"
    result = translate_signs(invalid_label)
    assert result is None, f"Expected None for invalid label '{invalid_label}', but got: {result}"

# Test that the translate_signs function returns a string type for valid labels
def test_translate_signs_output_type():
    test_labels = [
        "headache", "fever", "cough", "cold", "chest_pain", "vomiting", "diarrhea",
        "back_pain", "joint_pain", "stomachache", "dizziness", "tiredness", "sore_throat",
        "toothache", "eye_pain"
    ]
    
    for label in test_labels:
        translated_text = translate_signs(label)
        assert isinstance(translated_text, str), f"Expected string output for label '{label}', but got: {type(translated_text)}"

# Test that the translate_signs function does not return an empty string
def test_translate_signs_non_empty():
    test_labels = [
        "headache", "fever", "cough", "cold", "chest_pain", "vomiting", "diarrhea",
        "back_pain", "joint_pain", "stomachache", "dizziness", "tiredness", "sore_throat",
        "toothache", "eye_pain"
    ]
    
    for label in test_labels:
        translated_text = translate_signs(label)
        assert len(translated_text) > 0, f"Translation for {label} is empty."

