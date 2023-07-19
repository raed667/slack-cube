# Slack Cube

## Introduction

Slack Cube is a physical cube that you keep on your desk. And when you place a specific side up, it updates your Slack status.

![Slack Cube](/img/cube.jpg)

## Bill of materials

![BBC micro:bit Go](/img/mb-go.webp)

One BBC micro:bit (v2) - 20$

One hollow wooden cube (12cm x 12cm x 12cm) - 6$

You will need access to the BBC micro:bit code editor [MakeCode](https://makecode.microbit.org/).

On your local machine, you'll need Python 3 installed and a code editor. 

PS: I only tested this project on a MacBook Pro M1 (MacOS 13.3) with Python 3.11.4

## Getting started

### Emitter: microcomputer

Plug your board using a USB port to the laptop and open [MakeCode](https://makecode.microbit.org/). Then create a new project called "Slack Cube" and leave other parameters as is.

Then drag and drop the file `microbit/microbit-Slack-Cube.hex` into the editor window. This will import the project in its 3 forms (Blocks, Python and JavaScript). 

![MakeCode](https://github.com/raed667/slack-cube/assets/1442690/3eac54d6-0483-410a-b9cd-6438a22da06a)

Click "Download", to download the code into your micro:bit board and follow the instructions. 

Finally disconnect the board from the laptop, place it into the cube and power it through the AAA batteries.

Press the `B` button on the micro:bit board to toggle data transmission.

### Receiver: laptop bluetooth

In the file `laptop/receiver.py` you'll need to setup the Slack API token (`token`) and the user-id (`user`). Follow the instructions included in the file.

In the `laptop` directory run the following command to install the dependencies: 

```sh
pip install -r requirements.txt
```

Then to run the script

```sh
python receiver.py
```

You can change which emoji is shown by modifying the values in the function `select_emoji()`.

## Notes

- You don't need such a large cube but the minimum recommended dimensions are 6cm x 6cm x 6cm .
- This could be achieved cheaper by using an Arduino or an ESP32 or any number of solutions. I just happened to have this hardware laying around.
- The receiver waits 5 seconds before calling the Slack API to make sure no accidental movements trigger an unwanted change.
- I just duct-taped the board to the inner wall of the cube. It seems to hold pretty well. The batteries are fixed likewise using UHU patafix.
