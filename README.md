# COVID-19-policy

This is an investigation into sentiment from tweets over time in response to COVID government policy decisions. This tool could be used for policy makers to assess public reaction to policy changes related to lockdown by using NLP to analyse language in tweets.

The Twitter data is sampled from a 7 minute window for 4 days in May with the Twitter API, from tweets containing the words related to COVID. Further analysis could use more tweets over a longer time period. Word usage and sentiment analysis are performed on a time series basis in an EDA <b>Covid Tweets EDA.ipynb</b>. 

The Oxford COVID Policy Tracker has been used to supplement the Twitter data with a policy stringency index by county over time. More information about this data set can be found at https://covidtracker.bsg.ox.ac.uk and https://github.com/OxCGRT/covid-policy-tracker. The Oxford data was used to plot time series data of deaths with policy stringency changes shown in <b>Time Series Stringency Analysis Oxford.ipynb</b>. 

Finally, both the Twitter and Oxford data have been plotted on a map for a specific day to see tweet sentiment by location (only for tweets in english) and Stringency Index by country in <b>Geographical Analysis Twitter.ipynb</b> and <b>Geographical Analysis Oxford.ipynb</b> respectively. 

To further the analysis, linear regression could be used to predict the percentage change in death toll due to changes in policy stringency, or specific policy measures. NLP could be used to identify a list of the top salient terms by country by sentiment category to get better insight into policy reaction. Clustering algorithms could be used to group countries by patterns in policy behaviour over time and/or confirmed case numbers. 

The <b>Combined_Analysis.ipynb</b> is the merged version of all ipython notebooks.
