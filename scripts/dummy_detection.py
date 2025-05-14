"""
Simulates the detection of medical signs for testing purposes.

This module mimics the output of a real detection model by returning
a predefined list of medical condition labels in English.
"""

def simulate_detection():
    """
    Simulates detection results by returning a hardcoded list of medical labels.

    Returns:
        list[str]: List of simulated detected medical labels.
    """
    simulated_labels = [
        "headache",
        "fever",
        "cough",
        "stomachache",
        "tiredness"
    ]
    return simulated_labels


if __name__ == "__main__":
    # For quick testing
    detections = simulate_detection()
    print("Simulated detections:", detections)
