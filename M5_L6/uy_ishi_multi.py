import pdfkit
from time import time_ns
import threading

def convert_to_pdf(url, pdf_filename, config):
    pdfkit.from_url(url, pdf_filename, configuration=config)


path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)
start_time = time_ns() // 1_000_000

threads = []

for i in range(1, 13):
    url = "https://multimediya.uz/multimediya/index.php?mavzu=" + str(i)
    pdf_filename = str(i) + '.pdf'
    t = threading.Thread(target=convert_to_pdf,args=(url, pdf_filename, config))
    threads.append(t)
    t.start()

for i in threads:
    t.join()

end = time_ns() // 1_000_000

print(end - start_time) #SINGEL(43052) - MULTI(15693) = 27359