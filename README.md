[![Current PyPI packages](https://badge.fury.io/py/suparunidic.svg)](https://pypi.org/project/suparunidic/)

# SuPar-UniDic

Tokenizer, POS-tagger, lemmatizer, and dependency-parser for modern and contemporary Japanese with BERT models.

## Basic usage

```py
>>> import suparunidic
>>> nlp=suparunidic.load()
>>> doc=nlp("太郎は花子が読んでいる本を次郎に渡した")
>>> print(type(doc))
<class 'spacy.tokens.doc.Doc'>
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
>>> for b in suparunidic.bunsetu_spans(doc):
...   for t in b.lefts:
...     print(suparunidic.bunsetu_span(t),"->",b,"("+deprelja[t.dep_]+")")
...
花子が -> 読んでいる (主語)
読んでいる -> 本を (連体修飾節)
太郎は -> 渡した (主語)
本を -> 渡した (目的語)
次郎に -> 渡した (斜格補語)
```

`suparunidic.load(UniDic,BERT)` loads a natural language processor pipeline, which uses `UniDic` for tokenizer POS-tagger and lemmatizer, then uses `BERT` for Biaffine dependency-parser of [SuPar](https://pypi.org/project/supar/). Available `UniDic` options are:

* `UniDic="gendai"`: Use [現代書き言葉UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_bccwj)
* `UniDic="spoken"`: Use [現代話し言葉UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_csj)
* `UniDic="novel"`: Use [近現代口語小説UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_novel).
* `UniDic="qkana"`: Use [旧仮名口語UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_qkana)
* `UniDic="kindai"`: Use [近代文語UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_kindai)
* `UniDic="kinsei"`: Use [近世江戸口語UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_kinsei-edo)
* `UniDic="kyogen"`: Use [中世口語UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_chusei-kougo)
* `UniDic="wakan"`: Use [中世文語UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_chusei-bungo)
* `UniDic="wabun"`: Use [中古和文UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_wabun)
* `UniDic="manyo"`: Use [上代語UniDic](https://clrd.ninjal.ac.jp/unidic/download_all.html#unidic_jodai)
* `UniDic=None` [unidic-lite](https://github.com/polm/unidic-lite) (default)

Available `BERT` options are:

* `BERT="bert-japanese-aozora6m3m-unidic32k-2m"` from [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) (default)
* `BERT="roberta-large-japanese-aozora"` from [roberta-large-japanese-aozora](https://huggingface.co/KoichiYasuoka/roberta-large-japanese-aozora)
* `BERT="roberta-large-japanese-aozora-char"` from [roberta-large-japanese-aozora-char](https://huggingface.co/KoichiYasuoka/roberta-large-japanese-aozora-char)
* `BERT="roberta-base-japanese-aozora"` from [roberta-base-japanese-aozora](https://huggingface.co/KoichiYasuoka/roberta-base-japanese-aozora)
* `BERT="roberta-base-japanese-aozora-char"` from [roberta-base-japanese-aozora-char](https://huggingface.co/KoichiYasuoka/roberta-base-japanese-aozora-char)
* `BERT="roberta-small-japanese-aozora"` from [roberta-small-japanese-aozora](https://huggingface.co/KoichiYasuoka/roberta-small-japanese-aozora)
* `BERT="roberta-small-japanese-aozora-char"` from [roberta-small-japanese-aozora-char](https://huggingface.co/KoichiYasuoka/roberta-small-japanese-aozora-char)
* `BERT="deberta-large-japanese-aozora"` from [deberta-large-japanese-aozora](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-aozora)
* `BERT="deberta-base-japanese-aozora"` from [deberta-base-japanese-aozora](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-aozora)
* `BERT="deberta-small-japanese-aozora"` from [deberta-small-japanese-aozora](https://huggingface.co/KoichiYasuoka/deberta-small-japanese-aozora)
* `BERT="deberta-base-japanese-unidic"` from [deberta-base-japanese-aozora](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-unidic) ([fugashi](https://pypi.org/project/fugashi/) required)
* `BERT="bert-base-japanese-char-extended"` from [bert-base-japanese-char-extended](https://huggingface.co/KoichiYasuoka/bert-base-japanese-char-extended)
* `BERT="bert-large-japanese-char-extended"` from [bert-large-japanese-char-extended](https://huggingface.co/KoichiYasuoka/bert-large-japanese-char-extended)
* `BERT="bert-base-japanese-char"` from [cl-tohoku](https://huggingface.co/cl-tohoku) ([fugashi](https://pypi.org/project/fugashi/) and [ipadic](https://pypi.org/project/ipadic/) required)
* `BERT="bert-base-japanese-whole-word-masking"` from [cl-tohoku](https://huggingface.co/cl-tohoku) ([fugashi](https://pypi.org/project/fugashi/) and [ipadic](https://pypi.org/project/ipadic/) required)
* `BERT="bert-large-japanese"` from [cl-tohoku](https://huggingface.co/cl-tohoku) ([fugashi](https://pypi.org/project/fugashi/) required)
* `BERT="bert-large-japanese-char"` from [cl-tohoku](https://huggingface.co/cl-tohoku) ([fugashi](https://pypi.org/project/fugashi/) required)
* `BERT="roberta-base-japanese"` from [nlp-waseda](https://huggingface.co/nlp-waseda) ([SentencePiece](https://pypi.org/project/sentencepiece/) required)
* `BERT="roberta-large-japanese"` from [nlp-waseda](https://huggingface.co/nlp-waseda) ([SentencePiece](https://pypi.org/project/sentencepiece/) required)
* `BERT="electra-base-japanese-discriminator"` from [izumi-lab](https://huggingface.co/izumi-lab) ([fugashi](https://pypi.org/project/fugashi/) and [ipadic](https://pypi.org/project/ipadic/) required)
* `BERT="bert-small-japanese"` from [izumi-lab](https://huggingface.co/izumi-lab) ([fugashi](https://pypi.org/project/fugashi/) and [ipadic](https://pypi.org/project/ipadic/) required)
* `BERT="electra-base-japanese-generator"` from [izumi-lab](https://huggingface.co/izumi-lab) ([fugashi](https://pypi.org/project/fugashi/) and [ipadic](https://pypi.org/project/ipadic/) required)
* `BERT="japanese-roberta-base"` from [rinna](https://huggingface.co/rinna) ([SentencePiece](https://pypi.org/project/sentencepiece/) required)
* `BERT="albert-japanese-v2"` from [alinear-corp](https://github.com/alinear-corp/albert-japanese) ([SentencePiece](https://pypi.org/project/sentencepiece/) required)
* `BERT="albert-base-japanese-v1"` from [ken11](https://huggingface.co/ken11)
* `BERT="electra-small-japanese-discriminator"` from [Cinnamon AI](https://huggingface.co/Cinnamon)
* `BERT="electra-small-japanese-generator"` from [Cinnamon AI](https://huggingface.co/Cinnamon)
* `BERT="ku-bert-japanese-large"` from [ku-bert-japanese](http://nlp.ist.i.kyoto-u.ac.jp/?ku_bert_japanese)
* `BERT="bert-base-ja-cased"` from [Geotrend](https://huggingface.co/Geotrend)
* `BERT="laboro-bert-japanese-large"` from [Laboro AI](https://github.com/laboroai/Laboro-BERT-Japanese)
* `BERT="nict-bert-base-japanese-100k"` from [NICT BERT](https://alaginrc.nict.go.jp/nict-bert/)
* `BERT="unihanlm-base"` from [microsoft/unihanlm-base](https://huggingface.co/microsoft/unihanlm-base)
* `BERT="distilbert-base-japanese"` from [bandainamco-mirai](https://huggingface.co/bandainamco-mirai)

## Installation for Linux

```sh
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

### BERT="bert-japanese-aozora6m3m-unidic32k-2m"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |84.91|74.07|77.78|
|UniDic="kindai"|74.77|69.09|69.09|
|UniDic="kinsei"|83.02|66.67|70.37|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|66.67|
|UniDic="kinsei"|78.95|67.92|64.15|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |74.35|56.00|56.00|
|UniDic="kindai"|74.35|53.33|53.33|
|UniDic="kinsei"|70.83|50.00|47.37|

### BERT="roberta-large-japanese-aozora"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |75.47|58.18|65.45|
|UniDic="kindai"|75.47|58.18|65.45|
|UniDic="kinsei"|66.67|52.63|56.14|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |87.50|82.35|78.43|
|UniDic="kindai"|83.19|78.43|74.51|
|UniDic="kinsei"|87.50|82.35|74.51|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |80.63|64.94|59.74|
|UniDic="kindai"|80.63|62.34|57.14|
|UniDic="kinsei"|78.12|59.74|54.55|

### BERT="roberta-large-japanese-aozora-char"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |79.25|69.09|76.36|
|UniDic="kindai"|79.25|69.09|76.36|
|UniDic="kinsei"|68.52|59.65|63.16|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|70.59|
|UniDic="kinsei"|85.71|78.43|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.44|61.33|61.33|
|UniDic="kindai"|76.44|61.33|61.33|
|UniDic="kinsei"|72.92|56.00|56.00|

### BERT="roberta-base-japanese-aozora"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |79.25|65.45|72.73|
|UniDic="kindai"|79.25|65.45|72.73|
|UniDic="kinsei"|68.52|60.71|64.29|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |87.50|82.35|78.43|
|UniDic="kindai"|83.19|78.43|74.51|
|UniDic="kinsei"|87.50|82.35|74.51|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.44|58.67|61.33|
|UniDic="kindai"|76.44|56.00|58.67|
|UniDic="kinsei"|73.96|53.33|56.00|

### BERT="roberta-base-japanese-aozora-char"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |83.02|70.37|77.78|
|UniDic="kindai"|83.02|70.37|77.78|
|UniDic="kinsei"|74.07|65.45|69.09|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|70.59|
|UniDic="kinsei"|85.71|78.43|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.44|57.89|57.89|
|UniDic="kindai"|76.44|55.26|55.26|
|UniDic="kinsei"|73.96|52.63|52.63|

### BERT="roberta-small-japanese-aozora"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |83.02|72.73|76.36|
|UniDic="kindai"|83.02|72.73|76.36|
|UniDic="kinsei"|70.37|60.71|64.29|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|70.59|
|UniDic="kinsei"|85.71|78.43|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |74.35|56.00|56.00|
|UniDic="kindai"|74.35|53.33|53.33|
|UniDic="kinsei"|71.88|50.67|50.67|

### BERT="roberta-small-japanese-aozora-char"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.36|65.45|72.73|
|UniDic="kindai"|77.36|65.45|72.73|
|UniDic="kinsei"|70.37|59.65|63.16|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|70.59|
|UniDic="kinsei"|85.71|78.43|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.30|53.33|53.33|
|UniDic="kindai"|73.30|50.67|50.67|
|UniDic="kinsei"|70.83|48.00|48.00|

### BERT="deberta-large-japanese-aozora"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |84.91|74.07|77.78|
|UniDic="kindai"|76.64|72.73|69.09|
|UniDic="kinsei"|81.13|66.67|70.37|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|66.67|
|UniDic="kinsei"|78.95|67.92|64.15|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.49|61.33|61.33|
|UniDic="kindai"|77.49|58.67|58.67|
|UniDic="kinsei"|73.96|55.26|52.63|

### BERT="deberta-base-japanese-aozora"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |86.79|77.78|77.78|
|UniDic="kindai"|76.64|72.73|69.09|
|UniDic="kinsei"|81.13|65.45|65.45|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|83.19|78.43|70.59|
|UniDic="kinsei"|78.95|67.92|64.15|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |72.25|53.33|53.33|
|UniDic="kindai"|72.25|50.67|50.67|
|UniDic="kinsei"|69.79|50.00|47.37|

### BERT="deberta-small-japanese-aozora"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |75.47|60.71|64.29|
|UniDic="kindai"|67.29|59.65|56.14|
|UniDic="kinsei"|71.70|50.91|54.55|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |83.93|74.51|70.59|
|UniDic="kindai"|79.65|70.59|62.75|
|UniDic="kinsei"|77.19|64.15|60.38|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |75.39|56.00|56.00|
|UniDic="kindai"|75.39|56.00|56.00|
|UniDic="kinsei"|71.88|52.63|50.00|

### BERT="deberta-base-japanese-unidic"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |86.79|77.78|77.78|
|UniDic="kindai"|76.64|72.73|69.09|
|UniDic="kinsei"|79.25|60.71|60.71|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |83.93|76.00|72.00|
|UniDic="kindai"|79.65|72.00|64.00|
|UniDic="kinsei"|77.19|65.38|61.54|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.49|61.33|61.33|
|UniDic="kindai"|77.49|58.67|58.67|
|UniDic="kinsei"|73.96|55.26|52.63|

### BERT="bert-base-japanese-char-extended"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |81.13|72.73|76.36|
|UniDic="kindai"|81.13|72.73|76.36|
|UniDic="kinsei"|68.52|59.65|63.16|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|70.59|
|UniDic="kinsei"|85.71|78.43|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |75.39|56.00|56.00|
|UniDic="kindai"|75.39|53.33|53.33|
|UniDic="kinsei"|71.88|48.00|48.00|

### BERT="bert-large-japanese-char-extended"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |75.47|64.29|71.43|
|UniDic="kindai"|75.47|64.29|71.43|
|UniDic="kinsei"|64.81|55.17|62.07|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|70.59|
|UniDic="kinsei"|85.71|78.43|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |78.53|64.00|64.00|
|UniDic="kindai"|78.53|61.33|61.33|
|UniDic="kinsei"|76.04|58.67|58.67|

### BERT="bert-base-japanese-char"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.36|64.29|71.43|
|UniDic="kindai"|77.36|64.29|71.43|
|UniDic="kinsei"|66.67|55.17|58.62|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |78.57|72.00|68.00|
|UniDic="kindai"|74.34|68.00|64.00|
|UniDic="kinsei"|78.57|72.00|64.00|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |75.39|58.67|58.67|
|UniDic="kindai"|75.39|56.00|56.00|
|UniDic="kinsei"|72.92|53.33|53.33|

### BERT="bert-base-japanese-whole-word-masking"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.58|57.14|64.29|
|UniDic="kindai"|73.58|57.14|64.29|
|UniDic="kinsei"|64.81|51.72|55.17|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|82.35|78.43|
|UniDic="kindai"|76.11|73.08|69.23|
|UniDic="kinsei"|85.71|82.35|74.51|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.30|52.63|52.63|
|UniDic="kindai"|73.30|52.63|52.63|
|UniDic="kinsei"|69.79|50.00|50.00|

### BERT="bert-large-japanese"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |79.25|65.45|72.73|
|UniDic="kindai"|79.25|65.45|72.73|
|UniDic="kinsei"|68.52|56.14|59.65|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |78.57|76.92|73.08|
|UniDic="kindai"|74.34|73.08|69.23|
|UniDic="kinsei"|78.57|76.92|69.23|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |78.53|59.74|57.14|
|UniDic="kindai"|78.53|57.14|54.55|
|UniDic="kinsei"|77.08|54.55|51.95|

### BERT="bert-large-japanese-char"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |79.25|69.09|72.73|
|UniDic="kindai"|79.25|69.09|72.73|
|UniDic="kinsei"|68.52|59.65|63.16|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |80.36|70.59|70.59|
|UniDic="kindai"|76.11|66.67|66.67|
|UniDic="kinsei"|80.36|70.59|66.67|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |74.35|53.33|53.33|
|UniDic="kindai"|74.35|50.67|50.67|
|UniDic="kinsei"|71.88|48.00|48.00|

### BERT="roberta-base-japanese"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |83.02|72.73|76.36|
|UniDic="kindai"|83.02|72.73|76.36|
|UniDic="kinsei"|72.22|63.16|66.67|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|83.19|78.43|74.51|
|UniDic="kinsei"|85.71|78.43|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |72.25|51.35|51.35|
|UniDic="kindai"|72.25|51.35|51.35|
|UniDic="kinsei"|69.79|48.65|48.65|

### BERT="roberta-large-japanese"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |79.25|65.45|69.09|
|UniDic="kindai"|69.16|60.71|57.14|
|UniDic="kinsei"|73.58|50.00|53.57|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|74.51|
|UniDic="kindai"|81.42|74.51|66.67|
|UniDic="kinsei"|78.95|67.92|64.15|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |72.25|57.89|57.89|
|UniDic="kindai"|72.25|55.26|55.26|
|UniDic="kinsei"|68.75|51.95|49.35|

### BERT="electra-base-japanese-discriminator"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |75.47|61.82|69.09|
|UniDic="kindai"|75.47|61.82|69.09|
|UniDic="kinsei"|64.81|52.63|56.14|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |87.50|82.35|78.43|
|UniDic="kindai"|83.19|78.43|74.51|
|UniDic="kinsei"|87.50|82.35|74.51|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.30|50.67|50.67|
|UniDic="kindai"|73.30|50.67|50.67|
|UniDic="kinsei"|70.83|48.00|48.00|

### BERT="bert-small-japanese"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |79.25|62.96|70.37|
|UniDic="kindai"|79.25|62.96|70.37|
|UniDic="kinsei"|70.37|57.14|60.71|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.79|73.08|69.23|
|UniDic="kindai"|72.57|69.23|65.38|
|UniDic="kinsei"|76.79|73.08|65.38|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |72.25|47.37|47.37|
|UniDic="kindai"|72.25|47.37|47.37|
|UniDic="kinsei"|69.79|42.67|45.33|

### BERT="electra-base-japanese-generator"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.36|64.29|71.43|
|UniDic="kindai"|77.36|64.29|71.43|
|UniDic="kinsei"|68.52|58.62|62.07|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.79|73.08|69.23|
|UniDic="kindai"|72.57|69.23|65.38|
|UniDic="kinsei"|76.79|73.08|65.38|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |69.11|45.33|45.33|
|UniDic="kindai"|69.11|45.33|45.33|
|UniDic="kinsei"|66.67|42.67|42.67|

### BERT="japanese-roberta-base"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.58|57.14|64.29|
|UniDic="kindai"|73.58|57.14|64.29|
|UniDic="kinsei"|64.81|51.72|55.17|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |87.50|82.35|78.43|
|UniDic="kindai"|83.19|78.43|74.51|
|UniDic="kinsei"|87.50|82.35|74.51|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |74.35|50.00|47.37|
|UniDic="kindai"|74.35|47.37|44.74|
|UniDic="kinsei"|71.88|44.74|42.11|

### BERT="albert-japanese-v2"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.36|64.29|71.43|
|UniDic="kindai"|77.36|64.29|71.43|
|UniDic="kinsei"|66.67|55.17|58.62|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.79|73.08|69.23|
|UniDic="kindai"|72.57|69.23|65.38|
|UniDic="kinsei"|76.79|73.08|65.38|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.30|51.95|49.35|
|UniDic="kindai"|73.30|49.35|46.75|
|UniDic="kinsei"|69.79|46.75|44.16|

### BERT="albert-base-japanese-v1"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.58|57.14|64.29|
|UniDic="kindai"|73.58|57.14|64.29|
|UniDic="kinsei"|64.81|51.72|55.17|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |76.79|73.08|69.23|
|UniDic="kindai"|74.34|69.23|65.38|
|UniDic="kinsei"|76.79|73.08|65.38|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |65.97|42.67|42.67|
|UniDic="kindai"|65.97|40.00|40.00|
|UniDic="kinsei"|64.58|39.47|39.47|

### BERT="electra-small-japanese-discriminator"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.58|57.14|64.29|
|UniDic="kindai"|73.58|57.14|64.29|
|UniDic="kinsei"|62.96|48.28|51.72|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.21|69.23|65.38|
|UniDic="kindai"|70.80|65.38|61.54|
|UniDic="kinsei"|73.21|69.23|61.54|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |74.35|50.00|47.37|
|UniDic="kindai"|74.35|50.00|47.37|
|UniDic="kinsei"|72.92|50.00|47.37|

### BERT="electra-small-japanese-generator"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.58|60.71|64.29|
|UniDic="kindai"|73.58|60.71|64.29|
|UniDic="kinsei"|66.67|55.17|58.62|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.21|69.23|65.38|
|UniDic="kindai"|70.80|65.38|61.54|
|UniDic="kinsei"|73.21|69.23|61.54|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |69.11|45.95|45.95|
|UniDic="kindai"|69.11|43.24|43.24|
|UniDic="kinsei"|66.67|40.54|40.54|

### BERT="ku-bert-japanese-large"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.36|65.45|72.73|
|UniDic="kindai"|77.36|65.45|72.73|
|UniDic="kinsei"|64.81|52.63|59.65|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |82.14|74.51|70.59|
|UniDic="kindai"|81.42|74.51|70.59|
|UniDic="kinsei"|82.14|74.51|66.67|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |62.83|39.47|42.11|
|UniDic="kindai"|62.83|36.84|39.47|
|UniDic="kinsei"|62.50|38.96|41.56|

### BERT="bert-base-ja-cased"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.58|58.18|65.45|
|UniDic="kindai"|73.58|58.18|65.45|
|UniDic="kinsei"|64.81|52.63|56.14|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.21|69.23|65.38|
|UniDic="kindai"|70.80|65.38|61.54|
|UniDic="kinsei"|73.21|69.23|61.54|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |63.87|41.56|44.16|
|UniDic="kindai"|63.87|38.96|41.56|
|UniDic="kinsei"|61.46|36.36|38.96|

### BERT="laboro-bert-japanese-large"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |71.70|56.14|63.16|
|UniDic="kindai"|71.70|56.14|63.16|
|UniDic="kinsei"|62.96|50.85|54.24|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |71.43|65.38|65.38|
|UniDic="kindai"|67.26|61.54|61.54|
|UniDic="kinsei"|71.43|65.38|61.54|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |67.02|42.67|42.67|
|UniDic="kindai"|67.02|40.00|40.00|
|UniDic="kinsei"|65.62|37.33|37.33|

### BERT="nict-bert-base-japanese-100k"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |67.92|49.12|52.63|
|UniDic="kindai"|67.92|49.12|52.63|
|UniDic="kinsei"|57.41|40.68|44.07|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |82.14|74.51|74.51|
|UniDic="kindai"|81.42|74.51|74.51|
|UniDic="kinsei"|82.14|74.51|70.59|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |68.06|41.10|43.84|
|UniDic="kindai"|68.06|38.36|41.10|
|UniDic="kinsei"|65.62|35.62|38.36|

### BERT="unihanlm-base"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |69.81|52.63|59.65|
|UniDic="kindai"|69.81|52.63|59.65|
|UniDic="kinsei"|61.11|47.46|50.85|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |85.71|78.43|78.43|
|UniDic="kindai"|79.65|70.59|70.59|
|UniDic="kinsei"|85.71|78.43|74.51|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |61.78|36.36|38.96|
|UniDic="kindai"|61.78|36.36|38.96|
|UniDic="kinsei"|60.42|36.36|38.96|

### BERT="distilbert-base-japanese"

|[舞姬](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/maihime-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |77.36|64.29|71.43|
|UniDic="kindai"|77.36|64.29|71.43|
|UniDic="kinsei"|68.52|58.62|62.07|

|[雪國](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/yukiguni-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |73.21|69.23|65.38|
|UniDic="kindai"|70.80|65.38|61.54|
|UniDic="kinsei"|73.21|69.23|61.54|

|[荒野より](https://github.com/KoichiYasuoka/UniDic2UD/blob/master/benchmark/koyayori-benchmark.tar.gz)|LAS|MLAS|BLEX|
|---------------|-----|-----|-----|
|UniDic="qkana" |63.87|34.67|40.00|
|UniDic="kindai"|63.87|32.00|37.33|
|UniDic="kinsei"|62.50|34.21|36.84|

## Author

Koichi Yasuoka (安岡孝一)

