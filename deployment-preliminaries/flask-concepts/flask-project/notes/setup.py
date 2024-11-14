from setuptools import setup, find_packages

setup(
    name="ml_regression_project",
    version="0.1.0",
    description="A machine learning regression model for predicting housing prices",
    author="Your Name",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "joblib",
        "pandas",
        "scikit-learn"
    ],
    entry_points={
        "console_scripts": [
            "run_app=app.app:main",
            "train_model=train:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
