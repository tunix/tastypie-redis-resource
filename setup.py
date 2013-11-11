# coding: utf-8

import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="tastypie-redis-resource",
    version="0.0.2",
    author="Alper Kanat",
    author_email="tunix@raptiye.org",
    description=("Tastypie Redis Resource"),
    keywords="tastypie rest api module resource redis",
    url="https://github.com/tunix/tastypie-redis-resource",
    install_requires = [
        'Django>=1.5',
        'django-tastypie>=0.10',
    ],
    packages=[
        'tastypie_redis',
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Environment :: Console",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Internet",
    ],
    include_package_data=True,
    zip_safe=False
)
