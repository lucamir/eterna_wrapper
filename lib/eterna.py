import platform
import subprocess as sp
import re
import pandas as pd
from datetime import timedelta


def predict() -> None:
    _os = platform.system()
    if ('Linux' in _os):
        _process = sp.Popen(['wine', r'./predict.exe'])
    elif ('Windows' in _os):
        _process = sp.Popen(['cmd','/c',r'.\predict'])
    else:
        exit(-1)
    _process.wait()

def update_project(_projectpath, _sitename) -> None:
    with open (_projectpath, 'w', encoding='utf-8') as f:
        line = f"{_sitename}    "
        f.write(line)
    f.close()

def update_site_ini(_site_ini, _startdate, _enddate, _samplerate) -> None:

    # read the file and update the specified parameters
    with open(_site_ini, 'r', encoding='utf-8') as f:
        _lines = f.readlines()
        for i, line in enumerate(_lines):
            if("SAMPLERATE" in line.strip()):
                _lines[i] = f"SAMPLERATE=     {_samplerate}          # sampling interval in seconds\n"
            if("INITIALEPO" in line.strip()):
                _lines[i] = f"INITIALEPO= {_startdate.year}   {_startdate.month}  {_startdate.day}  # initia\n"
            if "PREDICSPAN" in line.strip():
                _difference = _enddate - _startdate
                _hours = (_difference.days + 1) * 24
                _lines[i] = f"PREDICSPAN=      {_hours}       # prediction time span in hours for PREDICT\n"
    f.close()

    # write the update file
    with open(_site_ini, 'w', encoding='utf-8') as f:
        f.writelines(_lines)
    f.close()

def parse_prediction(_input_path, _output_path, _samplerate=1) -> None:
    # read the file and get the data start index and the end index
    with open(_input_path, 'r', encoding='utf-8') as f:
        _lines = f.readlines()
        _start = 0
        _end = len(_lines) - 2
        for i, line in enumerate(_lines):
            if("77777777" in line.strip()):
                _start = i + 1
    f.close()

    # generate and array of arrays that contains for each row the splitted columns
    _splitted = [re.split(r'\s+', item.strip()) for item in _lines[_start:_end]]

    columns = ['Date', 'Time', 'Tide'] # columns of the dataframe
    df = pd.DataFrame(_splitted, columns=columns) # dataframe of the prediction
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d') # convert date to datetime

    _initial_datetime = df['Date'].iloc[0]
    _delta_samplerate = timedelta(seconds=_samplerate)

    df['Date'] = _initial_datetime + df.index * _delta_samplerate
    df['Tide'] = df['Tide'].astype(float)
    df['Tide'] = df['Tide'] / 10
    df = df.drop(columns=['Time']) # delete the time counter column
    df.to_csv(_output_path, index=False) # write the dataframe on the output csv file