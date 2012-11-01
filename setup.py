#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='catkin_basic',
    version='0.0.1',
    packages=['catkin_basic'],
    package_dir = {'catkin_basic':'src/catkin_basic'},
    scripts = [],
    install_requires=['catkin-pkg'],
    package_data = {'catkin_basic': ['resources/templates/*']},
    author='Wim Meeussen',
    author_email='wim@hidof.com',
    maintainer='Wim Meeussen',
    maintainer_email='wim@hidof.com',
    url='http://www.ros.org/wiki/catkin_basic',
    download_url='http://pr.willowgarage.com/downloads/catkin_basic/',
    keywords=['ROS'],
    classifiers=['Programming Language :: Python',
                 'License :: OSI Approved :: BSD License'],
    description="An easy way to use catkin",
    long_description="""
An easy way to use catkin
""",
    license='BSD'
)
