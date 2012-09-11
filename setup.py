#!/usr/bin/env python

from distutils.core import setup

setup(name='python-novnc',
      version='2012.1~e3',
      description='NoVNC python libraries',
      author='Ghe Rivero',
      author_email='ghe.rivero@stackops.com',
      url='http://www.stackops.com',
      packages = ['novnc'],
      package_dir = {'novnc':'utils'},
      py_modules=['wsproxy','websocket','web','json2graph','img2js'],
)
