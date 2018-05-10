from setuptools import setup, find_packages


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


version = '1.0.3'

README="""Small Python library for process SRP requests for AWS Cognito. This library was initially included in the [Warrant](https://www.github.com/capless/warrant) library. We decided to separate it because not all projects and workfows need all of the helper classes and functions in Warrant."""

setup(
    name='warrant-lite',
    version=version,
    description=README,
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    keywords='aws,cognito,srp,capless',
    author='Capless.io',
    author_email='opensource@capless.io',
    maintainer='Brian Jinwright',
    packages=find_packages(),
    url='https://github.com/capless/warrant-lite',
    license='Apache License 2.0',
    install_requires=parse_requirements('requirements.txt'),
    include_package_data=True,
    zip_safe=True,

)
