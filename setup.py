from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='trst',
    version='0.1',
    description='Tufts Robotic Sailing Autonomous Boat Package',
    long_description=readme,
    author='Alexander Tong',
    author_email='alexanderytong@gmail.com',
    url='https://github.com/tuftsrobotics/trst',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

