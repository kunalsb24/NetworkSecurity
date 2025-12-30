'''
The setup.py file is an essential component of a Python 
project that uses setuptools for packaging and distribution. 
It contains metadata about the project and instructions on how to install it.
Here is an example of a typical setup.py file:
'''
from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """Read the requirements from the requirements.txt file."""
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            #Read all lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
    name='NETWORKSECURITY',
    version='0.0.1',
    author='Kunal Bhajbhuje',
    author_email="kunalbhajbhuje5@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)

