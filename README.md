# MD_link_generator
It is a CLI tool to search all .md file in given directory and create md link from names of md file.
```
  for eg. for file name foo.md
  link will be created as
  [foo](Files/foo.html)
```

## Installation
For Installing dependancy run following command in root directory of folder.
1. pip3 install -r requirements.txt

## Usage

Usage: main.py [OPTIONS]

Options:

  -l, --level INTEGER  specify levels of  searching in sub directories
  
  -b, --bottom         Bottom up searching searching in sub directories.Default is Top Down searching.

  -i, --in-dir TEXT    Enter path of input directory
  --help               Show this message and exit.

## Example :-
1. python3 main.py

   It will search all files in current directory of script
1. python3 main.py -i path/to/input/dir 
   
   It will search all files in given directory
1. python3 main.py -i path/to/input/dir -l 4
   
   It will search all files in given directory to sub directory at 4th level. you can specifiy level as per need.By default it will search in all levels of sub directories.
1. python3 main.py -i path/to/input/dir -l 4 -b
   
   It will search all files in given directory to sub directory at 4th level in bottom up manner. Default is Top Down searching.
