from setuptools import find_packages, setup

# a way to open the README file via long discription
with open("README.md", "r") as fh:
    long_description = fh.read()

# meta data about our package
setup(
    name="my_lambdata-RMDircio", # the name that you will install via pip
    version="1.0",
    author="Regina Dircio",
    author_email="reginadircio@gmail.com",
    description="A short description",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/RMDircio/lambdata-RMDircio",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)