#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author : xiexx
@email  : xiaoxuanemail@163.com
"""

import logging
import os


class LoggerUtil:
    _format_str = '%(asctime)s.%(msecs)03d %(levelname)s [%(processName)s-%(process)d] [%(threadName)s-%(thread)d] ' \
                  '[%(module)s.%(funcName)s] From %(pathname)s[line:%(lineno)d]: %(message)s'

    def __init__(self, name=None, level=logging.DEBUG, file_path=None, format_str=None,
                 mode='a+', encoding='utf-8'):
        if name is None:
            name = self.__str__()
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.format = format_str if format_str else LoggerUtil._format_str
        formatter = logging.Formatter(self.format, datefmt='%Y-%m-%d %H:%M:%S')
        console_handler = logging.StreamHandler()
        self.logger.addHandler(console_handler)
        console_handler.setFormatter(formatter)
        if file_path is not None:
            f, _ = os.path.split(file_path)
            if not os.path.isdir(f):
                os.makedirs(f, exist_ok=True)
            file_handler = logging.FileHandler(file_path, mode=mode, encoding=encoding)
            self.logger.addHandler(file_handler)
            file_handler.setFormatter(formatter)

