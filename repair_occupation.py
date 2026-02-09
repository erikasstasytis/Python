import json
import re

# Read the corrupted file
with open('occupation_getting_and_knowing_data_Exercises.ipynb', 'r') as f:
    content = f.read()

# Remove Git merge conflict markers
content = re.sub(r'<<<<<<< HEAD\n(.*?)\n=======\n.*?\n>>>>>>.*?\n', r'\1\n', content, flags=re.DOTALL)

# Try to parse and validate
try:
    data = json.loads(content)
    with open('occupation_getting_and_knowing_data_Exercises.ipynb', 'w') as f:
        json.dump(data, f, indent=1)
    print("✓ Occupation exercises file has been repaired successfully!")
except json.JSONDecodeError as e:
    print(f"Could not repair: {e}")
