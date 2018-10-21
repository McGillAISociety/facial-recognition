import yaml
from boundingbox import start_inference

def main():

	IP = None
	WEIGHT_DIRECTORY = None
	FRAME_PREVIEW = False

	with open("settings.yaml",'r') as stream:
		try:
			settings = yaml.load(stream)
			if ('IP' not in settings):
				raise ValueError("IP not listed in settings.yaml")
			if ('WEIGHT_DIRECTORY' not in settings):
				raise ValueError("WEIGHT_DIRECTORY not listed in settings.yaml")
			if ('FRAME_PREVIEW' not in settings):
				raise ValueError("FRAME_PREVIEW not listed in settings.yaml")


			IP = settings['IP']
			WEIGHT_DIRECTORY = settings['WEIGHT_DIRECTORY']
			FRAME_PREVIEW = settings['FRAME_PREVIEW']


			if (IP == None): ipstr = "BUILT_IN_WEBCAM"
			else:  ipstr = IP

			print("\nSTARTING INFERENCE\n\n\tVideo Source: "  + ipstr +  "\n\tWeight Directory: " + WEIGHT_DIRECTORY + "\n" + "\tPreview: " + str(FRAME_PREVIEW) + "\n")
			
			start_inference(IP,WEIGHT_DIRECTORY,FRAME_PREVIEW);

		except yaml.YAMLError as exc:
			print(exc)

if __name__ == "__main__":
	main();
