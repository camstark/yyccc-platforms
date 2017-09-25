import spacy
import csv, pandas as pd

from scattertext import produce_scattertext_explorer
from scattertext.CorpusFromPandas import CorpusFromPandas

nlp = spacy.en.English()
platforms = pd.read_csv('official-candidate-platforms.csv')

corpus = CorpusFromPandas(platforms,
                          category_col='incumbent',
                          text_col='platform',
                          nlp=nlp).build()

incumbent = produce_scattertext_explorer(corpus,
                                    category='incumbent',
                                    category_name='Incumbent',
                                    not_category_name='Challenger',
                                    minimum_term_frequency=8,
                                    width_in_pixels=1000,
                                    filter_unigrams=True,
                                    metadata=platforms['meta'])

office = CorpusFromPandas(platforms,
                          category_col='office',
                          text_col='platform',
                          nlp=nlp).build()

mayor = produce_scattertext_explorer(office,
                                    category='Mayor',
                                    category_name='Mayor',
                                    not_category_name='Councillor',
                                    minimum_term_frequency=8,
                                    width_in_pixels=1000,
                                    filter_unigrams=True,
                                    metadata=platforms['meta'])

open('./office.html', 'wb').write(mayor.encode('utf-8'))
open('./incumbent.html', 'wb').write(incumbent.encode('utf-8'))
print('Open ./incumbent.html in Chrome or Firefox.')
