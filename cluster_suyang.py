import pandas as pd
from sklearn.cluster import KMeans

# 安装必要的库（如果尚未安装）
# pip install pandas scikit-learn openpyxl

# 读取 Excel 文件
df = pd.read_excel("data_y.xlsx")

# 对每个字段进行一维 K-means 聚类
fields = ["MATH", "READ", "SCIE"]
for field in fields:
    # 重塑数据以适应 KMeans
    data = df[field].values.reshape(-1, 1)
    kmeans = KMeans(n_clusters=4, random_state=0).fit(data)
    # 创建新的列来保存聚类标签
    df[f"{field}_Cluster"] = kmeans.labels_

# 导出到新的 Excel 文件
df.to_excel("clustered_data.xlsx", index=False)
