#!/usr/bin/env python3
"""
PDF Converter - Convert Markdown and HTML files to PDF

This script provides a simple command-line interface to convert
Markdown (.md) and HTML (.html) files to PDF format.

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

    # Wrap in a basic HTML template with styling
    # Using Devonshire branding standards
    full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        /* Body Text: Georgia, Regular */
        body {{
            font-family: Georgia, 'Times New Roman', serif;
            line-height: 1.2;
            color: #333;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
        }}

        /* Headers H1, H2: Times New Roman, Bold, Small Caps */
        h1, h2 {{
            font-family: 'Times New Roman', Times, serif;
            font-weight: bold;
            font-variant: small-caps;
            color: #14213D;
            margin-top: 24px;
            margin-bottom: 16px;
            line-height: 1.25;
        }}
        h1 {{ font-size: 2em; border-bottom: 2px solid #14213D; padding-bottom: 0.3em; }}
        h2 {{ font-size: 1.5em; border-bottom: 1px solid #14213D; padding-bottom: 0.3em; }}

        /* Headers H3-H6: Georgia (body font) */
        h3, h4, h5, h6 {{
            font-family: Georgia, 'Times New Roman', serif;
            font-weight: 600;
            margin-top: 24px;
            margin-bottom: 16px;
            line-height: 1.25;
        }}
        h3 {{ font-size: 1.25em; }}
        h4 {{ font-size: 1.1em; }}
        h5 {{ font-size: 1em; }}
        h6 {{ font-size: 0.9em; }}

        /* Quotes/Callouts: Times New Roman Italic, 12pt */
        blockquote {{
            font-family: 'Times New Roman', Times, serif;
            font-style: italic;
            font-size: 12pt;
            margin: 1em 0;
            padding: 0 1em;
            color: #333;
            border-left: 0.25em solid #14213D;
        }}

        /* Captions & Footnotes: Georgia Italic, 10pt */
        figcaption, caption, .caption, small, .footnote {{
            font-family: Georgia, 'Times New Roman', serif;
            font-style: italic;
            font-size: 10pt;
            color: #555;
        }}

        /* Code blocks */
        code {{
            background-color: #f6f8fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 85%;
        }}
        pre {{
            background-color: #f6f8fa;
            padding: 16px;
            border-radius: 6px;
            overflow: auto;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
        }}

        /* Tables */
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
        }}
        table th, table td {{
            border: 1px solid #dfe2e5;
            padding: 6px 13px;
            font-family: Georgia, 'Times New Roman', serif;
        }}
        table th {{
            background-color: #f6f8fa;
            font-weight: 600;
        }}
        table caption {{
            font-family: Georgia, 'Times New Roman', serif;
            font-style: italic;
            font-size: 10pt;
            color: #555;
            margin-bottom: 8px;
        }}

        /* Images */
        img {{
            max-width: 100%;
        }}

        /* Links */
        a {{
            color: #14213D;
            text-decoration: none;
        }}
        a:hover {{
            text-decoration: underline;
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
        description='Convert Markdown or HTML files to PDF',
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
        version='%(prog)s 1.0.0'
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
