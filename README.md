# Wrapper python for Eterna 3.30.
This Python script provides a simple interface for running the Eterna prediction Windows .exe file.

To use this wrapper, the contents of this repository must be placed under the `C:\\` path. Additionally, rename the main folder from eterna_wrapper to eterna33.

Once the files are in the correct location, open a terminal window and run the following command:

**_Note: This code has also been tested on Ubuntu with Wine installed!_**

For Ubuntu, the only difference is the path where the folder needs to be placed. Instead of placing it under `C:\\`, it should go under `/home/user/.wine/drive_c/`. 
Refer to the Wine documentation to determine the correct location of the `C:\\` equivalent folder.

Command to Run the Prediction Script

Full command syntax:
```sh
python3 .\main.py --sitename=PARIS --startdate=01/01/2024 --enddate=10/01/2024 --samplerate=10
```

Or in shorthand form:
```sh
python3 .\main.py -s PARIS -sd 01/01/2024 -ed 10/01/2024 -sr=10
```

**_Note: Ensure you have the sites folder set up. An example sites folder is included in this repository. You will need to configure the parameters according to your use case, similar to how you would use the stock Eterna tool._**
