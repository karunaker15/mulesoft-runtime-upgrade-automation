from pathlib import Path
import re
import json

OLD_VERSION = "4.6.0"
NEW_VERSION = "4.9.23"

# Update pom.xml
pom = Path("pom.xml")

if pom.exists():
    content = pom.read_text()
    content = content.replace(OLD_VERSION, NEW_VERSION)
    pom.write_text(content)

# Update mule-artifact.json
artifact = Path("mule-artifact.json")

if artifact.exists():
    data = json.loads(artifact.read_text())

    if data.get("minMuleVersion"):
        data["minMuleVersion"] = NEW_VERSION

    artifact.write_text(json.dumps(data, indent=2))

print("Runtime upgraded")