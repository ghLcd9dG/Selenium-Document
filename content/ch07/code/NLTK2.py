# -*- coding: utf-8 -*-
# @Author: name
# @Date:   2018-07-31 21:14:15
# @Last Modified by:   name
# @Last Modified time: 2018-07-31 21:57:09

from bs4 import BeautifulSoup
import urllib.request

import sys
import io
'''
基础：万丈高楼平地起 —— Redis 基础数据结构
千里之行，始于足下。本节我们的学习目标是：快速理解并掌握 Redis 的基础知识。

由于本节内容是 Redis 最简单最容易掌握的知识，如果读者已经很熟悉 Redis 的基础数据结构，从珍惜生命的角度出发，你可以略过本节内容，跳到下一节继续阅读。如果你觉得本节的动画有点晃眼，阅读起来不那么舒服，可以看看作者的另一篇文章《Redis 数据结构基础教程》。

要体验 Redis，我们先从 Redis 安装说起。

Redis 安装
体验 Redis 需要使用 Linux 或者 Mac 环境，如果是 Windows 可以考虑使用虚拟机。主要方式有四种：

使用 Docker 安装。
通过 Github 源码编译。
直接安装 apt-get install(Ubuntu)、yum install(RedHat) 或者 brew install(Mac)。
如果读者懒于安装操作，也可以使用网页版的 Web Redis 直接体验。...


'''
#python print()在控制台会默认转换为gbk输出，但是部分utf-8编码没有对应的gbk，
#所以会报错，我们设置默认输出编码为utf8就没有问题了。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
response = urllib.request.urlopen('')
html = response.read()
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = text.split()
print(tokens)