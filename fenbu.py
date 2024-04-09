import pandas as pd

# 定义要保留的字段
columns_to_keep = [
    'CNT', 'ST347Q01JA'
]

# 读取 Excel 文件
df = pd.read_excel('filtered_data.xlsx')

# 仅保留指定的字段
filtered_df = df[columns_to_keep]

# 导出到新的 Excel 文件
filtered_df.to_excel('data_fenbu.xlsx', index=False)
