'''
Created on 2020年3月15日

@author: zcy
'''
from django import template

register = template.Library()
 
@register.simple_tag
def indexCN(index):
    return num_to_char(index)

def num_to_char(num):
    """数字转中文"""
    num=str(num)
    new_str=""
    num_dict={"0":u"零","1":u"一","2":u"二","3":u"三","4":u"四","5":u"五","6":u"六","7":u"七","8":u"八","9":u"九"}
    listnum=list(num)
    # print(listnum)
    shu=[]
    for i in listnum:
        # print(num_dict[i])
        shu.append(num_dict[i])
    new_str="".join(shu)
    # print(new_str)
    return new_str