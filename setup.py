import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


setup(
    name='django_transit',
    version='0.0',
    packages=['django_transit'],
    description='a django transit implementation',
    long_description=README,
    author='Matteo SCARPA',
    author_email='me@fundor333.com',
    url='https://github.com/fundor333/django_transit/',
    license='MIT',
    install_requires=[
        'Django>2.0',
    ]
)
