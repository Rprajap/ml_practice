from setuptools import find_packages,setup

from typing import List
file_path = "requirements.txt"
HYPEN_E_DOT = "-e ."
def get_requirements_list(file_path:str)->List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n",'') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
    
setup (
name='ml_project',
project_name="Machine learnign project",
license='0.0.1',
description='General project structue',
author="Ramdas",
author_email="ramdasprajapati460@gmail.com",
packages= find_packages(),
install_requires = get_requirements_list(file_path)
)