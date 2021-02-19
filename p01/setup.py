import setuptools

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("./cifastapi/VERSION_FULL", "r", encoding="utf-8") as fh:
    version = fh.read()


setuptools.setup(
    name="cifastapi", # Replace with your own username
    version=version,
    author="Jose Ibanez",
    author_email="jose.ibanez@vodafone.com",
    description="test github actions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoseIbanez",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
