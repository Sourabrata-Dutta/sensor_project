from setuptools import find_packages,setup
from typing import List
HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        return requirements
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)    

setup(
    name='Fault Detection',
    version='0.0.1',
    author='Sourabrata Dutta',
    author_mail='sourabratadutta27@gmail.com',
    install_requirements=get_requirements('requirements.txt'),
    packages=find_packages()
)
