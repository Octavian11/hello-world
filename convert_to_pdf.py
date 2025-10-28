#!/usr/bin/env python3
"""
PDF Converter - Convert Markdown and HTML files to PDF

This script provides a simple command-line interface to convert
Markdown (.md) and HTML (.html) files to PDF format with
professional Private Equity investment communication formatting.

Dependencies:
    - markdown2: For converting Markdown to HTML
    - weasyprint: For converting HTML to PDF

Usage:
    python convert_to_pdf.py input_file.md [output_file.pdf]
    python convert_to_pdf.py input_file.html [output_file.pdf]
"""

import argparse
import sys
from pathlib import Path

try:
    import markdown2
except ImportError:
    print("Error: markdown2 is not installed. Run: pip install markdown2")
    sys.exit(1)

try:
    from weasyprint import HTML, CSS
except ImportError:
    print("Error: weasyprint is not installed. Run: pip install weasyprint")
    sys.exit(1)


def convert_markdown_to_html(markdown_content):
    """Convert Markdown content to HTML."""
    html_content = markdown2.markdown(
        markdown_content,
        extras=[
            'fenced-code-blocks',
            'tables',
            'header-ids',
            'task_list',
            'strike',
            'code-friendly'
        ]
    )

    # Wrap in a professional HTML template with PE-standard styling
    # Using Devonshire Partners - Independent Sponsor Brand Palette
    full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        /* Devonshire Partners Brand Palette Colors:
           Primary: #14213D (Midnight Blue) - Authority, intelligence, institutional strength
           Secondary: #3A3A3A (Graphite Gray) - Precision, sophistication, modern professionalism
           Accent: #B8860B (Royal Gold) - Performance, excellence, ambition
           Neutral: #FFFFFF (White) - Clean backgrounds
           Support: #43617D (Steel Blue) - Charts, gradient accents, digital highlights
        */

        /* Professional Document Layout - PE Investment Communication Standards */
        @page {{
            size: letter;
            margin: 0.75in 1in;
        }}

        /* Body Text: Georgia, 11pt - Professional Standard */
        body {{
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 11pt;
            line-height: 1.8;
            color: #000000;
            background-color: #FFFFFF;
            max-width: none;
            margin: 0;
            padding: 0;
        }}

        /* H1: Cover Page / Document Title */
        h1 {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 28pt;
            font-weight: bold;
            color: #14213D;
            text-align: center;
            margin: 2.5in 0 0.5in 0;
            padding: 0;
            line-height: 1.3;
            letter-spacing: 0.5px;
            border: none;
            page-break-after: always;
        }}

        /* H2: Section Headers */
        h2 {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 16pt;
            font-weight: bold;
            color: #14213D;
            margin: 36pt 0 18pt 0;
            padding: 0 0 8pt 0;
            border-bottom: 2px solid #14213D;
            line-height: 1.3;
            letter-spacing: 0.3px;
            page-break-after: avoid;
        }}

        /* H3: Subsection Headers */
        h3 {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 13pt;
            font-weight: bold;
            color: #43617D;
            margin: 24pt 0 12pt 0;
            padding: 0;
            line-height: 1.3;
            page-break-after: avoid;
        }}

        h4 {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 12pt;
            font-weight: bold;
            color: #3A3A3A;
            margin: 18pt 0 10pt 0;
        }}

        h5, h6 {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 11pt;
            font-weight: bold;
            color: #3A3A3A;
            margin: 14pt 0 8pt 0;
        }}

        /* Paragraphs */
        p {{
            margin: 0 0 12pt 0;
            text-align: justify;
            orphans: 3;
            widows: 3;
        }}

        /* Lists - Professional PE Style */
        ul, ol {{
            margin: 12pt 0 18pt 0;
            padding-left: 28pt;
        }}

        li {{
            margin: 0 0 8pt 0;
            line-height: 1.6;
        }}

        ul {{
            list-style-type: disc;
        }}

        ul ul {{
            list-style-type: circle;
            margin-top: 6pt;
        }}

        /* Horizontal Rules - Section Dividers */
        hr {{
            border: none;
            border-top: 1px solid #CCCCCC;
            margin: 24pt 0;
            page-break-after: avoid;
        }}

        /* Blockquotes - Executive Callouts */
        blockquote {{
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 11pt;
            font-style: italic;
            margin: 18pt 0 18pt 28pt;
            padding: 14pt 20pt;
            color: #14213D;
            background-color: #F8F9FA;
            border-left: 4px solid #B8860B;
            page-break-inside: avoid;
        }}

        /* Strong/Bold - Key Metrics and Emphasis */
        strong, b {{
            color: #14213D;
            font-weight: bold;
        }}

        /* Emphasis */
        em, i {{
            color: #000000;
            font-style: italic;
        }}

        /* Code blocks - Financial Data / Metrics */
        code {{
            background-color: #F8F9FA;
            padding: 2pt 6pt;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 10pt;
            color: #3A3A3A;
        }}

        pre {{
            background-color: #F8F9FA;
            padding: 14pt;
            border-radius: 4px;
            border-left: 3px solid #43617D;
            margin: 16pt 0;
            overflow-x: auto;
            page-break-inside: avoid;
        }}

        pre code {{
            background-color: transparent;
            padding: 0;
        }}

        /* Tables - Professional Financial Tables */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 18pt 0;
            page-break-inside: avoid;
        }}

        table th, table td {{
            border: 1px solid #CCCCCC;
            padding: 10pt 14pt;
            font-family: Georgia, 'Times New Roman', serif;
            text-align: left;
            vertical-align: top;
        }}

        table th {{
            background-color: #14213D;
            color: #FFFFFF;
            font-weight: bold;
            font-family: 'Times New Roman', Times, serif;
            font-size: 11pt;
        }}

        table caption {{
            font-family: Georgia, 'Times New Roman', serif;
            font-style: italic;
            font-size: 10pt;
            color: #3A3A3A;
            margin-bottom: 10pt;
            text-align: left;
        }}

        /* Links - Professional Style */
        a {{
            color: #14213D;
            text-decoration: none;
        }}

        a:hover {{
            color: #B8860B;
            text-decoration: underline;
        }}

        /* Images */
        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 18pt auto;
        }}

        /* Captions & Footnotes */
        figcaption, caption, .caption, small, .footnote {{
            font-family: Georgia, 'Times New Roman', serif;
            font-style: italic;
            font-size: 9pt;
            color: #3A3A3A;
            line-height: 1.4;
        }}

        /* Page breaks */
        .page-break {{
            page-break-before: always;
        }}

        /* Avoid breaks after headings */
        h1, h2, h3, h4, h5, h6 {{
            page-break-after: avoid;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""
    return full_html


def convert_html_to_pdf(html_content, output_path):
    """Convert HTML content to PDF."""
    HTML(string=html_content).write_pdf(output_path)


def convert_file_to_pdf(input_path, output_path=None):
    """
    Convert a Markdown or HTML file to PDF.

    Args:
        input_path: Path to the input file (.md or .html)
        output_path: Path to the output PDF file (optional)

    Returns:
        Path to the generated PDF file
    """
    input_path = Path(input_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    # Determine output path if not specified
    if output_path is None:
        output_path = input_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path)

    # Read input file
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Convert based on file type
    if input_path.suffix.lower() == '.md':
        print(f"Converting Markdown file: {input_path}")
        html_content = convert_markdown_to_html(content)
    elif input_path.suffix.lower() in ['.html', '.htm']:
        print(f"Converting HTML file: {input_path}")
        html_content = content
    else:
        raise ValueError(f"Unsupported file type: {input_path.suffix}. Use .md, .html, or .htm")

    # Convert to PDF
    print(f"Generating PDF: {output_path}")
    convert_html_to_pdf(html_content, output_path)

    print(f"✓ Successfully created: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown or HTML files to PDF with professional PE formatting',
        epilog='Examples:\n'
               '  %(prog)s README.md\n'
               '  %(prog)s document.md output.pdf\n'
               '  %(prog)s page.html report.pdf',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        'input',
        help='Input file (.md or .html)'
    )

    parser.add_argument(
        'output',
        nargs='?',
        help='Output PDF file (optional, defaults to input filename with .pdf extension)'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 2.0.0'
    )

    args = parser.parse_args()

    try:
        convert_file_to_pdf(args.input, args.output)
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
