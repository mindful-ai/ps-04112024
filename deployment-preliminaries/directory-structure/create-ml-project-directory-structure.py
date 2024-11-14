import os

# Define the project directory and subdirectories
project_structure = {
    'data': {
        'raw': [],
        'processed': [],
        'external': []
    },
    'notebooks': [],
    'src': {
        'data_preprocessing': ['data_cleaning.py'],
        'models': ['train_model.py', 'model_utils.py'],
        'evaluation': ['evaluate.py'],
        'utils': ['helper_functions.py']
    },
    'config': ['config.yaml'],
    'requirements.txt': None,
    'setup.py': None,
    'README.md': None,
    '.gitignore': None
}

def create_project_structure(base_dir, structure):
    """
    Recursively creates directories and files based on the provided structure.

    :param base_dir: Base directory where the project is created
    :param structure: Dictionary representing the project structure
    """
    for name, substructure in structure.items():
        # Create directory
        dir_path = os.path.join(base_dir, name)
        if isinstance(substructure, list):  # If it's a list, create files
            os.makedirs(dir_path, exist_ok=True)
            for file in substructure:
                open(os.path.join(dir_path, file), 'w').close()
        elif isinstance(substructure, dict):  # If it's a dictionary, recursively create subdirectories
            os.makedirs(dir_path, exist_ok=True)
            create_project_structure(dir_path, substructure)
        else:  # If it's a file
            open(dir_path, 'w').close()

# Specify the base directory for the project
base_dir = 'my_ml_project'

# Create the project structure
create_project_structure(base_dir, project_structure)

print(f"Project directory structure created at: {base_dir}")
