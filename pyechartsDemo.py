from pyecharts.charts import Bar


def map():
    bar = Bar()
    bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    bar.render("mycharts.html")
    bar.render()

#生成html
if __name__ == '__main__':
   map()