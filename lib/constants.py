from os import getcwd, pardir, path
from os.path import abspath, basename

# ------- DIRECTORY PATH -------
WORKING_DIRECTORY = getcwd()
PARENT_WORKING_DIRECTORY = abspath(path.join(WORKING_DIRECTORY, pardir))

# ------- PATHS -------
def script_path() -> str:
    """
    Function that return the main project directory

    Returns:
        string: Main project directory
    """
    current_dir = PARENT_WORKING_DIRECTORY
    dirnames = current_dir.split("/")
    project_folder_name = basename(WORKING_DIRECTORY)
    directory = (
        f"{PARENT_WORKING_DIRECTORY}/{project_folder_name}"
        if dirnames[-1] != f"{project_folder_name}"
        else PARENT_WORKING_DIRECTORY
    )
    return directory

PROJECT_PATH = f"{script_path()}/project"
COMMDAT_PATH = f"{script_path()}/commdat"
PREDICTIONS_PATH = f"{script_path()}/predictions"
