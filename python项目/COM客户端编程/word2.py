from win32com.client import Dispatch, constants
from win32com.client.gencache import EnsureDispatch

EnsureDispatch('Word.Application')  # makepy 导入Word类库，否则constants无法使用

msword = Dispatch('Word.Application')
msword.Visible = True  # 是否可见
msword.DisplayAlerts = 0

doc = msword.Documents.Open(FileName=strDir + r'tbbts01e01.docx')  # 打开已有文件
newdoc = msword.Documents.Add()  # 添加新文件

newdoc.SaveAs('new.docx')