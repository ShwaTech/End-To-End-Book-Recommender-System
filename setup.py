from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "End-To-End-Book-Recommender-System"
REPO_OWNER = "ShwaTech"
AUTHOR_USER_NAME = "Mohamed Fathy"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{REPO_OWNER}/{REPO_NAME}",
    author_email="skwakesh13579@gmail.com",
    packages=find_packages(),
    license="Apache",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)