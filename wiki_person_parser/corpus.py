# -*- coding: utf-8 -*-
"""
@author : xiexx
@email  : xiaoxuanemail@163.com
"""
import re
from wiki_person_parser.utils import split_sentence
from difflib import SequenceMatcher
import jieba
import math
import itertools
import random
import json


class NoItemException(Exception):

    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


def _raise_no_item_exception(func):
    def wrap(instance, *args, **kwargs):
        if instance.item is None:
            raise NoItemException('the item is None, please set the item.')
        return func(instance, *args, **kwargs)

    return wrap


def _format(value: str):
    return value.replace(
        '\\', r'\\').replace(
        '(', r'\(').replace(
        ')', r'\)').replace(
        '[', r'\[').replace(
        ']', r'\]').replace(
        '.', r'\.').replace(
        '?', r'\?').replace(
        '*', r'\*').replace(
        '^', r'\^').replace(
        '$', r'\$').replace(
        '+', r'\+').replace(
        '|', r'\|')


class Corpus:

    def __init__(self,
                 entry_alias='Alias',
                 field_thr=0.7,
                 sentence_thr=0.7,
                 match_ratio=0.7,
                 match_type='char',
                 max_paragraph_length=3):
        assert 0 < field_thr <= 1 and 0 < sentence_thr <= 1 and 0 < match_ratio <= 1, \
            f'阈值必须处于(0, 1]之前，当前field_thr={field_thr}，sentence_thr={sentence_thr}, match_char_ratio={match_ratio}'
        assert max_paragraph_length >= 1, f'段落包含的句子数必须在[1, +∞)，当前max_paragraph_length={max_paragraph_length}'
        assert match_type in ['char', 'all word', 'part word'], f'匹配类型为字符或词类型，当前match_type={match_type}'
        self._item = None
        self._fields = None
        self._text = None
        self._title = None
        self.entry_alias = entry_alias
        self.field_thr = field_thr
        self.sentence_thr = sentence_thr
        self.max_paragraph_length = max_paragraph_length
        self.match_ratio = match_ratio
        self.match_type = match_type

    def set_item(self, item):
        self._item = item
        self._text = item.get('string_text', '')
        self._fields = item.get('fields', {})
        self._title = item.get('entry', '')

    @property
    def item(self):
        return self._item

    @property
    def json_item(self):
        return json.dumps(self._item, ensure_ascii=False, indent=3)

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
    def json_fields(self):
        return json.dumps(self._fields, ensure_ascii=False, indent=3)

    @property
    @_raise_no_item_exception
    def alias(self):
        alias = set(self._fields.get(self.entry_alias, {}).get('values', []))
        alias.add(self._title)
        return alias

    def _get_multi_field_keys(self):
        keys = {}
        string = self._item.get('primary_entity_props', {}).get('multi_values_field', '')
        if not string:
            return keys
        for i in string.split('\n'):
            s = i.split(':')
            p = re.sub(r'_', '', s[1]).lower().strip()
            p = r'\n(%s)' % _format('%%%'.join([j.strip() for j in p.split(',') if j.strip()])[1:-1]).replace('%%%',
                                                                                                              '|')
            if len(p) >= len(keys.get(s[0], '')):
                keys[s[0]] = p
        return keys

    @property
    @_raise_no_item_exception
    def entities(self):
        if not self._fields:
            return {}
        multi_filed_keys = self._get_multi_field_keys()
        _entities = {}
        for key, value in self._fields.items():
            if key in multi_filed_keys.keys():
                for inner_value in value['values']:
                    inner_value = re.sub(multi_filed_keys[key], r'\n\n\n\n\n\1', inner_value)
                    inner_res = inner_value.split('\n\n\n\n\n')
                    for inner in inner_res:
                        temp = inner.split(':')
                        ll = _entities.get(f'{key}({temp[0].strip()})', [])
                        if temp[1].strip() not in ll:
                            ll.append(temp[1].strip())
                        _entities[f'{key}({temp[0].strip()})'] = ll
            else:
                _entities[key] = value['values']
        return _entities

    @property
    @_raise_no_item_exception
    def json_entities(self):
        return json.dumps(self.entities, ensure_ascii=False, indent=3)

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
                if ii - oi + 1 <= self.max_paragraph_length:
                    _paragraphs.append(_paragraph)
                else:
                    break
        return _paragraphs

    def _get_match_char(self, value, ignore_space=True, **kwargs):
        if self.match_type == 'part word':
            value = jieba.lcut(value)
        match_length = int(len(value) * self.match_ratio)
        _values = set()
        for oi in range(len(value)):
            _v_length = 0
            _chars = value[oi]
            if value[oi].strip():
                _v_length += 1
            v_length = _v_length if ignore_space else 1
            if match_length <= v_length:
                _values.add(_format(_chars))
            for ii in range(oi + 1, len(value)):
                _chars += value[ii]
                if value[ii].strip():
                    _v_length += 1
                v_length = _v_length if ignore_space else ii - oi + 1
                if v_length >= match_length:
                    _values.add(_format(_chars))
                    break
        return _values

    def _get_match_word(self, value, ignore_space=True, choice=10):
        value = jieba.cut(value)
        _values = []
        for word in value:
            m_w = self._get_match_char(value=word, ignore_space=ignore_space)
            _values.append(m_w)
        try:
            num = math.ceil(math.log(choice, len(_values)))
        except ZeroDivisionError:
            num = min([choice, len(_values)])
        _values = [random.sample(i, min([num, len(i)])) for i in _values]
        _values = [''.join(i) for i in itertools.product(*_values)]
        _values = set(random.sample(_values, min([choice, len(_values)])))
        return _values

    def _get_alia_value(self, value):
        for v in self.alias:
            if value in v:
                return v
        return ''

    @_raise_no_item_exception
    def corpus(self, top_k=1, ignore_space=True, choice=10, rjson=True):
        match_func = self._get_match_word if self.match_type == 'all word' else self._get_match_char
        _corpus = {'title': self._title,
                   'sentences': []}
        alia_pattern = set()
        for alia in self.alias:
            alia_pattern.update(match_func(alia, ignore_space, choice=choice))
        alia_pattern = rf"({'|'.join(alia_pattern)})"
        for key, value in self.entities.items():
            for inner_value in value:
                for sentence in self.paragraphs:
                    field_pattern = rf"({'|'.join(match_func(inner_value, ignore_space, choice=choice))})"
                    pattern = rf".*{alia_pattern}.*?{field_pattern}|{field_pattern}.*?{alia_pattern}.*"
                    result = re.search(pattern, sentence, flags=re.I)
                    if result:
                        score = SequenceMatcher(lambda x: x == ' ', sentence.lower(),
                                                result.group(0).lower()).quick_ratio()
                        if score >= self.sentence_thr:
                            alia = result.group(1) if result.group(1) else result.group(4)
                            alia = alia if alia else ''
                            field = result.group(2) if result.group(2) else result.group(3)
                            field = field if field else ''
                            _alia = self._get_alia_value(alia)
                            score1 = SequenceMatcher(lambda x: x == ' ', alia.lower(), _alia.lower()).quick_ratio()
                            score2 = SequenceMatcher(lambda x: x == ' ', field.lower(),
                                                     inner_value.lower()).quick_ratio()
                            if score1 >= self.field_thr and score2 >= self.field_thr:
                                _corpus['sentences'].append(
                                    {'sentence': sentence,
                                     'alia': _alia,
                                     'value': inner_value,
                                     'field': key,
                                     'alia_score': score1,
                                     'value_score': score2,
                                     'sentence_score': score,
                                     'match_alia': alia,
                                     'match_value': field}
                                )
        sort_sent = {k: [] for k in self.entities.keys()}
        for sentence in _corpus['sentences']:
            sort_sent[sentence['field']].append(sentence)
        sort_sent = {k: sorted(v, key=lambda dic: dic['sentence_score'], reverse=True)[:top_k] for k, v in
                     sort_sent.items() if v}
        _corpus['sentences'] = sort_sent
        if rjson:
            return json.dumps(_corpus, ensure_ascii=False, indent=3)
        return _corpus
