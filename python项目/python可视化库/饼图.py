from collections import Counter
from math import pi
import pandas as pd
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
output_file("pie.html")
x = Counter({ # 数据与权重
    '中国': 157,
    '美国': 93,
    '日本': 89,
    '巴西': 63,
    '德国': 44,
    '印度': 42,
    '意大利': 40,
    '澳大利亚': 35,
    '法国': 31,
    '西班牙': 29
})
data = pd.DataFrame.from_dict(dict(x), orient='index').reset_index().rename(index=str, columns={0:'value', 'index':'country'})
data['angle'] = data['value']/sum(x.values()) * 2*pi
data['color'] = Category20c[len(x)]
p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value")
p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None # 网格线颜色
show(p)