# WikiPersonParser
- [x] 用于对维基百科的人物表格基础数据进行解析并生成三元组
- [x] 构建是以马来西亚语为基础进行构建
- [x] 可通过自定义模板拓展解析器进行任意语种的解析（该语种的维基百科数据中含有表格数据且是规范化的）
- [x] 通过生成的三元组和对应词条的纯文本数据可以生成符合（句子，实体一，实体二，关系）格式的语料
- [ ] 拓展多语种支持
- [ ] 对多个语言表示的同一人物的关系和实体进行对齐

# 安装
pip install wiki_person_parser-0.0.1-py3-none-any.whl

# 使用
## XMLParser解析器
#### 对于格式如下所示的xml字符串或xml文件
```xml
<test>
    <page>
        <title>Salvador Sobral</title>
        <ns>0</ns>
        <id>982642</id>
        <revision>
            <id>4781586</id>
            <parentid>4781570</parentid>
            <timestamp>2020-04-29T22:34:29Z</timestamp>
            <contributor>
                <username>Fandi89</username>
                <id>172012</id>
            </contributor>
            <comment>Kemaskini.</comment>
            <model>wikitext</model>
            <format>text/x-wiki</format>
            <text bytes="3286" xml:space="preserve">{{Infobox musical artist
| name = Salvador Sobral &lt;br /&gt;&lt;small&gt;[[Order of Merit (Portugal)|ComM]]&lt;/small&gt;
| background = solo_singer
| image = Salvador Sobral RedCarpet Kyiv 2017.jpg
| caption = Sobral di [[Kiev]] tahun 2017
| birth_name = Salvador Vilar Braamcamp Sobral
| birth_date = {{birth date and age|df=yes|1989|12|28}}
| birth_place = [[Lisbon]], Portugal
| origin = 
| genre = {{hlist|[[Muzik alternatif]]|[[soul]]|[[jazz]]}}
| occupation = Penyanyi
| instrument = {{hlist|Vokal|piano}}
| years_active = 2009–kini
| label = Valentim de Carvalho
| associated_acts = {{hlist|Noko Woi|[[Luísa Sobral]]|[[Alexander Search (band)|Alexander Search]]}}
| website = 
}}

'''Salvador Vilar Braamcamp Sobral''' {{small|[[Ordem do Mérito (Portugal)|ComM]]}} [|saɫvɐˈðoɾ viˈlaɾ bɾɐ̃ˈkɐ̃p suˈβɾaɫ], lahir 28 Disember 1989) ialah seorang penyanyi lelaki Portugal. Beliau meraih kemenangan negara tersebut yang pertama malah yang tertinggi (sebanyak 758 mata dari juri dan penonton&lt;ref&gt;{{cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|title=Portugal's Salvador Sobral wins Eurovision Song Contest|publisher=CNN|author=Laura Smith-Spark and Steve Almasy|accessdate=14 May 2017|archiveurl=https://web.archive.org/web/20170513230359/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|archivedate=13 May 2017|df=}}&lt;/ref&gt;&lt;ref&gt;{{cite web|url=https://www.bbc.com/news/live/entertainment-arts-39894917|title=Full coverage: Eurovision 2017|date=13 Mei 2017|publisher=BBC|accessdate=13 May 2017|archiveurl=https://web.archive.org/web/20170514041738/http://www.bbc.com/news/live/entertainment-arts-39894917|archivedate=14 May 2017|df=}}&lt;/ref&gt;) dalam acara [[Pertandingan Lagu Eurovision 2017]] yang diadakan di [[Kiev]] dengan lagu &quot;Amar pelos dois&quot; gubahan [[Luísa Sobral]], kakaknya.&lt;ref&gt;{{Cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |title=Portugal's Salvador Sobral wins Eurovision Song Contest |last=CNN |first=Laura Smith-Spark and Steve Almasy |website=CNN |access-date=2017-05-17  |archiveurl=https://web.archive.org/web/20170516172215/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |archivedate=16 May 2017 |df= }}&lt;/ref&gt;

==Diskografi==

===Album studio===
* ''Excuse Me'' (2016)
* ''Paris, Lisboa'' (2019)

==Rujukan==
{{reflist|2}}

{{s-start}}
{{S-ach}}
{{succession box
| before=[[Leonor Andrade]]&lt;br/&gt;dengan &quot;[[Há um mar que nos separa]]&quot;
| title=[[Portugal di Pertandingan Lagu Eurovision]]
| years=[[Pertandingan Lagu Eurovision 2017|2017]]
| after=[[Cláudia Pascoal]]&lt;br/&gt;dengan &quot;[[O jardim]]&quot;
}}
{{succession box
| before={{flagicon|Ukraine}} [[Jamala]]&lt;br /&gt;dengan &quot;[[1944 (lagu)|1944]]&quot;
| title=[[Senarai pemenang Pertandingan Lagu Eurovision|Pemenang Pertandingan Lagu Eurovision]]
| years=[[Pertandingan Lagu Eurovision 2017|2017]]
| after={{flagicon|Israel}} [[Netta Barzilai|Netta]]&lt;br /&gt;dengan &quot;[[Toy (lagu)|Toy]]&quot;
}}
{{s-end}}

{{Senarai pemenang Pertandingan Lagu Eurovision}}
{{Kawalan kewibawaan}}

[[Kategori:Kelahiran 1989]]
[[Kategori:Pemenang Pertandingan Lagu Eurovision]]
[[Kategori:Orang hidup]]
[[Kategori:Penyanyi lelaki Portugal]]</text>
            <sha1>4i8j3argp30g0seiighm734ngzfnn0s</sha1>
        </revision>
    </page>
    <page>
        <title>Oryctolagus</title>
        <ns>0</ns>
        <id>238308</id>
        <redirect title="Arnab Eropah"/>
        <revision>
            <id>1347339</id>
            <timestamp>2010-12-10T16:14:41Z</timestamp>
            <contributor>
                <username>Malurian123</username>
                <id>10336</id>
            </contributor>
            <minor/>
            <comment>Melencong ke [[Arnab Eropah]]</comment>
            <model>wikitext</model>
            <format>text/x-wiki</format>
            <text bytes="26" xml:space="preserve">#REDIRECT [[Arnab Eropah]]</text>
            <sha1>49i7t6crhim1r3hrnvhdb9b0lqw628q</sha1>
        </revision>
    </page>
</test>
```
#### 可以采用XMLParser解析器对其进行解析，并生成JSON数据
```python
from wiki_person_parser import XMLParser

xml_parser = XMLParser(code='ms')
xml_parser.parse_file('./test.xml')
# 对于大文件数据可采用
# xml_parser.parse_file_block('./test.xml')
xml_parser.save('./test.json', encoding='utf-8')
```
#### 其生成的JSON数据格式如下所示，键为该词条的id，值中包括词条名title、链接url、符合wiki标语语言的所有文本all text、符合wiki标记语言的人物表格信息info text和不包括表格信息的纯文本内容string text
```json
{
   "982642": {
      "title": "Salvador Sobral",
      "id url": "https://ms.wikipedia.org/wiki?curid=982642",
      "title url": "https://ms.wikipedia.org/wiki/Salvador_Sobral",
      "all text": "{{Infobox musical artist\n| name = Salvador Sobral <br /><small>[[Order of Merit (Portugal)|ComM]]</small>\n| background = solo_singer\n| image = Salvador Sobral RedCarpet Kyiv 2017.jpg\n| caption = Sobral di [[Kiev]] tahun 2017\n| birth_name = Salvador Vilar Braamcamp Sobral\n| birth_date = {{birth date and age|df=yes|1989|12|28}}\n| birth_place = [[Lisbon]], Portugal\n| origin =\n| genre = {{hlist|[[Muzik alternatif]]|[[soul]]|[[jazz]]}}\n| occupation = Penyanyi\n| instrument = {{hlist|Vokal|piano}}\n| years_active = 2009–kini\n| label = Valentim de Carvalho\n| associated_acts = {{hlist|Noko Woi|[[Luísa Sobral]]|[[Alexander Search (band)|Alexander Search]]}}\n| website =\n}}\n\n'''Salvador Vilar Braamcamp Sobral''' {{small|[[Ordem do Mérito (Portugal)|ComM]]}} [|saɫvɐˈðoɾ viˈlaɾ bɾɐ̃ˈkɐ̃p suˈβɾaɫ], lahir 28 Disember 1989) ialah seorang penyanyi lelaki Portugal. Beliau meraih kemenangan negara tersebut yang pertama malah yang tertinggi (sebanyak 758 mata dari juri dan penonton<ref>{{cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|title=Portugal's Salvador Sobral wins Eurovision Song Contest|publisher=CNN|author=Laura Smith-Spark and Steve Almasy|accessdate=14 May 2017|archiveurl=https://web.archive.org/web/20170513230359/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|archivedate=13 May 2017|df=}}</ref><ref>{{cite web|url=https://www.bbc.com/news/live/entertainment-arts-39894917|title=Full coverage: Eurovision 2017|date=13 Mei 2017|publisher=BBC|accessdate=13 May 2017|archiveurl=https://web.archive.org/web/20170514041738/http://www.bbc.com/news/live/entertainment-arts-39894917|archivedate=14 May 2017|df=}}</ref>) dalam acara [[Pertandingan Lagu Eurovision 2017]] yang diadakan di [[Kiev]] dengan lagu \"Amar pelos dois\" gubahan [[Luísa Sobral]], kakaknya.<ref>{{Cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |title=Portugal's Salvador Sobral wins Eurovision Song Contest |last=CNN |first=Laura Smith-Spark and Steve Almasy |website=CNN |access-date=2017-05-17  |archiveurl=https://web.archive.org/web/20170516172215/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |archivedate=16 May 2017 |df= }}</ref>\n\n==Diskografi==\n\n===Album studio===\n* ''Excuse Me'' (2016)\n* ''Paris, Lisboa'' (2019)\n\n==Rujukan==\n{{reflist|2}}\n\n{{s-start}}\n{{S-ach}}\n{{succession box\n| before=[[Leonor Andrade]]<br/>dengan \"[[Há um mar que nos separa]]\"\n| title=[[Portugal di Pertandingan Lagu Eurovision]]\n| years=[[Pertandingan Lagu Eurovision 2017|2017]]\n| after=[[Cláudia Pascoal]]<br/>dengan \"[[O jardim]]\"\n}}\n{{succession box\n| before={{flagicon|Ukraine}} [[Jamala]]<br />dengan \"[[1944 (lagu)|1944]]\"\n| title=[[Senarai pemenang Pertandingan Lagu Eurovision|Pemenang Pertandingan Lagu Eurovision]]\n| years=[[Pertandingan Lagu Eurovision 2017|2017]]\n| after={{flagicon|Israel}} [[Netta Barzilai|Netta]]<br />dengan \"[[Toy (lagu)|Toy]]\"\n}}\n{{s-end}}\n\n{{Senarai pemenang Pertandingan Lagu Eurovision}}\n{{Kawalan kewibawaan}}\n\n[[Kategori:Kelahiran 1989]]\n[[Kategori:Pemenang Pertandingan Lagu Eurovision]]\n[[Kategori:Orang hidup]]\n[[Kategori:Penyanyi lelaki Portugal]]",
      "info text": "{{Infobox musical artist\n| name = Salvador Sobral <br /><small>[[Order of Merit (Portugal)|ComM]]</small>\n| background = solo_singer\n| image = Salvador Sobral RedCarpet Kyiv 2017.jpg\n| caption = Sobral di [[Kiev]] tahun 2017\n| birth_name = Salvador Vilar Braamcamp Sobral\n| birth_date = {{birth date and age|df=yes|1989|12|28}}\n| birth_place = [[Lisbon]], Portugal\n| origin =\n| genre = {{hlist|[[Muzik alternatif]]|[[soul]]|[[jazz]]}}\n| occupation = Penyanyi\n| instrument = {{hlist|Vokal|piano}}\n| years_active = 2009–kini\n| label = Valentim de Carvalho\n| associated_acts = {{hlist|Noko Woi|[[Luísa Sobral]]|[[Alexander Search (band)|Alexander Search]]}}\n| website =\n}}",
      "string text": "\n\nSalvador Vilar Braamcamp Sobral Ordem do Mérito (Portugal) [|saɫvɐˈðoɾ viˈlaɾ bɾɐ̃ˈkɐ̃p suˈβɾaɫ], lahir 28 Disember 1989) ialah seorang penyanyi lelaki Portugal. Beliau meraih kemenangan negara tersebut yang pertama malah yang tertinggi (sebanyak 758 mata dari juri dan penonton) dalam acara Pertandingan Lagu Eurovision 2017 yang diadakan di Kiev dengan lagu \"Amar pelos dois\" gubahan Luísa Sobral, kakaknya.\n\nDiskografi\n\nAlbum studio\n Excuse Me (2016)\n Paris, Lisboa (2019)\n\nRujukan\n2\n\n\n\n\n\n\n\n\n\n\nKategori:Kelahiran 1989\nKategori:Pemenang Pertandingan Lagu Eurovision\nKategori:Orang hidup\nKategori:Penyanyi lelaki Portugal"
   },
   "238308": {
      "title": "Oryctolagus",
      "redirect title": "Arnab Eropah",
      "id url": "https://ms.wikipedia.org/wiki?curid=238308",
      "title url": "https://ms.wikipedia.org/wiki/Oryctolagus",
      "all text": "#REDIRECT [[Arnab Eropah]]",
      "string text": "REDIRECT Arnab Eropah",
      "redirect url": "https://ms.wikipedia.org/wiki/Arnab_Eropah"
   }
}
```
#### XMLParser解析器的参数说明如下
- handler：wiki内容解析器，默认为WikiContentHandler处理
- filter_categories：定义该字段可以在解析过程中保留特定类别的数据，例如在马来西亚语数据中定义filter_categories=['Orang', 'Tokoh', 'Kelahiran', 'Kematian']可以解析出属于人物的词条
- category：该字段表示对应语种中表示类别的单词，例如在马来西亚语中定义category='Kategori'
- code：对应语种的ISO639-1编码
- category_wiki_type：表示形容类别的数据只能出现在定义的字段中，若不在，解析过程中会过滤掉这些数据，默认值为category_wiki_type=['wikilinks']，表示类别数据出现在wiki标记语言中的链接标记中
***
## 模板引擎解析抽取三元组
#### 对于已解析完成的JSON数据中的all text（也可以是符合wiki标记语言的字符串数据，数据格式如下）
```text
{{Infobox musical artist
| name = Salvador Sobral <br /><small>[[Order of Merit (Portugal)|ComM]]</small>
| background = solo_singer
| image = Salvador Sobral RedCarpet Kyiv 2017.jpg
| caption = Sobral di [[Kiev]] tahun 2017
| birth_name = Salvador Vilar Braamcamp Sobral
| birth_date = {{birth date and age|df=yes|1989|12|28}}
| birth_place = [[Lisbon]], Portugal
| origin =
| genre = {{hlist|[[Muzik alternatif]]|[[soul]]|[[jazz]]}}
| occupation = Penyanyi
| instrument = {{hlist|Vokal|piano}}
| years_active = 2009–kini
| label = Valentim de Carvalho
| associated_acts = {{hlist|Noko Woi|[[Luísa Sobral]]|[[Alexander Search (band)|Alexander Search]]}}
| website =
}}

'''Salvador Vilar Braamcamp Sobral''' {{small|[[Ordem do Mérito (Portugal)|ComM]]}} [|saɫvɐˈðoɾ viˈlaɾ bɾɐ̃ˈkɐ̃p suˈβɾaɫ], lahir 28 Disember 1989) ialah seorang penyanyi lelaki Portugal. Beliau meraih kemenangan negara tersebut yang pertama malah yang tertinggi (sebanyak 758 mata dari juri dan penonton<ref>{{cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|title=Portugal's Salvador Sobral wins Eurovision Song Contest|publisher=CNN|author=Laura Smith-Spark and Steve Almasy|accessdate=14 May 2017|archiveurl=https://web.archive.org/web/20170513230359/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|archivedate=13 May 2017|df=}}</ref><ref>{{cite web|url=https://www.bbc.com/news/live/entertainment-arts-39894917|title=Full coverage: Eurovision 2017|date=13 Mei 2017|publisher=BBC|accessdate=13 May 2017|archiveurl=https://web.archive.org/web/20170514041738/http://www.bbc.com/news/live/entertainment-arts-39894917|archivedate=14 May 2017|df=}}</ref>) dalam acara [[Pertandingan Lagu Eurovision 2017]] yang diadakan di [[Kiev]] dengan lagu "Amar pelos dois" gubahan [[Luísa Sobral]], kakaknya.<ref>{{Cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |title=Portugal's Salvador Sobral wins Eurovision Song Contest |last=CNN |first=Laura Smith-Spark and Steve Almasy |website=CNN |access-date=2017-05-17  |archiveurl=https://web.archive.org/web/20170516172215/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |archivedate=16 May 2017 |df= }}</ref>

==Diskografi==

===Album studio===
* ''Excuse Me'' (2016)
* ''Paris, Lisboa'' (2019)

==Rujukan==
{{reflist|2}}

{{s-start}}
{{S-ach}}
{{succession box
| before=[[Leonor Andrade]]<br/>dengan "[[Há um mar que nos separa]]"
| title=[[Portugal di Pertandingan Lagu Eurovision]]
| years=[[Pertandingan Lagu Eurovision 2017|2017]]
| after=[[Cláudia Pascoal]]<br/>dengan "[[O jardim]]"
}}
{{succession box
| before={{flagicon|Ukraine}} [[Jamala]]<br />dengan "[[1944 (lagu)|1944]]"
| title=[[Senarai pemenang Pertandingan Lagu Eurovision|Pemenang Pertandingan Lagu Eurovision]]
| years=[[Pertandingan Lagu Eurovision 2017|2017]]
| after={{flagicon|Israel}} [[Netta Barzilai|Netta]]<br />dengan "[[Toy (lagu)|Toy]]"
}}
{{s-end}}

{{Senarai pemenang Pertandingan Lagu Eurovision}}
{{Kawalan kewibawaan}}

[[Kategori:Kelahiran 1989]]
[[Kategori:Pemenang Pertandingan Lagu Eurovision]]
[[Kategori:Orang hidup]]
[[Kategori:Penyanyi lelaki Portugal]]
```
#### 可以利用模板引擎解析获得三元组数据
```python
from wiki_person_parser import Parser
string = """
{all text类型数据}
"""
result = Parser.parse_wiki_data(data=string, entry='Salvador Sobral')
print(result)
```
#### 抽取结果如下所示
```json
{
   "template_name": [
      "Musical Artist"
   ],
   "entry": "Salvador Sobral",
   "all_text": "\n{{Infobox musical artist\n| name = Salvador Sobral <br /><small>[[Order of Merit (Portugal)|ComM]]</small>\n| background = solo_singer\n| image = Salvador Sobral RedCarpet Kyiv 2017.jpg\n| caption = Sobral di [[Kiev]] tahun 2017\n| birth_name = Salvador Vilar Braamcamp Sobral\n| birth_date = {{birth date and age|df=yes|1989|12|28}}\n| birth_place = [[Lisbon]], Portugal\n| origin =\n| genre = {{hlist|[[Muzik alternatif]]|[[soul]]|[[jazz]]}}\n| occupation = Penyanyi\n| instrument = {{hlist|Vokal|piano}}\n| years_active = 2009–kini\n| label = Valentim de Carvalho\n| associated_acts = {{hlist|Noko Woi|[[Luísa Sobral]]|[[Alexander Search (band)|Alexander Search]]}}\n| website =\n}}\n\n'''Salvador Vilar Braamcamp Sobral''' {{small|[[Ordem do Mérito (Portugal)|ComM]]}} [|saɫvɐˈðoɾ viˈlaɾ bɾɐ̃ˈkɐ̃p suˈβɾaɫ], lahir 28 Disember 1989) ialah seorang penyanyi lelaki Portugal. Beliau meraih kemenangan negara tersebut yang pertama malah yang tertinggi (sebanyak 758 mata dari juri dan penonton<ref>{{cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|title=Portugal's Salvador Sobral wins Eurovision Song Contest|publisher=CNN|author=Laura Smith-Spark and Steve Almasy|accessdate=14 May 2017|archiveurl=https://web.archive.org/web/20170513230359/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html|archivedate=13 May 2017|df=}}</ref><ref>{{cite web|url=https://www.bbc.com/news/live/entertainment-arts-39894917|title=Full coverage: Eurovision 2017|date=13 Mei 2017|publisher=BBC|accessdate=13 May 2017|archiveurl=https://web.archive.org/web/20170514041738/http://www.bbc.com/news/live/entertainment-arts-39894917|archivedate=14 May 2017|df=}}</ref>) dalam acara [[Pertandingan Lagu Eurovision 2017]] yang diadakan di [[Kiev]] dengan lagu \"Amar pelos dois\" gubahan [[Luísa Sobral]], kakaknya.<ref>{{Cite web|url=http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |title=Portugal's Salvador Sobral wins Eurovision Song Contest |last=CNN |first=Laura Smith-Spark and Steve Almasy |website=CNN |access-date=2017-05-17  |archiveurl=https://web.archive.org/web/20170516172215/http://www.cnn.com/2017/05/13/europe/ukraine-eurovision-song-contest-grand-finals/index.html |archivedate=16 May 2017 |df= }}</ref>\n\n==Diskografi==\n\n===Album studio===\n* ''Excuse Me'' (2016)\n* ''Paris, Lisboa'' (2019)\n\n==Rujukan==\n{{reflist|2}}\n\n{{s-start}}\n{{S-ach}}\n{{succession box\n| before=[[Leonor Andrade]]<br/>dengan \"[[Há um mar que nos separa]]\"\n| title=[[Portugal di Pertandingan Lagu Eurovision]]\n| years=[[Pertandingan Lagu Eurovision 2017|2017]]\n| after=[[Cláudia Pascoal]]<br/>dengan \"[[O jardim]]\"\n}}\n{{succession box\n| before={{flagicon|Ukraine}} [[Jamala]]<br />dengan \"[[1944 (lagu)|1944]]\"\n| title=[[Senarai pemenang Pertandingan Lagu Eurovision|Pemenang Pertandingan Lagu Eurovision]]\n| years=[[Pertandingan Lagu Eurovision 2017|2017]]\n| after={{flagicon|Israel}} [[Netta Barzilai|Netta]]<br />dengan \"[[Toy (lagu)|Toy]]\"\n}}\n{{s-end}}\n\n{{Senarai pemenang Pertandingan Lagu Eurovision}}\n{{Kawalan kewibawaan}}\n\n[[Kategori:Kelahiran 1989]]\n[[Kategori:Pemenang Pertandingan Lagu Eurovision]]\n[[Kategori:Orang hidup]]\n[[Kategori:Penyanyi lelaki Portugal]]\n",
   "string_text": "\n\n\nSalvador Vilar Braamcamp Sobral Ordem do Mérito (Portugal) [|saɫvɐˈðoɾ viˈlaɾ bɾɐ̃ˈkɐ̃p suˈβɾaɫ], lahir 28 Disember 1989) ialah seorang penyanyi lelaki Portugal. Beliau meraih kemenangan negara tersebut yang pertama malah yang tertinggi (sebanyak 758 mata dari juri dan penonton) dalam acara Pertandingan Lagu Eurovision 2017 yang diadakan di Kiev dengan lagu \"Amar pelos dois\" gubahan Luísa Sobral, kakaknya.\n\nDiskografi\n\nAlbum studio\n Excuse Me (2016)\n Paris, Lisboa (2019)\n\nRujukan\n2\n\n\n\n\n\n\n\n\n\n\nKategori:Kelahiran 1989\nKategori:Pemenang Pertandingan Lagu Eurovision\nKategori:Orang hidup\nKategori:Penyanyi lelaki Portugal\n",
   "info_text": "{{Infobox musical artist\n| name = Salvador Sobral <br /><small>[[Order of Merit (Portugal)|ComM]]</small>\n| background = solo_singer\n| image = Salvador Sobral RedCarpet Kyiv 2017.jpg\n| caption = Sobral di [[Kiev]] tahun 2017\n| birth_name = Salvador Vilar Braamcamp Sobral\n| birth_date = {{birth date and age|df=yes|1989|12|28}}\n| birth_place = [[Lisbon]], Portugal\n| origin =\n| genre = {{hlist|[[Muzik alternatif]]|[[soul]]|[[jazz]]}}\n| occupation = Penyanyi\n| instrument = {{hlist|Vokal|piano}}\n| years_active = 2009–kini\n| label = Valentim de Carvalho\n| associated_acts = {{hlist|Noko Woi|[[Luísa Sobral]]|[[Alexander Search (band)|Alexander Search]]}}\n| website =\n}}",
   "fields": {
      "Genre": {
         "relation_props": {
            "zh": "体裁/类型（文学、艺术、电影或音乐的）"
         },
         "values": [
            "Muzik alternatif, soul, jazz"
         ]
      },
      "Label": {
         "relation_props": {
            "zh": "唱片公司"
         },
         "values": [
            "Valentim de Carvalho"
         ]
      },
      "Instruments": {
         "relation_props": {
            "zh": "乐器"
         },
         "values": [
            "Vokal, piano"
         ]
      },
      "Associated Acts": {
         "relation_props": {
            "zh": "相关艺术家/相关表演者"
         },
         "values": [
            "Noko Woi, Luísa Sobral, Alexander Search (band)"
         ]
      },
      "Name": {
         "relation_props": {
            "zh": "名字"
         },
         "values": [
            "Salvador Sobral",
            "Order of Merit (Portugal)"
         ]
      },
      "Alias": {
         "relation_props": {
            "zh": "别名"
         },
         "values": [
            "Salvador Vilar Braamcamp Sobral"
         ]
      },
      "Occupation": {
         "relation_props": {
            "zh": "职业/工作"
         },
         "values": [
            "Penyanyi"
         ]
      },
      "Years Active": {
         "relation_props": {
            "zh": "活跃年份"
         },
         "values": [
            "2009–kini"
         ]
      },
      "Birth": {
         "relation_props": {
            "zh": "出生信息"
         },
         "values": [
            "birth date:1989, 12, 28\nbirth place:Lisbon, Portugal"
         ]
      }
   },
   "primary_entity_props": {
      "multi_values_field": "Birth: (_Birth Date, _Birth Place)"
   }
}
```
#### 也可以采用网络请求进行在线解析
```python
from wiki_person_parser import Parser
import json
result = Parser.parse_wiki_title(title='Salvador Sobral', code='ms', https_proxy=None)
print(json.dumps(result, ensure_ascii=False, indent=3))
```
#### Parser解析器的方法说明如下
- parse_wiki_data：对数据格式为all text（或符合wiki标记语言）的字符串进行解析并抽取三元组数据，其参数如下
    - data：传入的数据
    - entry: 词条名
    - force：强解析，为True时采用强解析，即对未出现在现有模板的新词条采用已定义的所有模板进行解析，为False时为弱解析，即对未出现在现有模板的新词条采用基础模板进行解析
- parse_wiki_title：对词条进行在线解析
    - title：词条名
    - code：对应语种的ISO639-1编码
    - https_proxy：https代理，默认None
    - force：同parse_wiki_data
    - get_redirect：是否采用词条重定向，为False时，如果该词条是重定向词条，会直接抛出异常
#### WikiContentHandler和Parser具有的类属性
##### 共有属性
- info_field：表示表格数据的字段名，与语种相关，在马来西亚语中info_field=Infobox
- base_template：基础模板，定义了基础映射集合和一系列方法
##### Parser独有属性
- default_template：对新词条（不能利用已有模板进行解析）的数据将会采用该模板进行解析，强解析时默认为TemplatePerson，弱解析时默认为TemplateBase
- map_template：模板与最显著职业映射，当词条出现在映射集合中时，采用映射的模板进行解析，否则采用default_template进行解析
***
## 自定义模板、拓展解析器
#### 当需要解析新语种或新出现的词条时（已定义模板不能解析的情况下），可以根据需求定义新的模板，并将新模板添加到解析器中
```python
from wiki_person_parser import TemplateBase, Parser, TemplateDefine, re_compile, TemplateResearchers


class TemplateDoctor(TemplateBase):
    template_name = 'Doctor'
    fields_map = {
        'Fields': ({'zh': '领域'}, ['field', 'fields']),
        '_Awards': ({'zh': '奖项'}, ['prizes'], re_compile(r'wards?', mode='e')),
        '_Years': ({'zh': '年份'}, re_compile(r'years?'))
    }
    fields_map.update(TemplateBase.fields_map)
    multi_values_field = {
        'Awards': ({'zh': '奖项'}, ['_Awards', '_Years'])
    }
    multi_values_field.update(TemplateBase.multi_values_field)
    multi_field_cond = {
        'Awards': ['_Awards']
    }
    multi_field_cond.update(TemplateBase.multi_field_cond)
    

class NewTemplatePerson(TemplateDefine):
    template_name = 'Doctor Or Researchers'
    define_template = [TemplateDoctor, TemplateResearchers]


class NewParser(Parser):
    base_template = TemplateBase
    default_template = NewTemplatePerson
    map_template = []
```
#### 如上所示则新定义了一个Doctor模板用来解析最显著职业为Doctor的，同时新定义了Person模板，该模板只解析Doctor或Researchers，最后将新定义的模板加到解析器中定义新解析器NewParser，对于输入的data，该解析器只会利用Doctor和Researchers模板进行解析
#### TemplateBase具有的属性和方法
##### 属性
- template_name：模板名称，对应最显著职业
- fields_map：单值关系集合，定义需要获取的属性，数据格式为dict类型，格式为{单值关系名: (关系属性[可缺失]，强匹配[list类型，可缺失，与弱匹配二选一]，弱匹配[re.Pattern类型，可缺失，与强匹配二选一])}，单值指的是类似出生信息只有一个值的时候，其内部不会有复杂的对应信息
- multi_values_field：多值属性集合，定义需要获取的多值属性，其内部有复杂的对应信息，比如获奖次数可能不止一次，每次获奖都包含奖项、获奖年份等信息，这些是一一对应的，格式为{多值关系名:(关系属性[可缺失]，[单值关系名...])}
- multi_field_cond：多值属性条件，防止误召回，比如对应奖项信息，只有出现奖项名该奖项信息才是有意义的，当只有奖项年份时，该数据会被直接过滤掉，格式为{多值关系名:[必须出现的单值关系名...]}
- dont_parse_type：解析时跳过的wiki标记语言类型，默认为[Argument, Comment]
- retain_template_name：解析wiki对象template时需要保存的模板名，通常情况下是因为模板名保存了必要的信息，比如某次比赛中的名次（金牌、银牌等）保存在模板名中
- discard_template_value：解析wiki对象template时需要剔除的特殊值，这些值往往无意义
- discard_wikilink_value：解析wiki对象WikiLink时需要剔除的值，这些值往往无意义
- retain_template_param：解析wiki对象template时需要保存的参数名，通常情况下是因为身高体重等字段的参数名中含有度量单位，例如m: 1.76，这些参数名需要保存，确保信息准确
- discard_tag_name：解析wiki对象tag时需要剔除的标签，这些值往往无意义
- discard_fields_value：对于自定义的所有字段，需要剔除的值，这些值往往无意义
- discard_text_value：解析wiki对象text时需要剔除的值
- replace_fields_value：对于自定义的所有字段，需要替换为空字符串的无意义的值
- replace_text_value：解析wiki对象text需要替换的值
##### 方法
- parse：递归解析wiki标记语言方法
- fields：获取已解析好的JSON数据
***
## 抽取句子语料
#### 在获取三元组数据后，可以利用三元组和纯文本作相似度计算获得格式为（句子，实体一，实体二，关系）的语料，可以根据相似度阈值作筛选或过滤
```python
from wiki_person_parser import Corpus, Parser

string = """
{all text类型数据}
"""
char_corpus = Corpus(max_paragraph_length=3, field_thr=0.8, sentence_thr=0.8, match_ratio=0.8)
all_word_corpus = Corpus(max_paragraph_length=3, field_thr=0.7, sentence_thr=0.7, match_ratio=0.6,
                         match_type='all word')
part_word_corpus = Corpus(max_paragraph_length=3, field_thr=0.6, sentence_thr=0.7, match_ratio=0.6,
                          match_type='part word')

res = Parser.parse_wiki_data(string, entry='Salvador Sobral')
char_corpus.set_item(res)
all_word_corpus.set_item(res)
part_word_corpus.set_item(res)
print('------fields------\n', char_corpus.json_entities, '\n------end------\n')
print('------char match------\n', char_corpus.corpus(), '\n------end------\n')
print('------part word match------\n', part_word_corpus.corpus(), '\n------end------\n')
print('------all word match------\n', all_word_corpus.corpus(), '\n------end------\n\n\n')
```
#### 其结果如下所示
- fields
```json
{
   "Name": [
      "Putera Naruhiko Higashikuni"
   ],
   "Alias": [
      "東久邇宮稔彦王"
   ],
   "Occupation": [
      "Kerabat F\\Diraja Jepun",
      "General"
   ],
   "Spouse": [
      "Toshiko Higashikuni"
   ],
   "Alma Mater": [
      "Akademi Tentera Empayar Imperial Jepun",
      "Maktab Perang Tentera Jepun",
      "Akademi Tentera Darat Empayar Imperial Jepun"
   ],
   "Father": [
      "Asahiko, Putera Kuni"
   ],
   "Mother": [
      "Terao Utako"
   ],
   "Honorific Prefix": [
      "Jeneral"
   ],
   "Party": [
      "Bebas"
   ],
   "Birth(birth date)": [
      "1887, 12, 3"
   ],
   "Birth(birth place)": [
      "Kyoto, Empayar Jepun"
   ],
   "Death(death date)": [
      "1990, 1, 20, 1887, 12, 3"
   ],
   "Death(death place)": [
      "Tokyo, Jepun"
   ],
   "Office(reign)": [
      "17 Ogos 1945 – 9 Oktober 1945"
   ],
   "Office(successor)": [
      "Kijūrō Shidehara"
   ],
   "Office(predecessor)": [
      "Kantarō Suzuki"
   ],
   "Office(succession)": [
      "Perdana Menteri Jepun ke-43"
   ],
   "Office(regent)": [
      "Hirohito"
   ],
   "Office(office)": [
      "Divisyen Tentera Darat Jepun ke-4, Perkhidmatan Udara Tentera Darat Imperial Jepun, Tentera Darat Jepun ke-2, General Defense Command"
   ],
   "Awards(awards)": [
      "Order of the Chrysanthemum",
      "Order of the Rising Sun berbunga Paulownia, Order of the Golden Kite"
   ],
   "Allegiance": [
      "Empayar Jepun"
   ],
   "Service Years": [
      "1908–1945"
   ],
   "Rank": [
      "Jeneral"
   ],
   "Branch": [
      "Tentera Darat Imperial Jepun"
   ],
   "Battles": [
      "Perang China-Jepun Kedua",
      "Perang Pasifik"
   ]
} 
```
- char match
```json
{
   "title": "Putera Naruhiko Higashikuni",
   "sentences": {
      "Name": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990ialah seorang putera Empayar Jepun yang berkhidmat sebagai seorang pegawai dalam Tentera Darat Imperial Jepun dan ke-43 Perdana Menteri Jepun dari 17 Ogos 1945 sehinggalah 9 oktober pada tahun yang sama dengan tempoh selama 54 hari.Ayahanda ipar Maharaja Hirohitoini merupakan Higashikuni adalah satu-satunya ahli kerabat diraja Jepun yang pernah mengetuai kabinet serta jeneral pegawai Tentera Darat Jepun terkabir yang memegang jawatan Perdana Menteri.",
            "alia": "東久邇宮稔彦王",
            "value": "Putera Naruhiko Higashikuni",
            "field": "Name",
            "alia_score": 0.8333333333333334,
            "value_score": 0.92,
            "sentence_score": 0.9928698752228164,
            "match_alia": "東久邇宮稔",
            "match_value": "Putera Naruhiko Higashi"
         }
      ],
      "Occupation": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990ialah seorang putera Empayar Jepun yang berkhidmat sebagai seorang pegawai dalam Tentera Darat Imperial Jepun dan ke-43 Perdana Menteri Jepun dari 17 Ogos 1945 sehinggalah 9 oktober pada tahun yang sama dengan tempoh selama 54 hari.",
            "alia": "Putera Naruhiko Higashikuni",
            "value": "General",
            "field": "Occupation",
            "alia_score": 0.92,
            "value_score": 0.8333333333333334,
            "sentence_score": 0.9985401459854014,
            "match_alia": "Putera Naruhiko Higashi",
            "match_value": "enera"
         }
      ],
      "Spouse": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990ialah seorang putera Empayar Jepun yang berkhidmat sebagai seorang pegawai dalam Tentera Darat Imperial Jepun dan ke-43 Perdana Menteri Jepun dari 17 Ogos 1945 sehinggalah 9 oktober pada tahun yang sama dengan tempoh selama 54 hari.Ayahanda ipar Maharaja Hirohitoini merupakan Higashikuni adalah satu-satunya ahli kerabat diraja Jepun yang pernah mengetuai kabinet serta jeneral pegawai Tentera Darat Jepun terkabir yang memegang jawatan Perdana Menteri.",
            "alia": "東久邇宮稔彦王",
            "value": "Toshiko Higashikuni",
            "field": "Spouse",
            "alia_score": 0.8333333333333334,
            "value_score": 0.9142857142857143,
            "sentence_score": 0.9828982898289829,
            "match_alia": "東久邇宮稔",
            "match_value": "hiko Higashikuni"
         }
      ],
      "Honorific Prefix": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990",
            "alia": "Putera Naruhiko Higashikuni",
            "value": "Jeneral",
            "field": "Honorific Prefix",
            "alia_score": 0.92,
            "value_score": 0.8333333333333334,
            "sentence_score": 1.0,
            "match_alia": "Putera Naruhiko Higashi",
            "match_value": "Jener"
         }
      ],
      "Rank": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990",
            "alia": "Putera Naruhiko Higashikuni",
            "value": "Jeneral",
            "field": "Rank",
            "alia_score": 0.92,
            "value_score": 0.8333333333333334,
            "sentence_score": 1.0,
            "match_alia": "Putera Naruhiko Higashi",
            "match_value": "Jener"
         }
      ]
   }
} 
```
- part word match
```json
{
   "title": "Putera Naruhiko Higashikuni",
   "sentences": {
      "Name": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990ialah seorang putera Empayar Jepun yang berkhidmat sebagai seorang pegawai dalam Tentera Darat Imperial Jepun dan ke-43 Perdana Menteri Jepun dari 17 Ogos 1945 sehinggalah 9 oktober pada tahun yang sama dengan tempoh selama 54 hari.Ayahanda ipar Maharaja Hirohitoini merupakan Higashikuni adalah satu-satunya ahli kerabat diraja Jepun yang pernah mengetuai kabinet serta jeneral pegawai Tentera Darat Jepun terkabir yang memegang jawatan Perdana Menteri.",
            "alia": "東久邇宮稔彦王",
            "value": "Putera Naruhiko Higashikuni",
            "field": "Name",
            "alia_score": 0.8333333333333334,
            "value_score": 1.0,
            "sentence_score": 0.9928698752228164,
            "match_alia": "東久邇宮稔",
            "match_value": "Putera Naruhiko Higashikuni"
         }
      ],
      "Honorific Prefix": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990",
            "alia": "Putera Naruhiko Higashikuni",
            "value": "Jeneral",
            "field": "Honorific Prefix",
            "alia_score": 1.0,
            "value_score": 1.0,
            "sentence_score": 1.0,
            "match_alia": "Putera Naruhiko Higashikuni",
            "match_value": "Jeneral"
         }
      ],
      "Rank": [
         {
            "sentence": "Jeneral Putera Naruhiko Higashikuni, 東久邇宮稔彦王, Higashikuni-no-miya Naruhiko Ō, 3 Disember 1887 – 20 Januari 1990",
            "alia": "Putera Naruhiko Higashikuni",
            "value": "Jeneral",
            "field": "Rank",
            "alia_score": 1.0,
            "value_score": 1.0,
            "sentence_score": 1.0,
            "match_alia": "Putera Naruhiko Higashikuni",
            "match_value": "Jeneral"
         }
      ]
   }
} 
```
- all word match
```json
{
   "title": "Putera Naruhiko Higashikuni",
   "sentences": {}
} 
```
#### Corpus类属性和方法
- 属性
    - item：传入的数据
    - title：词条名
    - text：纯文本数据
    - sentences：句子
    - paragraphs：段落
    - alias：别名
    - fields：三元组，包含属性
    - entities：三元组，不包含属性
- 方法
    - set_item：设置实例数据
    - corpus：获取语料，其参数如下
        - top_k：获取阈值前k的句子
        - ignore_space：相似度匹配时是否忽略空格
        - choice：全词匹配时每个词的相似项的数目
        - rjson：返回JSON格式的数据
