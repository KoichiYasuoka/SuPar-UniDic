import os,setuptools
with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/SuPar-UniDic"

setuptools.setup(
  name="suparunidic",
  version="1.4.3",
  description="Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese with BERT models",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="NLP Japanese spaCy",
  packages=setuptools.find_packages(),
  install_requires=[
    "unidic2ud>=3.0.6",
    "spacy>=2.2.2",
    "supar>=1.1.4",
    "torch<2.6",
    "transformers<4.45",
    "unidic-lite>=1.0.8"
  ],
  python_requires=">=3.7",
  package_data={"suparunidic":["suparmodels/*/*.txt","suparmodels/*/*.json"]},
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
    "Topic :: Text Processing :: Linguistic",
    "Natural Language :: Japanese"
  ],
  project_urls={
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
