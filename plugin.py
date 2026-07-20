#!/usr/bin/env python3

import argparse
from pathlib import Path

from paddleocr import *


def predict(xopp_path: str):

    print("#########################################\n" + xopp_path + "\n#########################################\n")
    ocr = PPStructureV3(
        enable_mkldnn=False,
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
    )
    result = ocr.predict(xopp_path + ".png")
    for res in result:
        res.save_to_markdown(xopp_path + ".md")


def main():
    parser = argparse.ArgumentParser(
        description="Convert an xopp to a markdown file using PaddleOCR"
    )
    parser.add_argument("xopp", help="Path to the input xopp")
    args = parser.parse_args()

    predict(args.xopp)


if __name__ == "__main__":
    main()
