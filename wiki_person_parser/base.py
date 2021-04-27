#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author : xiexx
@email  : xiaoxuanemail@163.com
"""

import logging
import mwparserfromhell as mwp
import re
from wiki_person_parser.utils import LoggerUtil
import os
import pywikibot

_CONSOLE_LOG_LEVEL = logging.WARNING

_console_log = LoggerUtil('wiki_person_parser.base.console', level=_CONSOLE_LOG_LEVEL)


def _is_int(string):
    try:
        int(string)
        return True
    except (TypeError, ValueError):
        return False


def _is_include_dict(array):
    for i in array:
        if isinstance(i, dict):
            return True
    return False


def _get_key(array):
    keys = []
    for i in array:
        for v in i.values():
            for k in v:
                e = list(k.keys())[0]
                if e not in keys:
                    keys.append(e)
    return keys


def _get_multi_values(array):
    ky = _get_key(array)
    ky = {k: [] for k in ky}
    for i in array:
        for k, v in i.items():
            for ii in v:
                kk = list(ii.keys())[0]
                vv = ii[kk]
                ky[kk].append(k.lower().split('_')[-1] + ':' + vv)
    result = []
    for i in ky.values():
        result.append('\n'.join(i))
    return result


def re_compile(s, mode='se', split='.*?', flags=re.I):
    assert mode in ['s', 'e', 'se'], f'不支持{mode}'
    _s = r'^'
    _e = r'$'
    if mode == 's':
        _p = _s + '%s'
    elif mode == 'e':
        _p = '%s' + _e
    else:
        _p = _s + '%s' + _e
    s = s.split('|')
    ss = []
    for j, i in enumerate(s):
        i_split = i.split(split)
        index = []
        for k in range(len(i_split) - 1):
            index.append('i' + str(j))
            index.append(str(j + k))
        ss.append(r'\s*?(?P<s_index%d>\d*)\s*?' % j + r'\D*?(?P<%s_index%s>\d*)\D*?'.join(
            i_split) % tuple(index) + r'\s*?(?P<e_index%d>\d*)\s*?' % j)
    s = '|'.join([_p % j for j in ss])
    return re.compile(r'%s' % s, flags=flags)


def _matches(string, match):
    def match1(i_s, i_m):
        assert isinstance(i_m, list) or isinstance(i_m, re.Pattern), f'类型不符，match类型{type(i_m)}'
        if isinstance(i_m, list):
            if i_s in i_m:
                return True, None
            else:
                return False, None
        else:
            res = re.search(i_m, i_s)
            if res:
                return True, res
            else:
                return False, None

    def match2(i_s, m_l, m_r):
        assert isinstance(m_l, list) and isinstance(m_r,
                                                    re.Pattern), f'类型不符，match[0]类型{type(m_l)}，match[1]类型{type(m_r)}'
        if i_s in m_l:
            return True, None
        elif re.search(m_r, i_s):
            return True, re.search(m_r, i_s)
        else:
            return False, None

    if match is None:
        return False, None

    assert isinstance(match, tuple), f'不支持的match类型{type(match)}'
    if len(match) == 1:
        return match1(string, match[0])
    elif len(match) == 2:
        if isinstance(match[0], dict):
            return match1(string, match[1])
        else:
            return match2(string, match[0], match[1])
    elif len(match) == 3:
        return match2(string, match[1], match[2])
    else:
        raise ValueError(f'不支持的match参数, {match}')


class QueryEngine:

    def __init__(self, code, https_proxy=None):
        self.site = pywikibot.Site(code)
        if https_proxy is not None:
            os.environ['HTTPS_PROXY'] = https_proxy

    def get_wiki_page(self, title, get_redirect=False, force=False):
        page = pywikibot.Page(self.site, title)
        return page.get(get_redirect=get_redirect, force=force)


class TemplateBase:
    # 模板名称，在构建图谱时模板名会当成节点的标签名
    template_name = 'Base'
    # 定义需要获取的字段，以下划线开头的字段表示为多值属性字段
    # 元组中第一个字典形式的数据在构建图谱时是作为边的公共属性
    fields_map = {
        'Name': ({'zh': '名字'}, ['name', 'nama'],),
        'Alias': (
            {'zh': '别名'}, ['alias', 'nickname', 'hangul', 'id', 'pseudonym', 'tradchinesename',
                           'pinyinchinesename', 'simpchinesename', 'nama penuh', 'hanja'],
            re_compile(r'other.*?names?|real.*?name|native.*?names?|player.*?name|chinese.*?name|nama.*?inggeris'
                       r'|birth.*?names?|full.*?name')),
        '_Birth': ({'zh': '出生信息'}, ['birth', 'born', 'keputeraan'],),
        '_Death': ({'zh': '死亡信息'}, ['died']),
        '_Birth Date': (
            {'zh': '出生时间'}, ['tarikh lahir'], re_compile(r'birth.*?date|date.*?birth|born.*?date|date.*?born'),),
        '_Birth Place': (
            {'zh': '出生地点'}, ['tempat lahir', 'tempat keputeraan'],
            re_compile(r'birth.*?place|place.*?birth|born.*?place|place.*?born')),
        'Retirement Date': ({'zh': '退休时间'}, ['retired'], re_compile(r'date.*?ret')),
        '_Birth City': ({'zh': '出生城市'}, re_compile(r'birth.*?city|city.*?birth|born.*?city|city.*?born'),),
        '_Birth Country': (
            {'zh': '出生国家'}, re_compile(r'birth.*?country|country.*?birth|born.*?country|country.*?born'),),
        'Height': ({'zh': '身高'}, ['height'],),
        'Weight': ({'zh': '体重'}, ['weight'],),
        'Nationality': ({'zh': '国籍/民族'}, ['nationality'],),
        'Website': ({'zh': '网站'}, ['website', 'url', 'homepage', 'laman web'],),
        'Origin': ({'zh': '出身/身世/血统'}, ['origin'],),
        'Religion': ({'zh': '宗教'}, ['religion', 'agama'],),
        'Education': ({'zh': '教育'}, ['education', 'pendidikan'],),
        'Occupation': ({'zh': '职业/工作'}, ['occupation', 'occupation(s)', 'pekerjaan', 'ocupation', 'occuption',
                                         'occuoation', 'profession'], re_compile(r'current.*?occupation|other.*?post')),
        'Years Active': ({'zh': '活跃年份'}, ['active', 'yeaesactive', 'era'], re_compile(r'year.*?active')),
        '_Death Date': ({'zh': '死亡时间'}, ['tarikh kematian'], re_compile(r'death.*?date|date.*?death'),),
        '_Death Place': ({'zh': '死亡地点'}, ['tempat kematian'], re_compile(r'death.*?place|place.*?death'),),
        '_Death Cause': ({'zh': '死因'}, re_compile(r'death.*?cause|cause.*?death')),
        '_Burial Place': ({'zh': '埋葬地点'}, re_compile(r'resting.*?place|burial.*?place'),),
        'Spouse': ({'zh': '配偶'}, ['spouse', 'pasangan', 'spouses', 'consort'],),
        'Parents': ({'zh': '父母'}, ['parents'],),
        'Sibling': ({'zh': '兄弟姐妹'}, ['sibling', 'saudara']),
        'Children': ({'zh': '孩子'}, ['children', 'issue', 'anak'],),
        'Gender': ({'zh': '性别'}, ['gender'],),
        'Alma Mater': ({'zh': '母校'}, re_compile(r'alma.*?mater'),),
        'Relatives': ({'zh': '关系'}, ['relatives,husband'], re_compile(r'relatives?|relations?|related.*?to'),),
        'Father': ({'zh': '父亲'}, ['father', 'bapa'],),
        'Mother': ({'zh': '母亲'}, ['mother', 'ibunda'],),
        'Residence': ({'zh': '住宅/(尤指)豪宅'}, ['residence', 'residential'],),
        'Known For': ({'zh': '著名'}, ['known'], re_compile(r'known.*?for'),),
        'Partner': ({'zh': '伙伴/搭档/合伙人'}, ['partner', 'partners'], re_compile(r'former.*?partner|domestic.*?partner')),
        'Citizenship': ({'zh': '公民/公民身份'}, ['citizenship'],),
        'Honorific Prefix': ({'zh': '尊称前缀'}, re_compile(r'honorific.*?prefix'),),
        'Honorific Suffix': ({'zh': '尊称后缀'}, re_compile(r'honorific.*?suffix'),),
        'Home Town': ({'zh': '家乡'}, re_compile(r'home.*?town'),),
        'Employer': ({'zh': '雇主'}, ['employer'],),
        'Family': ({'zh': '家庭/亲属'}, ['family', 'house', 'royal house'],),
        'Ethnicity': ({'zh': '种族'}, ['ethnicity', 'ethnic'],),
        'Subject': ({'zh': '学科'}, ['subject', 'discipline'],),
        'Works': ({'zh': '作品'}, ['works'],),
        'Notable Works': ({'zh': '著名作品'},
                          re_compile(r'notable.*?works?|magnum.*?opus?')),
        'Debut Works': ({'zh': '处女作'}, re_compile(r'debut.*?works?')),
        'Roles': ({'zh': '角色'}, re_compile(r'roles?'),),
        'Notable Roles': ({'zh': '著名角色'}, re_compile(r'notable.*?roles?'),),
        'Net Worth': ({'zh': '净值'}, re_compile(r'net.*?worth'),),
        'Awards': ({'zh': '奖项'}, ['prizes'], re_compile(r'wards?', mode='e'),),
        'Projects': ({'zh': '项目'}, re_compile(r'projects?', mode='e'),),
        'Institutions': (
            {'zh': '机构（包括大学、银行等规模大的机构以及代理机构和工作机构）'}, ['agency', 'organization'],
            re_compile(r'institutions?|work.*?institutions?')),
        'School': ({'zh': '学校'}, ['school', 'college'], re_compile(r'high.*?school')),
        'Hair Color': ({'zh': '发色'}, ['haircolour'], re_compile(r'hair.*?color')),
        'Eye Color': ({'zh': '眼睛颜色'}, ['eyecolour'], re_compile(r'eye.*?color')),
        'Measurements': ({'zh': '三围'}, ['measurements'],),
        'Salary': ({'zh': '薪资'}, ['salary']),
        'Party': ({'zh': '政党'}, ['party'],),
        'Car': ({'zh': '汽车'}, ['car']),
        'Ancestry': ({'zh': '祖籍'}, ['ancestry']),
        'Blood Type': ({'zh': '血型'}, re_compile(r'blood.*?type')),
        'Country': ({'zh': '国家'}, ['country']),
        'Influenced': ({'zh': '受影响'}, ['influenced', 'dipengaruhi'],),
        'Influences': ({'zh': '影响'}, ['influences', 'pengaruh'],),
        'Interests': ({'zh': '兴趣'}, re_compile(r'main.*?interests?')),
        'Previous Occupation': ({'zh': '以前的职业'}, re_compile(r'previous.*?occupation|previous.*?post')),
        'Title': ({'zh': '头衔/职称'}, ['title']),
        'Status': ({'zh': '状态'}, ['dead'], re_compile(r'status', mode='e')),
        'Movement': ({'zh': '(具有共同思想或目标的)运动'}, ['movement', 'movements']),
        'Period': ({'zh': '(人生或国家历史的)时期'}, ['period'])
    }
    # 多值属性字段
    multi_values_field = {
        'Birth': ({'zh': '出生信息'}, ['_Birth Date', '_Birth Place', '_Birth City', '_Birth Country', '_Birth']),
        'Death': ({'zh': '死亡信息'}, ['_Death Date', '_Death Place', '_Burial Place', '_Death', '_Death Cause']),
        # 'Relatives': (
        #     {'zh': '关系'},
        #     ['_Parents', '_Sibling', '_Relatives', '_Family'])
    }
    # 多值字段中必须出现的字段，若没有出现，则认为这个多值字段没有意义
    multi_field_cond = None
    # 在解析时跳过的类型
    dont_parse_type = [mwp.wikicode.Argument, mwp.wikicode.Comment]
    # 解析wiki对象template时需要保存的模板名，通常情况下是因为模板名保存了必要的信息，比如某次比赛中的名次（金牌、银牌等）保存在模板名中
    retain_template_name = (re.compile(r'medal'),)
    # 解析wiki对象template时需要剔除的特殊值，这些值往往无意义
    discard_template_value = (['zh-hans'], re.compile(r'\.svg$|\.png$|\.jpg$|\.jpeg$'))
    # 解析wiki对象WikiLink时需要剔除的值，这些值往往无意义
    discard_wikilink_value = (re.compile(r'\.svg$|\.png$|\.jpg$|\.jpeg$'),)
    # 解析wiki对象template时需要保存的参数名，通常情况下是因为身高体重等字段的参数名中含有度量单位，例如m: 1.76，这些参数名需要保存，确保信息准确
    retain_template_param = (['m', 'end', 'reason', 'award', 'ft', 'in', 'meter', 'meters',
                              'cm', 'kg'], re.compile(r'\d+'))
    # 解析wiki对象tag时需要剔除的标签，这些值往往无意义
    discard_tag_name = (['ref', 'table'],)
    # 对于自定义的所有字段，需要剔除的值，这些值往往无意义
    discard_fields_value = (re.compile(r'nama.*?amerika|nama.*?korea'),)
    # 解析wiki对象text时需要剔除的值
    discard_text_value = None
    # 对于自定义的所有字段，需要替换为空字符串的无意义的值
    replace_fields_value = re.compile(
        r'<\s*small\s*/*?\s*>|<\s*big\s*/*?\s*>|<\s*span\s*/*?\s*>|<\s*nowiki\s*/*?\s*>|<\s*div\s*/*?\s*>')

    def __init__(self, values, entry):
        """
        :param values: 待解析的字典数据
        :param entry: title，词条名
        """
        # 每个字段含有的props和values
        self._fields = {'template_name': self.template_name,
                        'fields': {
                            k: {'relation_props': v[0], 'values': []} if isinstance(v[0], dict) else {'values': []} for
                            k, v in self.fields_map.items()},
                        'entry': entry}
        # 对待解析的字典数据做字段匹配
        self._get_field_values(values)
        # 多值属性不为空时，将多值属性解析成一一对应
        self._process_multi_values_field(entry)

    def _check(self, kkk, vvv):
        temp = set([list(i.keys())[0] for i in vvv])
        if set(self.multi_field_cond.get(kkk, [])).issubset(temp):
            return True
        return False

    def _get_field_values(self, values):
        for k, v in values.items():
            field = None
            index = None
            for kk, vv in self.fields_map.items():
                # 字段匹配
                tag, res = _matches(k.lower().strip(), vv)
                if tag:
                    field = kk
                    # 是否包含多值数据，检查下标
                    if res:
                        groups = [int(i) for i in res.groups() if i]
                        if groups:
                            index = groups.pop()
                    break
            if field:
                # 对wiki对象递归解析
                p_v = self.parse(v.strip())
                h_v = ''.join([str(i) for i in p_v]).strip()
                if h_v:
                    h_v = re.sub(self.replace_fields_value, '', h_v)
                    _console_log.logger.debug(f'\n{field}: {h_v}\n')
                    if index:
                        h_v = {index: h_v}
                        if h_v not in self._fields['fields'][field]['values'] and not \
                                _matches(str(h_v).lower(), self.discard_fields_value)[0]:
                            self._fields['fields'][field]['values'].append(h_v)
                    else:
                        l_h_v = h_v.split('\n')
                        for h_v in l_h_v:
                            h_v = h_v.strip()
                            if h_v and h_v not in self._fields['fields'][field]['values'] and not \
                                    _matches(str(h_v).lower(), self.discard_fields_value)[0]:
                                self._fields['fields'][field]['values'].append(h_v)

    def _process_multi_values_field(self, entry):
        if self.multi_values_field is not None:
            fields_values = {k: v for k, v in self._fields['fields'].items() if
                             v['values'] and all([k not in kk[-1] for kk in
                                                  self.multi_values_field.values()])}
            multi_values_field = {
                k: {'relation_props': v[0], 'values': []} if isinstance(v[0], dict) else {'values': []} for
                k, v in self.multi_values_field.items()}
            for k, v in self._fields['fields'].items():
                if v['values']:
                    for i_k, i_v in self.multi_values_field.items():
                        i_f = i_v[-1]
                        if k in i_f:
                            for iii, jjj in enumerate(v['values']):
                                if not isinstance(jjj, dict):
                                    v['values'][iii] = {str(0) + str(iii): jjj}
                            multi_values_field[i_k]['values'].append({k: v['values']})

            # 检查是否包含必须有的字段
            check = self._check if self.multi_field_cond is not None else lambda *args: True

            multi_values_field = {k: v for k, v in multi_values_field.items() if v['values'] and check(k, v['values'])}
            # 为主实体entry增加props, 构建知识图谱时有用
            name = []
            for k, v in multi_values_field.items():
                name.append(
                    f"{k}: ({', '.join([list(i.keys())[0] for i in v['values']])})"
                )
                v['values'] = _get_multi_values(v['values'])
            fields_values.update(multi_values_field)
            if name:
                self._fields['primary_entity_props'] = {'multi_values_field': '\n'.join(name)}

            # 检查不在多值属性要求的字段是否包含多值数据，如果包含超过2个，抛出异常，有1个时会给出警告
            _values = set([j for i in self.multi_values_field.values() for j in i[-1]])
            _multi = []
            for k, v in fields_values.items():
                if k not in _values:
                    if _is_include_dict(v['values']):
                        _multi.append(k)
            if len(_multi) >= 2:
                raise ValueError(
                    f"field({entry}, {', '.join(_multi)})包含字典即多值数据，不能当成单独字段解析，请将该字段放入multi_values_field中进行解析")
            elif _multi:
                _console_log.logger.warning(f"未指定在multi_values_field中多值字段({entry}, {_multi[0]})")
                fields_values[_multi[0]]['values'] = [list(i.values())[0] if isinstance(i, dict) else i for i in
                                                      fields_values[_multi[0]]['values']]
        # 多值属性为空时，自动将多值属性解析为一个other info字段
        else:
            fields_values = {}
            multi_values_field = []
            name = []
            for k, v in self._fields['fields'].items():
                if v['values']:
                    if _is_include_dict(v['values']):
                        for iii, jjj in enumerate(v['values']):
                            if not isinstance(jjj, dict):
                                v['values'][iii] = {str(0) + str(iii): jjj}
                        multi_values_field.append({k: v['values']})
                        name.append(k)
                    else:
                        fields_values[k] = v
            if multi_values_field:
                if len(name) == 1:
                    fields_values.update({name[0]: {'relation_props': self.fields_map[name[0]][0],
                                                    'values': [list(list(i.values())[0].values())[0] for i
                                                               in
                                                               multi_values_field]}})
                else:
                    fields_values.update({'Other Info': {'relation_props': {'zh': '其他信息'},
                                                         'values': _get_multi_values(multi_values_field)}})
                self._fields['primary_entity_props'] = {'multi_values_field': f"Other Info: ({', '.join(name)})"}
        self._fields['fields'] = fields_values

    @classmethod
    def parse(cls, p_t):
        # 递归解析wiki对象
        p_t = mwp.parse(p_t)
        p_t = p_t.filter(recursive=False)
        for i, j in enumerate(p_t):
            if isinstance(j, mwp.wikicode.Template):
                if str(j.name).strip().lower() == 'br':
                    p_t[i] = mwp.parse('\n')
                else:
                    values = []
                    for k in j.params:
                        tag, res = _matches(str(k.name).strip().lower(), cls.retain_template_param)
                        res = res.group() if res else ''
                        if tag and not _matches(str(k.value).strip().lower(), cls.discard_template_value)[0]:
                            if _is_int(res):
                                values.append(str(k.value))
                            else:
                                values.append(f"[{str(k.name).strip()}: {str(k.value)}]")
                    if _matches(str(j.name).strip().lower(), cls.retain_template_name)[0]:
                        res = f"[{str(j.name).strip()}: {', '.join(values)}]"
                    else:
                        res = ', '.join(values)
                    p_t[i] = mwp.parse(res)
            elif isinstance(j, mwp.wikicode.ExternalLink):
                p_t[i] = j.url
            elif isinstance(j, mwp.wikicode.Tag):
                if not _matches(str(j.tag).strip().lower(), cls.discard_tag_name)[0]:
                    rs = mwp.parse('\n') if str(j.tag).strip().lower() == 'br' else mwp.parse(
                        str(j.contents))
                else:
                    rs = mwp.parse(None)
                p_t[i] = rs
            elif isinstance(j, mwp.wikicode.Wikilink):
                if not _matches(str(j.title).strip().lower(), cls.discard_wikilink_value)[0]:
                    p_t[i] = mwp.parse(str(j.title))
                else:
                    p_t[i] = mwp.parse(None)
            elif isinstance(j, mwp.wikicode.HTMLEntity):
                p_t[i] = mwp.parse(j.normalize())
            elif isinstance(j, mwp.wikicode.Heading):
                p_t[i] = mwp.parse(str(j.title))
            elif any([isinstance(j, k) for k in cls.dont_parse_type]):
                p_t[i] = mwp.parse(None)
        if all([isinstance(ii, mwp.wikicode.Text) for ii in p_t]):
            p_t = [t for t in p_t if not _matches(str(t).lower(), cls.discard_text_value)[0]]
            return p_t
        return cls.parse(p_t)

    @property
    def fields(self):
        # 获取字典类型的数据
        return self._fields

    def __str__(self):
        return self.template_name


class TemplateOfficer(TemplateBase):
    template_name = 'Officer'
    fields_map = {
        '_Reign': ({'zh': '君主统治时期/任期/当政期'}, re_compile(r'reign'),),
        '_Successor': ({'zh': '（政党、政府的）接替者/继任者'}, ['heir'], re_compile(r'successor|succeeded|succeeding')),
        '_Predecessor': ({'zh': '（政党、政府的）前任'}, ['pendahulu'], re_compile(r'predecessor|preceded|preceding'),),
        '_Coronation': ({'zh': '加冕礼'}, re_compile(r'coronation'),),
        '_Succession': ({'zh': '继任/继承权（尤指王位的）'}, re_compile(r'succession'),),
        '_Regent': ({'zh': '摄政者'}, re_compile(r'regent'),),
        '_Office': ({'zh': '要职'}, re_compile(r'office\D{,2}|order'),),
        '_Prime Minister': ({'zh': '总理/首相'}, re_compile(r'prime.*?minister'),),
        '_Minister': ({'zh': '部长/大臣'}, re_compile(r'minister'),),
        '_Term Start': ({'zh': '（政党、政府的）任期开始时间'}, re_compile(r'term.*?start'),),
        '_Term End': ({'zh': '（政党、政府的）任期结束时间'}, re_compile(r'term.*?end'),),
        '_Term': ({'zh': '（政党、政府的）任期'}, re_compile(r'term'),),
        '_Monarch': ({'zh': '君主/帝王'}, re_compile(r'monarch')),
        '_Majority': ({'zh': '(获胜的)票数/多数票'}, re_compile(r'majority')),
        '_Assembly': ({'zh': '议会'}, re_compile(r'assembly')),
        '_State': ({'zh': '州'}, ['negeri'], re_compile(r'state')),
        '_Deputy': ({'zh': '副职'}, re_compile(r'deputy'),),
        '_Leader': ({'zh': '领导'}, re_compile(r'leader'),),
        '_Alongside': ({'zh': '合作/并肩工作'}, re_compile(r'alongside'),),
        '_President': ({'zh': '总统'}, re_compile(r'president'),),
        '_Vice President': ({'zh': '副总统'}, re_compile(r'vice.*?president'),),
        '_Governor': ({'zh': '总督/州长'}, re_compile(r'governor|governor.*?general'),),
        '_Vice Governor': ({'zh': '副总督/副州长'}, re_compile(r'vice.*?governor')),
        '_Appointer': ({'zh': '任命者'}, re_compile(r'appointer'),),
        'Cabinet': ({'zh': '内阁'}, ['cabinet'],),
        'Department': ({'zh': '部门'}, ['department'],),
        'Allegiance': ({'zh': '(对政党、宗教、统治者的)忠诚/效忠'}, re_compile(r'allegiance')),
        '_Nominator': ({'zh': '提名人'}, re_compile(r'nominator'),),
        '_Chancellor': ({'zh': '(德国或奥地利的)总理/(英国的)财政大臣/(英国大学的)名誉校长'}, re_compile(r'chancellor'),),
        '_Lieutenant': ({'zh': '中尉'}, re_compile(r'lieutenant'),),
        '_Appointed': ({'zh': '任职日期'}, re_compile(r'appointed'),),
        'Service Years': ({'zh': '服务年限'}, re_compile(r'service.*?years?')),
        'Rank': ({'zh': '等级/军衔'}, ['rank']),
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Office': ({'zh': '重要职务'},
                   ['_Reign', '_Successor', '_Predecessor', '_Coronation', '_Succession', '_Regent', '_Office',
                    '_Prime Minister', '_Minister', '_Term Start', '_Term End', '_Term', '_Monarch', '_Majority',
                    '_Assembly', '_State', '_Deputy', '_Leader', '_Alongside', '_President', '_Vice President',
                    '_Governor', '_Appointer', '_Nominator', '_Chancellor', '_Lieutenant', '_Appointed',
                    '_Vice Governor'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)


class TemplateSportsPlayer(TemplateBase):
    template_name = 'Sports Player'
    fields_map = {
        'Current Club': ({'zh': '目前俱乐部'}, re_compile(r'current.*?club'),),
        'Club Number': ({'zh': '运动员编号'}, re_compile(r'club.*?number'),),
        'Position': ({'zh': '运动员定位'}, ['position'],),
        '_Years': ({'zh': '年份'}, re_compile(r'years?|club.*?years?'),),
        '_Clubs': ({'zh': '服役俱乐部'}, re_compile(r'clubs?'),),
        '_Caps(Goals)': ({'zh': '出场数(进球数)'}, re_compile(r'caps\(goals\)'),),
        '_Caps': ({'zh': '出场数'}, re_compile(r'caps?'),),
        '_Goals': ({'zh': '进球数'}, re_compile(r'goals?'),),
        '_National Years': ({'zh': '国家队服役年份'}, re_compile(r'national.*?years?'),),
        '_National Team': ({'zh': '国家队'}, re_compile(r'national.*?teams?'),),
        '_National Caps(Goals)': ({'zh': '在国家队出场数(在国家队进球数)'}, re_compile(r'national.*?caps\(goals\)'),),
        '_Youth Clubs': ({'zh': '青年俱乐部'}, re_compile(r'youth.*?clubs?'),),
        '_Youth Years': ({'zh': '青年俱乐部服役年份'}, re_compile(r'youth.*?years?'),),
        '_Youth Caps(Goals)': ({'zh': '在青年俱乐部出场数(在青年俱乐部进球数)'}, re_compile(r'youth.*?caps\(goals\)'),),
        '_Youth Caps': ({'zh': '在青年俱乐部出场数'}, re_compile(r'youth.*?caps?'),),
        '_Youth Goals': ({'zh': '在青年俱乐部进球数'}, re_compile(r'youth[-_\s]*goals?'),),
        '_National Caps': ({'zh': '在国家队出场数'}, re_compile(r'national.*?caps?'),),
        '_National Goals': ({'zh': '在国家队进球数'}, re_compile(r'national[-_\s]*goals?'),),
        'Total Caps': ({'zh': '总出场数'}, re_compile(r'total.*?caps?'),),
        'Total Goals': ({'zh': '总进球数'}, re_compile(r'total.*?goals?'),),
        '_Manager Clubs': ({'zh': '管理俱乐部'}, re_compile(r'manager.*?clubs?'),),
        '_Manager Years': ({'zh': '管理俱乐部年份'}, re_compile(r'manager.*?years?'),),
        'Coach': ({'zh': '教练'}, ['coach'],),
        'Medal': ({'zh': '奖牌'}, re_compile(r'medal.*?templates?'),),
        'Competition': ({'zh': '比赛信息'}, re_compile(r'results?', mode='e')),
        'Style': ({'zh': '风格'}, ['handedness'], re_compile(r'plays?')),
        'Event': ({'zh': '比赛项目'}, ['event']),
        'Head Coach': ({'zh': '总教练'}, re_compile(r'head.*?coach')),
        'Sports': ({'zh': '运动项目'}, re_compile(r'sports?')),
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {'Clubs': ({'zh': '服役俱乐部'}, ['_Years', '_Clubs', '_Caps', '_Goals', '_Caps(Goals)']),
                          'National Team': (
                              {'zh': '服役国家队'},
                              ['_National Years', '_National Team', '_National Caps', '_National Goals',
                               '_National Caps(Goals)']),
                          'Youth Clubs': ({'zh': '服役青年俱乐部'},
                                          ['_Youth Clubs', '_Youth Years', '_Youth Caps(Goals)', '_Youth Caps',
                                           '_Youth Goals']),
                          'Manager Clubs': ({'zh': '管理俱乐部'}, ['_Manager Clubs', '_Manager Years'])}
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {'Clubs': ['_Clubs'],
                        'National Team': ['_National Team'],
                        'Youth Clubs': ['_Youth Clubs'],
                        'Manager Clubs': ['_Manager Clubs']}


class TemplatePerformanceWorker(TemplateBase):
    template_name = 'Performance Worker'
    fields_map = {
        'Genre': ({'zh': '体裁/类型（文学、艺术、电影或音乐的）'}, ['genre', 'genres'],),
        'Label': ({'zh': '唱片公司'}, ['label', 'company', 'syarikat pengurusan'], re_compile(r'record.*?label')),
        'Instruments': ({'zh': '乐器'}, ['instrument', 'instruments', 'instrumen'],),
        'Notable Instruments': ({'zh': '著名乐器'}, re_compile(r'notable.*?instruments?')),
        'Voice Type': ({'zh': '声音类型'}, re_compile(r'voice.*?type'),),
        'Associated Acts': (
            {'zh': '相关艺术家/相关表演者'}, re_compile(r'associated.*?acts?')),
        'Current Members': ({'zh': '现有成员'}, re_compile(r'current.*?members?'),),
        'Past Members': ({'zh': '过去成员'}, re_compile(r'past.*?members?'),),
        'Location': ({'zh': '表演场地/外景拍摄地'}, ['location']),
        'Dress Size': ({'zh': '服装尺码'}, re_compile(r'dress.*?size'),),
        'Shoe Size': ({'zh': '鞋子尺码'}, re_compile(r'shoe.*?size'),),
        'Number Films': ({'zh': '电影数目'}, re_compile(r'number.*?films'),),
        'Orientation': ({'zh': '性取向'}, ['orientation'],),
        'Films': ({'zh': '电影'}, ['films', 'film'],),
        'Agent': ({'zh': '经纪人'}, ['agent'],),
        'Television': ({'zh': '电视节目'}, ['television'],),
        'Medium': ({'zh': '(传播信息的)媒介'}, ['medium']),
        'Fan Club': ({'zh': '粉丝俱乐部'}, ['kelab peminat'])
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateResearchers(TemplateBase):
    template_name = 'Researchers'
    fields_map = {
        'Workplace': ({'zh': '工作地'}, re_compile(r'work.*?places?')),
        '_Thesis Year': ({'zh': '论文年份'}, re_compile(r'thesis.*?years?')),
        '_Thesis Title': ({'zh': '论文标题'}, re_compile(r'thesis.*?titles?')),
        '_Thesis Url': ({'zh': '论文链接'}, re_compile(r'thesis.*?urls?')),
        'Fields': ({'zh': '领域'}, ['field', 'fields']),
        'Academic Advisors': ({'zh': '学术顾问'}, re_compile(r'academic.*?advisors?')),
        'Doctoral Advisors': ({'zh': '博士生导师'}, re_compile(r'doctoral.*?advisors?')),
        'Boards': ({'zh': '董事会'}, ['boards']),
        'Doctoral Students': ({'zh': '博士生'}, re_compile(r'doctoral.*?students?')),
        'Notable Students': ({'zh': '著名学生'}, re_compile(r'notable.*?students?')),
        'Contributions': ({'zh': '贡献'}, ['contributions', 'contribution']),
        'Notable Ideas': ({'zh': '著名想法'}, re_compile(r'notable.*?ideas?')),
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Thesis': ({'zh': '论文'}, ['_Thesis Title', '_Thesis Year', '_Thesis Url'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Thesis': ['_Thesis Title']
    }
