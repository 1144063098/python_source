from pyecharts import Bar
attr =["衬衫","羊毛衫","雪纺衫","裤子","运动鞋","短袖"]
v1=[35,25,36,20,75,90]
v2=[10,25,18,60,20,110]
v3=[29,20,33,40,51,100]
bar = Bar("柱状图数据堆叠事例")
bar.add("商家A",attr,v1,is_stack=True,is_label_show=True)
bar.add("商家B",attr,v2,is_stack=True,is_label_show=True)
bar.add("商家C",attr,v3,is_stack=True,is_label_show=True)
bar.render()