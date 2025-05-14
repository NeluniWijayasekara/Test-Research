# This file is required to treat the utils directory as a Python package.
# It can remain empty or contain initialization code that should run when
# the package is imported.

# Importing modules for direct access when importing utils.
from .label_map import label_map
from .helpers import draw_label, preprocess_image, postprocess_predictions

# Optional: If need to initialize any variables or configurations
# for package, can do it here.

# Example: Defining default configurations
config = {
    "image_size": (640, 640),               # Default image size for preprocessing
    "confidence_threshold": 0.5,            # Default confidence threshold for predictions
    "font": "cv2.FONT_HERSHEY_SIMPLEX",     # Default font for labels in draw_label
    "font_scale": 1,                        # Default font scale for labels
    "color": (0, 255, 0),                   # Default label color (Green in BGR)
    "thickness": 2                          # Default thickness for label text
}

# Can add other initialization or global variables as needed.

# Example: Defining a simple function that might be used across the utils package
def initialize():
    print("Initializing utils module...")
    print(f"Configuration: {config}")

# Initialization code could also be added here if any initial setup or logging is required
# For instance, we could print out the configuration when the package is imported:

initialize()
