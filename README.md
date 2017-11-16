# Sprint 1: Data File Formats for N00bs

11/16/17

**Author:** Runjini Murthy


__*Project Description:*__ Introduce the complete data novice to three key file types: CSV, XML, JSON.  It will explain the features of each file type, use cases for each, and demonstrate a process to convert the commonly known CSV to XML and JSON respectively using Python scripts.


### Summary
CSV is a commonly used data file format for business, XML and JSON offer additional benefits.  XML offers the ability to show hierarchies in data, using human readable language to describe the fields and values, but it is the largest of the file sizes, because there are open and close tags for each element.  JSON is the best of both worlds, using human readable language but preserving data hierarchies in a file smaller than XML.  

The exercise of converting file formats involves Python, Atom, and command line. The Python script is written in Atom and executed in the command line.  The two scripts used are below.  In order to execute the function, the following must be typed into the command line/terminal:  
python filename.py

### CSV to XML Conversion Code
```python
# csv2xml.py
# FB - 201010107
# First row of the csv file must be header!

# example CSV file: myData.csv
# id,code name,value
# 36,abc,7.6
# 40,def,3.6
# 9,ghi,6.3
# 76,def,99

import csv

csvFile = 'Public_Art.csv'
xmlFile = 'Public_Art.xml'

csvData = csv.reader(open(csvFile))
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0"?>' + "\n")
# there must be only one top-level tag
xmlData.write('<csv_data>' + "\n")

rowNum = 0
for row in csvData:
    if rowNum == 0:
        tags = row
        # replace spaces w/ underscores in tag names
        for i in range(len(tags)):
            tags[i] = tags[i].replace(' ', '_')
    else:
        xmlData.write('<row>' + "\n")
        for i in range(len(tags)):
            xmlData.write('    ' + '<' + tags[i] + '>' \
                          + row[i] + '</' + tags[i] + '>' + "\n")
        xmlData.write('</row>' + "\n")

    rowNum +=1

xmlData.write('</csv_data>' + "\n")
xmlData.close()


```

### CSV to JSON Conversion Code
```python
import pandas as pd
df = pd.read_csv('Public_Art.csv')
# any operations on dataframe df
df.to_json('Public_Art.json')
print ("Conversion complete!")
```

### Key Command Line Functions
cd = change directory  
pwd = print working directory  
ls = list items in the current folder  
cd .. = move up one folder  
python filename.py = execute scripts

### Helpful Links
[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Data Format Comparison 1](http://1zinearticles.com/?CSV-vs-XML-vs-JSON---Which-is-the-Best-Response-Data-Format?&id=4073117)

[Data Format Comparison 2](http://json.org/example.html)

[CSV to XML code source](http://code.activestate.com/recipes/577423-convert-csv-to-xml/)
