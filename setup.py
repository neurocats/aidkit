"""Basic file to install aidkit with pip."""
from setuptools import setup, find_packages
import re

with open('requirements.txt') as fp:
    INSTALL_REQUIRES = list()
    for line in fp:
        pattern = r'(?<=\-r\s)[\w\/.]+'
        path = re.findall(pattern, line)[0]
        with open(path) as f:
            INSTALL_REQUIRES.append(f.read())
    INSTALL_REQUIRES = "\n".join(INSTALL_REQUIRES)


setup(
    name='aidkit',
    version='0.1.0',
    description="aidkit, the first aid kit for AI development, verification & validation. The "
                "AI-debugging &-boosting toolkit is both the embodiment of quality standards, as "
                "well as the plug & play tool for AI developers who want to put their model "
                "through its paces in every section of the AI lifecycle to reduce "
                "costs / iterations. ",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    url='aidkit.ai',
    author='neurocat GmbH',
    author_email='dev@neurocat.ai',
    license='GNU AGPLv3',
    install_requires=INSTALL_REQUIRES
)
