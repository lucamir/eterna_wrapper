
from shutil import copy
from os import remove, makedirs, path
from datetime import datetime
from typing import Optional
from glob import glob

from lib.constants import COMMDAT_PATH

def clear_uft() -> None:
    """
    Remove all files with a .uft extension from the COMMDAT_PATH directory.

    This function searches for all files with a .uft extension within the
    specified directory and deletes each one. It is primarily used to
    prevent errors related to unwanted files remaining in the system.

    Returns
    -------
    None
    """
    paths = glob(COMMDAT_PATH + '/*.uft')
    for _path in paths:
        delete_file(_path)

def move_file(_from, _to) -> None:
    """
    Move a file from one location to another.

    Parameters
    ----------
    _from : str
        The path of the file to be moved.
    _to : str
        The path to move the file to.

    Returns
    -------
    None
    """
    makedirs(path.dirname(_to), exist_ok=True)
    copy(_from, _to)
    remove(_from)

def copy_file(_from, _to) -> None:
    """
    Copy a file from one location to another.

    Parameters
    ----------
    _from : str
        The path of the file to be copied.
    _to : str
        The path to copy the file to.

    Returns
    -------
    None
    """
    copy(_from, _to)

def delete_file(_path) -> None:
    """
    Deletes a file.

    Parameters
    ----------
    _path : str
        The path of the file to be deleted.

    Returns
    -------
    None
    """
    remove(_path)

def detect_datetime_format(string) -> Optional[str]:
    """
    Detects the datetime format from a given string.

    Given a string, detect the datetime format used in the string. The
    function will try to parse the string using different datetime formats
    and return the format that was successfully parsed.

    The formats that are tried are:
    - "%Y-%m-%d", "%y-%m-%d",
    - "%d-%m-%Y", "%d-%m-%y",
    - "%m-%d-%Y", "%m-%d-%y",
    - "%d/%m/%Y", "%d/%m/%y",
    - "%m/%d/%Y", "%m/%d/%y",
    - "%Y/%m/%d", "%y/%m/%d"

    Parameters
    ----------
    string : str
        The string to detect the datetime format from.

    Returns
    -------
    Optional[str]
        The datetime format used in the string, or None if no format
        was detected.
    """
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
