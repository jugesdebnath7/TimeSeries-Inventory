# setup.py placeholder 
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "TimeSeries-Inventory"
SRC_REPO = "timeseries_inventory"
AUTOHR_USER_NAME = "jugesdebnath7"
AUTHOR_EMAIL = "jugesdebnath7@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTOHR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "Time Series Inventory Project",
    long_description = long_description,
    long_description_content_type= "text/markdown",
    url = f"https://github.com/{AUTOHR_USER_NAME}/{REPO_NAME}",
    packages = setuptools.find_packages(where = "src"),
    classifiers=[
            "Programming Language :: Python 3", 
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent"
    ],
    python_requires = ">=3.6",
    package_dir={"": "src"},
    project_urls= {
            "Source Code": f"https://github.com/{AUTOHR_USER_NAME}/{REPO_NAME}",
            "Bug Tracker": f"https://github.com/{AUTOHR_USER_NAME}/{REPO_NAME}/issues"
    }
)
