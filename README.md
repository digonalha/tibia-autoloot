# Tibia Autoloot - Python 3.7.x
Simple script for autoloot around the character with only one click and super fast! 

_Disclaim:
All my scripts are made linux based. Im using Xubuntu 18.4, but probably they will work with Windows too with some changes. If you need some help, please contact me sending an issue. And hey, I will encourage code improvements too, feel free to send me a pull request anytime!_

## Requirements:
To work, you only need install pynput lib. To install just run

> ~$ pip install pynput==1.4

or install by requirements.txt running

> pip install -r requirements.txt

For reference: https://pythonhosted.org/pynput/

## How to:
To get the mouse positions, run the script _get_mouse_position.py_ (the script have a 1sec cooldown, put the mouse on position and run. The script will print on shell the current mouse position) and replace in positions list at line #10.

![image](https://user-images.githubusercontent.com/21348986/52380561-67964980-2a55-11e9-90b0-e3406d279c67.png)

 All done, then just make the script an executable file with

> chmod +x autoloot.py 

and use the 'Keyboard > Apps Shorcuts' to create a command shortcut. The command will be like that:

> /bin/bash -c "/path/to/file/autoloot.py" 

and make the shortcut of your choice.


