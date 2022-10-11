from setuptools import setup, find_packages

setup(
    name="propaneplot",
    version="1.0.0",
    description="Propane Usage Projections",
    url="",
    author="Elliot Dronebarger",
    author_email="elliot.dronebarger@gmail.com",
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.6.1',
        'numpy==1.23.3'
    ],
    entry_points={
        'console_scripts': [
            'propane-plot = propaneplot.plot:local_main',
        ],
    }
)
