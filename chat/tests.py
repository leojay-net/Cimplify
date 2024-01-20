# import requests
# from io import BytesIO
# from pypdf import PdfReader

# url = "https://cimpliffy.com/admin/files/_OceanofPDF.com_How_Spies_Think__Ten_Lessons_in_Intelligen_-_David_Omand.pdf#toolbar=0"
 
# # Requests URL and get response object
# response = requests.get(url)
# bytes_stream = BytesIO(response.content)
# pdf_loader = PdfReader(bytes_stream)
# # pages = pdf_loader.load_and_split()
# context = "\n\n".join(str(p.extract_text()) for p in pdf_loader.pages)
# print(context)

