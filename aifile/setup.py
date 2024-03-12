# aifile/setup.py
from setuptools import setup, find_packages

setup(
    name='aifile',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'numpy',
        'speechrecognition',
    ],
    entry_points={
        'console_scripts': [
            'filely = aifile.filely:main',
        ],
    },
)
