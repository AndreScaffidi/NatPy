import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NatPy",
    version="0.1.1",
    author="Tomas Howson and Andre Scaffidi",
    author_email="tomas.howson@adelaide.edu.au, andre.scaffidi@adelaide.edu.au",
    description="Convert the units of particle physics quantities.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreScaffidi/NatPy",
    packages=setuptools.find_packages(),
    install_requires=['numpy', 'astropy'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
