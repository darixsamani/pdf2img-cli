from pdf2img_cli.pdf2img import Pdf2Img


def main(pdf, ouput):
    
	pdf2img = Pdf2Img(pdf, ouput)
	pdf2img.to_image()