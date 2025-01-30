from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="interfolio_api",
    version="0.92",
    description="A Python client for Interfolio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rice-University-Academic-Affairs/Interfolio-API",
    author="Rice University Office of the Vice Provost of Academic Affairs",
    author_email="vpaa@rice.edu",
    packages=["interfolio_api"],
    zip_safe=False,
    install_requires=["requests"],
)
