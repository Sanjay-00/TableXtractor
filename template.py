import os

PROJECT_NAME = "TableXtractor"

structure = {
    PROJECT_NAME: [
        "app.py",
        "requirements.txt",
        "README.md",
        ".gitignore",
        "outputs/",
        "sample_pdfs/",
        "tests/",
        "src/",
        "src/__init__.py",
        "src/pdf_utils.py",
        "src/excel_writer.py"
    ]
}

default_gitignore = """__pycache__/
outputs/
*.pyc
*.xlsx
*.log
.env
.streamlit/
"""

readme_content = f"# 📄 {PROJECT_NAME.replace('-', ' ').title()}\n\nStreamlit app to extract tables from PDFs and export to Excel.\n"

def create_project():
    for base, items in structure.items():
        if not os.path.exists(base):
            os.mkdir(base)
            print(f"📁 Created project folder: {base}")
        os.chdir(base)
        for item in items:
            if item.endswith("/"):
                os.makedirs(item, exist_ok=True)
                print(f"📁 Created folder: {item}")
            else:
                with open(item, "w", encoding="utf-8") as f:  # FIXED ENCODING
                    if item == ".gitignore":
                        f.write(default_gitignore)
                    elif item == "README.md":
                        f.write(readme_content)
                    else:
                        f.write("")  # empty file
                print(f"📄 Created file: {item}")
        break  # only 1 project level

if __name__ == "__main__":
    create_project()
    print("\n✅ Project scaffold generated successfully!")
