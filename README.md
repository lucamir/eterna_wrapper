# Wrapper python for Eterna 3.30.

This python code provides a simple interface to run the eterna prediction windows .exe

The content of this repository need to be placed under the `C:\\` path and renamed the main folder from "eterna_wrapper" to "eterna33".
Once the code is placed on the correct path you just need to open a terminal window and run the following command.

**NOTICE: This code was also tested on an Ubuntu OS with wine installed!**

If you are using Ubuntu the only difference is related to the path where you need to place the folder.
Instead of place the folder on `C:\\` you need to place the folder on `/home/user/.wine/drive_c/` check the wine documentation for detect the correct position of the `C:\\` equivalent folder.

Command for run the prediction script:

```sh
python3 .\main.py --sitename=PARIS --startdate=01/01/2024 --enddate=10/01/2024 --samplerate=10
```

or in short form:

```sh
python3 .\main.py -s PARIS -sd 01/01/2024 -ed 10/01/2024 -sr=10
```

**_Obviously you need to have the sites folder, you find one site example folder in this repo as example and you need to tune the params like you are using the stock eterna._**
