from os import rename, remove
from os.path import join
from subprocess import run

#### Edit these globals
PROJECT_NAME = input("Project Name: ")
PROJECT_VERSION = "0.0.1"
PROJECT_AUTHOR = input("Author Name: ")
PROJECT_DESCRIPTION = input("Project Description: ")
####



PROJECT_NAME_STR = "TEMPLATE_NAME"
PROJECT_VERSION_STR = "VERSION_NUMBER"
PROJECT_AUTHOR_STR = "AUTHOR_NAME"
PROJECT_DESCRIPTION_STR = "TEMPLATE_DESCRIPTION"

SOLUTION_CMD = "xmake project -k vsxmake"
BUILD_CMD = "xmake build"


def update_xmake():
    with open("xmake.lua", "r", encoding="utf-8") as file:
        xmake = file.read()

    if PROJECT_NAME:
        xmake = xmake.replace(PROJECT_NAME_STR, PROJECT_NAME)
    if PROJECT_VERSION:
        xmake = xmake.replace(PROJECT_VERSION_STR, PROJECT_VERSION)
    if PROJECT_AUTHOR:
        xmake = xmake.replace(PROJECT_AUTHOR_STR, PROJECT_AUTHOR)
    if PROJECT_DESCRIPTION:
        xmake = xmake.replace(PROJECT_DESCRIPTION_STR, PROJECT_DESCRIPTION)

    with open("xmake.lua", "w", encoding="utf-8") as file:
        file.write(xmake)


def update_ini():
    rename(
        join("contrib", "config", "PluginName.ini"),
        join("contrib", "config", f"{PROJECT_NAME}.ini"),
    )


def update_settings():
    with open(join("src", "Settings.cpp"), "r", encoding="utf-8") as f:
        settings_cpp = f.read()

    settings_cpp = settings_cpp.replace("PluginName.ini", f"{PROJECT_NAME}.ini")

    with open(join("src", "Settings.cpp"), "w", encoding="utf-8") as f:
        f.write(settings_cpp)


def run_commands():
    run(SOLUTION_CMD, shell=True)
    run(BUILD_CMD, shell=True)


def main():
    update_xmake()
    update_ini()
    update_settings()
    run_commands()
    remove(__file__)


if __name__ == "__main__":
    main()
