import pandas as pd

# 读取CSV文件
data = pd.read_csv('All_threat_data.csv')

# 提取"Fam"列的数据
fam_data = data['Status']

# 打印"Fam"列中所有的元素
print(fam_data)

unique_elements = fam_data.unique()
print(unique_elements)

# 使用pandas的factorize函数对Fam列进行编码，赋予每个不同的元素一个唯一的整数标识
labels, uniques = pd.factorize(fam_data)

# 将编码后的标签赋值回原表
data['Status'] = labels+1  # 加1是为了实现
print(data['Status'])
data.to_csv('process_test.csv', index=False)


# import pandas as pd
#
# # 读取CSV文件
# data = pd.read_csv('process.csv')
#
# # 将 "GenSpec" 列中的 "_" 替换为 "."
# data['GenSpec'] = data['GenSpec'].str.replace('_', '.')
# print(data['GenSpec'])
# # 存回CSV文件
# data.to_csv('process.csv', index=False)

