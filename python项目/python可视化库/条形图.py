from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
output_file("colormapped_bars.html")#  配置输出文件名
fruits = ['Apples', '魅族', 'OPPO', 'VIVO', '小米', '华为'] # 数据
counts = [5, 3, 4, 2, 4, 6] # 数据
source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))
p = figure(x_range=fruits, y_range=(0,9), plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")# 条形图配置项
p.vbar(x='fruits', top='counts', width=0.9, color='color', legend="fruits", source=source)
p.xgrid.grid_line_color = None # 配置网格线颜色
p.legend.orientation = "horizontal" # 图表方向为水平方向
p.legend.location = "top_center"
show(p) # 展示图表