from pathlib import Path
import re
import json

NEW_VERSION = "4.9.23"

# Update pom.xml
pom = Path("pom.xml")

if pom.exists():
    content = pom.read_text()

    # Replace 4.6.0, 4.6.1, 4.6-java17, 4.6.5-java17, etc.
    content = re.sub(r"4\.6([.-][A-Za-z0-9]+)*", NEW_VERSION, content)

    pom.write_text(content)

# Update mule-artifact.json
artifact = Path("mule-artifact.json")

if artifact.exists():
    data = json.loads(artifact.read_text())

    if "minMuleVersion" in data:
        data["minMuleVersion"] = "4.9.0"

    artifact.write_text(json.dumps(data, indent=2))

print("Runtime upgraded")
