import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 示例：读取一个示例Excel文件
# 实际应用中，请替换为您的Excel文件路径
file_path = 'data_y.xlsx'  # 更换为你的文件路径
df = pd.read_excel(file_path)

# 定义进行聚类的字段
fields = ["MATH", "READ", "SCIE"]

# 对每个字段进行一维 K-means 聚类并排序聚类中心
for field in fields:
    # 重塑数据以适应 KMeans
    data = df[field].values.reshape(-1, 1)
    kmeans = KMeans(n_clusters=4, random_state=0).fit(data)

    # 排序聚类中心并获取排序后的标签
    sorted_centroids = np.argsort(kmeans.cluster_centers_.sum(axis=1))
    sorted_labels = np.zeros_like(kmeans.labels_)
    for i in range(4):
        sorted_labels[kmeans.labels_ == sorted_centroids[i]] = i + 1

    # 将排序后的标签添加到数据框中
    df[f"{field}_Cluster"] = sorted_labels

# 保存排序后的聚类结果到新的Excel文件
output_file_path = 'clustered_data_new.xlsx'  # 更换为你的输出文件路径
df.to_excel(output_file_path, index=False)

# 可视化聚类结果
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharey=True)
for i, field in enumerate(fields):
    axes[i].scatter(df[field], [0] * len(df), c=df[f"{field}_Cluster"], cmap='viridis', label=f'{field} Clusters')
    axes[i].set_title(f'{field} Clusters')
    axes[i].set_xlabel(field)
    axes[i].legend()
    axes[i].set_yticks([])

plt.tight_layout()

# 保存可视化图
visualization_file_path = 'clustered_visualization.png'  # 更换为你的可视化图保存路径
plt.savefig(visualization_file_path)

plt.show()

