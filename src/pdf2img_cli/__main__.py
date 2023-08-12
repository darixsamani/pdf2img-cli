import argparse
from . import main


	
parser = argparse.ArgumentParser(description='This is CLI for simple paragraph recoginitive based on morphological operator')
		
parser.add_argument('--pdf', type=str, help="""Entrer le pdf  que tu souhaites extrait les images""")

parser.add_argument('--ouput', type=str, help="""Entrer le dossier ou l'on mettre les images""")
		
args = parser.parse_args()

if __name__ == '__main__':


	main(args.pdf, args.ouput)