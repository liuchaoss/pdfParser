import pdf2docx
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='merge PDF files from a directory')
    parser.add_argument('-i', action='store', dest='input', help='the path for PDF file')
    parser.add_argument('-o', action='store', dest='output', help='the path for generated file')
    args = parser.parse_args()

    p = pdf2docx.parse(args.input, args.output)
