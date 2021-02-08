#!/usr/bin/env python
# coding: utf-8

#
import os
import re
import pandas as pd 
import sys

dirname = os.path.dirname(__file__)
filename1 = os.path.join(dirname, 'worldcities.csv')
filename2=os.path.join(dirname, 'NationalNames.csv')
filename3=os.path.join(dirname, 'comps.csv')
filename4=os.path.join(dirname, 'month.csv')
filename5=os.path.join(dirname, 'country.csv')

dates=pd.read_csv(filename4)
COUNTRY=pd.read_csv(filename5)
COUNTRY=COUNTRY['Country']
data = pd.read_csv(filename1)
DATES=dates['Tarihler']

names=pd.read_csv(filename2)

names.drop_duplicates(subset ="Name", 
                     keep = 'first', inplace = True) 
LOCATIONS=data['city']
COMPANIES=pd.read_csv(filename3,encoding="utf-8")
COMPANIES['name'] = COMPANIES['name'].str.upper() 
COMPANIES=COMPANIES['name']

PERSONS=names['Name']



line_number=1
with open(sys.argv[1],encoding="utf-8") as f:
    for line in f:
        for ind in LOCATIONS.index:
            if re.search(r'\b'+LOCATIONS[ind]+r'\b', line):
                print("Line "+str(line_number),": LOCATION ",LOCATIONS[ind])
        for ind2 in PERSONS.index:
            if re.search(r'\b'+PERSONS[ind2]+r'+\b', line):
                print("Line "+str(line_number),": PERSON",PERSONS[ind2])
        
        for ind3 in COMPANIES.index:
            temp_line=line.upper()
            try:
                if re.search(r'\b'+COMPANIES[ind3]+r'\b', temp_line):
                    print("Line "+str(line_number),": ORGANIZATION",COMPANIES[ind3])
            except:
                z=10
        for ind4 in DATES.index:
            if re.search(r'\b'+DATES[ind4]+r'\b', line):
                print("Line "+str(line_number),": DATE",DATES[ind4])
        for ind5 in COUNTRY.index:
            if re.search(r'\b'+COUNTRY[ind5]+r'\b', line):
                print("Line "+str(line_number),": LOCATION",COUNTRY[ind5])
  

        if 'Müze' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?:Müze|Müze\w+)',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)  ## Müze 2k
        if 'Üniversite' in line:   
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ Üniversite\w+',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)  ## Müze 2k   
        if 'AŞ' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?:A.Ş|LTD)',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        if 'işbirliği' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=işbirliği\w+)',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        if 'yıl' in line:
            results=re.findall(r'\d{4}(?=\s+yıl\w+)',line)
            for current in results:
                print("Line "+str(line_number),": DATE ",current)
        if 'tarih' in line:
            results=re.findall(r'\d{2}\W\d{2}\W\d{4}(?:\s+tarih\w+)',line)
            for current in results:
                print("Line "+str(line_number),": DATE ",current)
        if 'ilçe' in line:
            results=re.findall(r'A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=\s+ilçe\w+)',line)
            for current in results:
                print("Line "+str(line_number),": LOCATION ",current)
        if 'Site' in line:
            results=re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Site\w+',line)
            for current in results:
                print("Line "+str(line_number),": LOCATION ",current)
        if 'Şenli' in line:   
            results=re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Şenli\w+',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        if 'Belediye' in line:
            results=re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Belediye\w+',line)
            for current in results:
                print("Line "+str(line_number),": LOCATION ",current)
        if 'Hastane' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+  Hastane\w+',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        if 'Vakf' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+  Vakf\w+',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        if 'Prof. Dr.' in line:
            results=re.findall(r'(?<=Prof. Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',line)
            for current in results:
                print("Line "+str(line_number),": LOCATION ",current)
        if 'Lider' in line:
            results=re.findall(r'(?<=[Ll]ideri )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*',line)
            for current in results:
                print("Line "+str(line_number),": PERSON ",current)
        if 'Sayın' in line:
            results=re.findall(r'[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Site\w+',line)
            for current in results:
                print("Line "+str(line_number),": LOCATION ",current)
        if 'kaybı' in line:
            results=re.findall(r'(?:[A-ZÇĞİÖŞÜ][a-zçğıöşü]*)(?=\skayb\w+ )',line)
            for current in results:
                print("Line "+str(line_number),": PERSON ",current)
        if 'bir araya geldiği' in line:
            results=re.findall(r'(?=bir araya geldiği) (?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+',line)
            for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=\W d{4}\Wd{2}\W )',line)
        for current in results:
                print("Line "+str(line_number),": PEOPLE ",current)
        if 'hanım' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=hanım|hanım\w+)',line)
            for current in results:
                print("Line "+str(line_number),": PEOPLE ",current)
        if 'abla' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=abla|abla\w+)',line)
            for current in results:
                print("Line "+str(line_number),": LOCATION ",current)
        if 'abi' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=abi|abim\w+)',line)
            for current in results:
                print("Line "+str(line_number),": PERSON2 ",current)
        if 'bey' in line:
            results=re.findall(r'(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=bey|bey\w+)',line)
            for current in results:
                print("Line "+str(line_number),": PERSON ",current)
        if 'a gid' in line:
            results=re.findall(r"(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)(?=\Wa\sgid\w+|a\sgit\w+)  ",line)
            for current in results:
                print("Line "+str(line_number),": LOCATION ",current)
        results=re.findall(r' [a-zçğıöşü]+[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]*',line)
        for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        results=re.findall(r' (?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+(?=[0-9]{2,})',line)
        for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        results=re.findall(r'(?:[A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+(?=\s[0-9]{2,})',line)
        for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)
        results=re.findall(r'(?:[A-ZÇĞİÖŞÜ]{3,})',line)
        for current in results:
                print("Line "+str(line_number),": ORGANIZATION ",current)

        
  
        
        line_number+=1
   

      
















