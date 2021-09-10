# MouseAI
Future Mouse Controller with Hand

### Preview
<p align="center">
  <img src="https://drive.google.com/uc?export=view&id=1LBasydxIj6C3YOo-BYKXunWXq1TuRxWl" />
</p>

### Controller
- ForeFinger == Pointer Mouse
- Thumb == Left Click
- Little Finger == Right Click
- Expand ForeFinger and Middle Finger == Left Drag
- Expand Thumb and ForeFinger == Click Space (For Playing dino :)

## Builded With

    - OpenCV
    - Numpy
    - Autopy
    - Keyboard
    - Mediapipe

## Prerequisite
- Python 3.7.9
- Webcam or VideoCam

## How to install
1. Install python (you can refer to [Python site](https://www.python.org/downloads/))
2. (Optional) Initiate venv by running <code>python -m venv ac_env</code>
2. Install library via pip from requirements.txt by running <code>python -m pip install requirements.txt</code>
3. Adjust the settings located at the <code>./settings/</code> folder (the <code>IS_CLICK_HAND_ON</code> and <code>IS_POINTER_HAND_ON
</code> value, you need to set the value to <code>True</code> to move your mouse, or keep it to <code>False</code> if you want to check for <em>ghost click</em> first)
4. Run with <code>python main.py</code>

### Notes for installation
#### Windows
You are good to go by just following the installation, no need for additional works

#### Linux
Makesure to use <b>XOrg</b> for the display server (Ubuntu 21.04 use wayland, you need to change it first) to enable the mouse library

#### Other OS (Including Mac)
Not yet tested
