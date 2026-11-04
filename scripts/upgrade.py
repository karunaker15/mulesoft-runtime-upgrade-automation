from pathlib import Path
import re
import json

# Update pom.xml
pom = Path("pom.xml")

if pom.exists():
    content = pom.read_text()

    # Update mule runtime versions
    content = re.sub(
        r"4\.6([.-][A-Za-z0-9]+)*",
        "4.9.23",
        content
    )

    # Update mule maven plugin version
    content = re.sub(
        r"<mule\.maven\.plugin\.version>.*?</mule\.maven\.plugin\.version>",
        "<mule.maven.plugin.version>4.9.1</mule.maven.plugin.version>",
        content,
        flags=re.DOTALL
    )

    # cloudHubDeployment
    pattern = r"<cloudHubDeployment>(.*?)</cloudHubDeployment>"

    def update_cloudhub(match):
        block = match.group(0)

        if "<javaVersion>" not in block:
            block = block.replace(
                "</cloudHubDeployment>",
                "    <javaVersion>17</javaVersion>\n</cloudHubDeployment>"
            )

        if "<releaseChannel>" not in block:
            block = block.replace(
                "</cloudHubDeployment>",
                "    <releaseChannel>LTS</releaseChannel>\n</cloudHubDeployment>"
            )

        return block

    content = re.sub(
        pattern,
        update_cloudhub,
        content,
        flags=re.DOTALL
    )

    # cloudhub2Deployment
    pattern = r"<cloudhub2Deployment>(.*?)</cloudhub2Deployment>"

    def update_cloudhub2(match):
        block = match.group(0)

        if "<javaVersion>" not in block:
            block = block.replace(
                "</cloudhub2Deployment>",
                "    <javaVersion>17</javaVersion>\n</cloudhub2Deployment>"
            )

        if "<releaseChannel>" not in block:
            block = block.replace(
                "</cloudhub2Deployment>",
                "    <releaseChannel>LTS</releaseChannel>\n</cloudhub2Deployment>"
            )

        return block

    content = re.sub(
        pattern,
        update_cloudhub2,
        content,
        flags=re.DOTALL
    )

    pom.write_text(content)

# Update mule-artifact.json
artifact = Path("mule-artifact.json")

if artifact.exists():
    data = json.loads(artifact.read_text())

    data["minMuleVersion"] = "4.9.0"

    artifact.write_text(json.dumps(data, indent=2))

print("Runtime upgraded")
