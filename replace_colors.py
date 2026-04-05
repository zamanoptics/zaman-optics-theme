import os
import re

replacements = [
    (r"(?i)#AFDCEC", "#FF8C00"),
    (r"(?i)#7FB8CC", "#E07800"),
    (r"(?i)#E8F6FB", "#FFF3E0"),
    (r"rgba\(\s*175\s*,\s*220\s*,\s*236", "rgba(255, 140, 0")
]

for root, _, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for file in files:
        if file.endswith((".css", ".liquid", ".js")):
            path = os.path.join(root, file)
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                continue
                
            new_content = content
            for pattern, repl in replacements:
                new_content = re.sub(pattern, repl, new_content)
                
            if content != new_content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
print("Done color replacement.")

