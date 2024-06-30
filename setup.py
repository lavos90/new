from setuptools import setup, find_packages
import os
import re
import codecs

NAME='new'
META_PATH=os.path.join('new','__init__.py')
REQUIREMENTS=[]
CLASSIFIERS=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programing Language :: Python',
]
HERE=os.path.abspath(os.path.dirname(__file__))




if __name__=='__main__':
    setup(
        name='new',
        description='esto es un trabajo new',
        license='MIT',
        url='https://github.com/lavos90/new.git',
        version='0.0.1',
        author='yadnier',
        author_email='yadnierc@gmail.com',
        long_description=open('README.md').read(),
        packages=find_packages(),
        zip_safe=False,
        install_requires=[],
        classifiers=[,
        ]
        )

