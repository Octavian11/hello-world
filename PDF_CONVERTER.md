# PDF Converter

A simple and powerful Python script to convert Markdown and HTML files to PDF format.

## Features

- Convert Markdown (.md) files to PDF
- Convert HTML files to PDF
- Beautiful default styling with GitHub-flavored theme
- Support for:
  - Code blocks with syntax highlighting
  - Tables
  - Images
  - Links
  - Headings
  - Blockquotes
  - Task lists
  - And more!

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install markdown2 weasyprint
```

### 2. Make the Script Executable (Optional)

```bash
chmod +x convert_to_pdf.py
```

## Usage

### Basic Usage

Convert a Markdown file to PDF:

```bash
python3 convert_to_pdf.py README.md
```

This will create `README.pdf` in the same directory.

### Specify Output File

```bash
python3 convert_to_pdf.py input.md output.pdf
```

### Convert HTML to PDF

```bash
python3 convert_to_pdf.py document.html report.pdf
```

### Help

```bash
python3 convert_to_pdf.py --help
```

## Examples

### Example 1: Convert README to PDF

```bash
python3 convert_to_pdf.py README.md
# Creates: README.pdf
```

### Example 2: Convert with Custom Output Name

```bash
python3 convert_to_pdf.py documentation.md final-report.pdf
# Creates: final-report.pdf
```

### Example 3: Convert HTML File

```bash
python3 convert_to_pdf.py webpage.html webpage.pdf
# Creates: webpage.pdf
```

## Styling

The converter includes beautiful default styling:

- **Typography**: Clean, readable fonts (system fonts: -apple-system, Segoe UI, Roboto, etc.)
- **Code**: Syntax-friendly monospace font with light gray background
- **Tables**: Bordered tables with header styling
- **Headings**: GitHub-style headings with bottom borders for H1 and H2
- **Links**: Blue hyperlinks
- **Blockquotes**: Left-bordered quotes with gray text

### Custom Styling

For HTML files, you can include your own CSS styles directly in the HTML file.

For Markdown files, you can modify the styling template in the `convert_markdown_to_html()` function inside `convert_to_pdf.py`.

## Supported Markdown Features

- Headers (H1-H6)
- Bold, italic, strikethrough
- Links and images
- Ordered and unordered lists
- Task lists (- [ ] and - [x])
- Code blocks (with triple backticks)
- Inline code
- Tables
- Blockquotes
- Horizontal rules

## Requirements

- Python 3.6+
- markdown2 >= 2.4.0
- weasyprint >= 60.0

## Troubleshooting

### Import Errors

If you see import errors, make sure dependencies are installed:

```bash
pip install markdown2 weasyprint
```

### Font Issues

WeasyPrint requires system fonts. On Linux, you may need to install font packages:

```bash
# Ubuntu/Debian
sudo apt-get install fonts-liberation

# Fedora
sudo dnf install liberation-fonts
```

### Large Files

For very large files, the conversion may take some time. The script will display progress messages.

## Technical Details

- **Markdown Processing**: Uses `markdown2` library with extras for enhanced features
- **PDF Generation**: Uses `weasyprint` library for high-quality PDF rendering
- **HTML Template**: Auto-generates a complete HTML document from Markdown with embedded CSS

## License

This script is provided as-is for use in your projects.

## Contributing

Feel free to modify and extend the script for your needs. Common customizations:

1. Add custom CSS themes
2. Support additional input formats
3. Add page numbering or headers/footers
4. Include table of contents generation
5. Add watermarks or branding

## Version

Current version: 1.0.0
