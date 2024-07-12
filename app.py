import pandas as pd
from flask import Flask
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie, Tab

app = Flask(__name__)


def create_bar_chart(file_path, x_axis_col, y_axis_col):
    df = pd.read_csv(file_path)
    bar = (
        Bar()
        .add_xaxis(df[x_axis_col].tolist())
        .add_yaxis("企业数量", df[y_axis_col].tolist())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="企业性质与数量的关系"))
    )
    return bar


def create_pie_chart(file_path, name_col, value_col):
    df = pd.read_csv(file_path)
    pie = (
        Pie()
        .add("", [(row[name_col], row[value_col]) for _, row in df.iterrows()])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}:{d}%"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="地区与职位数量的关系")
        )
    )
    return pie


def create_ring_chart(file_path, name_col, value_col):
    df = pd.read_csv(file_path)
    pie = (
        Pie()
        .add("", [(row[name_col], row[value_col]) for _, row in df.iterrows()], radius=["40%", "75%"])
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}:{d}%"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="薪资与数量的关系"),
            legend_opts=opts.LegendOpts(is_show=False))
    )
    return pie


@app.route('/', methods=['GET', 'POST'])
def index():
    bar_chart_html = create_bar_chart('comptypenum.csv', 'company_type', 'count')
    pie_chart_html = create_pie_chart('cityjob.csv', 'job_city', 'count')
    ring_chart_html = create_ring_chart('salary.csv', 'salary', 'count')
    tab = Tab()
    tab.page_title = '基于pyspark智联招聘数据分析'
    tab.add(bar_chart_html, '企业性质统计')
    tab.add(pie_chart_html, '地区与职位')
    tab.add(ring_chart_html, '薪资与数量')
    return tab.render_embed()


if __name__ == '__main__':
    app.run()
