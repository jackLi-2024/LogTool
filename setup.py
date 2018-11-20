#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
File:   LogTool.py
Author: Lijiacai (1050518702@qq.com)
Date: 2018-11-20
Description:
   setup tool
"""

import os
import sys

cur_dir = os.path.split(os.path.realpath(__file__))[0]
sys.path.append("%s/" % cur_dir)

from setuptools import setup
from setuptools import find_packages

setup(
    name="LogTool",
    version="18.11.20",
    keywords=("pip", "LogTool", "log"),
    description="The package for logging",
    long_description="The package uses the dictionary method of " + 
                     "logging module to achieve log rollback and other output."
    license="MIT LICENCE",

    url="https://github.com/lijiacaigit/LogTool",
    author="Lijiacai",
    author_email="1050518702@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["logging"]  # 这个项目需要的第三方库
)
