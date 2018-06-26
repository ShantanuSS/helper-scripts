"""
This script can be use to edit csv files.
"""

import csv, os
import sys

csv.field_size_limit(sys.maxsize)

def read_csv(file_path, fields, rows):
    with open(file_path, 'rU') as csvFile:
        reader = csv.DictReader(csvFile, dialect=csv.excel)
        if fields:
            reader.fieldnames.extend(fields)
            del fields[:]
        fields.extend(reader.fieldnames)
        rows.extend(reader)
    print '## READ FILE:', os.path.basename(file_path)


def write_csv(file_path, fields, rows):
    with open(file_path, 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields, lineterminator='\n')
        writer.writerow(dict(zip(fields, fields)))
        for row in rows:
            writer.writerow(row)
    print '## FILE WRITTEN', os.path.basename(file_path)


if __name__ == '__main__':
    filepath = './Karna_3.csv'
    prepend_key = "BOX5/"

    #path2 = './tx_Kerala.csv'
    #path3 = './test/newdelhi.csv'
    #path1 = './test/tx___Kerala.csv'
    r = [], []
    #rr = [], []

    read_csv(filepath, r[0], r[1])

    neww = []
    for idx ,row in enumerate(r[1]):
        #if row['FATE']== 'CONFIRMED':# and r[1][idx]['FATE'] != 'CONFIRMED':
        if "," in row['Images URL']:
            spl = row['Images URL'].split(',')
            neww = [ (prepend_key + xx) for xx in spl ]
            row['Images URL'] = ','.join(neww)
        else:
            # if row['State'].lower() not in row['h_address'].lower() or 'india' not in row['h_address'].lower():
                # print idx, "--->", row['h_address']
            row['Images URL'] = prepend_key + row["Images URL"]

            #print "##", idx, row['Name'], "--->", row['h_name']        
    
    write_csv(filepath, r[0], r[1])
