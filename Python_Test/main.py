import glob
import csv
import math

csv_files = glob.glob('*.csv')
start_text = "Delta Temperature (degC)"

f = csv_files[0]

time_errors = 0
logtime_errors = 0
temp_errors = 0

with open(f, 'r', newline='') as file:
    reader = csv.reader(file)
    for line in reader:
        if start_text in line:
            break

    mins = 4
    t = 0
    sampleTime = 1/15
    for row in reader:
        time = float(row[0])
        logtime = abs(float(row[1]))
        temp = abs(float(row[2]))
        # print(row)
        t += sampleTime
        if not (time * 0.95 <= t <= time * 1.05):
            print(row, t, "s")
            time_errors += 1

        if not (logtime * 0.95 - 0.0001 <= abs(math.log(t)) <= logtime * 1.05 + 0.0001):
            print(row, math.log(t), "ln s")
            logtime_errors += 1

        if not(temp * 0.90 - 0.01 <= abs(math.sin(t)) <= temp * 1.1 + 0.01):
            print(row, math.sin(t), "C")
            temp_errors += 1


print(f"\nErrors:\n\tTime: {time_errors}\n\tLog Time: {logtime_errors}\n\tTemp: {temp_errors}\n\ntotal errors:"
      f" {time_errors + logtime_errors + temp_errors}")