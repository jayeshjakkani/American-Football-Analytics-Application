from setuptools import setup, find_packages

def get_requirements(filename):
    with open(filename) as f:
        requirements = f.read().splitlines()
    return requirements

setup(name='AFAA',
      version='2.0',
      description='CSC 510: Software Engineering Project 2',
      author='Jayesh Jakkani',
      author_email='jjakkan@ncsu.edu',
      license="MIT",
      packages=find_packages(),
      python_requires=">=3.3",
      install_requires = get_requirements("requirements.txt"),
      include_package_data=True,
     )
