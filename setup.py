import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqlite3dict", # Replace with your own username
    version="1.0.1",
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
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Utilities",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent"
    ]
)