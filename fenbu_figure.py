import pandas as pd
import matplotlib.pyplot as plt

# 请替换为您的Excel文件路径
file_path = 'data_fenbu.xlsx'
df = pd.read_excel(file_path)

# 选择港澳台地区
regions = ['TAP', 'MAC', 'HKG']
df_filtered = df[df['CNT'].isin(regions)]

# 分组并统计 ST347Q01JA 字段的值
count_data = df_filtered.groupby('CNT')['ST347Q01JA'].value_counts().unstack(fill_value=0)

# 绘制柱状图
count_data.plot(kind='bar', figsize=(10, 6))
plt.title('ST347Q01JA Counts in Hong Kong, Macau, and Taiwan')
plt.xlabel('Region')
plt.ylabel('Counts')
plt.xticks(rotation=0)

# 保存图像
plt.savefig('st347q01ja_counts_by_region.png')

plt.show()
