import PyPDF2

# Create a PdfFileMerger object
pdf_merger = PyPDF2.PdfFileMerger()

# Open the two PDF files
pdf_file_1 = open("file_1.pdf", "rb")
pdf_file_2 = open("file_2.pdf", "rb")

# Create PdfFileReader objects for the two PDF files
pdf_reader_1 = PyPDF2.PdfFileReader(pdf_file_1)
pdf_reader_2 = PyPDF2.PdfFileReader(pdf_file_2)

# Add the pages from the two PDF files to the PdfFileMerger object
pdf_merger.append(pdf_reader_1)
pdf_merger.append(pdf_reader_2)

# Close the two PDF files
pdf_file_1.close()
pdf_file_2.close()

# Write the merged PDF file to a new file
pdf_merger.write("merged.pdf")
