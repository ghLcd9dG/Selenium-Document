# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-08-01 10:27:51
# @Last Modified by:   name
# @Last Modified time: 2018-08-01 10:30:22
from nltk.corpus import wordnet

syn = wordnet.synsets("pain")
#输出定义
print(syn[0].definition(),"\n")
#输出样例
print(syn[0].examples())
