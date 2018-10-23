
![AI Society](https://avatars1.githubusercontent.com/u/27787344?s=200&v=4)
# Facial Recognition Design Project


## Installation

#### Virtual Environment

It is recommended to create a python virtualenv to manage dependencies before running to make sure packages from different projects do not interfere with each other. You can install virtualenv via

`pip3 install virtualenv`

To build a virtualenv in your current project directory run 

`python3 -m virtualenv env`

To start the virtual environment, run the following command:

`source env/bin/activate`

#### Requirements

Install dependencies by running  `pip3 install -r requirements.txt`

#### Facenet

#### Settings
A `settings.yaml` file must be included in the same directory as main.py before running the script. 
An example template is as follows:

```
IP: <INSERT_CAMERA_IP_HERE>
WEIGHT_DIRECTORY: <INSERT_DIRECTORY_HERE>
FRAME_PREVIEW: OFF 
```

## Running
After editing the `settings.yaml` file with your webcam IP and weight directory, simply run `python3 main.py` and ensure your ip camera is properly streaming.
