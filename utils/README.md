# 🛠️ Utils Module

This folder contains utility modules used throughout the project to support sign detection and translation in Sinhala. These scripts handle reusable logic, mappings, and preprocessing/postprocessing steps to keep the main code clean and modular.

---

## 📂 Files Overview

### `label_map.py`

Provides a dictionary mapping of medical sign labels (e.g., `headache`, `fever`) to their respective **Sinhala sentence translations**.

#### ✅ Example:

```python
from utils.label_map import label_map

label = "headache"
sinhala_text = label_map[label]  # Output: "මගේ හිස වේදනාව"
