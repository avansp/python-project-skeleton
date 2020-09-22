from setuptools import setup, find_packages

setup(
    name='myproject',
    author='My Self',
    author_email='somehwere@world.com',
    version='0.1.0',
    license='LICENSE',
    description='This is my new project',
    packages=find_packages(),
    long_description=open('README.md').read(),
)
