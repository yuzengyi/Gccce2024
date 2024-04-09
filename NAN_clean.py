import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('data_init.xlsx')

# 删除含有缺失值的行
df_cleaned = df.dropna()

# 导出到新的 Excel 文件
df_cleaned.to_excel('cleaned_data.xlsx', index=False)
