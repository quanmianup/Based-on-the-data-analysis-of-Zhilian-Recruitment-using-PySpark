# 基于pyspark智联招聘数据分析

## 实战目标

掌握hadoop大数据的基本技术，熟悉使用pyspark技术，学会编写spark RDD程序，学会使用DataFrame，学会使用spark Sql 语句，学会利用spark读取 MySQL 数据库的数据，学会利用 jieba分词框架，学会使用python网络爬虫框架，学会使用pyecharts数据可视化技术，掌握python web框架flask的使用。

## 涉及知识
Python语言、hadoop大数据技术、pyspark、mysql、flask框架、pyEcharts可视化技术、html、css、JavaScript、linux常用命令、jieba分词。

## 项目描述
利用requests模块编写爬虫程序，将智联招聘网的职位信息爬取到本地。

利用hadoop大数据平台将数据存储。

利用pyspark进行数据分析，分析的内容有统计不同地区的招聘职位数量、统计企业性质类型数量、统计薪资等级数量统计。

利用flask框架结合pyecharts或echarts将分析的结果进行数据可视化。

## 数据采集及处理
打开python3.6的终端安装bs4和pandas两个库

在Pycharm中新建项目“cy_0001”（项目名称为自己的姓名+学号）,在“cy_0001”项目下新建python文件进行爬虫；

爬取智联招聘网站的数据：爬取城市：北京、上海、广州、深圳、天津、武汉、成都、杭州八个城市的;职务搜索关键字为“人力”的数据；爬取字段：职位名称、公司名称、薪资、工作城市、工作经验、学历要求、企业类型；

利用requests模块编写爬虫程序；

利用BeautifullSoup解析html文件；

将智联招聘网的职位信息爬取到本地，保存的文件需要以自己的学号加姓名:如cy_0001.txt。

## 数据分析
1. 启动hadoop系统，打开终端，依次输入命令进行以下操作：      

* a.格式化数据    

* b.启动hadoop

* c.查看是否启动成功

2.上传数据至HDFS，在终端依次输入对应的命令进行操作：    

* a.在HDFS上创建zhilian文件夹      

* b.将爬取智联的数据上传至HDFS      

* c.查看是否上传成功

3.启动pyspark并进行数据分析，在终端输入命令依次进行以下操作：      

* a.启动pyspark      

* b.spark读取HDFS数据    

* c.统计文件内容有多少行      

* e.利用map转换 ，使用split将数据根据“|"拆分    

* f.创建DataFrame，导入row模块，通过RDD2创建DataFrame，定义DataFrame的每一个字段名与数据类型    

* g.创建了zhilian_rows之后，使用sqlContext.createDataFrame()方法写入zhilian_rows数据，创建DataFrame，然后使用.printSchema(方法查看DataFrames的Schema    

* h.使用DataFrame分析公司性质与数量的关系    

* i.保存分析公司性质与数量关系的结果到本地comptypenum.csv文件中      

* j.使用DataFrame分析地区与职位数量的关系    

* k.保存分析地区与数量关系的结果到本地cityjob.csv文件中    

* l.使用DataFrame分析薪资与数量的关系    

* m.保存分析薪资与数量关系的结果到本地salary.csv文件中

## 数据可视化
1. 在zhilianspark工程中，右键选择工程目录，新建templates文件夹

2. 在python3.6的终端安装pyecharts和flask

3. 找到pyecharts的安装目录，终端输入：pip show pyecharts

4. 将pyecharts安装目录下的templates里面的文件’全部复制‘到工程目录下的’templates‘

5. 新建server.py文件，选中工程目录zhilianspark，右键新建python文件

6. 在server.py文件编写数据可视化代码

7. 选中server.py，右键run，启动服务

8. 看到地址后，双击地址，自动打开浏览器，在浏览器中查看可视化效果。

## 项目结构

### 文件结构

```
Based-on-the-data-analysis-of-Zhilian-Recruitment-using-PySpark/
├── templates/
│   ├── components.html
│   ├── macro
│   ├── nb_components.html
│   ├── nb_jupyter_globe.html
│   ├── nb_jupyter_lab.html
│   ├── nb_jupyter_lab_tab.html
│   ├── nb_jupyter_notebook.html
│   ├── nb_jupyter_notebook_tab.html
│   ├── nb_nteract.html
│   ├── simple_chart.html
│   ├── simple_globe.html
│   ├── simple_page.html
│   ├── simple_tab.html
│   └── temp_charts.html
├── README.md
├── app.py
├── cityjob.csv
├── comptypenum.csv
├── data.txt
├── py_sparkdata.py
├── salary.csv
└── sprider-zhilian.py
```

### 主要文件说明：
- `sprider-zhilian.py`：实现智联招聘网站数据爬取，包含请求处理、HTML解析和数据存储功能
- `py_sparkdata.py`：Spark数据分析流程，包含HDFS数据读取、RDD转换、DataFrame操作和结果输出
- `app.py`：基于Flask+pyecharts的可视化系统，集成柱状图、饼图等多种可视化图表
- `templates/`：存放Echarts可视化模板文件，支持交互式数据展示
