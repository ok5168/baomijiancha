'''
2020-2-13 OK!
'''

import re
import os, sys,time
import random
# import easygui as g

biaoti="保密检查文件批量修改程序 2019-11-19 v1.4"
TiShi='''
保密检查文件批量修改程序 2019-11-19 v1.4
软件开发者：ssdhx
把之前需要修改的文件统一放到一个目录里
'''

# print(TiShi)

# # 终端交互模式
# path=input("输入要替换的目录:")  #要替换的目录  手工改
# mytime0=input("输入要替换成的日期(如：2018-06-27) ")  #要替换成的日期   手工改


# print(mytime0)

def chuli(mytime0,path):
    '''
    mytime0
    path
    '''
    mytime1=mytime0.replace("-","年",1)
    mytime1=mytime1.replace("-","月",1)
    mytime2=mytime1+"日"

    #把目录中所有/换成\;如果不以/结尾的，再结尾加上/
    path=path.replace("\\","/")
    if path.endswith('/')==False:
        path=path+"/"
    # print(path)


    pattern_1 = '[1-9]\\d*-[0-9]\\d*-[0-9]\\d*'
    pattern_2 = '[1-9]\\d*年[0-9]\\d*月[0-9]\\d*日'
    pattern_3 = '\\d{2}:\\d{2}:\\d{2}'  #后面会随机替换小、分、秒

    html_1='<a href="file://'
    html_2='" target="_blank" >'
    html_3='</a><br>'
    jieguo=""

    dirs = os.listdir( path )
    # 输出所有文件和文件夹
    for file in dirs:

        #改文件内容：
        file=path+file
        
        

        random.seed()
        xiaoshi=str(random.randint(8,11)).zfill(2) #生成小时
        fenzhon=str(random.randint(1,59)).zfill(2) #生成分钟
        miao=str(random.randint(1,59)).zfill(2) #生成秒
        tihuanwei_3=xiaoshi +':'+fenzhon+':'+miao  #要替换成的日间 
        
        
        fo=open(file,"r+")
        line=fo.read()
        num = re.sub(pattern_1, mytime0, line)
        num = re.sub(pattern_2, mytime2, num)
        num = re.sub(pattern_3, tihuanwei_3, num)
        fo=open(file,"w+")
        fo.write(num)
        fo.close()
        
        #改文件名：
        weijianminshijian = '\d{2}时\d{2}分\d{2}'
        weijianminshijian2=xiaoshi+'时'+fenzhon+'分'+miao
        newfile=re.sub(pattern_2,mytime2,file)
        newfile=re.sub(weijianminshijian,weijianminshijian2,newfile)
        os.rename(file,newfile)
        print(newfile)

        # myWin.plainTextEdit.appendPlainText(newfile)
        # time.sleep(0.5)
        
        # tem=html_1+newfile+html_2+html_3
        jieguo=jieguo+newfile+"\n"


        # 修改文件的  修改时间
        timestring = mytime0+' '+tihuanwei_3     #修改成如：'2016-12-21 10:22:56'
        mtime=time.mktime(time.strptime(timestring, '%Y-%m-%d %H:%M:%S')) #得到时间戳
        os.utime(newfile,(mtime, mtime))
    # print(jieguo)
    return(jieguo)

# input('''
# 完成任务！
# 请按任意键结束！
# ''')