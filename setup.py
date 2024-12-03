from setuptools import setup, find_packages

setup(
    name='is_ai_odd',
    version='1.0',
    author='trimpta',
    author_email='hi@trimpta.com',
    description='A Python package that leverages AI to identify odd patterns in data using generative models.',
    long_description='The `is_ai_odd` package provides a simple interface to identify patterns in data that could be considered "odd" or out of place using Google\'s generative AI models. This package is designed for developers looking to integrate advanced machine learning techniques into their projects, without the need for deep AI expertise.',
    long_description_content_type='text/markdown',
    url='https://github.com/trimpta/is_ai_odd',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'google-generativeai',
    ],
    python_requires='>=3.9',
    entry_points={},
)
