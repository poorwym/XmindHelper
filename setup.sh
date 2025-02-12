#!/bin/bash
set -e

# 清理pip缓存
echo "清理pip缓存..."
pip cache purge

# 检测操作系统类型
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "检测到Mac操作系统"
    echo "安装tesseract和poppler..."
    
    # 检查是否安装了Homebrew
    if ! command -v brew &> /dev/null; then
        echo "未检测到Homebrew,开始安装Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    # 使用Homebrew安装tesseract和poppler
    brew install tesseract
    brew install poppler
    
    echo "tesseract和poppler安装完成"
fi


# 创建新的conda环境
echo "创建conda环境XmindHelper..."
conda create -n XmindHelper python=3.10 -y

echo "开始设置pptx2pdf"

# 安装pptx2pdf及其依赖
echo "安装pptx2pdf..."
conda run -n XmindHelper pip install -r vendor/pptx2pdf/requirements.txt

echo "pptx2pdf环境配置完成！"

echo "开始设置aisuite"

# 安装aisuite及其依赖
echo "安装aisuite..."
conda run -n XmindHelper pip install aisuite[all]

echo "aisuite环境配置完成！"

echo "开始设置PDFInsight"

# 安装PDFInsight及其依赖
echo "安装PDFInsight..."
conda run -n XmindHelper pip install -r vendor/PDFInsight/requirements.txt

echo "PDFInsight环境配置完成！"

echo "全部安装完成！"
echo "请记住使用前需要激活conda环境："
echo "conda activate XmindHelper"

