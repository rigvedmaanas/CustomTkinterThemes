from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="CustomTkinterThemes",
    version="1.0.0",
    description="A theme manager for CustomTkinter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rigvedmaanas/CustomTkinterThemes",
    author="Rigved Maanas",
    author_email="rigvedmaanas@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "customtkinter"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_data={
        "customtkinterthemes": ["themes/*.json", "fonts/*.ttf"],
    }
)
