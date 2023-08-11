from pathlib import Path
from pdf2image import convert_from_path, convert_from_bytes

class Pdf2Img:

    def __init__(self, pdf, ouput) -> None:
        self.pdf = Path(pdf)
        self.output = Path(ouput)
    

    def extrat_image(self):
        self.images = convert_from_path(self.pdf)

    def to_image(self):
        self.extrat_image()
        for page,i in zip(self.images,range(len(self.images)+1)):
            name_pdf = self.pdf.name.split('.')[0]
            if not self.output.is_dir():
                self.output.mkdir(parents=True, exist_ok=True)
                
            name = self.output / name_pdf
            
            page.save(f"./{name}_{i}.png", 'JPEG')
            print(f"save image : ./{name}_{i}.png")