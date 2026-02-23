from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(requirements_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    with open(requirements_path, 'r') as f:
        requirements = f.read().splitlines()

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(  
    name='mlproject',
    version='0.1',
    author='Anmol',
    author_email='anmol5581@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(requirements_path='requirements.txt')
)
