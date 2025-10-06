from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="EfficientLoFTR",
    version="1.0.0",
    packages=[f"EfficientLoFTR.{pkg}" for pkg in find_packages(where="src")],
    package_dir={"EfficientLoFTR": "src"},
    install_requires=requirements,
)