from setuptools import setup, find_packages

setup(
    name="hustle_forge",
    version="0.1.0",
    description="0-budget AI side-hustle toolkit — generate a full business kit offline.",
    packages=find_packages(),
    include_package_data=True,
    package_data={"hustle_forge": ["data/*.json", "templates/*.md"]},
    python_requires=">=3.8",
    entry_points={"console_scripts": ["hustle_forge=hustle_forge.cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
