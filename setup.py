from setuptools import setup, find_packages

setup(
    name="pypox",
    version="0.1.0",
    author="Karl Robeck Alferez",
    author_email="karlalferezfx@gmail.com",
    description="python web framework for building web application using fastapi and react",
    packages=find_packages(),
    entry_points={"console_scripts": ["pypox=pypox.__init__:app"]},
    install_requires=["typer", "uvicorn[standard]", "fastapi", "watchfiles", "bs4"],
    include_package_data=True,
    package_data={"": ["*.js", "*.css", "*.html", "*.jsx"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.4",
)
