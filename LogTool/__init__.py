#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
File:   __init__.py
Author: Lijiacai (1050518702@qq.com)
Date: 2018-11-20
Description:
    The package uses the dictionary method of logging module to achieve log rollback and other output.
    for example:
        from LogTool import LogTool
        logger = LogTool.init_log("test", "filetime", level="DEBUG", when="s", backupCount=5,
                       filename="./log/test_file.log")
        logger.warn("hello world")
"""
