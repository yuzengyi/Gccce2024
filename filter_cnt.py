import pandas as pd
import pyreadstat

# 读取.sav文件
df, meta = pyreadstat.read_sav('CY08MSP_STU_QQQ.sav')

# 筛选 CNT 字段中为 HKG、MAC、TAP 的行
filtered_df = df[df['CNT'].isin(['HKG', 'MAC', 'TAP'])]

# 导出到 Excel 文件
filtered_df.to_excel('filtered_data.xlsx', index=False)
