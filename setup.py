from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()


setup(
    name="MLOps",
    version='0.1',
    author='Nilabja Ray',
    packages=find_packages(),
    install_requires=requirements
)