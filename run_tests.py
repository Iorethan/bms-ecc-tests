#!/usr/bin/env python

import subprocess
import os

ERROR_RATE = 17

def comparator(left, right):
    if int(left[4:]) > int(right[4:]):
        return 1
    if int(left[4:]) < int(right[4:]):
        return -1
    return 0

def get_seconds(time):
    return float(time[1].split("user")[0])

megabyte = 1024 * 1024
tests = filter(lambda x: x[-4:] != ".out" and x[-3:] != ".ok" and x[-4:] != ".err" and x[:1] != ".", os.listdir("data/"))
tests = sorted(tests, cmp=comparator)

total = 0
result_pass = 0
time_pass = 0
size_pass = 0

print("Random error tests with " + str(ERROR_RATE) + "% of the file corrupted:")
for test in tests:
    total += 1
    max_time = 10 * float(test[4:]) / megabyte
    max_size = float(test[4:]) * 1.75
    time_encode = get_seconds(subprocess.Popen(["time", "src/bms2A", "data/" + test], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate())
    size = os.path.getsize("data/" + test + ".out")
    subprocess.call(["./errInjecter", "-i", "data/" + test + ".out", "-r", str(ERROR_RATE)])
    time_decode = get_seconds(subprocess.Popen(["time", "src/bms2B", "data/" + test + ".out.err"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate())
    result = subprocess.call(["diff", "data/" + test, "data/" + test + ".out.err.ok"])

    print(test)
    result = "OK" if result == 0 else "FAIL"
    result_pass += 1 if result == "OK" else 0
    print("Comparison: \t" + result + "\tencode\tdecode\tlimit")
    result = "OK" if time_encode <= max_time and time_decode <= max_time else "FAIL"
    time_pass += 1 if result == "OK" else 0
    print("Time \t\t" + result + " \t" + str(time_encode) + "s\t" + str(time_decode) + "s\t" + str(max_time) + "s")
    result = "OK" if size <= max_size else "FAIL"
    size_pass += 1 if result == "OK" else 0
    print("Size: \t\t" + result + "\t" + str(size) + "\t(limit: " + str(int(max_size)) + ")")

print("Block error tests with " + str(ERROR_RATE) + "% of the file corrupted:")
for test in tests:
    total += 1
    max_time = 10 * float(test[4:]) / megabyte
    max_size = float(test[4:]) * 1.75
    currupted_size = int(float(test[4:]) * ERROR_RATE / 100.0)
    time_encode = get_seconds(subprocess.Popen(["time", "src/bms2A", "data/" + test], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate())
    size = os.path.getsize("data/" + test + ".out")
    subprocess.call(["./errInjecter", "-i", "data/" + test + ".out", "-b", str(currupted_size)])
    time_decode = get_seconds(subprocess.Popen(["time", "src/bms2B", "data/" + test + ".out.err"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate())
    result = subprocess.call(["diff", "data/" + test, "data/" + test + ".out.err.ok"])

    print(test)
    result = "OK" if result == 0 else "FAIL"
    result_pass += 1 if result == "OK" else 0
    print("Comparison: \t" + result + "\tencode\tdecode\tlimit")
    result = "OK" if time_encode <= max_time and time_decode <= max_time else "FAIL"
    time_pass += 1 if result == "OK" else 0
    print("Time \t\t" + result + " \t" + str(time_encode) + "s\t" + str(time_decode) + "s\t" + str(max_time) + "s")
    result = "OK" if size <= max_size else "FAIL"
    size_pass += 1 if result == "OK" else 0
    print("Size: \t\t" + result + "\t" + str(size) + "\t(limit: " + str(int(max_size)) + ")")

print("Results:")
print("Comparisons: \t" + str(result_pass) + "/" + str(total))
print("Time: \t\t" + str(time_pass) + "/" + str(total))
print("Size: \t\t" + str(size_pass) + "/" + str(total))
print("Final result: \t" + ("OK" if result_pass + time_pass + size_pass == 3 * total else "FAIL"))
