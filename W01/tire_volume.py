import datetime;
import math;

width = float(input('Enter the width of the tire in mm (ex 205): '));
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '));
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '));

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000;

print(f'The approximate volume is {volume:.2f} liters');

current_date = datetime.datetime.now();

with open('volume.txt', 'at') as volume_file:
    print(f'{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}', file=volume_file);
