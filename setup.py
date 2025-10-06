from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="EfficientLoFTR",
    version="1.0",
    packages=find_packages(),
    install_requires=requirements,
)