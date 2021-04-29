#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name='wiki_person_parser',
    version='0.0.1',
    description='Automatically parse the character data on Wikipedia and generate high-quality triples',
    author='xiexx',
    author_email='xiaoxuanemail@163.com',
    install_requires=['tqdm', 'mwparserfromhell', 'pywikibot', 'strsimpy'],
    packages=find_packages(),
    license='MIT Licence',
    url='https://github.com/xiaoxuanyo/WikiPersonParser'
)
