import fnmatch
import os
import sys 
import csv
import click
import math

@click.command()
@click.option('--level','-l',default=math.inf,type=int,help='specify levels of  searching in sub directories')
@click.option('--bottom','-b',is_flag=True,help='Bottom up searching searching in sub directories. Default is Top to Bottom.')
@click.option('--in-dir','-i',default='./',help='Enter path of input directory')
def createCSV(in_dir,level,bottom):
    assert os.path.isdir(in_dir)
    num_dir_prefix=in_dir.count(os.path.sep)
    #print(num_dir_prefix)
    #print(level)
    outputFileName="output_of_link.csv"
    heading=['S no.','File Name','Link']
    with open(outputFileName,'w') as csvOutput:
        csvWriter=csv.writer(csvOutput)
        csvWriter.writerow(heading)
        entryCounter=1
        # search in directory or subdirectory based on flag
        for (root,dirs,files) in os.walk(in_dir,topdown=not bottom):
            if num_dir_prefix + level >= root.count(os.path.sep):
                #print(root)
                #print(root.count(os.path.sep))
                for f in fnmatch.filter(files,"*.md"):
                    #create MD type link from file name
                    link="["+f+"](Files/"+f[:-3]+".html)"
                    # added entry in csv 
                    csvWriter.writerow([entryCounter,f,link])
                    entryCounter +=1
    


if __name__ == '__main__':
    createCSV()


