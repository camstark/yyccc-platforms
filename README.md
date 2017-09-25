#### 2017 Calgary Municipal Election Candidate Platforms

0. Definitely use Python 3.x, I tried to get by with 2.7 and it...did not go well.

1. Install the [Scattertext](https://github.com/JasonKessler/scattertext) package by Jason Kessler.  
`$ pip3 install scattertext && python -m spacy download en`

2. Get the candidate profile information from [Calgary Democracy](http://calgarydemocracy.ca/levels/calgary/elections/2017/official-profiles). Or [use the ones I already downloaded](https://github.com/camstark/yyccc-platforms/blob/gh-pages/official-candidate-profiles.csv) from there.  
And read [@yycelect](https://twitter.com/yycelect)/[&grant](https://twitter.com/grant)'s thoughts about The City not making this information available in a reusable, machine-readable format.

3. Clean up the [official-candidate-profiles.csv](https://github.com/camstark/yyccc-platforms/blob/gh-pages/official-candidate-profiles.csv) data a bit to prepare for analysis and save as [official-candidate-platforms.csv](https://github.com/camstark/yyccc-platforms/blob/gh-pages/official-candidate-platforms.csv):  
`$ python3 datamunge.py`

4. Create the two visualizations of the platform data (incumbents vs. challengers & mayoral candidates vs councillor candidates):  
`$ python3 platforms.py`

5. You could optionally run scattertext from the command line instead of using `platforms.py`

  Incumbents vs. Challengers:
~~~
scattertext --datafile=official-candidate-platforms.csv \
--text_column=platform --category_column=incumbent --positive_category=incumbent \
--category_display_name=Incumbent --not_category_display_name=Challenger \
--minimum_term_frequency=8 --metadata_column=meta \
--outputfile=incumbent.html
~~~

  Mayoral Candidates vs. Councillor Candidates:
~~~
scattertext --datafile=official-candidate-platforms.csv \
--text_column=platform --category_column=office --positive_category=Mayor \
--category_display_name=Mayor --not_category_display_name=Councillor \
--minimum_term_frequency=8 --metadata_column=meta \
--outputfile=office.html
~~~

  Options to consider:  
 * `minimum_term_frequency=8` means that a term needs to show up 8 times to appear in the chart  
 * adding the `--one_use_per_doc` flag would only count a word once in any given platform rather than every time it appears (e.g. "Druh")  
 * There might be a few other useful parameters to test to change the output...  

7. I made a few tweaks to the output HTML by hand.
 * I renamed incumbent.html to index.html for ease of loading.
 * I increased the radius of the circles.
 * I added buttons to toggle between the two pages.  
