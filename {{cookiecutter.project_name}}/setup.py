from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.project_name}}",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "scrapy",
    ],
    entry_points={
        "scrapy": [
            "settings = {{cookiecutter.project_name}}.settings",
        ],
    },
)
