from pyecharts import Polar
import random
data_1 = [(10, random.randint(1, 100)) for i in range(300)]
data_2 = [(11, random.randint(1, 100)) for i in range(300)]
polar = Polar("极坐标系-散点图示例", width=1200, height=600)
polar.add("", data_1, type='scatter')
polar.add("", data_2, type='scatter')
polar.render()