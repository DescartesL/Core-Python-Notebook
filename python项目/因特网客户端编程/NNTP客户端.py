import os
import nntplib
import socket

HOST = 'your.nntp.server'
GRNM = 'group name'
USER = 'user'
PASS = 'password'

def main():
    try:
        n = nntplib.NNTP(HOST)    #尝试连接 NNTP 服务器，如果失败就退出
        #,user=USER,password=PASS
    except socket.gaierror as e:
        print('ERROR:cannot reach host "%s"' % HOST)
        print('    ("%s")' % eval(str(e))[1])
        return
    except nntplib.NNTPPermanentError as e:
        print('ERROR:access denied on "%s"' % HOST)
        print('    %s' % str(e))
        return
    print('****connected to host "%s"' % HOST)

    try:
        rsp, ct , fst, lst, grp = n.group(GRNM)    #尝试读取指定的新闻组
    except nntplib.NNTPTemporaryError as e:      #如果新闻组不存在、或服务器没有保存这个新闻组，或需要身份验证等就退出
        print('ERROR: cannot load group "%s"' % GRNM)
        print('    "%s"' % str(e))
        print('     server may require authentication')
        print('     uncomment/edit login line above')
        n.quit()
        return
    except nntplib.NNTPTemporaryError as e:
        print('ERROR: group "%s" unavaliable' % GRNM)
        print('    %s' % str(e))
        n.quit()
        return
    print('*** found newsgroup "%s"' % GRNM)

    rng = '%s-%s' % (lst,lst)     #给定想要提取消息头的文章范围，因为要获取最后一条信息，所以范围是最后--最后
    rsp, frm = n.xhdr('from',rng)     #获取制定范围的文章信息：服务器响应，指定范围的消息头列表 frm-文章来源
    rsp, sub = n.xhdr('subject',rng)    #sub 文章子标题
    rsp, dat = n.xhdr('date',rng)   #文章主文本
    print('''
            *** found last article (#%s):
            from:%s
            subject:%s
            date:%s
            ''' % (lst, frm[0][1], sub[0][1], dat[0][1]))
           # '''
            #由于上边选取的范围只有最后一个，所以只获取第一个元素【0】，数
            #据元素是一个长度为2的元组，包含文章编号和数据字符串，因此数据字符串frm[0][1]
            #'''
    rsp, anum, mid, data = n.body(lst)   #根据最后一篇文章的 id 获取（服务器响应信息，文章编号，消息 id，文章所有行）
    displayFirst20(data)  #调用方法只保存前20个有意义的行
    n.quit()      #退出



def displayFirst20(data):
    '''
    获取 data 内前20个有意义的行
    '''
    print('*** first (<=20) meaningful lines:\n')
    count = 0    #创建一个计数器
    '''
    获取文章行列表，rstrip()方法删除字符串尾随的空格
    '''
    lines = (line.rstrip() for line in data)
    lastBlank = True     #上一行为空的标识，作为判断条件
    for line in lines:
        if line:
            lower = line.lower()  #将 line 内容转换小写
            if (lower.startswith('>') and not \
                lower.startswith('>>>')) or \
                lower.startswith('|') or \
                lower.startswith('in article') or \
                lower.endswith('writes:') or \
                lower.endswith('wrote:'):
                continue

        if not lastBlank or (lastBlank and line):  #如果上一行不是空行，或者上一行为空行，但当前行不为空时
            print('    %s' % line)
            if line:         #如果当前行不为空，计数器+1，lastBank 为 false，上一行不为空
                count += 1
                lastBlank = False
            else:
                lastBlank = True

        if count == 20:
            break

if __name__ == '__main__':
    main()
