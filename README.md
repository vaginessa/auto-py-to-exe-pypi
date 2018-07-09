<h1 align="center">Auto PY to EXE</h1>
<p align="center">A .py to .exe converter using a simple graphical interface built using <a href="https://github.com/ChrisKnott/Eel">Eel</a> and <a href="http://www.pyinstaller.org/">pyinstaller</a> in Python.</p>

<div align="center">
    <img src="https://i.imgur.com/EuUlayC.png" alt="Empty interface">
</div>

## Installation

### Prerequisites
 - Python : Python 2.7, 3.3 - 3.6
 - Chrome : to run the user interface in; eel uses this (app mode)

### Via [PyPI](https://pypi.org/project/auto-py-to-exe/)
```
$ pip install auto-py-to-exe
```

### Via [GitHub](https://github.com/brentvollebregt/auto-py-to-exe)
```
$ git clone https://github.com/brentvollebregt/auto-py-to-exe.git
$ cd auto-py-to-exe
$ ./setup.py install
```

## Usage
Simply run the application by calling it in the terminal:
```
$ auto-py-to-exe
```

You can also pass a file as an argument to pre-fill the script location field:
```
$ auto-py-to-exe my_script.py
```

After you have the GUI displayed simply select your options and click convert:
1. Select your script location (paste in or use a file explorer)
    - Outline will become blue when file exists
2. Select other options and add things like an icon or other files
3. Click the big blue button at the bottom to convert
4. Find your converted files in /output when completed

## Video
If you need something visual to help you get started, [I made a video for the original release of this project](https://youtu.be/OZSZHmWSOeM), some things may be different but the same concepts still apply.

## Screenshots
![Empty interface](https://i.imgur.com/dd0LC2n.png)
![Filled out](https://i.imgur.com/f3TEnZI.png)
![Converting](https://i.imgur.com/MjdONcC.png)
