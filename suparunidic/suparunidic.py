#! /usr/bin/python3 -i
# coding=utf-8

import os
PACKAGE_DIR=os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_DIR=os.path.join(PACKAGE_DIR,"suparmodels")
MODEL_URL="https://raw.githubusercontent.com/KoichiYasuoka/SuPar-UniDic/main/suparunidic/suparmodels/"

class SuParAPI(object):
  def __init__(self,model):
    from supar import Parser
    d=os.path.join(DOWNLOAD_DIR,model)
    with open(os.path.join(d,"filesize.txt"),"r") as f:
      r=f.read()
    for t in r.split("\n"):
      s=t.split()
      if len(s)==2:
        f=os.path.join(d,s[0])
        try:
          z=os.path.getsize(f)
        except:
          z=-1
        if z!=int(s[1]):
          from suparunidic.download import download
          download(MODEL_URL+model+"/",s[0],d)
    t=os.getcwd()
    os.chdir(DOWNLOAD_DIR)
    self.supar=Parser.load(os.path.join(model,model+".supar"))
    os.chdir(t)
  def __call__(self,conllu):
    c=conllu.split("\n")
    u=[]
    e=""
    p="PUNCT"
    for s in c:
      if s.startswith("#"):
        continue
      if s=="":
        if e!="":
          if p not in ["PUNCT","SYM"]:
            e+="。"
          u.append(e.strip().split())
          e=""
          p="PUNCT"
      else:
        t=s.split("\t")
        e+=t[1]+" "
        p=t[3]
    d=self.supar.predict(u,lang=None)
    i=j=0
    for k,s in enumerate(c):
      if s.startswith("#"):
        continue
      if s=="":
        i+=1
        j=0
      else:
        t=s.split("\t")
        head=str(d.sentences[i].values[6][j])
        deprel=d.sentences[i].values[7][j]
        if deprel=="root":
          if head!="0":
            deprel="advcl" if int(head)>int(t[0]) else "parataxis"
        elif deprel=="advmod":
          t[3]="ADV"
        elif deprel=="amod":
          t[3]="ADJ"
        elif deprel=="aux" or deprel=="cop":
          t[3]="AUX"
        elif deprel=="det":
          t[3]="DET"
        elif deprel=="nummod":
          t[3]="NUM"
        if t[3]=="AUX" and deprel not in ["aux","cop"]:
          if t[4].startswith("動詞"):
            t[3]="VERB"
          elif t[4].startswith("形"):
            t[3]="ADJ"
          elif t[4].startswith("名詞"):
            t[3]="NOUN"
        if head=="0" or head==t[0]:
          head="0"
          deprel="root"
        t[6]=head
        t[7]=deprel
        c[k]="\t".join(t)
        j+=1
    return "\n".join(c)

def load(UniDic=None,BERT=None):
  import unidic2ud.spacy
  if UniDic==None:
    UniDic="unidic-lite"
  nlp=unidic2ud.spacy.load(UniDic,None)
  if BERT==None:
    BERT="bert-japanese-aozora6m3m-unidic32k-2m"
  nlp.tokenizer.model.udpipe=SuParAPI(BERT)
  nlp.tokenizer.model.model=BERT
  return nlp

