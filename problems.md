Problems
==========
##Data requirements
###Large n requirements
For our data to be complete enough to suggest hashtags for a large range of tweets we need a very large n. 100,000 tweets worked well enough to predict only very popular hashtags with simple combinations of words. More data will improve our results but has increased processing time.
###Real time processing
Currently our algorithm must analyze the entire set of parsed data every time new information is added. To fix this we would need to use an algorithm that has the capability to add new information to existing confidence rules that can add rules or change the confidence of existing rules. This is challenging because much of the data that is used to create the rules will have to be included in order to update each rule reliably.
###Time frame
Given the volatile nature of social networks in general and especially Twitter hash tags that are relavent to certain words may be replaced by other hash tags based on recent events. One solution to this could be to remove data no longer contained in a sliding window of time behind the current date. Another solution is to apply a function that weights newer data heavier than older data but implementing this solution incurs the overhead of time data to weight being to be calculated at the time of tweet analyzation.
