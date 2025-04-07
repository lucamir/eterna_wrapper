# Wrapper python for Eterna 3.30.
This Python script provides a simple interface for executing the Eterna prediction Windows .exe file.

To use this wrapper, the contents of the repository must be placed under the `C:\\` directory. Additionally, the main folder should be renamed from eterna_wrapper to eterna33.

Once the files are in the correct location, a terminal window should be opened and the following command executed.

**Note: This code has also been tested on Ubuntu using Wine.**

For Ubuntu, the only difference lies in the folder path. Instead of placing it under `C:\\`, it should be placed under `/home/user/.wine/drive_c/`. 
Refer to the Wine documentation to determine the correct equivalent path for the `C:\\` drive.

### Command to Run the Prediction Script

Full command syntax:
```sh
python3 .\main.py --sitename=PARIS --startdate=01/01/2024 --enddate=10/01/2024 --samplerate=10
```

Or in shorthand form:
```sh
python3 .\main.py -s PARIS -sd 01/01/2024 -ed 10/01/2024 -sr=10
```

**_Note: Ensure you have the sites folder set up. An example sites folder is included in this repository. You will need to configure the parameters according to your use case, similar to how you would use the stock Eterna tool._**
