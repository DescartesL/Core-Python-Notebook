import ftplib
import os
import socket

HOST='ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e :
        print ('ERROR: cannot reach "%s"' % HOST)
        return
    print ('*** Connected to host "%s"' % HOST)

    try:
        f.login()
    except (ftplib.error_perm):
        print ("ERROR: cannot login anonymously")
        f.quit()
        return
    print ('*** Logged in as "anonymous"')


    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print ('ERROR: cannot CD to "%s"' % DIRN)
        f.quit()
        return
    print ('*** Changed to "%s" folder' % DIRN)

    try:
        # 应该把文件对象保存到一个变量中， 如变量loc ， 然后把loc.write 传给ftp.retrbinary()方法
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print ('ERROR: cannot read file "%s"' % FILE)
        # 如果由于某些原因我们无法保存这个文件，那要把存在的空文件给删掉，以防搞乱文件系统
        os.unlink(FILE)
    else:
        # 我们使用了try-except-else 子句，而不是写两遍关闭FTP连接然后返回的代码
        print ('*** Downloaded "%s" to CWD' % FILE)
        f.quit()
        return

if __name__ == '__main__':
    main()