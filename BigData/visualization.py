# -*- coding: utf-8 -*-
import os
from pyecharts import Bar, Map, Page, Pie, configure, WordCloud, Grid, Line,Timeline

configure(global_theme="vintage")



value = []
attr= []
map0 = Map("世界地图示例",width=1600,height=1600)
map0.add("世界地图", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000')
map0.render("world.html")

# 世界地图数据

page=Page()


columns=["北美销量","欧洲销量","日本销量","其他地区销量"]
saledata=[4392.95,2434.13,1291.01,797.75]
pie=Pie("1980-2019 游戏总销量饼图","各市场销量占额")
pie.add("销量",columns,saledata,is_legend_show=False,is_label_show=True)
pie.render("全球销量饼图.html")



人均购买列=["北美","欧洲","日本","其他地区","全球平均"]
人均购买量=[4392.95/368,2434.13/746.4,1291.01/126.3,797.75/(7800-368-746.4-126.3),8920.44/7800]
PeopleAverage=Bar("全球人均电子游戏购买量")
PeopleAverage.add("A",人均购买列,人均购买量,is_label_show=True,is_stack=True)
PeopleAverage.render("全球人均销量.html")


游戏出版公司词云=WordCloud("游戏出版商销量词云图",title_pos="right")
Factory=["Nintendo","EA","Activision","Sony Computer Entertainment","Ubisoft","Take-Two","THQ","Konami","Sega",
         " Bandai Mamco","Microsoft","Capcom","Atari","Warner Bros.","Square Enix","Disney","Eidos","LucasArts","Methesda","Midway games"]
value=[1786.55, 1110.31, 727.45, 607.49, 474.71, 399.53
, 340.76
, 283.63
, 272.98
, 254.09
, 245.79
, 200.89, 157.22
, 153.89, 145.18
, 119.96, 98.97
, 87.34, 82.14, 69.84]
游戏出版公司词云.add("游戏出版公司销量排行",Factory,value,shape="diamond")
游戏出版公司词云.render("词云.html")
NintenLine=Line("任天堂历年发售游戏总销量")
Ninyear=[]
for i in range(1983,2021):
    Ninyear.append(i)
Ningame=[4.28,
5.94,
185.71999999999994,
19.520000000000003,
44.98,
35.92,
125.6,
69.24000000000002,
68.06,
80.62,
53.8,
41.360000000000014,
42.94,
64.64,
63.16000000000001,
120.91999999999999,
93.82000000000001,
107.33999999999997,
109.42000000000002,
67.22,
105.27999999999999,
113.93999999999997,
184.92000000000002,
375.68000000000006,
262.93999999999994,
214.14000000000004,
251.31999999999996,
130.02,
162.25999999999996,
101.86,
145.08000000000007,
123.64000000000001,
60.79999999999999,
89.93999999999998,
199.22,
132.86,
101.5,
29.34,
]
NintenLine.add("任天堂",Ninyear,Ningame)
NintenLine.render("任天堂发售游戏销量趋势.html")


EAgame=[
    0,0,0,0,0,0,0,0,0.14,0,
0.12,0,
3.9999999999999996,
7.839999999999999,
16.939999999999994,
14.600000000000001,
39.70000000000002,
25.600000000000005,
41.019999999999996,
94.76000000000002,
88.32000000000001,
68.96000000000002,
69.88,
58.64000000000002,
105.94000000000001,
120.76,
100.45999999999998,
93.69999999999997,
89.75999999999998,
42.05999999999999,
57.94000000000001,
39.339999999999996,
43.32,
72.19999999999997,
28.320000000000007,
35.47999999999999,
14.3,
    0
]
NintenLine.add("EA",Ninyear,EAgame)
NintenLine.render("任天堂_EA发售游戏销量趋势.html")


page.add(pie)
page.add(游戏出版公司词云)
page.add(PeopleAverage)
page.add(NintenLine)
page.render(os.getcwd()+"\\result\\游戏总销量饼图.html")


#选取1985，1990，1995，2000，2005，2010，2015七个节点
PublisherPie=Timeline("历年游戏市场占比_每五年抽样一次",timeline_bottom=0)
pie_1985=Pie()
pie_1985.add("1985",["Nintendo","Mycom","Namco Bandai games","Hudson Soft","Capcom","Activition"],[49.95,0.02,1.46,1.03,1,0.48])

pie_1990=Pie()
pie_1990.add("1990",
             [ 'Nintendo',
     'Enix Corporation',
    'Sega',
    'Konami Digital Entertainment',
    'Capcom',
    'SquareSoft', 'Namco Bandai Games',
],
             [35.49,3.12,2.6,2.23,3.92,1.4,1.63])
pie_1995=Pie()
list_1995=['18.449999999999996', 'Sony Computer Entertainment',
'16.719999999999995', 'Nintendo',
'7.9300000000000015', 'Sega',
'5.1', 'SquareSoft',
'4.21', 'Activision',
'3.329999999999999', 'Electronic Arts',
'3.32', 'Enix Corporation',
'3.03', 'Ubisoft',
'2.7899999999999996', 'Konami Digital Entertainment',
'2.5199999999999996', 'Namco Bandai Games',
'2.46', 'Acclaim Entertainment',
'1.6900000000000004', 'Psygnosis',
'1.56', 'Virgin Interactive',
'1.25', 'ASCII Entertainment',
'1.12', 'Crystal Dynamics',
'1.11', 'Atlus',
'0.8200000000000001', 'Hudson Soft',
'0.7600000000000001', 'Banpresto',
'0.71', 'Quest',
'0.63', 'Laguna',
'0.63', 'THQ',
'0.6', 'Jaleco',
'0.54', 'Tecmo Koei',
'0.51', 'Epoch',
'0.47', 'Compile',
'0.4', 'ChunSoft',
'2','Others'
]
F1995=[]
D1995=[]
for i in range(len(list_1995)):
    if (i%2==0):
        D1995.append(float(list_1995[i]))
    else:
        F1995.append(list_1995[i])
pie_1995.add("1995",F1995,D1995)

pie_2000=Pie()
list_2000=['34.050000000000004', 'Nintendo',
'25.13', 'Electronic Arts',
'21.689999999999994', 'Sony Computer Entertainment',
'15.859999999999998', 'THQ',
'14.48', 'Activision',
'9.700000000000001', 'Namco Bandai Games',
'8.47', 'Konami Digital Entertainment',
'6.55', 'SquareSoft',
'6.029999999999999', 'Take-Two Interactive',
'5.59', 'Acclaim Entertainment',
'5.359999999999999', 'Enix Corporation',
'4.8100000000000005', 'Atari',
'4.75', 'Ubisoft',
'4.56', 'Eidos Interactive',
'4.2', 'Midway Games',
'3.8800000000000003', 'Sega',
'3.0799999999999996', '3DO',
'2.5500000000000003', 'Virgin Interactive',
'2.44', 'Crave Entertainment',
'18.38','Others'
]
F=[]
D=[]
Others=[]
print(sum(Others))

for i in range(len(list_2000)):
    if (i%2==0):
        D.append(float(list_2000[i]))
    else:
        F.append(list_2000[i])
pie_2000.add("2000",F,D)

pie_2010=Pie()
list_2010=['81.38000000000001', 'Electronic Arts',
'63.390000000000015', 'Activision',
'61.07', 'Nintendo',
'49.160000000000004', 'Microsoft Game Studios',
'42.61999999999998', 'Ubisoft',
'35.839999999999996', 'Take-Two Interactive',
'34.89', 'Sony Computer Entertainment',
'22.889999999999993', 'Sega',
'22.109999999999996', 'THQ',
'20.499999999999996', 'Disney Interactive Studios',
'18.549999999999997', 'Konami Digital Entertainment',
'17.439999999999998', 'Square Enix',
'16.41', 'Namco Bandai Games',
'15.570000000000004', 'Warner Bros. Interactive Entertainment',
'14.380000000000003', 'Capcom',
'14.259999999999996', '505 Games',
'70','Others'
]
F=[]
D=[]
Others=[]
print(sum(Others))

for i in range(len(list_2010)):
    if (i%2==0):
        D.append(float(list_2010[i]))
    else:
        F.append(list_2010[i])
pie_2010.add("2010",F,D)

pie_2019=Pie()
list_2019=[
'101.5', 'Nintendo',
'60.26', 'Activision',
'16', '2K Sports',
'14.3', 'Electronic Arts',
'8.4', 'NetherRealm Studios',
'7.56', 'EA Sports',
'6', 'Keen Software House',
'2.66', 'Coffee Stain Studios',
'2.44', 'Sega',

'15','Others'
]
F=[]
D=[]
Others=[]
print(sum(Others))

for i in range(len(list_2019)):
    if (i%2==0):
        D.append(float(list_2019[i]))
    else:
        F.append(list_2019[i])
pie_2019.add("2019",F,D)


PublisherPie.add(pie_1985,"1985")
PublisherPie.add(pie_1990,"1990")
PublisherPie.add(pie_1995,"1995")
PublisherPie.add(pie_2000,"2000")
PublisherPie.add(pie_2010,"2010")
PublisherPie.add(pie_2019,"2019")
PublisherPie.render("历年游戏市场占比.html")

