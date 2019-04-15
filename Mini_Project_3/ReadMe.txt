
Addition Requirements to run the code.

Please note, the processing of the code takes a while, so be a bit patient while it runs.

Using the Anaconda3 command prompt:

1. First change the directory to the folder where the you extracted the nutrient-db-master

For example, extract the file to my desktop as follows:

(C:\ProgramData\Anaconda3) C:\Users\Tawanda Vera>cd Desktop\nutrient-db-master

2. Second, the nutrientdb.py is written in python 2.7,
  therefore there is need to change the module to a python 3.6 file.

For example, use the in built 2to3 script from Anaconda3 scripts folder as follows:

(C:\ProgramData\Anaconda3) C:\Users\Tawanda Vera\Desktop\nutrient-db-master>python C:/ProgramData/Anaconda3/Scripts/2to3-script.py -w nutrientdb.py

3.I then used the python 3 modified nutrientdb.py to create the JSON file. The code requires pymongo, 
which is installed using (pip install pymongo). 
After, the installation the pymongo then run the following code:

For example:

(C:\ProgramData\Anaconda3) C:\Users\Tawanda Vera\Desktop\nutrient-db-master>python nutrientdb.py -e > nutrients.json

4.

5.from pandas.io.json import json_normalize

For example: 
vera = [{'state': 'Florida',
         'shortname': 'FL',
         'info': {
               'governor': 'Rick Scott'
          },
         'counties': [{'name': 'Dade', 'population': 12345},
                      {'name': 'Broward', 'population': 40000},
                      {'name': 'Palm Beach', 'population': 60000}]},
        {'state': 'Ohio',
         'shortname': 'OH',
         'info': {
               'governor': 'John Kasich'
          },
         'counties': [{'name': 'Summit', 'population': 1234},
                      {'name': 'Cuyahoga', 'population': 1337}]}]

result = json_normalize(vera, 'counties', ['state', 'shortname',
                                           ['info', 'governor']])
 

