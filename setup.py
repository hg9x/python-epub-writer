import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-epub-writer",
    version="0.0.2",
    author="Starr Yang",
    author_email="starryangt@gmail.com",
    description="Package for writing epubs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/starryangt/python-epub-writer",
    packages=setuptools.find_packages(),
    install_requires=[
        "beautifulsoup4",
        "aiofiles",
        "aiohttp"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
