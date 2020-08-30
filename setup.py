"""Settings to assist package installation"""

import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(name='the-ascii-art-project',
                 version='0.1',
                 author='RaDroid',
                 license='MIT open-source licence',
                 long_description=long_description,
                 packages=setuptools.find_packages(),
                 zip_safe=False,
                 install_requires=[],
                 classifiers=[
                     'Development Status :: 2 - Beta',
                     'Intended Audience :: End Users/Desktop',
                     'License :: MIT',
                     'Operating System :: Linux/MacOs',
                     'Programming Language :: Python',
                     'Topic :: Desktop Environment'
                 ]
                 )
