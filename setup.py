from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="healthcare-ai-for-good",
    version="0.1.0",
    author="Healthcare AI Community",
    author_email="healthcare-ai@github.com",
    description="Open-source AI solutions for healthcare accessibility, patient safety, and clinical outcomes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kakshak07/healthcare-ai-for-good",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Medical/Dental",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19",
        "pandas>=1.0",
        "scikit-learn>=0.24",
        "torch>=1.8",
        "transformers>=4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.9",
            "mypy>=0.900",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
        ],
    },
)
