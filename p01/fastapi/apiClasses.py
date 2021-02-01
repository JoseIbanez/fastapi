from typing import Optional

from enum import Enum
from fastapi import FastAPI, Body, HTTPException, status
from pydantic import BaseModel, Field
import time
import producer
import json


class AZ(str, Enum):
    """
    Availability Zone Id
    """
    az1 = 'AZ1'
    az2 = 'AZ2'
    az3 = 'AZ3'
    az4 = 'AZ4'

class Datacenter(str, Enum):
    """
    Datacenter
    """
    rat = 'Ratingen'
    mil = 'Milan'
    dub = 'Dublin'
    swi = 'Swindon'

class OperatingSystem(str, Enum):
    """
    Operating System
    """
    rhel7 = "RHEL7"
    rhel8 = "RHEL8"
    w2k12 = "Windows 2012"
    w2k19 = "Windows 2019"

class TShirtSize(str, Enum):
    """
    TShirt Size name, see http://aaa for furder details
    """
    c1_small = "c1.small"
    c1_medium = "c1.medium"
    c1_large = "c1.large"

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

class VMRequest(BaseModel):
    """
    VM Request parameters
    """
    dc: Datacenter = Field("Ratingen", title="Target datacenter" )
    az: AZ = Field("AZ1", title="Target Availability Zone")
    rd: str = Field("VOD", title="Target Routing Domain")
    os: OperatingSystem = Field("RHEL8", title="Target Operating System")
    size: TShirtSize = Field("c1.small", title="VM size, CPU and Memory") 

class VMInstance(BaseModel):
    """
    VM parameters
    """
    id: str = Field(..., title="Id")
    vmname: str = Field("vg0000yw", title="VM Name")
    dc: Datacenter = Field("Ratingen", title="Current datacenter" )
    az: AZ = Field("AZ1", title="Current Availability Zone")
    rd: str = Field("VOD", title="Routing Domain")
    os: OperatingSystem = Field("RHEL8", title="Current Operating System")
    size: TShirtSize = Field("c1.small", title="Current VM size: CPU and Memory") 

class GenericTask(BaseModel):
    name: str
    delay: int
    value: str
    result: str
