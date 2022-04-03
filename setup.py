import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tkintermd",
    version="0.0.3",
    description="A Python based Markdown editor with HTML preview",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hreikin/tkintermd",
    author="hreikin",
    author_email="hreikin@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["tkintermd"],
    include_package_data=True,
    install_requires=["markdown", "pygments", "tkinterweb"],
    entry_points={
        "console_scripts": [
            "tkintermd=tkintermd.__main__:main",
        ]
    },
)
