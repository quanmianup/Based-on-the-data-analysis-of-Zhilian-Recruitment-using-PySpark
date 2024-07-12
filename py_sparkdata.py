from pyspark.sql import Row
from pyspark.sql import SparkSession
import os

os.environ["PYSPARK_PYTHON"] = "/opt/conda3/bin/python3"
os.environ["PYSPARK_DRIVER_PYTHON"] = "/opt/conda3/bin/python3"
# 创建 SparkSession
spark = SparkSession.builder.getOrCreate()

# spark读取HDFS数据
lines = spark.read.text("hdfs://localhost:8020/data.txt").rdd.map(lambda x: x.value)
# 统计文件内容有多少行
num_lines = lines.count()
print("文件行数:", num_lines)

# 利用map转换，使用split将数据根据“|"拆分
split_lines = lines.map(lambda line: line.split("|"))

# 创建 Row 对象的 RDD
row_rdd = split_lines.map(
    lambda x: Row(job_name=x[1], company_name=x[2], salary=x[3], job_city=x[0], job_experience=x[5], job_education=x[6],
                  company_type=x[7]))

# 创建 DataFrame
df = spark.createDataFrame(row_rdd)
# 查看DataFrames的Schema
df.printSchema()

# 分析公司性质与数量的关系
result_company_type = df.groupBy("company_type").count()
# 分析地区与职位数量的关系
result_city_job = df.groupBy("job_city").count()
# 分析薪资与数量的关系
result_salary = df.groupBy("salary").count()

result_company_type.show()
result_city_job.show()
result_salary.show()

# 保存公司性质分析结果到 CSV
result_company_type.toPandas().to_csv("comptypenum.csv", index=False)
# 保存地区与职位数量分析结果到 CSV
result_city_job.toPandas().to_csv("cityjob.csv", index=False)
# 保存薪资与数量分析结果到 CSV
result_salary.toPandas().to_csv("salary.csv", index=False)
