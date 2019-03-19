import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='uprime',
    version='1.0',
    author="Robert Astel",
    author_email="rob.astel@gmail.com",
    license="Apache License 2.0",
    description="Automatic control chart calculation and plotting for the u'-chart.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Dashlane/uprime",
    packages=find_packages(),
    classifiers=[
            'License :: OSI Approved :: Apache Software License'
    ],
    install_requires=[
        'pandas',
        'matplotlib'
    ]
)