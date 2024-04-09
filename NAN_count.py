import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('data.xlsx')

# 计算每列的缺失值数
missing_values = df.isnull().sum()

# 将结果转换为 DataFrame
missing_values_df = missing_values.reset_index()
missing_values_df.columns = ['Column', 'MissingValues']

# 导出到新的 Excel 文件
missing_values_df.to_excel('missing_values_report.xlsx', index=False)
