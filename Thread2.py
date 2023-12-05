import time
import json
import requests
from datetime import datetime
import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Map
from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB


# 定义抓取数据函数:https://beishan.blog.csdn.net/
def Domestic():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    reponse = requests.get(url=url).json()
    data = json.loads(reponse['data'])
    return data


def Oversea():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'
    reponse = requests.get(url=url).json()
    data = json.loads(reponse['data'])
    return data

def excel_a(china_data):
    china_list = []
    for a in range(len(china_data)):
        province = china_data[a]['name']
        confirm = china_data[a]['total']['confirm']
        heal = china_data[a]['total']['heal']
        dead = china_data[a]['total']['dead']
        nowConfirm = confirm - heal - dead
        china_dict = {}
        china_dict['province'] = province
        china_dict['nowConfirm'] = nowConfirm
        china_list.append(china_dict)
    #保存数据
    china_data = pd.DataFrame(china_list)
    china_data.to_excel("a.xlsx", sheet_name="biubiu",index=False)  # 存储为EXCEL文件
    china_data.head()

def excel_b(china_data):
    china_list = []
    for a in range(len(china_data)):
        province = china_data[a]['name']
        confirm = china_data[a]['total']['confirm']
        heal = china_data[a]['total']['heal']
        dead = china_data[a]['total']['dead']
        nowConfirm = confirm - heal - dead
        china_dict = {}
        china_dict['province'] = province
        china_dict['nowConfirm'] = nowConfirm
        china_list.append(china_dict)
    # 保存数据
    china_data = pd.DataFrame(china_list)
    china_data.to_excel("a.xlsx", sheet_name="biubiu", index=False)  # 存储为EXCEL文件
    china_data.head()

def ChainMap(china_data):
    # 生成一个动态图，只是展示国内的展示图
    m = Map()
    m.add("", [
        list(z)
        for z in zip(list(china_data["province"]), list(china_data["nowConfirm"]))
    ], maptype="china", is_map_symbol_show=False)
    m.set_global_opts(
        title_opts=opts.TitleOpts(title="COVID-19中国现有地区现有确诊人数地图"),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            pieces=[
                {
                    "min": 5000,
                    "label": '>5000',
                    "color": "#893448"
                },  # 不指定 max，表示 max 为无限大
                {
                    "min": 1000,
                    "max": 4999,
                    "label": '1000-4999',
                    "color": "#ff585e"
                },
                {
                    "min": 500,
                    "max": 999,
                    "label": '500-1000',
                    "color": "#fb8146"
                },
                {
                    "min": 101,
                    "max": 499,
                    "label": '101-499',
                    "color": "#ffA500"
                },
                {
                    "min": 10,
                    "max": 100,
                    "label": '10-100',
                    "color": "#ffb248"
                },
                {
                    "min": 1,
                    "max": 9,
                    "label": '1-9',
                    "color": "#fff2d1"
                },
                {
                    "max": 1,
                    "label": '0',
                    "color": "#ffffff"
                }
            ]))
    m.render_notebook()
    m.render("chain.html")

if __name__ == '__main__':
    #国内用户信息
    domestic = Domestic()
    #国外用户信息
    oversea = Oversea()
    #地区数据信息
    areaTree = domestic['areaTree']
    #国外用户信息
    foreignList = oversea['foreignList']

    #子信息
    china_data = areaTree[0]['children']

    #国外疫情数据提取
    world_data = foreignList
    world_list = []

    for a in range(len(world_data)):
        # 提取数据
        country = world_data[a]['name']
        nowConfirm = world_data[a]['nowConfirm']
        confirm = world_data[a]['confirm']
        dead = world_data[a]['dead']
        heal = world_data[a]['heal']
        # 存放数据
        world_dict = {}
        world_dict['country'] = country
        world_dict['nowConfirm'] = nowConfirm
        world_dict['confirm'] = confirm
        world_dict['dead'] = dead
        world_dict['heal'] = heal
        world_list.append(world_dict)

    #国外数据统计
    world_data = pd.DataFrame(world_list)
    world_data.to_excel("b.xlsx", index=False)
    world_data.head()

    #数据整合
    world_data.loc[world_data['country'] == "中国"]
    print(world_data.loc[world_data['country'] == "中国"])
    #获取用户信息中的中国用户信息，并添加到world_data的数据中
    confirm = areaTree[0]['total']['confirm']  # 提取中国累计确诊数据
    heal = areaTree[0]['total']['heal']  # 提取中国累计治愈数据
    dead = areaTree[0]['total']['dead']  # 提取中国累计死亡数据
    nowConfirm = confirm - heal - dead  # 计算中国现有确诊数量

    #将数据填充到world_data中
    world_data = world_data.append(
        {
            'country': "中国",
            'nowConfirm': nowConfirm,
            'confirm': confirm,
            'heal': heal,
            'dead': dead
        },
        ignore_index=True)
    world_data.loc[world_data['country'] == "中国"]

