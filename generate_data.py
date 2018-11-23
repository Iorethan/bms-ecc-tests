#!/usr/bin/env python

import subprocess

megabyte = 1024 * 1024
sizes = [
    megabyte,
    megabyte + 1,
    megabyte + 2,
    2 * megabyte - 2,
    2 * megabyte - 1,
    2 * megabyte,
    2 * megabyte + 1,
    2 * megabyte + 2,
    3 * megabyte,
    5 * megabyte
]

for size in sizes:
    subprocess.call(["dd", "if=/dev/urandom", "of=data/data" + str(size), "bs=1", "count=" + str(size)])
