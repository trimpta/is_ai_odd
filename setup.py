from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='is-ai-odd',
    version='1.1',
    author='trimpta',
    author_email='hi@trimpta.com',
    description='A Python package that leverages AI to identify odd patterns in data using generative models.',
    long_description=long_description,
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
