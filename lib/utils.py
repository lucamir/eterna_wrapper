from shutil import copy
from os import remove, makedirs, path
from datetime import datetime
from typing import Optional
from glob import glob

from lib.constants import COMMDAT_PATH

def clear_uft() -> None:
    paths = glob(COMMDAT_PATH + '/*.uft')
    for _path in paths:
        delete_file(_path)

def move_file(_from, _to) -> None:
    makedirs(path.dirname(_to), exist_ok=True)
    copy(_from, _to)
    remove(_from)

def copy_file(_from, _to) -> None:
    copy(_from, _to)

def delete_file(_path) -> None:
    remove(_path)

def detect_datetime_format(string) -> Optional[str]:
    formats_to_try = [
        "%Y-%m-%d", "%y-%m-%d",
        "%d-%m-%Y", "%d-%m-%y",
        "%m-%d-%Y", "%m-%d-%y",
        "%d/%m/%Y", "%d/%m/%y",
        "%m/%d/%Y", "%m/%d/%y",
        "%Y/%m/%d", "%y/%m/%d"
    ]

    for dt_format in formats_to_try:
        try:
            _ = datetime.strptime(string, dt_format)
            return dt_format
        except ValueError:
            pass
    return None
