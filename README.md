# Magnify

> Convert handwritten Xournal++ notes into editable Markdown using local OCR.

Magnify is a plugin for **Xournal++** that recognizes handwritten notes on the current page of a notebook and exports the recognized text as a Markdown (`.md`) file.

Unlike cloud-based OCR solutions, Magnify performs recognition **locally** using the **PaddleOCR Python API**, keeping your notes private while providing fast offline processing.

## Features

- Recognize handwritten notes from the current Xournal++ page
- Export OCR results as a Markdown (`.md`) file
- 100% local processing with PaddleOCR
- Seamless integration with Xournal++
- Powered by the PaddleOCR Python API

## How it works

1. Open your notebook in Xournal++.
2. Navigate to the page you want to convert.
3. Run the **Magnify** plugin (or with `CTRL + m`). 
4. Magnify export the page as a `.png`, sends it to `plugin.py` file, and recognizes the handwritten text using PaddleOCR local python API.
5. The recognized text is exported as a Markdown file next to your notebook.

## Requirements

- Xournal++
- Python 3.12
- PaddleOCR

## Installation

Clone the repository into the plugin folder of Xournal++:

```bash
git clone https://github.com/AvenReal/Magnify /usr/share/xournalpp/plugins/Magnify
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Open a Xournal++ notebook.
2. Go to the page you want to recognize.
3. Launch **Magnify** from the Plugins menu (or with `CTRL + m`).
4. Wait for the OCR process to complete.
5. Open the generated `.md` file.

## Example

### Handwritten page

## Privacy

Magnify performs OCR **entirely on your machine**.

No images or handwritten notes are uploaded to external services. All recognition is performed locally through the PaddleOCR Python API.

## Roadmap

- [x] Handwritten OCR
- [x] Markdown export
- [ ] Multi-page export
- [ ] Toggle console visibility
- [ ] Multiple console support (currently: only kitty)

## Contributing

Contributions are welcome! Whether it's bug reports, feature requests, or pull requests, any help is appreciated.

## License

This project is licensed under the terms of the LICENSE file.
