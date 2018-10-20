import yaml
from boundingbox import start_inference

def main():

	IP = None
	WEIGHT_DIRECTORY = None

	with open("settings.yaml",'r') as stream:
		try:
			settings = yaml.load(stream)
			if ('IP' not in settings):
				raise ValueError("IP not listed in settings.yaml")
			if ('WEIGHT_DIRECTORY' not in settings):
				raise ValueError("WEIGHT_DIRECTORY not listed in settings.yaml")

			IP = settings['IP']
			WEIGHT_DIRECTORY = settings['WEIGHT_DIRECTORY']

			printf("Starting inference with ip "  + IP +  " and weight directory " + WEIGHT_DIRECTORY)
			
			start_inference(IP,WEIGHT_DIRECTORY);

		except yaml.YAMLError as exc:
			print(exc)

if __name__ == "__main__":
	main();