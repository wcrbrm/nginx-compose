from setuptools import setup

setup(
   name='nginx-compose',
   version='1.0',
   description='Command-line tool to create NGINx configuration files from YAML files',
   author='Web Cerebrium',
   author_email='webcerebrium@gmail.com',
   packages=['nginx-compose'],  #same as name
   install_requires=["pyyaml"], #external packages as dependencies
   scripts=[
    'nginx-compose.py'
   ]
)