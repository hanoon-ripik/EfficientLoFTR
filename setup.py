from setuptools import setup, find_packages

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Get version from __init__.py or set default
def get_version():
    return "1.0.0"

setup(
    name="EfficientLoFTR",
    version=get_version(),
    author="Yifan Wang, Xingyi He, Sida Peng, Dongli Tan, Xiaowei Zhou",
    author_email="",  # Add contact email if available
    description="Efficient LoFTR: Semi-Dense Local Feature Matching with Sparse-Like Speed",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/zju3dv/EfficientLoFTR",
    project_urls={
        "Bug Reports": "https://github.com/zju3dv/EfficientLoFTR/issues",
        "Source": "https://github.com/zju3dv/EfficientLoFTR",
        "Documentation": "https://zju3dv.github.io/efficientloftr",
        "Paper": "https://zju3dv.github.io/efficientloftr/files/EfficientLoFTR.pdf",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "isort",
            "flake8",
        ],
        "docs": [
            "sphinx",
            "sphinx-rtd-theme",
            "myst-parser",
        ],
    },
    entry_points={
        "console_scripts": [
            "eloftr-train=train:main",
            "eloftr-test=test:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.yaml", "*.yml", "*.json", "*.txt", "*.md"],
    },
    zip_safe=False,
    keywords=[
        "computer-vision",
        "feature-matching",
        "local-features",
        "deep-learning",
        "pytorch",
        "cvpr2024",
        "loftr",
        "semi-dense",
        "sparse-matching",
    ],
    license="MIT",
    platforms=["any"],
)
