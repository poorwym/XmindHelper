import sys
import os
import shutil

# 添加项目根目录到Python路径
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

from vendor.pptx2pdf import pptx2pdf
from vendor.PDFInsight.PDFInsight import par_pdf_by_path

def move_pdf_to_int(pdf_dir):
    os.makedirs("int/pdf", exist_ok=True)
    if os.path.exists(pdf_dir):
        pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
        dest_dir = os.path.join(root_dir, "int", "pdf")
        for pdf_file in pdf_files:
            shutil.move(os.path.join(pdf_dir, pdf_file), os.path.join(dest_dir, pdf_file))
            print(f"移动文件: {os.path.join(pdf_dir, pdf_file)} 到 {os.path.join(dest_dir, pdf_file)}")

def process_pdfs_to_txt():
    """处理int/pdf目录下的所有PDF文件并将文本保存到int/txt目录"""
    pdf_dir = os.path.join(root_dir, "int", "pdf")
    txt_dir = os.path.join(root_dir, "int", "txt")
    
    # 创建txt输出目录
    os.makedirs(txt_dir, exist_ok=True)
    
    # 获取所有PDF文件
    pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_dir, pdf_file)
        # 生成对应的txt文件名（将.pdf替换为.txt）
        txt_file = pdf_file.rsplit('.', 1)[0] + '.txt'
        txt_path = os.path.join(txt_dir, txt_file)
        
        print(f"开始处理: {pdf_file}")
        print(f"pdf_dir: {pdf_dir}")
        print(f"pdf_path: {pdf_path}")
        try:
            # 使用PDFInsight处理PDF文件
            text_content = par_pdf_by_path([pdf_path], ocr = False) #希望传入一个列表
            
            # 将提取的文本保存到txt文件
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(text_content)
            print(f"成功处理: {pdf_file} -> {txt_file}")
        except Exception as e:
            print(f"处理 {pdf_file} 时出错: {str(e)}")

if __name__ == "__main__":
    # 获取用户输入
    step = 1
    
    if step <= 1:
        # 转换pptx为pdf step1
        pptx2pdf.convert_ppt_to_pdf("data/pptx")

        # 获取data/pdf目录路径
        pdf_dir = os.path.join("data", "pptx", "pdf")
        
        # 如果pdf目录存在
        move_pdf_to_int(pdf_dir)

        # 删除空的pdf目录
        os.rmdir(pdf_dir)
    
    if step <= 2:
        # 处理PDF文件并生成文本文件 step2
        process_pdfs_to_txt()

    

