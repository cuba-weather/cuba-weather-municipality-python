from setuptools import setup

from cuba_weather_municipality import __version__

setup(
    name='cuba_weather_municipality',
    version=__version__,
    packages=[
        'cuba_weather_municipality', 
        'cuba_weather_municipality/data_providers',
        'cuba_weather_municipality/models',
        'cuba_weather_municipality/repositories',
        'cuba_weather_municipality/utils'
    ],
    url='https://github.com/cuba-weather/cuba-weather-municipality-python',
    license='MIT',
    author='Cuban Open Source Community',
    description='A tool implemented in Python for the Cuba Weather project to work with the municipalities of Cuba.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
