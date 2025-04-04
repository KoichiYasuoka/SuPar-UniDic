#! /bin/sh
if [ $# -eq 0 ]
then set `echo *-*`
fi
for M
do if [ -s $M.supar ]
   then continue
   elif [ -s $M.supar.10 ]
   then cat $M.supar.[1-9] $M.supar.[1-9][0-9] > $M.supar
   elif [ -s $M.supar.1 ]
   then cat $M.supar.[1-9] > $M.supar
   elif [ -s ja_gsd_modern.conllu ]
   then nawk '
BEGIN{
  f[0]="test.conllu";
  f[1]="dev.conllu";
  for(i=2;i<10;i++)
    f[i]="train.conllu";
}
{
  printf("%s\n",$0)>f[i%10];
  if($0=="")
    i++;
}' ja_gsd_modern.conllu
        case $M in
        *-char-extended|roberta-*-aozora*|deberta-*) B=KoichiYasuoka/$M ;;
        bert-base-japanese-*|bert-large-japanese*) B=cl-tohoku/$M ;;
        distilbert-base-japanese) B=bandainamco-mirai/$M ;;
        electra-small-japanese-*) B=Cinnamon/$M ;;
        albert-japanese-v2) B=ALINEAR/$M ;;
	japanese-roberta-base) B=rinna/$M ;;
	bert-base-ja-cased) B=Geotrend/$M ;;
	bert-small-japanese|electra-base-japanese-*) B=izumi-lab/$M ;;
	albert-base-japanese-v1) B=ken11/$M ;;
	roberta-base-japanese|roberta-large-japanese) B=nlp-waseda/$M ;;
        *) B=$M ;;
        esac
        python3 -m supar.cmds.biaffine_dep train -b -d 0 -p $M/$M.supar -c biaffine-dep-en -f bert --bert $B --train train.conllu --dev dev.conllu --test test.conllu --embed=''
   fi
done
exit 0
