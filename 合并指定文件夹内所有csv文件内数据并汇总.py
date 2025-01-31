import os
import pandas as pd
import chardet

def detect_encoding(file_path):
    """检测文件的编码格式"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def merge_csv_files(folder_path, output_file):
    """
    合并文件夹下所有CSV文件的数据，并生成一个新的汇总文件。

    :param folder_path: 包含CSV文件的文件夹路径
    :param output_file: 输出的汇总文件路径
    """
    # 获取文件夹下所有CSV文件
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
    
    # 检查是否存在CSV文件
    if not csv_files:
        print("文件夹中没有CSV文件！")
        return
    
    # 初始化一个空列表，用于存储所有数据
    all_data = []
    
    # 遍历所有CSV文件并读取数据
    for file in csv_files:
        file_path = os.path.join(folder_path, file)
        try:
            # 检测文件编码
            encoding = detect_encoding(file_path)
            print(f"检测到文件 {file} 的编码为: {encoding}")
            # 读取CSV文件
            df = pd.read_csv(file_path, encoding=encoding)
            all_data.append(df)  # 将数据添加到列表中
            print(f"已读取文件: {file}")
        except Exception as e:
            print(f"读取文件 {file} 时出错: {e}")
    
    # 合并所有数据
    if all_data:
        merged_data = pd.concat(all_data, ignore_index=True)
        # 将合并后的数据保存到新的CSV文件
        merged_data.to_csv(output_file, index=False, encoding='utf-8')
        print(f"所有CSV文件已合并，并保存到: {output_file}")
    else:
        print("没有有效数据可以合并！")


# 示例用法
if __name__ == "__main__":
    # 设置文件夹路径和输出文件路径
    folder_path = r"E:\123"  # 替换为你的CSV文件夹路径
    output_file = r"E:\123\merged_file.csv"  # 替换为你的输出文件路径
    
    # 调用函数合并CSV文件
    merge_csv_files(folder_path, output_file)
