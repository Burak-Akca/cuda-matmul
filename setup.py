from setuptools import setup, find_packages
import os

setup(
    name="cudamatmul",
    version="0.1.0",
    author="Burak Akça",
    author_email="burak@example.com",
    description="CUDA destekli matris çarpımı modülü",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={"cudamatmul": ["*.pyd"]},  # .pyd dosyasını dahil et!
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
