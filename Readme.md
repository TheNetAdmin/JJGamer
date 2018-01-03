# Jump-Jump auto Gamer

## Introduction

The auto gamer of Wechat's Jump-Jump game, written in python, with opencv-python.

## Usage

1. Install **adb** tool, connect your Android phone via USB port, execute `adb devices` to connect the adb to Android.
1. Create device specification script under *Devices* folder, `SamsungS8.py` for example.
1. Describe the device specification in your device script, change the import in `Gamer.py` from `SonyXZ` to your device.
1. Run the script `Gamer.py` with python3.

## Dependency

Install these dependencies via `pip`:
  - opencv-python
  - matplotlib
  - numpy

## License
![license](https://img.shields.io/github/license/mashape/apistatus.svg)

This project is released under MIT License.