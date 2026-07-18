#!/usr/bin/env python3

import argparse
from pathlib import Path

from paddleocr import *


def image_to_md(image_path: str):
    # ocr = PaddleOCR(
    #     use_doc_orientation_classify=False,
    #     use_doc_unwarping=False,
    #     use_textline_orientation=False,
    #     engine="paddle",
    #     ocr_version="PP-FormulaNet",
    #     enable_mkldnn=False,
    #     text_det_thresh=0.15,
    #     text_det_box_thresh=0.3,
    #     text_det_unclip_ratio=2.0,
    #     text_det_limit_side_len=3072
    # )
    ocr = PPStructureV3(
        enable_mkldnn=False,
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
    )
    result = ocr.predict(image_path)
    for res in result:
        res.save_to_img("output")

        res.save_to_json("output")


def main():
    parser = argparse.ArgumentParser(
        description="Convert an image to a searchable pdf using PaddleOCR"
    )
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()

    image_to_md(args.image)


if __name__ == "__main__":
    main()
