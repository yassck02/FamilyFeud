@echo off
for /F "tokens=1 delims=." %%A in ("%~0") do set WD=%%A
set PATH=%WD%\bin;%path%
set HOME=/home
set SHELL=/bin/bash
set COURSE=/lib/course
bash --login -i
