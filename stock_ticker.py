import urllib
import re
import datetime
import sys

symbols_list = ["singer","aptech","arssinfra","bhel","careerp","centralbk","centurytex","chettice","coalindia","crewbos","denabank",
                "dhanbank","edelweiss","escorts","gtl","hclinfo","hindoilexp","ivrclltd","jmfinan","jyotist","kernex",
                "ksoil","litl","lloydele","mangchem","onmobile","patelen","pnb","prajind","ramcoind","recltd","renuka",
                "shasunpha","shilpamedca","sintex","sksmicro","strtech","tataglobal","timken","uco","uflex",
                "unitech","unitedbnk","vipind","zylog"]
i=0
while i<len(symbols_list):

        url = "http://in.finance.yahoo.com/q?s="+symbols_list[i]+"&ql=1"
        htmlfile = urllib.urlopen(url)
        htmltext = htmlfile.read()
        regex3 = '<div class="title"><h2>(.+?)</h2>'
        pattern3 = re.compile(regex3)
        company_name = re.findall(pattern3,htmltext)

        regex = '<span id="yfs_l84_'+symbols_list[i]+"."+"bo"+'">(.+?)</span>'
        pattern = re.compile(regex)
        price = re.findall(pattern,htmltext)

        regex1 = '<span id="yfs_g53_'+symbols_list[i]+".bo"+'">(.+?)</span>'
        pattern1 = re.compile(regex1)
        day_low = re.findall(pattern1,htmltext)

        regex1 = '<span id="yfs_h53_'+symbols_list[i]+".bo"+'">(.+?)</span>'
        pattern2 = re.compile(regex1)
        day_high = re.findall(pattern2,htmltext)
        #print  "Company:",company_name,"price is:",price,"day's low :",day_low,"day's high:",day_high,"\n"
        local_time = datetime.datetime.now().strftime('%b-%d-%G')
        sys.stdout = open(r'/home/amit/pivot-table-'+str(local_time)+'.txt','a')



        pp = (float(price[0])+float(day_high[0])+float(day_low[0]))/3
        r1 = (2 * float(pp)) - float(day_low[0])
        r2 = float(pp) + (float(day_high[0])-float(day_low[0]))
        r3 = float(day_high[0]) + 2 * (float(pp) - float(day_low[0]))
        s1 = (2 * float(pp)) - float(day_high[0])
        s2 = float(pp) - (float(day_high[0])-float(day_low[0]))
        s3 = float(day_low[0]) - 2 * (float(pp) - float(day_low[0]))
        print "Company name:",company_name,"\n"
        print "\t Resistance 3:",r3,"\n"
        print "\t Resistance 2:",r2,"\n"
        print "\t Resistance 1:",r1,"\n"
        print "\t Pivot Point :",pp,"\n"
        print "\t Support 1   :",s1,"\n"
        print "\t Support 2   :",s2,"\n"
        print "\t Support 3   :",s3,"\n"

        i+=1

