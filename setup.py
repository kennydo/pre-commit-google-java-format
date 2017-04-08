import sys
from setuptools import find_packages
from setuptools import setup


setup(
    name='pre_commit_google_java_format',
    description='pre-commit plugin to format files using https://github.com/google/google-java-format',
    url='https://github.com/kennydo/pre-commit-google-java-format',
    version='0.0.1',

    author='Kenny Do',
    author_email='chinesedewey@gmail.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'format-with-google-java-format = pre_commit_google_java_format.cli:main',
        ],
    },
)
