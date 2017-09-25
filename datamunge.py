import csv, pandas as pd

platforms = pd.read_csv('official-candidate-profiles.csv')
platforms = platforms[['office','name','platform']]
platforms = platforms[~platforms['office'].str.contains('School Board')]
platforms['incumbent'] = platforms['name'].str.contains('Nenshi|Sutherland|Magliocca|Chu|Farrell|Woolley|Carra|Ray Jones|Keating|Urquhart|Demong')
platforms['incumbent'] = platforms['incumbent'].replace({True:'incumbent', False:'challenger'})
platforms['meta'] = platforms['name'] + ' - ' + platforms['office']
platforms['platform'] = platforms['platform'].str.replace("<[^>]*>", "")
# platforms['platform'] = platforms['platform'].str.replace("[0-9]*", "")
platforms = platforms[platforms['platform'].notnull()]
platforms = platforms[['office','name','incumbent','meta','platform']]

platforms.to_csv('official-candidate-platforms.csv',sep=",",encoding='utf=8',index=False)
