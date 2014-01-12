# CooCo
Converts CooRecorder output files (Cybis Dendro) to COFECHA input files (Tucson).

## What is it?
CooRecorder is a tool commonly used in dendrochronology (tree-ring dating) to measure ring widths. This data is used in the tool COFECHA to measure a tree's age against an anchored chronology. Typically, to get the measurments from CooRecorder to COFECHA takes a lot of hand-processing. CooCo does away with that by converting the files for you.

## How do I use it?
### To convert one file
```
cooco \path\to\file.txt -o \path\to\output.txt
```
CooCo will output to .\output.txt by default. Entries are named by the last 7 characters of the input file for that entry.
### To convert a folder full of files
```
cooco \path\to\files -o \path\to\output.txt
```
### To convert several files
```
cooco \path\to\file1.txt \path\to\file2.txt ...
```