import requests
import os

# Dify 应用的 API 端点
api_endpoint = "http://106.54.241.89/v1/completion-messages"

# 设置请求头，包括 API 密钥
headers = {
    "Authorization": "Bearer app-JGZR0LA9QHLt8UBlK5WFA0Oo",
    "Content-Type": "application/json"
}


def get_all_txt_files():
    txt_files = []
    for root, dirs, files in os.walk('int/txt'):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return txt_files

def read_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def send_txt_to_dify():
    # 获取所有txt文件路径
    txt_files = get_all_txt_files()
    print(txt_files)
    # 创建markdown目录（如果不存在）
    markdown_dir = 'int/markdown'
    os.makedirs(markdown_dir, exist_ok=True)

    # 为每个txt文件创建对应的markdown文件
    for txt_file in txt_files:
        # 获取文件名(不含扩展名)
        base_name = os.path.splitext(os.path.basename(txt_file))[0]
        
        # 构建markdown文件路径
        markdown_path = os.path.join(markdown_dir, f"{base_name}.md")
        
        print(f"创建markdown文件: {markdown_path}")
        
        # 创建空的markdown文件
        with open(markdown_path, 'w', encoding='utf-8'):
            pass

        print(f"正在处理文件: {txt_file}")
        content = read_txt_file(txt_file)
        print(f"文件内容长度: {len(content)}")

        # 定义请求数据
        data = {
            "inputs": {
                "copy": content,
            },
            "response_mode": "blocking",
            "user": "poorwym"
        }

        # 发送 POST 请求
        response = requests.post(api_endpoint, headers=headers, json=data)

        print("HTTP 状态码:", response.status_code)
        print("服务器返回的内容:", response.text)  # 添加这一行

        # 检查响应状态码
        if response.status_code == 200:
            # 请求成功，处理响应数据
            try:
                result = response.json()
                print("AI 回复:", result["answer"])
                # 将AI回复写入对应的markdown文件
                with open(markdown_path, 'w', encoding='utf-8') as f:
                    f.write(result["answer"])

            except requests.exceptions.JSONDecodeError as e:
                print("JSON 解析错误:", e)
        else:
            # 请求失败，打印错误信息
            print("请求失败，状态码:", response.status_code)
            print("错误信息:", response.text)
if __name__ == "__main__":
    send_txt_to_dify()