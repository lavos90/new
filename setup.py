from setuptools import setup, find_packages
 
if __name__=='__main__':
    setup(name='new',
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
          classifiers=['Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programing Language :: Python',
          ]
          )












