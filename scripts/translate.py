"""
Translates detected medical labels into Sinhala sentences using the label map.
"""

from utils.label_map import label_map
from scripts.dummy_detection import simulate_detection


def translate_labels_to_sinhala(labels):
    """
    Translate a list of English labels into Sinhala sentences.

    Args:
        labels (list of str): List of detected English labels.

    Returns:
        list of str: List of translated Sinhala sentences.
    """
    translated = []
    for label in labels:
        sinhala_sentence = label_map.get(label, f"[සිංහලට පරිවර්තනයක් නොමැත: {label}]")
        translated.append(sinhala_sentence)
    return translated


if __name__ == "__main__":
    # Simulate detections
    detected_labels = simulate_detection()

    # Translate to Sinhala
    translated_sentences = translate_labels_to_sinhala(detected_labels)

    # Display results
    print("🩺 Detected Labels:", detected_labels)
    print("🌐 Sinhala Translations:")
    for sentence in translated_sentences:
        print(" -", sentence)
