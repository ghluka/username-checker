"""Updates the list of websites in the README
"""

import glob

files = sorted(glob.glob("./src/checkers/*.py", recursive=True))
with open("README.md", "r", encoding="utf-8") as f:
    f_text = f.read()
    md = f_text.split("<!-- Websites start -->")[0]
    md += f"<!-- Websites start -->[{len(files)} total]\n"

    for file in files:
        file = file.replace("\\", "/")
        with open(file, "r", encoding="utf8") as f:
            link = f.readlines()[0].strip().removeprefix("\"\"\"")
        website = file.split("/")[-1].removesuffix(".py").replace("-", ".").capitalize()
        md += f"\n- [{website}]({link})"

    md += "\n\n<!-- Websites end -->"
    md += f_text.split("<!-- Websites end -->")[1]

with open("README.md", "w", encoding="utf-8") as f:
    f.write(md)
