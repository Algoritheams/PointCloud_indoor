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
import math

class LidarScan:
    def __init__(self, num_points=360, radius=10):
        self.num_points = num_points
        self.radius = radius
        self.points = []

    def generate_scan(self):
        self.points = []
        angle_increment = 360 / self.num_points

        for i in range(self.num_points):
            angle = math.radians(i * angle_increment)
            x = self.radius * math.cos(angle)
            y = self.radius * math.sin(angle)
            self.points.append((x, y))

    def print_scan(self):
        for point in self.points:
            print(f"Point: {point}")

# Example usage:
lidar_scan = LidarScan()
lidar_scan.generate_scan()
lidar_scan.print_scan()


