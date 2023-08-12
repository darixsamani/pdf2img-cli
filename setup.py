#!/usr/bin/env python
from setuptools import setup



with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='pdf2img_cli',
    version='0.0.2',
    packages=['pdf2img_cli'],
    license='MIT license',
    description="simple cli for paragraphe recognition",
    long_description= long_description,
    long_description_content_type="text/markdown",

    
    url='https://github.com/darixsamani/pdf2img_cli',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
    python_requires='>=3.6',                
    py_modules=["pdf2img_cli"],             
    package_dir={'':'./src'},     
    install_requires=[
        'pdf2image==1.16.3',
        'pdf2img==0.1.2',
        'Pillow==10.0.0',

    ],

    entry_points={
        'console_scripts': [
            'pdf2img_cli = pdf2img_cli:main',
        ]
    }             
)
