from setuptools import setup, find_packages
import os.path

here = os.path.dirname(__file__)

descr_file = os.path.join(here, "README.md")
version_file = os.path.join(here, "src", "startggapi", "__version__.py")

version_info = {}
with open(version_file, "r") as f:
    exec(f.read(), version_info)

dev_requirements = ["coverage", "pre-commit", "pytest", "pytest-cov", "tox", "responses"]

setup(
    name=version_info["__title__"].lower(),
    version=version_info["__version__"],
    packages=find_packages("src", exclude=["test"]),
    package_dir={"": "src"},
    description=f"{version_info['__title__']} is a thin wrapper on top of the StartGG GraphQL APIs",
    long_description="Start.gg GraphQL wrapper",
    author="Lucky Daisy LLC",
    url="https://github.com/Caja-de-Dano/StartGG-API",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    license="MIT",
    install_requires=["requests"],
    extras_require={"dev": dev_requirements},
)
