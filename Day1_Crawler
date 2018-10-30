# -*- coding:utf-8 -*-
from urllib import request
import re
import os

class QSBK:
    def __init__(self):
        self.page_index = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0' # 该参数每个网页的这个不一样
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
        req = request.Request(url, headers=self.headers)
        response = request.urlopen(req)
        page = response.read()
        page = page.decode('utf-8')
        return page

    def getPageItems(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div.*?author.*?clearfix">.*?<a.*?<h2>(.*?)</h2>.*?</div.*?' +
                             '<a.*?class="contentHerf".*?<div.*?"content".*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(), item[1].strip()])
        return pageStories

    def loadPage(self):
        # 如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.page_index)
                if pageStories:
                    self.stories.append(pageStories)
                    self.page_index += 1

    def getEachStory(self, pageStories, page):
        # 遍历一页的段子
        for story in pageStories:
            # 等待用户输入,每当输入回车一次，判断一下是否要加载新页面
            user_input = input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print("第%d页\t发布人:%s\t内容:%s" % (page, story[0], story[1]))
            cur_path = os.path.abspath('.')
            file_name = os.path.join(cur_path,'qiubai.txt')
            file_to_write = open(file_name, 'w+')
            #file_to_write.write(str(story).encode('utf-8'))
            file_to_write.write(str(story))

    def start(self):
        print('正在读取糗事百科,按回车查看新段子，Q退出')
        self.enable = True
        self.loadPage()
        pageIndex = 0
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                pageIndex += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getEachStory(pageStories, pageIndex)

spider = QSBK()
spider.start()
