import subprocess
from multiprocessing import Pool
from time import perf_counter

def convert_pdf_to_image(pdf_url):
    output_folder = "C:\\Users\\user\\Desktop\\python\\5-oy\\test"
    pdf_number = pdf_url.split("=")[-1]
    output_file = f"{output_folder}/{pdf_number}.jpg"
    command = f'"C:/Program Files/wkhtmltopdf/bin/wkhtmltoimage" "{pdf_url}" "{output_file}"'
    subprocess.call(command, shell=True)

if __name__ == "__main__":
    start = perf_counter()

    urls = [f"https://multimediya.uz/e-kitob/index.php?mavzu={i}" for i in range(1, 11)]

    with Pool(processes=4) as pool:
        pool.map(convert_pdf_to_image, urls)

    end = perf_counter()
    print(f"Conversion completed in {end - start:.3f} seconds.")
    # 18.533                    #30.884 - 18.533 = 12.351