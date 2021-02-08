Location list is taken from https://simplemaps.com/data/world-cities.
People is taken from https://www.kaggle.com/kaggle/us-baby-names(Some common turkish name added manually)
ORGANIZATIONS is taken from https://www.kaggle.com/peopledatalabssf/free-7-million-company-dataset.
DATE -->manually implemented
COUNTRY is taken from https://ulusalbayrak.com/menudetay.php?id=119



Reg 1= [a-zçğıöşü]+[A-ZÇĞİÖŞÜ]+[a-zçğıöşü]* --> find names such as iPhone 
Reg 2= [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ Üniversite\w+ --> find Multiple word and single word universities such as Yıldız Teknik Üniversitesi and Sabancı Üniversitesi
Reg 3=(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?:Müze|Müze\w+) --> find Multiple word and single word universities Müze however it also considired 
Reg 4=(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?:A.Ş|LTD) find Multiple word and single word A.Ş and LTD companies
Reg 5=(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=işbirliği\w+) This regular experesion is searching for "Proper Nouns" işbirliği however does not print işbirliği because of ?=
Reg 6= \d{4}(?=\s+yıl\w+) looking for meantion of yıl and 4 digit number before yıl
Reg 7='\d{2}\W\d{2}\W\d{4}(?:\s+tarih\w+) Searching for date such as with any delimiter such as 19.02.20 tarihinde or 19-02.30 tarihinde
Reg 8=r'A-ZÇĞİÖŞÜ][a-zçğıöşü]*(?=\s+ilçe\w+)' Searching for ilçe and proper noun before that. Does not print ilçe
Reg 9='[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Site\w+'  find Multiple word and single word site
Reg 10='[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Şenli\w+'  find Multiple word and single word şenlik
Reg 11='[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Belediye\w+'  find Multiple word and single word Belediye
Reg 12='[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Hastane\w+'  find Multiple word and single word Hastane
Reg 13='[A-ZÇĞİÖŞÜ][a-zçğıöşü]* Vakf\w+'  find Multiple word and single vakif
Reg 14='(?<=Prof. Dr. )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*' Looking for Prof Dr and Name,Surname
Reg 15='(?<=[Ll]ideri )[A-ZÇĞİÖŞÜ][a-zçğıöşü]*\s[A-ZÇĞİÖŞÜ][a-zçğıöşü]*' Looking for lider of some ORGANIZATIONS however lider can be a tittle starting with small l. As a result it is searching for Lider or Lider with some name and Surname
Reg 16=(?:[A-ZÇĞİÖŞÜ][a-zçğıöşü]*)(?=\s+kayb\w+ ) looking for one prope noun and "kayb\w+"
Reg 17=(?=bir araya geldiği) (?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ looking for an organiztion with "bir araya geldiği")
Reg 18='(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=\W d{4}\Wd{2} )+' Looking for a past person with Furkan Canbal(1920-75)
Reg 19=?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=hanım|hanım\w+)' Looking for abla/hanım/bey and proper nouns before these
Reg 20=?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=abla|abla\w+)'
Reg 21=?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=abim|abim\w+)'
Reg 22=?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+ (?=bey|bey\w+)'
Reg 23=?: (?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)(?='a)(?=gid\w+|git\w+) Looking for locations with 'a gitmek and 'a gidiyorum
Reg 24=(?: [A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+(?=[0-9]{2,}) looking for brand Fifa 19 or organiztion such as Forever 21
Reg 25= (?:[A-ZÇĞİÖŞÜ][a-zçğıöşü]*)+(?=\s[0-9]{2,}*) looking for corparation such as Century 21
Reg 26=?:[A-ZÇĞİÖŞÜ]{3,}) looking for word that has more than 2 capital letter such as CHP



r'\b'+COMPANIES[ind3]+r'\b' --> Exact match for lexicons
b'+PERSONS[ind2]+r'\b'
b'+LOCATIONS[ind]+r'\b
r'\b'+DATES[ind4]+r'\b'
r'\b'+COUNTRY[ind5]+r'\b'
    





