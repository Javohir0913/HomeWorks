import subprocess
from time import perf_counter
start = perf_counter()

output_folder = "C:\\Users\\user\\Desktop\\python\\5-oy\\test"
for i in range(1, 11):
    pdf_url = "https://multimediya.uz/e-kitob/index.php?mavzu=" + str(i)
    command = f'"C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage" "{pdf_url}" "{output_folder}/{i}.jpg"'
    subprocess.call(command, shell=True)

end = perf_counter()
print(f"{end - start:.3f}")
# 30.884