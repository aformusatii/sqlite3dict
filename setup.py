import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlite3dict", # Replace with your own username
    version="0.0.3",
    author="aformusatii",
    author_email="aformusatii@gmail.com",
    description="Wrapper around sqlite3 to work with dictionaries",
    long_description=long_description,
    keywords="sqlite sqlite3 json database tinydb nosql sql",
    long_description_content_type="text/markdown",
    url="https://github.com/aformusatii/sqlite3dict",
    packages=setuptools.find_packages(),
    install_requires=[],
    use_2to3=True,
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    # python_requires='>=2.7',
)