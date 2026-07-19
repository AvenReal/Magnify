#!/usr/bin/env python3

import argparse
from pathlib import Path

from paddleocr import *


def predict(image_path: str, output_path = "/usr/share/xournalpp/plugins/Magnify/outputs"):
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
        res.save_to_img(output_path)

        res.save_to_json(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Convert an image to a searchable pdf using PaddleOCR"
    )
    parser.add_argument("image", help="Path to the input image")
    args = parser.parse_args()

    predict(args.image)


if __name__ == "__main__":
    main()
