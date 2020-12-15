import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="",
    version="0.1.1",
    author="Isaac Griffith",
    author_email="grifisaa@isu.edu",
    description="",
    long_description=long_description,
    url="https://github.com/xrese/avista-predictive-maintenance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)