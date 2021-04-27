#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author : xiexx
@email  : xiaoxuanemail@163.com
"""

import json
from tqdm import tqdm
import xml.sax
import io
import re
from wiki_person_parser.base import TemplateBase, QueryEngine
from wiki_person_parser.templates import TemplatePerson, TEMPLATE_MAP
import mwparserfromhell as mwp


class InfoField:
    info_field = 'Infobox'
    base_template = TemplateBase

    @classmethod
    def matches(cls, obj):
        if re.search(r'%s' % cls.info_field, str(obj), re.I):
            return False
        return True


class WikiContentHandler(xml.sax.handler.ContentHandler, InfoField):
    __wiki_type_choice = ['arguments', 'comments', 'external_links',
                          'headings', 'html_entities', 'tags', 'templates',
                          'text', 'wikilinks']

    def __init__(self, filter_categories=None, category=None, code='ms', skip_num=None,
                 category_wiki_type=['wikilinks']):
        assert set(category_wiki_type).issubset(
            set(self.__wiki_type_choice)), f'错误的wiki_type类型，可选的wiki_type有{self.__wiki_type_choice}'
        super(WikiContentHandler, self).__init__()
        self._buffer = ''
        self._current_tag = None
        self._per_page = {}
        self._code = code
        self._category_wiki_type = category_wiki_type
        self.pages = {}
        if filter_categories is not None:
            assert category is not None, '指定filter_categories后，应提供对应语言的category。'
            assert isinstance(filter_categories, list), f'不支持的filter_categories类型{type(filter_categories)}，目前仅支持list类型。'
            if skip_num is None:
                split_tag = r'.*?[:：].*?'
            else:
                assert isinstance(skip_num, int), f'skip_num必须是int类型，不支持类型skip_num: {type(skip_num)}。'
                split_tag = r'.{,%d}[:：].{,%d}' % (skip_num, skip_num)
            self._filter_categories = [category + split_tag + i for i in filter_categories]
        else:
            self._filter_categories = None

    def startElement(self, name, attrs):
        if name in ['title', 'text', 'id']:
            self._current_tag = name
        elif name == 'redirect':
            self._per_page['redirect title'] = attrs['title']

    def endElement(self, name):
        if name == self._current_tag:
            if not self._per_page.get(name):
                self._per_page[name] = self._buffer
            self._buffer = ''
            self._current_tag = None
        if name == 'page':
            _text = mwp.parse(self._per_page['text'])
            _res = []
            for funs in self._category_wiki_type:
                fun = getattr(_text, f'filter_{funs}')
                _res.extend([str(i) for i in fun(recursive=False)])
            _text = ''.join(_res)
            if self._filter_categories is None or re.search(r'%s' % '|'.join(self._filter_categories),
                                                            _text, re.I):
                self._per_page['id url'] = 'https://%s.wikipedia.org/wiki?curid=%s' % (self._code, self._per_page['id'])
                self._per_page['title url'] = 'https://%s.wikipedia.org/wiki/%s' % (
                    self._code, self._per_page['title'].replace(' ',
                                                                '_'))
                self._per_page['all text'] = self._per_page.pop('text')
                self._per_page['info text'] = ''.join([str(i) for i in
                                                       mwp.parse(self._per_page['all text']).filter_templates(
                                                           matches=r'%s' % self.info_field, recursive=False)])
                wiki_text = ''.join(
                    [str(i) for i in
                     mwp.parse(self._per_page['all text']).filter(matches=self.matches, recursive=False)])
                self._per_page['string text'] = ''.join(
                    [str(i) for i in self.base_template.parse(wiki_text)]).strip(' ')
                if self._per_page.get('redirect title'):
                    self._per_page['redirect url'] = 'https://%s.wikipedia.org/wiki/%s' % (self._code, self._per_page[
                        'redirect title'].replace(' ', '_'))
                self._per_page = {k: v for k, v in self._per_page.items() if v}
                self.pages[self._per_page.pop('id')] = self._per_page
            self._per_page = {}

    def characters(self, content):
        if self._current_tag:
            self._buffer += content

    @classmethod
    def get_wiki_types(cls):
        return cls.__wiki_type_choice


class XMLParser:

    def __init__(self, filter_categories=None, category=None, code='ms', skip_num=None,
                 category_wiki_type=['wikilinks']):
        self.handler = WikiContentHandler(filter_categories, category, code, skip_num, category_wiki_type)
        self.parser = xml.sax.make_parser()
        self.parser.setFeature(xml.sax.handler.feature_namespaces, 0)
        self.parser.setContentHandler(self.handler)
        self._input_source = None

    @property
    def wiki_types(self):
        return self.handler.get_wiki_types()

    def parse_file(self, xml_file):
        self.parser.parse(xml_file)
        return self.handler.pages

    def parse_string(self, xml_string):
        if self._input_source is None:
            self._input_source = xml.sax.xmlreader.InputSource()
        if isinstance(xml_string, str):
            self._input_source.setCharacterStream(io.StringIO(xml_string))
        else:
            self._input_source.setByteStream(io.BytesIO(xml_string))
        self.parser.parse(self._input_source)
        return self.handler.pages

    def parse_file_block(self, xml_file):
        num = 0
        with open(xml_file, 'r', encoding='utf-8') as f:
            for _ in tqdm(f, desc='正在获取文件大小信息...', leave=False):
                num += 1
        with open(xml_file, 'r', encoding='utf-8') as f:
            for line in tqdm(f, desc='正在获取文件...', total=num):
                self.parser.feed(line)
        return self.handler.pages

    def save(self, path, encoding='utf-8'):
        with open(path, 'w+', encoding=encoding) as f:
            json.dump(self.handler.pages, f, ensure_ascii=False, indent=3)


class Parser(InfoField):
    default_template = TemplatePerson
    map_template = TEMPLATE_MAP

    @staticmethod
    def _init(code, https_proxy=None):
        return QueryEngine(code, https_proxy)

    @classmethod
    def parse_wiki_data(cls, data, force=True, entry=None):
        """
        :param data: 必须是符合wiki语法格式的字符串
        :param force:
        :param entry:
        :return:
        """
        _props = []
        fields = {'template_name': [],
                  'entry': entry}
        default_temp = cls.default_template if force else cls.base_template
        fields['all_text'] = data
        data = mwp.parse(data)
        wiki_text = ''.join(
            [str(i) for i in data.filter(matches=cls.matches, recursive=False)])
        string_text = ''.join([str(i) for i in cls.base_template.parse(wiki_text)]).strip(' ')
        if string_text:
            fields['string_text'] = string_text
        info_text = ''.join([str(i) for i in data.filter_templates(matches=r'%s' % cls.info_field, recursive=False)])
        if info_text:
            fields['info_text'] = info_text
        temp = data.filter_templates(matches=cls.info_field)
        if temp:
            tem = temp.pop(0)
            values = {str(p.name).strip(): str(p.value) for p in tem.params if str(p.value)}
            template = cls.map_template.get(
                str(tem.name).strip().lower(), default_temp) if isinstance(cls.map_template, dict) else default_temp
            res = template(values, entry)
            if res.template_name not in fields['template_name']:
                fields['template_name'].append(res.template_name)
            fields['fields'] = res.fields['fields']
            if res.fields.get('primary_entity_props'):
                if res.fields['primary_entity_props']['multi_values_field'] not in _props:
                    _props.append(res.fields['primary_entity_props']['multi_values_field'])
            for t in temp:
                values = {str(p.name).strip(): str(p.value) for p in t.params if str(p.value)}
                template = cls.map_template.get(
                    str(tem.name).strip().lower(), default_temp) if isinstance(cls.map_template, dict) else default_temp
                res = template(values, entry)
                if res.template_name not in fields['template_name']:
                    fields['template_name'].append(res.template_name)
                for i, j in res.fields['fields'].items():
                    if i not in fields['fields'].keys():
                        fields['fields'][i] = j
                    else:
                        for k in j['values']:
                            if k not in fields['fields'][i]['values']:
                                fields['fields'][i]['values'].append(k)
                if res.fields.get('primary_entity_props'):
                    for i_s in res.fields['primary_entity_props']['multi_values_field'].split('\n'):
                        if i_s not in _props:
                            _props.append(i_s)
        if _props:
            fields['primary_entity_props'] = {'multi_values_field': '\n'.join(_props)}
        if not fields['template_name']:
            fields.pop('template_name')
        return fields

    @classmethod
    def parse_wiki_title(cls, title, code, https_proxy=None, force=True, get_redirect=False, page_info=False):
        """
        :param title: 条目
        :param code:
        :param https_proxy:
        :param force:
        :param get_redirect:
        :param page_info:
        :return:
        """
        query = cls._init(code, https_proxy)
        data = query.get_wiki_page(title, get_redirect=get_redirect, force=page_info)
        return cls.parse_wiki_data(data, force, title)
