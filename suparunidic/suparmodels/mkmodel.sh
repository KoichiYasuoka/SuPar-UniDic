#! /bin/sh
# pip3 install torch==1.7.1+cu101 torchvision==0.8.2+cu101 -f https://download.pytorch.org/whl/torch_stable.html
# pip3 install supar==1.1.0
if [ $# -eq 0 ]
then set `echo *-*`
fi
for M
do if [ -s $M.supar ]
   then continue
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
        bert-base-japanese-*) B=cl-tohoku/$M ;;
        bert-large-japanese*) B=cl-tohoku/$M ;;
        distilbert-base-japanese) B=bandainamco-mirai/$M ;;
        electra-small-japanese-*) B=Cinnamon/$M ;;
        albert-japanese-v2) B=ALINEAR/$M ;;
        *) B=$M ;;
        esac
        python3 -m supar.cmds.biaffine_dep train -b -d 0 -p $M/$M.supar -c biaffine-dep-en -f bert --bert $B --train train.conllu --dev dev.conllu --test test.conllu --embed=''
   fi
done
exit 0
