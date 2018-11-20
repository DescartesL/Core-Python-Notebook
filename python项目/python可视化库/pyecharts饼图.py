import random
from pyecharts import Pie
attr = ['A', 'B', 'C', 'D', 'E', 'F']
pie = Pie("饼图示例", width=1000, height=600)
pie.add(
    "",
    attr,
    [random.randint(0, 100) for _ in range(6)],
    radius=[50, 55],
    center=[25, 50],
    is_random=True,
)
pie.add(
    "",
    attr,
    [random.randint(20, 100) for _ in range(6)],
    radius=[0, 45],
    center=[25, 50],
    rosetype="area",
)
pie.add(
    "",
    attr,
    [random.randint(0, 100) for _ in range(6)],
    radius=[50, 55],
    center=[65, 50],
    is_random=True,
)
pie.add(
    "",
    attr,
    [random.randint(20, 100) for _ in range(6)],
    radius=[0, 45],
    center=[65, 50],
    rosetype="radius",
)
pie.render()