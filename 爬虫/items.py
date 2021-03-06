#!/usr/bin python
# -*- encoding: utf-8 -*-
'''
@Author  :   Celeste Young
@File    :   items.py    
@Time    :   2021/1/13 14:09  
@Tips    :    
'''
import scrapy


class JianshuArticleItem(scrapy.Item):
    avatar = scrapy.Field()  # 头像
    nickname = scrapy.Field()  # 昵称
    time = scrapy.Field()  # 发表时间
    wrap_img = scrapy.Field()  # 封面（缺省值）
    title = scrapy.Field()  # 标题
    abstract = scrapy.Field()  # 正文部分显示
    read = scrapy.Field()  # 查看人数
    comments = scrapy.Field()  # 评论数
    like = scrapy.Field()  # 喜欢（点赞）
    detail = scrapy.Field()  # 文章详情url
    pass