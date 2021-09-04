#!/usr/bin/env python3
import markdown, pdfkit
import sys, os

def get_options():
    opt = {
        'page-size': 'A4',
        'margin-top': '20mm',
        'margin-right': '20mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'encoding': "UTF-8"
    }
    return opt

def convert_file(filename):
    # Markdownのテキストを読む
    with open(filename, "rt", encoding="utf-8") as fp:
        text = fp.read()
    # HTMLに変換
    md = markdown.Markdown()
    body = md.convert(text)
    
    adir = os.path.dirname(__file__)
    with open(os.path.join(adir, "template.html")) as fp:
        tpl = fp.read()
    with open(os.path.join(adir, "style.css")) as fp:
        css = fp.read()
    html = tpl
    html = html.replace("__HTML__", body)
    html = html.replace("__CSS__", css)
    print(html)

    # PDFで出力
    outfile = filename + ".pdf"
    pdfkit.from_string(html, outfile, options=get_options())




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("[USAGES] text2pdf (file.md)")
        quit()
    convert_file(sys.argv[1])

