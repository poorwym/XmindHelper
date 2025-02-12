
# 最终效果

对所有data目录下的文件导出为xmind格式的思维导图。

# 实现思路

1. 遍历data目录下的所有文件 **done**
2. 把所有文件转换为pdf格式 **done**
3. 把所有pdf转换成markdown/txt **done**
4. 利用大语言模型工作流把markdown/txt转换为结构化json格式，要求中文
5. 对json格式进行解析，转换为xmind格式
6. 输出xmind文件