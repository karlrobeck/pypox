from setuptools import setup, find_packages

setup(
    name="pypox",
    version="1.2.1",
    author="Karl Robeck Alferez",
    author_email="karlalferezfx@gmail.com",
    description="",
    packages=find_packages(),
    install_requires=["uvicorn[standard]", "fastapi"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.0",
)
