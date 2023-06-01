import pathlib

from setuptools import find_packages, setup

from src.color_explo import __DESCRIPTION__, __PACKAGE_NAME__, __VERSION__

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

with open(here / "requirements.txt", "r") as requirements_file:
    install_requires = [
        requirement.strip()
        for requirement in requirements_file.readlines()
        if (requirement.strip() and requirement.strip()[:1] != "#")
    ]


setup(
    name=__PACKAGE_NAME__,
    version=".".join([str(v) for v in __VERSION__]),
    description=__DESCRIPTION__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="JBocage",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=install_requires,
    entry_points={"console_scripts": ["c-explo = color_explo.cli.main:cli"]},
)
