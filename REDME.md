# BMS project 2 test suite

## Components
Makefile:           predefined controls
generate_data.py:   tool for generating data files
run_tests.py:       testing script
errInjecter:        tool for corrupting encoded files available at
                    https://www.fit.vutbr.cz/study/courses/BMS/public/proj2018/p2.html

## Preparation
1. Create data files (once)
    > make data
2. Copy your source code to src/
3. Compile your project
    > make prepare

## Configuration
To generate files with different sizes modify sizes array in generate_data.py.
To change severity of the corruption modify ERROR_RATE in run_tests.py.

## Usage
1. Run test
    > make test
