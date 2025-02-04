from setuptools import find_packages,setup
from typing import List 

def get_requirements()->List[str]:
    
    requirement_list:List[str] = []

    try :
        with open('requirements.txt','r') as file :
            lines = file.readlines()
            for  line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError :
        print("requirement.txt file not found")
    
    return requirement_list
setup(
    name ="NetworkSecurity",
    version="0.0.1",
    author ="Arvind A",
    author_email="arv020302@gmail.com",
    package_data=find_packages(),
    install_requires= get_requirements()

)
