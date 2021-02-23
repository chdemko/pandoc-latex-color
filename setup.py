"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/chdemko/pandoc-latex-color
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path, makedirs

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open("README.md", encoding="utf-8") as stream:
    LONG_DESCRIPTION = stream.read()

setup(
    name="pandoc-latex-color",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    # The project's description
    description="A pandoc filter for changing color in LaTeX",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    # The project's main homepage.
    url="https://github.com/chdemko/pandoc-latex-color",
    # The project's download page
    download_url="https://github.com/chdemko/pandoc-latex-color/archive/develop.zip",
    # Author details
    author="Christophe Demko",
    author_email="chdemko@gmail.com",
    # Maintainer details
    maintainer="Christophe Demko",
    maintainer_email="chdemko@gmail.com",
    # Choose your license
    license="BSD-3-Clause",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Specify the OS
        "Operating System :: OS Independent",
        # Indicate who your project is intended for
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Filters",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    # What does your project relate to?
    keywords="pandoc filters latex color",
    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    py_modules=["pandoc_latex_color"],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={"console_scripts": ["pandoc-latex-color = pandoc_latex_color:main"]},
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["panflute>=2.0"],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        "dev": ["check-manifest"],
        "test": [
            "black",
            "tox",
            "coverage",
            "pylint",
            "Pygments",
            "radon",
            "mypy",
            "pytest-cov",
        ],
    },
    # packages=find_packages(),
    # include_package_data = True,
)
