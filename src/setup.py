from setuptools import setup

setup(
    name="interfolio_api",
    version="0.1",
    description="A Python client for Interfolio",
    url="https://github.com/Rice-University-Academic-Affairs/Interfolio-API",
    author="Rice University Office of the Vice Provost of Academic Affairs",
    author_email="vpaa@rice.edu",
    packages=["interfolio_api"],
    zip_safe=False,
    install_requires=["requests"],
)
