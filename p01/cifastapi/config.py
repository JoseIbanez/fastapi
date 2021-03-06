#!/usr/bin/env python
""" Get configuration for the rest of the application
"""

import json
import os

def getVersion():
    """
    Get release version
    """

    # Get version from file
    versionFile = "/etc/cifastapi/VERSION_FULL"

    try:
        with open(versionFile) as file:
            version = file.read()
    except OSError:
        return None

    return version.replace("\n","")


def getConfig(param):
    """
    Get configuration parameter
    1st try to find a ENV var
    2nd open the config file
    """

    param_env = param.replace(".","_").upper()

    #print(f"param: {param} / {param_env}")

    if os.environ.get(param_env):
        return os.environ.get(param_env)

    # Get config from file
    configFile = os.environ.get("CONFIGFILE") or "/etc/cifastapi/file.config"

    try:
        with open(configFile) as json_file:
            config = json.load(json_file)
    except OSError:
        return None
    except json.decoder.JSONDecodeError:
        return None

    value = safeget(config,param.split("."))

    return value


def safeget(dct, keys):
    """
    Get a nested value in a json file
    Only nested dict is supported, no lists
    """
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct



if __name__ == "__main__":


    print("USER: "+getConfig("USER"))
    print("user: "+getConfig("user"))

    print(f"user.1: {getConfig('user.1')}")
    print(f"user.2: {getConfig('user.2')}")
