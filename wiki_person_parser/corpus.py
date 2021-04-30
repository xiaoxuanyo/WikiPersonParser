# -*- coding: utf-8 -*-
"""
@author : xiexx
@email  : xiaoxuanemail@163.com
"""
import re


class NoDataException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def _raise_no_item_exception(func):
    def wrap(instance, *args, **kwargs):
        if instance.item is None:
            raise NoDataException('the item is None, please set the item.')
        return func(instance, *args, **kwargs)

    return wrap


class Corpus:

    def __init__(self,
                 entry_alias='Alias',
                 field_thr=0.85,
                 sentence_thr=0.7,
                 max_paragraph_length=3):
        assert 0 < field_thr <= 1 and 0 < sentence_thr <= 1, \
            f'阈值必须处于(0, 1]之前，当前field_thr={field_thr}，sentence_thr={sentence_thr}'
        assert max_paragraph_length >= 1, f'段落包含的句子数必须在[1, +∞)，当前max_paragraph_length={max_paragraph_length}'
        self._item = None
        self._fields = None
        self._text = None
        self._title = None
        self.entry_alias = entry_alias
        self.field_thr = field_thr
        self.sentence_thr = sentence_thr
        self.max_paragraph_length = max_paragraph_length

    def set_item(self, item):
        self._item = item
        self._text = item.get('string_text', '')
        self._fields = item.get('fields', {})
        self._title = item.get('entry', '')

    @property
    def item(self):
        return self._item

    @property
    @_raise_no_item_exception
    def title(self):
        return self._title

    @property
    @_raise_no_item_exception
    def text(self):
        return self._text

    @property
    @_raise_no_item_exception
    def fields(self):
        return self._fields

    @property
    @_raise_no_item_exception
    def alias(self):
        alias = set(self._fields.get(self.entry_alias, {}).get('values', []))
        alias.add(self._title)
        return alias

    def __get_multi_field_keys(self):
        keys = []
        string = self._item.get('primary_entity_props', {}).get('multi_values_field', '')
        string = re.sub(r'\(.*?\)', '', string)
        for i in string.split(':'):
            if i.strip():
                keys.append(i.strip())
        return keys

    @property
    @_raise_no_item_exception
    def entities(self):
        multi_filed_keys = self.__get_multi_field_keys()
        res = {}
        for key, value in self._fields.items():
            if key in multi_filed_keys:
                for inner_value in value['values']:
                    inner_res = inner_value.split('\n')
                    for inner in inner_res:
                        temp = inner.split(':')
                        ll = res.get(f'{key}({temp[0].strip()})', [])
                        if temp[1].strip() not in ll:
                            ll.append(temp[1].strip())
                        res[f'{key}({temp[0].strip()})'] = ll
            else:
                res[key] = value['values']
        return res

    @property
    @_raise_no_item_exception
    def sentences(self):
        return [sent.strip() for sent in split_sentence(self._text) if sent.strip()]

    @property
    @_raise_no_item_exception
    def paragraphs(self):
        _paragraphs = []
        _sentences = self.sentences
        for oi in range(len(_sentences)):
            _paragraph = _sentences[oi]
            _paragraphs.append(_paragraph)
            for ii in range(oi + 1, len(_sentences)):
                _paragraph += _sentences[ii]
                if ii - oi <= self.max_paragraph_length:
                    _paragraphs.append(_paragraph)
        return _paragraphs


if __name__ == '__main__':
    import json
    from wiki_person_parser.utils import split_sentence
    from wiki_person_parser.parser import Parser

    with open('./ms_person_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    corpus = Corpus()
    corpus.set_item(Parser.parse_wiki_data(data['657138']['all text'], entry=data['657138']['title']))

    sentences = corpus.paragraphs
    for i in sentences:
        print('sentence', i)
    #
    # from difflib import SequenceMatcher
    # from strsimpy.normalized_levenshtein import NormalizedLevenshtein
    #
    # s0 = 'Senarai anjing tertua'
    # s1 = 'Anjing tertua sehingga Lucky (?-2008)'
    # sim = SequenceMatcher(lambda x: x == ' ', s0, s1)
    # print('lib', sim.ratio())
    # sim = NormalizedLevenshtein()
    # print('nor', sim.similarity(s0, s1))
    # from strsimpy.jaro_winkler import JaroWinkler
    #
    # sim = JaroWinkler()
    # print('jar', sim.similarity(s0, s1))
