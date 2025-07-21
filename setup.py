from setuptools import find_packages, setup
from typing import List

#function used to put iinside tthe install_reuiires
def get_reuirements(file_path:str) -> list[str]:
    '''
    this function will return the list of installation
    requirements needed to run the package in the setup()
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # manipulate the list to get rid the new lines
        [req.replace("\n","") for req in requirements]
        # do not iinclude -e .
        if "-e ." in requirements:
            requirements.remove("-e .")
        
        return requirements

# setup the metadata of the project
setup(
name="mlProjectOne",
version='0.0.1',
author="Mark Alford Jr",
author_email='makralfordjr@gmail.com',
packages=find_packages(),
install_requires = get_reuirements("requirements.txt")
)