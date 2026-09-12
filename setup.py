from pathlib import Path
import re
from setuptools import find_packages, setup

ROOT = Path(__file__).parent
VERSION = re.search(
    r"__version__\s*=\s*[\'\"]([^\'\"]+)",
    (ROOT / "ecopy" / "__init__.py").read_text(encoding="utf-8"),
).group(1)

setup(
    name="ecopy",
    version=VERSION,
    description="EcoPy: Ecological Data Analysis in Python",
    long_description=(ROOT / "README.rst").read_text(encoding="utf-8"),
    long_description_content_type="text/x-rst",
    url="https://github.com/Auerilas/ecopy",
    author="Nathan Lemoine",
    author_email="lemoine.nathan@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.11",
    install_requires=[
        "numpy>=2.0",
        "scipy>=1.16",
        "matplotlib>=3.8",
        "pandas>=2.0",
        "patsy>=1.0",
    ],
    extras_require={
        "cython": ["Cython>=3.0"],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
)
