# Central configuration file for customizable parameters

# Model
MODEL_DIR = "model"
MODEL_FILENAME = "best.pt"
MODEL_PATH = f"{MODEL_DIR}/{MODEL_FILENAME}"

# Confidence Threshold
CONFIDENCE_THRESHOLD = 0.5  # Change to suit your requirement (0 to 1)

# Image preprocessing
INPUT_IMAGE_WIDTH = 640
INPUT_IMAGE_HEIGHT = 640
INPUT_IMAGE_SIZE = (INPUT_IMAGE_WIDTH, INPUT_IMAGE_HEIGHT)

# Display settings
LABEL_FONT = 0  # cv2.FONT_HERSHEY_SIMPLEX
LABEL_FONT_SCALE = 1.0
LABEL_FONT_COLOR = (0, 255, 0)  # Green
LABEL_FONT_THICKNESS = 2
LABEL_POSITION = (30, 50)  # Top-left position for label text

# Label map
LABEL_MAP_PATH = "utils/label_map.py"
SUPPORTED_LANGUAGES = ["si"]  # Currently only Sinhala (extendable)

# Logging
LOG_DIR = "logs"
