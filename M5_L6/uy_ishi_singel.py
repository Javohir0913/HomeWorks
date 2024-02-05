import pdfkit
from time import time_ns

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

config = pdfkit.configuration(wkhtmltopdf = path_wkhtmltopdf)

start_time = time_ns() // 1_000_000

for i in range(1, 13):
    pdfkit.from_url("https://multimediya.uz/multimediya/index.php?mavzu="+str(i),
                    str(i)+".pdf", configuration=config)

end = time_ns() // 1_000_000

print(end - start_time) #43052