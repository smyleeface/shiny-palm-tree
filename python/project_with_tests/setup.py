#!/usr/bin/env python

from setuptools import setup

setup(
    name='SongListUpload',
    version='1.0',
    description='Adds songs from a CSV to a dynamodb',
    author='PattyR (smyleeface)',
    author_email='patty.ramert@gmail.com',
    install_requires=[
        'boto3>=1.12.41'
    ],
    tests_require=[
        'pytest>=5.4.1<6.0.0',
        'mock>=4.0.2<5.0.0'
    ],
    test_suite='tests.songlist_upload_testsuite',
)


