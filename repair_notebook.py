import json
import re

# Read the corrupted file
with open('chipotle_getting_and_knowing_data_Exercises.ipynb', 'r') as f:
    content = f.read()

# Remove Git merge conflict markers
# Keep the HEAD version (first part)
content = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>.*?\n', r'\1\n', content, flags=re.DOTALL)

# Try to parse and validate
try:
    data = json.loads(content)
    with open('chipotle_getting_and_knowing_data_Exercises.ipynb', 'w') as f:
        json.dump(data, f, indent=1)
    print("✓ File has been repaired successfully!")
except json.JSONDecodeError as e:
    print(f"Could not repair: {e}")
