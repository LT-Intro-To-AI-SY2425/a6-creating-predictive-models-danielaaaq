# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that? It's not entirely accurate, because of the data not being scaled to what we are looking for. This could've made the data mess up.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain. By using the standardscaler it made the data more accurate, its accurate enough for the case given. 

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about? The model has majority of the results right, however there was some outliers leading up to what we were looking for. 

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model. No, because the model would result in a neative outcome rather than a positive one. 

