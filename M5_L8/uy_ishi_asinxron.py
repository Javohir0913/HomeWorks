import fitz
from PIL import Image
import asyncio
import os
from concurrent.futures import ThreadPoolExecutor

pdf_folder = os.getcwd()
output_folder = os.path.join(os.getcwd(), "output_images")
os.makedirs(output_folder, exist_ok=True)


def convert_pdf_to_images(pdf_path, output_folder,pdf_file):
    pdf_document = fitz.open(pdf_path)
    num_pages = pdf_document.page_count
    print(f"{pdf_path} ichida: {num_pages} sahifa")
    for page_number in range(num_pages):
        page = pdf_document.load_page(page_number)
        image_list = page.get_pixmap()
        image = Image.frombytes("RGB", [image_list.width, image_list.height], image_list.samples)
        image.save(os.path.join(output_folder, f"{pdf_file.replace(".pdf", "")}_page_{page_number + 1}.jpg"))
    pdf_document.close()


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as executor:
        tasks = []
        for pdf_file in os.listdir(pdf_folder):
            if pdf_file.endswith(".pdf"):
                task = loop.run_in_executor(executor, convert_pdf_to_images, pdf_file, output_folder,pdf_file)
                tasks.append(task)
        for i in tasks:
            await i


if __name__ == '__main__':
    asyncio.run(main())