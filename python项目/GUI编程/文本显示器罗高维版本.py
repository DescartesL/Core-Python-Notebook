import wx
def openfile(event):
    path = path_text.GetValue()
    with open(path,'r',encoding='utf-8') as f:
        content_text.SetValue(f.read())

app = wx.App()#实例化一个主循环
frame = wx.Frame(None,title='GUI是真的难',pos=(1000,200),size = (500,400))#实例化一个窗口

panel = wx.Panel(frame)

path_text = wx.TextCtrl(panel)
open_button = wx.Button(panel,label='打开')
open_button.Bind(wx.EVT_BUTTON,openfile)# 绑定打开文件事件到open_button按钮上

save_button = wx.Button(panel,label = '保存')

content_text=wx.TextCtrl(panel,style = wx.TE_MULTILINE)#  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行

box = wx.BoxSizer()#不带参数表示默认实例化一个水平尺寸器
box.Add(path_text,proportion =5,flag =wx.EXPAND|wx.ALL,border = 3)#添加组件
#proportion：相对比例
#flag：填充的样式和方向,wx.EXPAND为完整填充，wx.ALL为填充的方向
#border：边框
box.Add(open_button,proportion  = 2,flag = wx.EXPAND|wx.ALL,border = 3)
box.Add(save_button,proportion  = 2,flag = wx.EXPAND|wx.ALL,border = 3)

v_box = wx.BoxSizer(wx.VERTICAL)#wx.VERTICAL实例化一个垂直尺寸器
v_box.Add(box,proportion =1,flag=wx.EXPAND|wx.ALL,border=3)
v_box.Add(content_text,proportion =5,flag=wx.EXPAND|wx.ALL,border = 3)

panel.SetSizer(v_box)#设置主尺寸器

frame.Show()#调用窗口展示功能
app.MainLoop()