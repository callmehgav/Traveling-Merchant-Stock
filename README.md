# Traveling-Merchant-Stock
### For Runescape 3 traveling merchant daily

This Program will return a string of the items in slot 2 and 3 of the merchants daily stock. No API is used for the items. The program has a dictionary of all possible combinations with the correct keys for the day attached. Uses same logic that the merchant uses. This will need updated if merchant stock is ever updated (items added).

### What to change
Open RunMe.py and correct reset time to your local reset time. E.G. Reset time is 7pm EST so variable resetTime has 19 in the hour slot. (7pm military time)

### How to run
If you're familiar with a python IDE running the program that way may be easier than using the terminal

### Run using the terminal
Go to the directory where you downloaded the file 
```$ cd Downloads/Traveling-Merchant-Stock-master/TravelingMerchantStock```

Install DateTime for python
```$pip install datetime```

Run the program
```python3 RunMe.py```
