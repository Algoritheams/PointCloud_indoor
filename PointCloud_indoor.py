import numpy as np
import pandas as pd
import open3d as o3d
import matplotlib.pyplot as plt
import yaml
import os


def read_file (file):
  with open(file, "r") as stream:
    try:
       read = yaml.safe_load(stream)
      return read
except yaml. YAMLError as exc:
print (exc) 


