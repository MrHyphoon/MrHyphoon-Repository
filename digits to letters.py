# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 19:50:43 2020

@author: hyphoon

这个代码实现一个功能。输入一串摁键符号，输出这串摁键符号能够组成
的所有可能的字符串，类似于用手机键盘打字。
"""
#引用一个叫itertools的包，这个包有个函数的作用是求笛卡尔积
import itertools

#定义一个字典mapping，指明每个摁键里面有哪些字符
mapping={"0":[''],"1":[''],"2":['a','b','c'],"3":['d','e','f'],\
        "4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],\
        "7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z'],\
        "*":['*'],"#":['#']}

#输入几个摁键
a=str(input("please input digits:  "))

#创建一个函数output，这个函数的作用是求一串摁键对应的所有可能的字符串
def output(a):
    l=[]
    for j in range(len(a)-1):
        if j==0:
            x=mapping[a[j]]
        else:
            x=l
            l=[]
        y=mapping[a[j+1]]
        for i in itertools.product(x,y):
            l.append(i[0]+i[1])
    return(l)

#打印出对应的所有可能的字符串
print("all possible letters:\n",output(a))


'''
以下是测试
测试1
please input digits:  532
all possible letters:
 ['jda', 'jdb', 'jdc', 'jea', 'jeb', 'jec', 'jfa', 'jfb', 'jfc', 'kda', 'kdb', 'kdc', 'kea', 'keb', 'kec', 'kfa', 'kfb', 'kfc', 'lda', 'ldb', 'ldc', 'lea', 'leb', 'lec', 'lfa', 'lfb', 'lfc']
 
测试2
please input digits:  531
all possible letters:
 ['jd', 'je', 'jf', 'kd', 'ke', 'kf', 'ld', 'le', 'lf']

测试3
please input digits:  503
all possible letters:
 ['jd', 'je', 'jf', 'kd', 'ke', 'kf', 'ld', 'le', 'lf']

测试4
please input digits:  5#3
all possible letters:
 ['j#d', 'j#e', 'j#f', 'k#d', 'k#e', 'k#f', 'l#d', 'l#e', 'l#f']
 
测试5
please input digits:  53*89
all possible letters:
 ['jd*tw', 'jd*tx', 'jd*ty', 'jd*tz', 'jd*uw', 'jd*ux', 'jd*uy', 'jd*uz', 'jd*vw', 'jd*vx', 'jd*vy', 'jd*vz', 'je*tw', 'je*tx', 'je*ty', 'je*tz', 'je*uw', 'je*ux', 'je*uy', 'je*uz', 'je*vw', 'je*vx', 'je*vy', 'je*vz', 'jf*tw', 'jf*tx', 'jf*ty', 'jf*tz', 'jf*uw', 'jf*ux', 'jf*uy', 'jf*uz', 'jf*vw', 'jf*vx', 'jf*vy', 'jf*vz', 'kd*tw', 'kd*tx', 'kd*ty', 'kd*tz', 'kd*uw', 'kd*ux', 'kd*uy', 'kd*uz', 'kd*vw', 'kd*vx', 'kd*vy', 'kd*vz', 'ke*tw', 'ke*tx', 'ke*ty', 'ke*tz', 'ke*uw', 'ke*ux', 'ke*uy', 'ke*uz', 'ke*vw', 'ke*vx', 'ke*vy', 'ke*vz', 'kf*tw', 'kf*tx', 'kf*ty', 'kf*tz', 'kf*uw', 'kf*ux', 'kf*uy', 'kf*uz', 'kf*vw', 'kf*vx', 'kf*vy', 'kf*vz', 'ld*tw', 'ld*tx', 'ld*ty', 'ld*tz', 'ld*uw', 'ld*ux', 'ld*uy', 'ld*uz', 'ld*vw', 'ld*vx', 'ld*vy', 'ld*vz', 'le*tw', 'le*tx', 'le*ty', 'le*tz', 'le*uw', 'le*ux', 'le*uy', 'le*uz', 'le*vw', 'le*vx', 'le*vy', 'le*vz', 'lf*tw', 'lf*tx', 'lf*ty', 'lf*tz', 'lf*uw', 'lf*ux', 'lf*uy', 'lf*uz', 'lf*vw', 'lf*vx', 'lf*vy', 'lf*vz']

'''   
    
    
    
    
    
    
    
    
    
    
    
    
    