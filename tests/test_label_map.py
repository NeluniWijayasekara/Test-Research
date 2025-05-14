import pytest
from utils.label_map import label_map

# Test that all medical conditions have corresponding Sinhala translations
def test_label_map_contains_all_keys():
    expected_keys = [
        "headache", "fever", "cough", "cold", "chest_pain", "vomiting", "diarrhea",
        "back_pain", "joint_pain", "stomachache", "dizziness", "tiredness", "sore_throat",
        "toothache", "eye_pain"
    ]
    for key in expected_keys:
        assert key in label_map, f"Missing translation for key: {key}"

# Test that all labels have correct translations
def test_label_map_translations():
    translation_tests = {
        "headache": "මගේ හිස වේදනාව",
        "fever": "මට උණක් තියෙනවා",
        "cough": "මට කැස්සක් තියෙනවා",
        "cold": "මට සෙරිනවා",
        "chest_pain": "මට නැවතීමක් තියෙනවා",
        "vomiting": "මට වමනයක් එනවා",
        "diarrhea": "මට පිටවීමක් තියෙනවා",
        "back_pain": "මට පිට වේදනාවක් තියෙනවා",
        "joint_pain": "මට සංධි වේදනාවක් තියෙනවා",
        "stomachache": "මට බඩ කැක්කුමක් තියෙනවා",
        "dizziness": "මට හිසරදයක් තියෙනවා",
        "tiredness": "මට පසුබැසීමක් හෝ මහන්සියක් ඇති",
        "sore_throat": "මට ගිලන්බෙර වේදනාවක් තියෙනවා",
        "toothache": "මට දත් වේදනාවක් තියෙනවා",
        "eye_pain": "මට ඇස් වේදනාවක් තියෙනවා"
    }
    for label, sinhala_translation in translation_tests.items():
        assert label_map[label] == sinhala_translation, f"Translation for {label} is incorrect"

# Test for missing or mismatched translation
def test_label_map_no_mismatches():
    for label, translation in label_map.items():
        assert isinstance(label, str), f"Label should be a string, but found {type(label)}"
        assert isinstance(translation, str), f"Translation should be a string, but found {type(translation)}"
        assert len(translation) > 0, f"Translation for {label} is empty"

# Test that label_map is a dictionary
def test_label_map_is_dict():
    assert isinstance(label_map, dict), "label_map should be a dictionary"

