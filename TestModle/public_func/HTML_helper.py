#coding='utf-8'
from django.utils.safestring import mark_safe

#分页功能方法

class Pageinfo(object):
    def __init__(self,current_page,all_count,per_item=5):
        self.current_page=current_page
        self.all_count=all_count
        self.per_item=per_item
    def start(self):
        return (self.current_page-1)*self.per_item
    def end(self):
        return self.current_page*self.per_item
    def all_page_count(self):
        temp = divmod(self.all_count, self.per_item)  # temp为（商，余数）
        if temp[1] == 0:
            all_page_count = temp[0]
        else:
            all_page_count = temp[0] + 1
        return all_page_count

def pager(page,all_page_count):
    page_html=[]
    first_page="<a href='caselist/%d'>首页</a>"%(1)     #显示首页

    page_html.append(first_page)
    if page<=1:
        pre_page="<a href='#'>上一页</a>"  #上一页
    else:
        pre_page = "<a href='/caselist/%d'>上一页</a>" % (page-1)
    page_html.append(pre_page)
    #每页显示11个页码
    if all_page_count<11:
        begin=0
        end=all_page_count
    else:
        if page<6:
            begin=0
            end=12
        else:
            if page+6>all_page_count:
                begin=page-6
                end=all_page_count
            else:
                begin=page-6
                end=page+5
    for i in range(begin,end):  #遍历所有页，对应跳转
        if page==i+1:
            a_html="<a style='color:red' href='/caselist/%d'>%d</a>"%(i+1,i+1)
        else:
            a_html = "<a href='/caselist/%d'>%d</a>" % (i + 1, i + 1)
        page_html.append(a_html)
    if page+1>=end:
        next_page = "<a href='#' >下一页</a>"  # 下一页
    else:
        next_page = "<a href='/caselist/%d' >下一页</a>" % (page + 1)  # 下一页
    page_html.append(next_page)
    end_html="<a href='/caselist/%d'>尾页</a>"%(all_page_count)    #显示尾页
    page_html.append(end_html)
    page_string=mark_safe(''.join(page_html))
    return page_string
