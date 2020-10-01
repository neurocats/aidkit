"""Basic file to install aidkit with pip."""
from setuptools import setup, find_packages
import re

with open('requirements.txt') as fp:
    INSTALL_REQUIRES = fp.read()
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='aidkit',
    version='0.1.2',
    description="aidkit, the first aid kit for AI development, verification & validation. The "
                "AI-debugging &-boosting toolkit is both the embodiment of quality standards, as "
                "well as the plug & play tool for AI developers who want to put their model "
                "through its paces in every section of the AI lifecycle to reduce "
                "costs / iterations. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    url='https://aidkit.ai/',
    author='neurocat GmbH',
    author_email='dev@neurocat.ai',
    license='GNU AGPLv3',
    install_requires=INSTALL_REQUIRES
)
