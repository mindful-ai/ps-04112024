import os

# Define the project directory structure
project_structure = {
    "ml_regression_project": [
        "README.md",
        "requirements.txt",
        "setup.py",
        "train.py",
        "MANIFEST.in",
        {
            "app": [
                "__init__.py",
                "app.py",
                "model.py",
                {
                    "templates": [
                        "index.html"
                    ]
                }
            ]
        },
        {
            "config": [
                "config.yaml",
                "__init__.py"
            ]
        },
        {
            "data": [
                "housing.csv",
                "__init__.py"
            ]
        },
        {
            "models": [
                "model.pkl",
                "__init__.py"
            ]
        },
        {
            "notebooks": [
                "data_preparation.ipynb"
            ]
        },
        {
            "static": [
                "style.css",
                "__init__.py"
            ]
        },
        {
            "ml_regression_project": [
                "__init__.py",
                "version.py"
            ]
        },
        {
            "tests": [
                "test_app.py"
            ]
        }
    ]
}

def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, dict):
            for folder, contents in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, contents)
        else:
            file_path = os.path.join(base_path, item)
            # Create an empty file
            with open(file_path, 'w') as f:
                if file_path.endswith(".py"):
                    f.write("# Placeholder for {}\n".format(item))
                elif file_path == os.path.join(base_path, "README.md"):
                    f.write("# ml_regression_project\n\nMachine Learning Regression Project\n")

# Create the project structure
create_structure(".", project_structure)

print("Directory structure created successfully!")
