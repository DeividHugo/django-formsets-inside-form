from setuptools import setup, find_packages

setup(
    name='django-formsets-inside-form',
    version='0.1',
    description='A library to handle formsets within forms in Django',
    author='Deivid Hugo',
    author_email='deividhugoof@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'Django>=2.0',
    ],
)
