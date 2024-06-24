import argparse
from datetime import datetime

from lib.constants import PROJECT_PATH, script_path
from lib.eterna import update_project, update_site_ini, predict, parse_prediction
from lib.utils import detect_datetime_format, copy_file, move_file, delete_file, clear_uft

def main():
    clear_uft() # delete the uft files inside the commdat for prevent error related to the hardware

    # parse arguments
    p = argparse.ArgumentParser(description='Python wrapper Eterna 3.3')
    p.add_argument("-s", "--sitename", action="store", type=str, required=True, help='Name of the site')
    p.add_argument("-sd", "--startdate", action="store", type=str, required=True, help='Initial datetime of the prediction')
    p.add_argument("-ed", "--enddate", action="store", type=str, required=True, help='End datetime of the prediction')
    p.add_argument("-sr", "--samplerate", action="store", type=int, required=True, help='Sampling rate')

    _arguments = p.parse_args()
    _script_path = script_path()

    _sitename = _arguments.sitename
    _startdate = _arguments.startdate
    _enddate = _arguments.enddate
    _samplerate = _arguments.samplerate

    # detect datetime format and format date
    _startdate_format = detect_datetime_format(_startdate)
    _enddate_format = detect_datetime_format(_enddate)
    _startdate= datetime.strptime(_startdate, _startdate_format)
    _enddate = datetime.strptime(_enddate, _enddate_format)

    _startdate_str = _startdate.strftime('%Y-%m-%d')
    _enddate_str = _enddate.strftime('%Y-%m-%d')

    # processing files paths
    _sites_ini = f"{_script_path}/sites/{_sitename}/{_sitename}.ini"
    _processed_ini = f"{_script_path}/{_sitename}    .ini"
    _processed_prd = f"{_script_path}/{_sitename}    .prd"
    _predictions_prd = f"{_script_path}/predictions/{_sitename}.prd"
    _predictions_csv = f"{_script_path}/predictions/{_sitename}_{_startdate_str}_{_enddate_str}_{_samplerate}s.csv"

    update_project(PROJECT_PATH, _sitename) # add to the project file the name of the ini file to laod.
    update_site_ini(_sites_ini, _startdate, _enddate, _samplerate) # update the ini with the params that you set as arguments
    copy_file(_sites_ini, _processed_ini) # copy the ini file to the project's root folder
    predict() # run the prediction
    delete_file(_processed_ini) # delete the ini file from the root folder
    move_file(_processed_prd, _predictions_prd) # move the prd file into the predictions folder
    parse_prediction(_predictions_prd, _predictions_csv, _samplerate) # parse the prd file and save it as csv
    delete_file(_predictions_prd) # delete the prd file from the predictions folder

if __name__ == '__main__':
    main()