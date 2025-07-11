# Python Wrapper for Eterna 3.30

This Python script provides a simple interface to execute the Eterna prediction tool (Windows `.exe` file) from the command line.

## 📁 Installation & Setup

To use this wrapper correctly:

- Place the contents of this repository directly under the `C:\` directory.
- Rename the main folder from `eterna_wrapper` to `eterna33`.

After setup, your folder structure should look like:

````markdown
C:\
└── eterna33\
    ├── main.py
    ├── predict.exe
    └── sites\
````


### 🐧 Running on Ubuntu (via Wine)

This wrapper has also been tested on **Ubuntu using Wine**.

In this case:

- Place the files under `/home/your-user/.wine/drive_c/eterna33/`
- Refer to the Wine documentation to confirm the correct location of your `C:\` drive.

## 🚀 Running the Prediction Script

### Full Syntax:
```bash
python3 main.py --sitename=PARIS --startdate=01/01/2024 --enddate=10/01/2024 --samplerate=10
```

### Shorthand Syntax:
```bash
python3 main.py -s PARIS -sd 01/01/2024 -ed 10/01/2024 -sr=10
```


**_Note: Ensure the sites folder is correctly set up.
An example sites folder is included in this repository. You will need to configure your site-specific parameters similarly to how you would with the stock Eterna tool.
_**

## 🛠 Dependencies

Python >= 3.6
Wine (required for Linux users)
