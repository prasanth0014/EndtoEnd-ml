from setuptools import find_namespace_packages,setup
from typing import List
HYPEN_E_DOT="-e ."
def get_requirements(file_path):
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[r.replace("\n","") for r in req]
    if HYPEN_E_DOT in req:
        req.remove(HYPEN_E_DOT)
    return req



setup(
    name='mlproject',
    version='0.0.1',
    author='Prasanth',
    author_email="pklprasanth522@gmail.com",
    packages=find_namespace_packages(),
    install_requires=get_requirements('requirements.txt')
)