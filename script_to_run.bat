@echo off

REM This file executes the data_processor.py program,

if not exist "input_data.txt" (
  echo Error: The input data file "input_data.txt" was not found.
  exit /b 1
)

python data_processor.py "input_data.txt"

echo Data processing script executed.
pause
