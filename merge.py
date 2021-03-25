import os
import PyPDF2
import argparse


def get_file_name(file_dir):
    file_list = [os.path.join(root, files_path)
                 for root, dirs, files in os.walk(file_dir)
                 for files_path in files
                 if str(files_path).endswith('pdf')
                 ]
    return file_list if file_list else []


def merge_pdf(file_path, outfile):
    output = PyPDF2.PdfFileWriter()
    output_pages = 0
    pdf_file_name = get_file_name(file_path)

    if pdf_file_name:
        for pdf_file in pdf_file_name:
            input_pdf = PyPDF2.PdfFileReader(open(pdf_file, "rb"))
            page_count = input_pdf.getNumPages()
            output_pages += page_count
            print("from:%s - %d page(s)" % (pdf_file, page_count))

            for iPage in range(page_count):
                output.addPage(input_pdf.getPage(iPage))

        print("to:%s - %d page(s)" % (outfile, output_pages))
        output_stream = open(outfile, "wb")
        output.write(output_stream)
        output_stream.close()
        print("done the PDF merge.")
    else:
        print("no PDF files for merge！")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='merge PDF files from a directory')
    parser.add_argument('-i', action='store', dest='input', help='the directory for merge')
    parser.add_argument('-o', action='store', dest='output', help='the file for merged PDF')
    args = parser.parse_args()

    merge_pdf(args.input, args.output)
