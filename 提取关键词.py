#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 01:47:28 2019

@author: liujun
"""

from jieba import analyse
import jieba
#方法1 用textrank
n=10
def textrank_extract(path,key_word=n):
    textrank=analyse.textrank
    keyword_list=[]
    for line in open(path,'r'): #每行为一个样本
            keywords=textrank(line,key_word) 
            for keyword in keywords:
                keyword_list.append(keyword)
    return keyword_list


#方法2  用tf_idf
#加载停用词
def get_stopword(stopword_path):
    stopwords=[]
    for line in open(stopword_path,'r'): #每行为一个stopWord
            stopwords.extend(line)
    return stopwords
#过滤
def word_filter(stopword_path,seg_list):
    stopwords=get_stopword(stopword_path)
    filter_list=[]
    for seg in seg_list:
        if not seg in stopwords and len(seg)>1:
            filter_list.append(seg)           
    return filter_list
#加载数据
def load_data(data_path,stopword_path):
    word_list=[]
    for line in open(data_path):
        content=line.strip()
        seg_list=jieba.cut(content)
        filter_list=word_filter(stopword_path,seg_list)
        word_list.append(filter_list)
    return word_list

def tfidf_extract(data_path,stopword_path,key_word=n):
    tfidf=analyse.extract_tags
    keyword_list=[]
    word_list=load_data(data_path,stopword_path)
    for line in word_list:
        keywords=tfidf(str(line),key_word)
        for keyword in keywords:
            keyword_list.append(keyword)
    return keyword_list

keyword_list1=textrank_extract('sample.txt',key_word=n)
keyword_list2=tfidf_extract('sample.txt','stopword.txt',key_word=n)

print("keyword_list1:{} ".format(keyword_list1))
print("keyword_list2:{} ".format(keyword_list2))



        
       
            
            
            
    
            