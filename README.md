[![Current PyPI packages](https://badge.fury.io/py/suparunidic.svg)](https://pypi.org/project/suparunidic/)

# SuPar-UniDic

Tokenizer, POS-tagger, lemmatizer, and dependency-parser for modern and contemporary Japanese with BERT models.

## Basic usage

```py
>>> import suparunidic
>>> nlp=suparunidic.load()
>>> doc=qkana("太郎は花子が読んでいる本を次郎に渡した")
>>> print(suparunidic.to_conllu(doc))
1	太郎	タロウ	PROPN	名詞-固有名詞-人名-名	_	12	nsubj	_	SpaceAfter=No|Translit=タロー
2	は	は	ADP	助詞-係助詞	_	1	case	_	SpaceAfter=No|Translit=ワ
3	花子	ハナコ	PROPN	名詞-固有名詞-人名-名	_	5	nsubj	_	SpaceAfter=No|Translit=ハナコ
4	が	が	ADP	助詞-格助詞	_	3	case	_	SpaceAfter=No|Translit=ガ
5	読ん	読む	VERB	動詞-一般	_	8	acl	_	SpaceAfter=No|Translit=ヨン
6	で	て	SCONJ	助詞-接続助詞	_	5	mark	_	SpaceAfter=No|Translit=デ
7	いる	居る	AUX	動詞-非自立可能	_	5	aux	_	SpaceAfter=No|Translit=イル
8	本	本	NOUN	名詞-普通名詞-一般	_	12	obj	_	SpaceAfter=No|Translit=ホン
9	を	を	ADP	助詞-格助詞	_	8	case	_	SpaceAfter=No|Translit=オ
10	次郎	ジロウ	PROPN	名詞-固有名詞-人名-名	_	12	obl	_	SpaceAfter=No|Translit=ジロー
11	に	に	ADP	助詞-格助詞	_	10	case	_	SpaceAfter=No|Translit=ニ
12	渡し	渡す	VERB	動詞-一般	_	0	root	_	SpaceAfter=No|Translit=ワタシ
13	た	た	AUX	助動詞	_	12	aux	_	SpaceAfter=No|Translit=タ

>>> import deplacy
>>> deplacy.render(doc,Japanese=True)
太郎 PROPN ═╗<════════╗ nsubj(主語)
は   ADP   <╝         ║ case(格表示)
花子 PROPN ═╗<══╗     ║ nsubj(主語)
が   ADP   <╝   ║     ║ case(格表示)
読ん VERB  ═╗═╗═╝<╗   ║ acl(連体修飾節)
で   SCONJ <╝ ║   ║   ║ mark(標識)
いる AUX   <══╝   ║   ║ aux(動詞補助成分)
本   NOUN  ═╗═════╝<╗ ║ obj(目的語)
を   ADP   <╝       ║ ║ case(格表示)
次郎 PROPN ═╗<╗     ║ ║ obl(斜格補語)
に   ADP   <╝ ║     ║ ║ case(格表示)
渡し VERB  ═╗═╝═════╝═╝ ROOT(親)
た   AUX   <╝           aux(動詞補助成分)

>>> from deplacy.deprelja import deprelja
>>> for b in spacy_syncha.bunsetu_spans(doc):
...   for t in b.lefts:
...     print(spacy_syncha.bunsetu_span(t),"->",b,"("+deprelja[t.dep_]+")")
...
花子が -> 読んでいる (主語)
読んでいる -> 本を (連体修飾節)
太郎は -> 渡した (主語)
本を -> 渡した (目的語)
次郎に -> 渡した (斜格補語)
```

`suparunidic.load(UniDic,BERT)` loads a natural language processor pipeline, which uses `UniDic` for tokenizer POS-tagger and lemmatizer, then uses `BERT` for Biaffine dependency-parser of [SuPar](https://pypi.org/project/supar/). Available `UniDic` options are:

* `UniDic="gendai"` [現代書き言葉UniDic](https://unidic.ninjal.ac.jp/download#unidic_bccwj)
* `UniDic="spoken"` [現代話し言葉UniDic](https://unidic.ninjal.ac.jp/download#unidic_csj)
* `UniDic="qkana"` [旧仮名口語UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_qkana)
* `UniDic="kindai"` [近代文語UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_kindai)
* `UniDic="kinsei"` [近世口語（洒落本）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_kinsei)
* `UniDic="kyogen"` [中世口語（狂言）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_kyogen)
* `UniDic="wakan"` [中世文語（説話・随筆）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_wakan)
* `UniDic="wabun"` [中古和文UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_wabun)
* `UniDic="manyo"` [上代（万葉集）UniDic](https://unidic.ninjal.ac.jp/download_all#unidic_manyo)
* `UniDic=None` [unidic-lite](https://github.com/polm/unidic-lite) (default)

Available `BERT` options are:

* `BERT="bert-japanese-aozora6m3m-unidic32k-2m"` from [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) (default)
* `BERT="nict-bert-base-japanese-100k"` from [NICT BERT 日本語 Pre-trained モデル](https://alaginrc.nict.go.jp/nict-bert/)
* `BERT="unihanlm-base"` from [microsoft/unihanlm-base](https://huggingface.co/microsoft/unihanlm-base)

## Installation for Linux

```sh
pip3 install git+https://github.com/yzhangcs/parser --user
pip3 install suparunidic --user
```

## Installation for Cygwin64

Make sure to get `python37-devel` `python37-pip` `python37-cython` `python37-numpy` `python37-wheel` `gcc-g++` `mingw64-x86_64-gcc-g++` `git` `curl` `make` `cmake`, and then:

```sh
curl -L https://raw.githubusercontent.com/KoichiYasuoka/CygTorch/master/installer/supar.sh | sh
pip3.7 install suparunidic
```

## Benchmarks

Results of [舞姬/雪國/荒野より-Benchmarks](https://colab.research.google.com/github/KoichiYasuoka/SuPar-UniDic/blob/main/benchmark.ipynb)

### bert-japanese-aozora6m3m-unidic32k-2m

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="kindai"|75.47|64.29|71.43|
|UniDic="qkana" |75.47|64.29|71.43|
|UniDic="kinsei"|66.67|55.17|58.62|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kinsei"|85.71|78.43|70.59|
|UniDic="kindai"|81.92|74.51|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.44|58.67|58.67|
|UniDic="kindai"|76.44|56.00|56.00|
|UniDic="kinsei"|72.92|53.33|53.33|

## Author

Koichi Yasuoka (安岡孝一)

