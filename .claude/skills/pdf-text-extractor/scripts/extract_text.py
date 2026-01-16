#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF文本提取脚本
版本: 1.0.0
依赖: PyPDF2==3.0.1, pdfplumber==0.10.3
错误码: 100-参数错误, 200-文件读取失败, 300-提取失败
"""
import argparse
import logging
import PyPDF2
import pdfplumber
from typing import Optional

# 日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("pdf-text-extractor")

def extract_pdf_text(input_path: str, output_path: Optional[str] = None) -> str:
    try:
        # 尝试用pdfplumber提取（支持表格文本）
        with pdfplumber.open(input_path) as pdf:
            text_result = []
            for page_num, page in enumerate(pdf.pages, 1):
                text = page.extract_text() or ""
                text_result.append(f"#### 第{page_num}页\n{text}")

            result = "### PDF文本提取结果（共{len(pdf.pages)}页）\n".format(len(pdf.pages))
            result += "\n".join(text_result)

            # 保存结果（可选）
            if output_path:
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(result)
            return result
    except PyPDF2.errors.PdfReadError:
        logger.error("文件读取失败，可能是加密或损坏")
        return "错误码200：文件读取失败，可能是加密或损坏的PDF文件"
    except FileNotFoundError:
        logger.error(f"文件不存在：{input_path}")
        return f"错误码100：文件不存在 - {input_path}"
    except Exception as e:
        logger.error(f"提取失败：{str(e)}")
        return f"错误码300：提取失败 - {str(e)}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PDF文本提取工具")
    parser.add_argument("--input", required=True, help="PDF文件路径")
    parser.add_argument("--output", help="输出文本文件路径（可选）")
    args = parser.parse_args()

    result = extract_pdf_text(args.input, args.output)
    print(result)
