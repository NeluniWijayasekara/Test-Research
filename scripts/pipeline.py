"""
Simulates the end-to-end pipeline for medical sign detection and Sinhala translation.
"""

from scripts.dummy_detection import simulate_detection
from scripts.translate import translate_labels_to_sinhala


def run_pipeline():
    """
    Run the simulated medical sign detection pipeline and return translations.

    Returns:
        dict: A dictionary with detected English labels and their Sinhala translations.
    """
    # Step 1: Simulate detections (replace with YOLOv8 in future)
    detected_labels = simulate_detection()

    # Step 2: Translate to Sinhala
    sinhala_translations = translate_labels_to_sinhala(detected_labels)

    # Step 3: Package results
    result = {
        "detected_labels": detected_labels,
        "sinhala_translations": sinhala_translations
    }

    return result


if __name__ == "__main__":
    output = run_pipeline()

    print("🩺 Detected Labels:")
    for label in output["detected_labels"]:
        print(" -", label)

    print("\n🌐 Sinhala Translations:")
    for sentence in output["sinhala_translations"]:
        print(" -", sentence)
