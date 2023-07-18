import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

    __version__ = "0.0.0.0"
    
    REP0_NAME = "Chicken_Disease_Prediction"
    AUTHOR_USER_NAME = "CDARSHAN"
    SRC_REPO = "Chicken_Disease_Prediction"
    AUTHOR_EMAIL = "darshanchindarkar234@gmail.com"

    setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="A small python app for Chicken Disease Prediction",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REP0_NAME}",
        project_urls={
            "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REP0_NAME}/issue",
            
        },
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
    )