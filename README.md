# OpenCV Pose Detection
### Simple pose detection with OpenCV
Requires camera, webcam or similar.

<hr>

Very simple implementation of OpenCV Pose Detection done from documentation
<br>
Overlays the nodes on the camera image


![Screenshot](screenshot.jpg?raw=true "App window")

<hr>

Open a command prompt and `cd` to a new directory of your choosing:

(optional; recommended) Create a virtual environment with:
```
python -m venv "venv"
venv\Scripts\activate
```

To install do:
```
git clone https://github.com/vluz/CVPoseDetect.git
cd CVPoseDetect
pip install -r requirements.txt
```

On first run it may download several models.
<br>
It will take quite some time, both on reqs above and on first run.
<br>
Please allow it time to finish.
<br>
All runs after the first are then faster to load.

To run do:<br>
`python posedetect.py` 


Note: Do not use this for production, it's untested
