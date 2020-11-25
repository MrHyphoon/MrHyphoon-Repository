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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    