import os

# Use the current working directory as the project root
project_root = os.getcwd()

# Define the directory structure
directories = [
    "data/raw",                # Raw input data
    "data/processed",          # Cleaned/processed data
    "notebooks",               # Jupyter notebooks
    "src/eda",                 # EDA scripts
    "src/modeling",            # Modeling scripts
    "src/testing",             # AB/statistical tests
    "src/utils",               # Helper utilities
    "models",                  # Trained models
    "reports",                 # Figures & outputs
    "assets",                  # Images for reports
    ".github/workflows",       # GitHub Actions CI/CD
]

# Define files and initial contents
files = {

    ".gitignore": "data/\n__pycache__/\n.env\n*.pkl\n*.csv\nmodels/\n",
    "requirements.txt": "pandas\nnumpy\nmatplotlib\nseaborn\nscikit-learn\nxgboost\nshap\ndvc\njupyter\n",
    "notebooks/EDA.ipynb": "",
    "notebooks/Modeling.ipynb": "",
    "notebooks/AB_Testing.ipynb": "",
}

# Create the directories
for directory in directories:
    path = os.path.join(project_root, directory)
    os.makedirs(path, exist_ok=True)

# Create the files
for filename, content in files.items():
    path = os.path.join(project_root, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

print("✅ Project structure created successfully in current directory.")
