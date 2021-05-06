#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author : xiexx
@email  : xiaoxuanemail@163.com
"""

from wiki_person_parser.base import (re_compile, TemplateBase, TemplateOfficer, TemplateResearchers,
                                     TemplatePerformanceWorker, TemplateSportsPlayer)


class TemplateMotorcycleRider(TemplateBase):
    template_name = 'Motorcycle Rider'
    fields_map = {
        'Current Team': ({'zh': '目前团队'}, re_compile(r'current.*?team'),),
        'Bike Number': ({'zh': '自行车号码'}, re_compile(r'bike.*?number'),)
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateEngineer(TemplateBase):
    template_name = 'Engineer'


class TemplateWarDetainee(TemplateBase):
    template_name = 'War Detainee'
    fields_map = {
        'Arrest Place': ({'zh': '逮捕地点'}, re_compile(r'arrest.*?place|place.*?arrest'),),
        'Arrest Date': ({'zh': '逮捕日期'}, re_compile(r'arrest.*?date|date.*?arrest'),),
        'Arresting Authority': ({'zh': '逮捕机关'}, re_compile(r'arresting.*?authority'),),
        'Detained At': ({'zh': '拘留处'}, re_compile(r'detained.*?at'),),
        'Charge': ({'zh': '指控'}, ['charge'],),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateTwitchStreamer(TemplateBase):
    template_name = 'Twitch Streamer'
    fields_map = {
        'Channel Name': ({'zh': '频道名'}, re_compile(r'channel.*?name')),
        'Followers': ({'zh': '关注者'}, re_compile(r'followers?')),
        'Views': ({'zh': '观看数'}, re_compile(r'views?'))
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateYouTubePersonality(TemplateBase):
    template_name = 'YouTube Personality'
    fields_map = {
        'Network': ({'zh': '网络'}, ['network']),
        'Catchphrase': ({'zh': '口号'}, ['catchphrase', 'catchphrases', 'catchphrase(s)']),
        'Views': ({'zh': '观看数'}, re_compile(r'views?')),
        'Channel Name': ({'zh': '频道名'}, re_compile(r'channel.*?name')),
        'Channel Url': ({'zh': '频道链接'}, ['channel', 'channels'], re_compile(r'channel.*?url')),
        'Subscribers': ({'zh': '订阅者'}, re_compile(r'subscribers?')),
        'Genre': ({'zh': '体裁/类型（文学、艺术、电影或音乐的）'}, ['genre', 'genres'],),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateAstronaut(TemplateBase):
    template_name = 'Astronaut'
    fields_map = {
        'Mission': ({'zh': '使命'}, ['mission']),
        'Space Time': ({'zh': '舱外活动时间'}, ['time'], re_compile(r'space.*?time')),
        'Selection': ({'zh': '选拔'}, ['selection']),
        'Rank': ({'zh': '等级/军衔'}, ['rank']),
        '_Eva': ({'zh': '舱外活动'}, re_compile(r'evas?|eva.*?time')),
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Eva': ({'zh': '舱外活动'}, ['_Eva'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)


class TemplateCelebrity(TemplateBase):
    template_name = 'Celebrity'


class TemplateJournalist(TemplateBase):
    template_name = 'Journalist'


class TemplateFashionDesigner(TemplateBase):
    template_name = 'Fashion Designer'
    fields_map = {
        'Tag': ({'zh': '标签'}, re_compile(r'label.*?name'))
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateMilitaryPerson(TemplateBase):
    template_name = 'Military Person'
    fields_map = {
        'Office': ({'zh': '重要职务'}, re_compile(r'commands?')),
        'Branch': ({'zh': '分支部门'}, re_compile(r'branch')),
        'Unit': ({'zh': '部队'}, re_compile(r'unit')),
        'Allegiance': ({'zh': '(对政党、宗教、统治者的)忠诚/效忠'}, re_compile(r'allegiance')),
        'Service Years': ({'zh': '服务年限'}, re_compile(r'service.*?years?')),
        'Battles': ({'zh': '战争'}, re_compile(r'battles?')),
        'Rank': ({'zh': '等级/军衔'}, ['rank']),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateArchitect(TemplateBase):
    template_name = 'Architect'
    fields_map = {
        'Buildings': ({'zh': '建筑物'}, re_compile(r'significant.*?buildings?'))
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateArchbishop(TemplateBase):
    template_name = 'Archbishop'
    fields_map = {
        '_Enthroned': ({'zh': '即位时间'}, ['enthroned']),
        '_Archbishop Of': ({'zh': '大主教'}, re_compile(r'archbishop', mode='s')),
        '_Consecration': ({'zh': '祝胜礼/授职礼'}, ['consecration']),
        'Motto': ({'zh': '座右铭'}, ['motto']),
        '_Ordination': ({'zh': '派立礼/授神职礼'}, ['ordination']),
        '_Consecrated By': ({'zh': '被祝胜/被授职'}, re_compile(r'consecrated', mode='s')),
        '_Ordained By': ({'zh': '被派立/被授神职'}, re_compile(r'ordained', mode='s')),
        '_Successor': ({'zh': '（政党、政府的）接替者/继任者'}, ['heir'], re_compile(r'successor|succeeded|succeeding')),
        '_Predecessor': ({'zh': '（政党、政府的）前任'}, ['pendahulu'], re_compile(r'predecessor|preceded|preceding'),),
        '_Ended': ({'zh': '结束时间'}, ['ended'])
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {'Office': ({'zh': '重要职务'},
                                     ['_Enthroned', '_Ended', '_Successor', '_Predecessor',
                                      '_Consecration', '_Consecrated By', '_Ordination', '_Ordained By',
                                      '_Archbishop Of'])}
    multi_values_field.update(TemplateBase.multi_values_field)


class TemplateFootballOfficial(TemplateBase):
    template_name = 'Football Official'
    fields_map = {
        '_League': ({'zh': '联盟'}, re_compile(r'league'),),
        '_Years': ({'zh': '年份'}, re_compile(r'years?'),),
        '_International Years': ({'zh': '国际年份'}, re_compile(r'international.*?years'),),
        '_International League': ({'zh': '国际联盟'}, re_compile(r'confederation'),),
        '_International Role': ({'zh': '国际角色'}, re_compile(r'international.*?roles?'),)
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'League': ({'zh': '联盟'}, ['_League', 'Roles', '_Years']),
        'International League': (
            {'zh': '国际联盟'}, ['_International League', '_International Role', '_International Years'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'League': ['_League'],
        'International League': ['_International League']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateGolfer(TemplateBase):
    template_name = 'Golfer'
    fields_map = {
        '_Years': ({'zh': '年份'}, re_compile(r'years?')),
        'Tour': ({'zh': '巡回比赛'}, re_compile(r'tour', mode='e')),
        'Turned Pro': ({'zh': '成为职业选手/专业选手'}, re_compile(r'year.*?professional|professional.*?years?')),
        'Wins': ({'zh': '获胜次数'}, re_compile(r'wins?', mode='e')),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateBoxer(TemplateBase):
    template_name = 'Boxer'
    fields_map = {
        'Ko': ({'zh': 'ko胜利次数'}, ['ko']),
        'Total': ({'zh': '总次数'}, ['total']),
        'Style': ({'zh': '风格'}, ['style']),
        'Wins': ({'zh': '获胜次数'}, re_compile(r'wins?')),
        'Draws': ({'zh': '平局次数'}, re_compile(r'draws?')),
        'Losses': ({'zh': '失败次数'}, re_compile(r'losses|loss'))
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateF1Driver(TemplateBase):
    template_name = 'F1 Driver'
    fields_map = {
        '_Car Number': ({'zh': '车号'}, re_compile(r'car.*?number')),
        '_Years': ({'zh': '年份'}, re_compile(r'years?')),
        'Last Win': ({'zh': '最后一次胜利'}, re_compile(r'last.*?win')),
        'Championships': ({'zh': '锦标赛'}, re_compile(r'championships?')),
        'Poles': ({'zh': '极点'}, re_compile(r'poles?')),
        '_Teams': ({'zh': '团队'}, ['team(s)'], re_compile(r'teams?')),
        'First Win': ({'zh': '第一次胜利'}, re_compile(r'first.*?win')),
        'Last Season': ({'zh': '最后一个赛季'}, re_compile(r'last.*?season')),
        'Races': ({'zh': '竞赛信息'}, re_compile(r'races?')),
        'Fastest Laps': ({'zh': '最快圈速'}, re_compile(r'fastest.*?laps?')),
        'Last Race': ({'zh': '最后一场竞赛'}, re_compile(r'last.*?race')),
        'First Race': ({'zh': '第一场竞赛'}, re_compile(r'first.*?race')),
        'Wins': ({'zh': '获胜次数'}, re_compile(r'wins?')),
        'Podiums': ({'zh': '领奖台次数'}, re_compile(r'podiums?')),
        'Points': ({'zh': '点/分'}, re_compile(r'points?')),
        'Last Position': ({'zh': '最后位置'}, re_compile(r'last.*?position')),
        'Best Finish': ({'zh': '最好战绩'}, re_compile('best.*?finish')),
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Teams': ({'zh': '团队/队伍'}, ['_Teams', '_Car Number', '_Years'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Teams': ['_Teams']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateVideoGamePlayer(TemplateBase):
    template_name = 'Video Game Player'
    fields_map = {
        '_Years': ({'zh': '年份'}, re_compile(r'years?')),
        '_Teams': ({'zh': '团队'}, re_compile(r'teams?')),
        '_Coach Years': ({'zh': '教练年份'}, re_compile(r'cyears?')),
        '_Coach Teams': ({'zh': '教练团队'}, re_compile(r'cteams?')),
        '_League': ({'zh': '联盟'}, re_compile(r'leagues?')),
        'Games': ({'zh': '游戏'}, re_compile(r'games?'))
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'League': ({'zh': '联盟'}, ['_League']),
        'Teams': ({'zh': '团队/队伍'}, ['_Teams', '_Years']),
        'Coach Teams': ({'zh': '教练团队/队伍'}, ['_Coach Teams', '_Coach Years'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'League': ['_League'],
        'Teams': ['_Teams'],
        'Coach Teams': ['_Coach Teams']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateArtist(TemplateBase):
    template_name = 'Artist'
    fields_map = {
        'Training': ({'zh': '训练/培训'}, ['training']),
        'Fields': ({'zh': '领域'}, ['field', 'fields']),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateMartialArtist(TemplateBase):
    template_name = 'Martial Artist'
    fields_map = {
        'Ko': ({'zh': 'ko胜利次数'}, re_compile(r'kowin', mode='e')),
        'Wins': ({'zh': '获胜次数'}, re_compile(r'wins?', mode='e')),
        'Draws': ({'zh': '平局次数'}, re_compile(r'draws?', mode='e')),
        'Losses': ({'zh': '失败次数'}, re_compile(r'loss|losses', mode='e')),
        'Style': ({'zh': '风格'}, ['style']),
        'Weight Class': ({'zh': '重量级'}, re_compile(r'weight.*?class'))
    }
    fields_map.update(TemplateBase.fields_map)


class TemplatePageantTitleholder(TemplateBase):
    template_name = 'Pageant Titleholder'
    fields_map = {
        'Competition': ({'zh': '比赛信息'}, re_compile(r'competitions?', mode='e')),
        'Agent': ({'zh': '经纪人'}, ['agent'],),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateWrestler(TemplateBase):
    template_name = 'Wrestler'
    fields_map = {
        'Trainer': ({'zh': '训练员/助理教练'}, ['trainer']),
        'Debut': ({'zh': '首次亮相'}, ['debut'])
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateChristianLeader(TemplateBase):
    template_name = 'Christian Leader'
    fields_map = {
        '_Enthroned': ({'zh': '即位时间'}, ['enthroned']),
        '_Archbishop Of': ({'zh': '大主教'}, re_compile(r'archbishop', mode='s')),
        '_Consecration': ({'zh': '祝胜礼/授职礼'}, ['consecration']),
        'Motto': ({'zh': '座右铭'}, ['motto']),
        '_Ordination': ({'zh': '派立礼/授神职礼'}, ['ordination']),
        '_Consecrated By': ({'zh': '被祝胜/被授职'}, re_compile(r'consecrated', mode='s')),
        '_Ordained By': ({'zh': '被派立/被授神职'}, re_compile(r'ordained', mode='s')),
        '_Successor': ({'zh': '（政党、政府的）接替者/继任者'}, ['heir'], re_compile(r'successor|succeeded|succeeding')),
        '_Predecessor': ({'zh': '（政党、政府的）前任'}, ['pendahulu'], re_compile(r'predecessor|preceded|preceding'),),
        '_Ended': ({'zh': '结束时间'}, ['ended'], re_compile(r'term.*?end')),
        '_Appointed': ({'zh': '任职日期'}, re_compile(r'appointed'),),
        '_Cardinal': ({'zh': '红衣主教/枢机主教'}, ['cardinal']),
        '_Created Cardinal By': ({'zh': '被创建基数'}, re_compile(r'created.*?cardinal', mode='s'))
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {'Office': ({'zh': '重要职务'},
                                     ['_Enthroned', '_Ended', '_Successor', '_Predecessor',
                                      '_Consecration', '_Consecrated By', '_Ordination', '_Ordained By',
                                      '_Archbishop Of', '_Cardinal', '_Created Cardinal By', '_Appointed'])}
    multi_values_field.update(TemplateBase.multi_values_field)


class TemplateCriminal(TemplateBase):
    template_name = 'Criminal'
    fields_map = {
        'Penalty': ({'zh': '刑罚/处罚'}, ['penalty'], re_compile(r'conviction.*?penalty')),
        'Victims': ({'zh': '受害人'}, re_compile(r'victims?')),
        'Conviction': ({'zh': '定罪'}, ['conviction']),
        'Allegiance': ({'zh': '(对政党、宗教、统治者的)忠诚/效忠'}, re_compile(r'allegiance')),
        'Motive': ({'zh': '动机'}, ['motive']),
        'Charge': ({'zh': '指控'}, ['charge'],),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateCyclist(TemplateBase):
    template_name = 'Cyclist'
    fields_map = {
        '_Pro Team': ({'zh': '专业团队'}, re_compile(r'pro.*?teams?')),
        'Medal': ({'zh': '奖牌'}, re_compile(r'medal.*?templates?'),),
        '_Pro Years': ({'zh': '专业团队年份'}, re_compile(r'pro.*?years?')),
        'Current Team': ({'zh': '目前团队'}, re_compile(r'current.*?team'),),
        'Major Wins': ({'zh': '重大胜利'}, re_compile(r'major.*?wins?'))
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Pro Team': ({'zh': '专业团队'}, ['_Pro Team', '_Pro Years'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Pro Team': ['_Pro Team']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateIceHockeyPlayer(TemplateBase):
    template_name = 'Ice Hockey Player'
    fields_map = {
        '_League': ({'zh': '联盟'}, re_compile(r'leagues?'),),
        '_Height(in)': ({'zh': '身高(英寸)'}, re_compile(r'height.*?in')),
        '_Height(ft)': ({'zh': '身高(英尺)'}, re_compile(r'height.*?ft')),
        'Draft Team': ({'zh': '选秀队'}, re_compile(r'draft.*?team')),
        '_Teams': ({'zh': '团队/队伍'}, re_compile(r'teams?')),
        'Position': ({'zh': '运动员定位'}, ['position'],),
        'Draft Year': ({'zh': '选秀年份'}, re_compile(r'draft.*?year')),
        'Career Start': ({'zh': '职业生涯开始'}, re_compile(r'career.*?start')),
        'Draft': ({'zh': '选秀'}, ['draft']),
        '_Weight(lb)': ({'zh': '体重(磅)'}, re_compile(r'weight.*?lbs?'))
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Teams': ({'zh': '团队/队伍'}, ['_Teams']),
        'League': ({'zh': '联盟'}, ['_League']),
        'Height': ({'zh': '身高'}, ['_Height(in)', '_Height(ft)']),
        'Weight': ({'zh': '体重'}, ['_Weight(lb)'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Teams': ['_Teams'],
        'League': ['_League']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateWriter(TemplateBase):
    template_name = 'Writer'
    fields_map = {
        'Language': ({'zh': '语言'}, ['language']),
        'Genre': ({'zh': '体裁/类型（文学、艺术、电影或音乐的）'}, ['genre', 'genres'],),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateMuslimScholar(TemplateBase):
    template_name = 'Muslim Scholar'


class TemplateSpy(TemplateBase):
    template_name = 'Spy'
    fields_map = {
        'Allegiance': ({'zh': '(对政党、宗教、统治者的)忠诚/效忠'}, re_compile(r'allegiance')),
        'Service Years': ({'zh': '服务年限'}, re_compile(r'service.*?years?')),
        'Service': ({'zh': '服务'}, ['service']),
        'Rank': ({'zh': '等级/军衔'}, ['rank']),
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateBasketballBiography(TemplateBase):
    template_name = 'Basketball Biography'
    fields_map = {
        '_Height(in)': ({'zh': '身高(英寸)'}, re_compile(r'height.*?in')),
        '_Height(ft)': ({'zh': '身高(英尺)'}, re_compile(r'height.*?ft')),
        'Highlights': ({'zh': '高光时刻'}, re_compile(r'highlights?')),
        '_Years': ({'zh': '年份'}, re_compile(r'years?')),
        '_Teams': ({'zh': '团队'}, re_compile(r'teams?')),
        '_Coach Years': ({'zh': '教练年份'}, re_compile(r'cyears?')),
        '_Coach Teams': ({'zh': '教练团队'}, re_compile(r'cteams?')),
        'Career Start': ({'zh': '职业生涯开始'}, re_compile(r'career.*?start')),
        'Career End': ({'zh': '职业生涯结束'}, re_compile(r'career.*?end')),
        'Career Number': ({'zh': '职业生涯号码'}, re_compile(r'career.*?number')),
        'Career Position': ({'zh': '职业生涯位置'}, re_compile(r'career.*?position')),
        '_Weight(lb)': ({'zh': '体重(磅)'}, re_compile(r'weight.*?lbs?')),
        'Draft Team': ({'zh': '选秀队'}, re_compile(r'draft.*?team')),
        'Draft Round': ({'zh': '选秀回合'}, re_compile(r'draft.*?round')),
        'Draft Year': ({'zh': '选秀年份'}, re_compile(r'draft.*?year')),
        'Draft Pick': ({'zh': '选秀选择'}, re_compile(r'draft.*?pick')),
        'Medal': ({'zh': '奖牌'}, re_compile(r'medal.*?templates?'),),
        'Coach Start': ({'zh': '教练生涯开始'}, re_compile(r'coach.*?start')),
        'Coach End': ({'zh': '教练生涯结束'}, re_compile(r'coach.*?end')),
        '_Stat Label': ({'zh': '统计信息(标题)'}, re_compile(r'stat.*?label')),
        '_Stat Value': ({'zh': '统计信息(值)'}, re_compile(r'stat.*?value')),
        '_Stat League': ({'zh': '统计信息(联盟)'}, re_compile(r'stat.*?league'))
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Height': ({'zh': '身高'}, ['_Height(in)', '_Height(ft)']),
        'Weight': ({'zh': '体重'}, ['_Weight(lb)']),
        'Teams': ({'zh': '团队/队伍'}, ['_Teams', '_Years']),
        'Statistics': ({'zh': '统计信息'}, ['_Stat League', '_Stat Label', '_Stat Value']),
        'Coach Teams': ({'zh': '教练团队/队伍'}, ['_Coach Teams', '_Coach Years'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Teams': ['_Teams'],
        'Coach Teams': ['_Coach Teams']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateReligiousBiography(TemplateBase):
    template_name = 'Religious Biography'
    fields_map = {
        'Denomination': ({'zh': '教派/宗派'}, ['denomination'])
    }
    fields_map.update(TemplateBase.fields_map)


class TemplateComicsCreator(TemplateBase):
    template_name = 'Comics Creator'


class TemplateRacingDriver(TemplateBase):
    template_name = 'Racing Driver'
    fields_map = {
        '_Year': ({'zh': '最好战绩年份'}, ['year']),
        '_Best Finish': ({'zh': '最好战绩'}, re_compile('best.*?finish')),
        'Poles': ({'zh': '极点'}, re_compile(r'poles?')),
        'Wins': ({'zh': '获胜次数'}, re_compile(r'wins?')),
        'Starts': ({'zh': '第一次数'}, re_compile(r'starts?')),
        '_Titles': ({'zh': '冠军'}, ['titles']),
        '_Title Years': ({'zh': '冠军年份'}, re_compile(r'title.*?years?')),
        '_Years': ({'zh': '年份'}, re_compile(r'award.*?years?')),
        'Last Series': ({'zh': '最后一个系列'}, re_compile(r'last.*?series?')),
        'First Year': ({'zh': '第一个系列'}, re_compile(r'first.*?year')),
        'Fastest Laps': ({'zh': '最快圈速'}, re_compile(r'fastest.*?laps?')),
        '_Prev Series Years': ({'zh': '以前的系列年份'}, re_compile(r'prev.*?series?.*?years?')),
        '_Prev Series': ({'zh': '以前的系列'}, re_compile(r'prev.*?series?')),
        'Car Number': ({'zh': '车号'}, re_compile(r'car.*?number')),
        'Current Team': ({'zh': '目前团队'}, re_compile(r'current.*?team'),),
        'Current Series': ({'zh': '目前系列'}, re_compile(r'current.*?series?')),
        '_Teams': ({'zh': '团队/队伍'}, re_compile(r'teams?')),
        'Former Teams': ({'zh': '著名团队/队伍'}, re_compile(r'former.*?teams?'))
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Teams': ({'zh': '团队/队伍'}, ['_Teams']),
        'Best Finish': ({'zh': '最好战绩'}, ['_Year', '_Best Finish']),
        'Titles': ({'zh': '冠军'}, ['_Titles', '_Title Years']),
        'Prev Series': ({'zh': '以前系列'}, ['_Prev Series Years', '_Prev Series'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Teams': ['_Teams'],
        'Best Finish': ['_Best Finish'],
        'Titles': ['_Titles']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateRoyalty(TemplateOfficer):
    template_name = 'Royalty'


class TemplateMinister(TemplateOfficer):
    template_name = 'Minister'


class TemplateOfficeholder(TemplateOfficer):
    template_name = 'Officeholder'


class TemplateVicePresident(TemplateOfficer):
    template_name = 'Vice President'


class TemplatePrimeMinister(TemplateOfficer):
    template_name = 'Prime Minister'


class TemplateMP(TemplateOfficer):
    template_name = 'Member of Parliament'


class TemplateGovernor(TemplateOfficer):
    template_name = 'Governor'


class TemplateSenator(TemplateOfficer):
    template_name = 'Senator'


class TemplatePresident(TemplateOfficer):
    template_name = 'President'


class TemplateJudge(TemplateOfficer):
    template_name = 'Judge'


class TemplateAM(TemplateOfficer):
    template_name = 'Assembly Member'


class TemplateMonarch(TemplateOfficer):
    template_name = 'Monarch'


class TemplateCabinetOfficer(TemplateOfficer):
    template_name = 'Cabinet Officer'


class TemplateIndianPolitician(TemplateOfficer):
    template_name = 'Indian Politician'


class TemplatePolitician(TemplateOfficer):
    template_name = 'Politician'
    fields_map = {
        'Unit': ({'zh': '部队'}, re_compile(r'unit')),
        'Branch': ({'zh': '分支部门'}, re_compile(r'branch')),
        'Battles': ({'zh': '战争'}, re_compile(r'battles?')),
    }
    fields_map.update(TemplateOfficer.fields_map)


class TemplateFirstLady(TemplateOfficer):
    template_name = 'First Lady'


class TemplateChineseActorSinger(TemplatePerformanceWorker):
    template_name = 'Chinese Actor And Singer'


class TemplateModel(TemplatePerformanceWorker):
    template_name = 'Model'


class TemplateAdultBiography(TemplatePerformanceWorker):
    template_name = 'Adult Biography'


class TemplateActor(TemplatePerformanceWorker):
    template_name = 'Actor'


class TemplateIndonesiaArtist(TemplatePerformanceWorker):
    template_name = 'Indonesia Artist'


class TemplateComedian(TemplatePerformanceWorker):
    template_name = 'Comedian'


class TemplateMusicalArtist(TemplatePerformanceWorker):
    template_name = 'Musical Artist'


class TemplateScientist(TemplateResearchers):
    template_name = 'Scientist'


class TemplateEconomist(TemplateResearchers):
    template_name = 'Economist'


class TemplatePhilosopher(TemplateResearchers):
    template_name = 'Philosopher'
    fields_map = {
        'Philosophy': ({'zh': '哲学'}, ['region'])
    }
    fields_map.update(TemplateResearchers.fields_map)


class TemplateFootballPlayer(TemplateSportsPlayer):
    template_name = 'Football Player'


class TemplateSwimmer(TemplateSportsPlayer):
    template_name = 'Swimmer'


class TemplateFieldHockeyPlayer(TemplateSportsPlayer):
    template_name = 'Field Hockey Player'


class TemplateTennisPlayer(TemplateSportsPlayer):
    template_name = 'Tennis Player'
    fields_map = {
        'Singles Record': ({'zh': '单打纪录'}, re_compile(r'single.*?record')),
        'Singles Titles': ({'zh': '单打冠军'}, re_compile(r'single.*?titles?')),
        'Highest Singles Ranking': ({'zh': '最高单打排名'}, re_compile(r'highest.*?single.*?ranking')),
        'Current Singles Ranking': ({'zh': '目前单打排名'}, re_compile(r'current.*?single.*?ranking')),
        'Doubles Record': ({'zh': '双打记录'}, re_compile(r'double.*?record')),
        'Doubles Titles': ({'zh': '双打冠军'}, re_compile(r'double.*?titles?')),
        'Highest Doubles Ranking': ({'zh': '最高双打排名'}, re_compile(r'highest.*?double.*?ranking')),
        'Current Doubles Ranking': ({'zh': '目前双打排名'}, re_compile(r'current.*?double.*?ranking')),
        'Mixed Titles': ({'zh': '混打冠军'}, re_compile(r'mixed.*?titles?')),
        'Mixed Record': ({'zh': '混打记录'}, re_compile(r'mixed.*?record')),
        'Turned Pro': ({'zh': '成为职业选手/专业选手'}, re_compile(r'turned.*?pro')),
        'Career Prize Money': ({'zh': '职业奖金'}, re_compile(r'career.*?prize.*?money')),
    }
    fields_map.update(TemplateSportsPlayer.fields_map)


class TemplateBadmintonPlayer(TemplateSportsPlayer):
    template_name = 'Badminton Player'
    fields_map = {
        'Highest Ranking': ({'zh': '最高排名'}, re_compile(r'highest.*?ranking')),
        'Current Ranking': ({'zh': '目前排名'}, re_compile(r'current.*?ranking')),
        'Career Record': ({'zh': '生涯记录'}, re_compile(r'career.*?record')),
        'Date Of Current Ranking': (
            {'zh': '目前排名日期'}, re_compile(r'date.*?current.*?ranking|current.*?ranking.*?date')),
        'Date Of Highest Ranking': (
            {'zh': '最高排名日期'}, re_compile(r'highest.*?ranking.*?date|date.*?highest.*?ranking')),
        '_Titles': ({'zh': '冠军'}, ['titles']),
    }
    fields_map.update(TemplateSportsPlayer.fields_map)
    multi_values_field = {
        'Titles': ({'zh': '冠军'}, ['_Titles', '_Title Years']),
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Titles': ['_Titles']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateSquashPlayer(TemplateSportsPlayer):
    template_name = 'Squash Player'
    fields_map = {
        'Date Of Current Ranking': (
            {'zh': '目前排名日期'}, re_compile(r'date.*?current.*?ranking|current.*?ranking.*?date')),
        'Date Of Highest Ranking': (
            {'zh': '最高排名日期'}, re_compile(r'highest.*?ranking.*?date|date.*?highest.*?ranking')),
        'Racquet': ({'zh': '球拍'}, ['racquet']),
        'Finals': ({'zh': '决赛'}, ['finals', 'final']),
        '_Titles': ({'zh': '冠军'}, ['titles']),
        'Highest Ranking': ({'zh': '最高排名'}, re_compile(r'highest.*?ranking')),
        'Current Ranking': ({'zh': '目前排名'}, re_compile(r'current.*?ranking')),
    }
    fields_map.update(TemplateSportsPlayer.fields_map)
    multi_values_field = {
        'Titles': ({'zh': '冠军'}, ['_Titles', '_Title Years']),
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Titles': ['_Titles']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateSportPerson(TemplateSportsPlayer):
    template_name = 'Sport Person'
    fields_map = {
        '_Teams': ({'zh': '团队/队伍'}, re_compile(r'teams?')),
        'College Team': ({'zh': '大学团队'}, re_compile(r'college.*?teams?')),
        'Training': ({'zh': '训练/培训'}, ['training']),
    }
    fields_map.update(TemplateSportsPlayer.fields_map)
    multi_values_field = {
        'Teams': ({'zh': '团队/队伍'}, ['_Teams'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Teams': ['_Teams']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)


class TemplateHandballPlayer(TemplateSportsPlayer):
    template_name = 'Handball Player'


class TemplateGymnast(TemplateSportsPlayer):
    template_name = 'Gymnast'


_TEMPLATE_MAP = {
    TemplateMotorcycleRider: ['infobox motorcycle rider'],
    TemplateEngineer: ['infobox engineer'],
    TemplateChineseActorSinger: ['infobox chinese actor and singer',
                                 'infobox chinese-language singer and actor'],
    TemplateRoyalty: ['infobox royalty', 'infobox diraja'],
    TemplateModel: ['infobox model'],
    TemplateMinister: ['infobox minister'],
    TemplateOfficeholder: ['infobox officeholder', 'infobox_officeholder'],
    TemplateFootballPlayer: ['infobox football biography', 'pemain bola infobox', 'football player infobox',
                             'infobox football biography 2', 'infobox biografi bolasepak'],
    TemplateFootballOfficial: ['infobox football official'],
    TemplateAdultBiography: ['infobox adult male', 'infobox adult biography'],
    TemplateActor: ['infobox actor', 'infobox actor voice', 'infobox_actor', 'infobox actress'],
    TemplateWarDetainee: ['infobox war on terror detainee', 'infobox wot detainees'],
    TemplateVicePresident: ['infobox vice president'],
    TemplateSwimmer: ['infobox swimmer'],
    TemplateIndonesiaArtist: ['infobox artis indonesia'],
    TemplatePrimeMinister: ['infobox_prime minister', 'infobox prime minister'],
    TemplateMP: ['infobox mp'],
    TemplateScientist: ['infobox ahli sains', 'infobox_scientist', 'infobox scientist'],
    TemplateEconomist: ['infobox economist'],
    TemplateGovernor: ['infobox governor general', 'infobox governor'],
    TemplateSenator: ['infobox senator'],
    TemplateGolfer: ['infobox golfer', 'infobox pemain golf'],
    TemplateFieldHockeyPlayer: ['infobox field hockey player'],
    TemplateTennisPlayer: ['infobox tennis biography', 'infobox tennis player'],
    TemplateBoxer: ['infobox peninju', 'infobox boxer'],
    TemplateTwitchStreamer: ['infobox twitch streamer'],
    TemplatePhilosopher: ['infobox philosopher', 'infobox_philosopher'],
    TemplateAstronaut: ['infobox angkasawan', 'infobox astronaut'],
    TemplateJudge: ['infobox judge'],
    TemplatePresident: ['infobox president', 'infobox_president'],
    TemplateCelebrity: ['infobox celebrity', 'infobox_celebrity'],
    TemplateSquashPlayer: ['infobox squash player'],
    TemplateF1Driver: ['infobox f1 driver', 'infobox le mans driver'],
    TemplateJournalist: ['infobox journalist'],
    TemplateFashionDesigner: ['infobox fashion designer'],
    TemplateMilitaryPerson: ['infobox military person', 'infobox anggota tentera'],
    TemplateVideoGamePlayer: ['infobox video game player'],
    TemplateSportPerson: ['infobox sportsperson'],
    TemplateArchitect: ['infobox arkitek', 'infobox architect'],
    TemplateArchbishop: ['infobox archbishop'],
    TemplateAM: ['infobox am'],
    TemplateMonarch: ['infobox monarch', 'infobox_monarch'],
    TemplateHandballPlayer: ['infobox handball biography'],
    TemplateArtist: ['infobox artist'],
    TemplateMartialArtist: ['infobox martial artist'],
    TemplateComedian: ['infobox comedian'],
    TemplateCabinetOfficer: ['infobox pegawai kabinet asasp@,', 'infobox us cabinet official'],
    TemplatePageantTitleholder: ['infobox pageant titleholder'],
    TemplateWrestler: ['infobox wrestler', 'infobox professional wrestler'],
    TemplateIndianPolitician: ['infobox indian politician'],
    TemplatePolitician: ['infobox_politician', 'infobox politician'],
    TemplateGymnast: ['infobox gymnast'],
    TemplateFirstLady: ['infobox first lady'],
    TemplateChristianLeader: ['infobox christian leader'],
    TemplateMusicalArtist: ['infobox musical artist', 'infobox musical artist 2', 'infobox musical_artist',
                            'infobox ahli muzik'],
    TemplateCriminal: ['infobox criminal'],
    TemplateCyclist: ['infobox cyclist'],
    TemplateIceHockeyPlayer: ['infobox ice hockey player'],
    TemplateWriter: ['infobox pengarang', 'infobox writer'],
    TemplateMuslimScholar: ['infobox muslim scholar'],
    TemplateSpy: ['infobox spy'],
    TemplateYouTubePersonality: ['infobox youtube personality'],
    TemplateBasketballBiography: ['infobox basketball biography'],
    TemplateReligiousBiography: ['infobox religious biography'],
    TemplateSportsPlayer: ['infobox badminton player'],
    TemplateComicsCreator: ['infobox comics creator'],
    TemplateRacingDriver: ['infobox racing driver']
}


class TemplateDefine:
    template_name = 'Define'

    define_template = [TemplateBase]

    def __init__(self, values, entry):
        _props = []
        self._fields = {'template_name': self.template_name,
                        'entry': entry}
        fields = self.define_template[0]
        self._fields['fields'] = fields(values, entry).fields['fields']
        for temp in range(1, len(self.define_template)):
            temp = self.define_template[temp]
            res = temp(values, entry)
            for k, v in res.fields['fields'].items():
                if self._fields['fields'].get(k):
                    for li in v['values']:
                        if li not in self._fields['fields'][k]['values']:
                            self._fields['fields'][k]['values'].append(li)
                else:
                    self._fields['fields'][k] = v
            if res.fields.get('primary_entity_props'):
                for i_s in res.fields['primary_entity_props']['multi_values_field'].split('\n'):
                    if i_s not in _props:
                        _props.append(i_s)
        if _props:
            self._fields['primary_entity_props'] = {'multi_values_field': '\n'.join(_props)}

    @property
    def fields(self):
        return self._fields

    def __str__(self):
        return self.template_name


class TemplatePerson(TemplateDefine):
    template_name = 'Person'
    define_template = list(_TEMPLATE_MAP.keys())


TEMPLATE_MAP = {i: k for k, v in _TEMPLATE_MAP.items() for i in v}
