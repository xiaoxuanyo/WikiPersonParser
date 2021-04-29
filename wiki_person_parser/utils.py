#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author : xiexx
@email  : xiaoxuanemail@163.com
"""

import logging
import os
import re


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


"""
split_sentence为来自HanLp的官方实现
https://github.com/hankcs/HanLP 
"""


SEPARATOR = r'@'
RE_SENTENCE = re.compile(r'(\S.+?[.!?])(?=\s+|$)|(\S.+?)(?=[\n]|$)', re.UNICODE)
AB_SENIOR = re.compile(r'([A-Z][a-z]{1,2}\.)\s(\w)', re.UNICODE)
AB_ACRONYM = re.compile(r'(\.[a-zA-Z]\.)\s(\w)', re.UNICODE)
UNDO_AB_SENIOR = re.compile(r'([A-Z][a-z]{1,2}\.)' + SEPARATOR + r'(\w)', re.UNICODE)
UNDO_AB_ACRONYM = re.compile(r'(\.[a-zA-Z]\.)' + SEPARATOR + r'(\w)', re.UNICODE)


def replace_with_separator(text, separator, regexs):
    replacement = r"\1" + separator + r"\2"
    result = text
    for regex in regexs:
        result = regex.sub(replacement, result)
    return result


def split_sentence(text, best=True):
    text = re.sub(r'([。！？\?])([^”’])', r"\1\n\2", text)
    text = re.sub(r'(\.{6})([^”’])', r"\1\n\2", text)
    text = re.sub(r'(\…{2})([^”’])', r"\1\n\2", text)
    text = re.sub(r'([。！？\?][”’])([^，。！？\?])', r'\1\n\2', text)
    for chunk in text.split("\n"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if not best:
            yield chunk
            continue
        processed = replace_with_separator(chunk, SEPARATOR, [AB_SENIOR, AB_ACRONYM])
        for sentence in RE_SENTENCE.finditer(processed):
            sentence = replace_with_separator(sentence.group(), r" ", [UNDO_AB_SENIOR, UNDO_AB_ACRONYM])
            yield sentence
