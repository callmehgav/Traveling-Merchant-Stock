from datetime import datetime

# merchStock - Dictionary that holds all combo of items that merchant can supply. This Dictonary will need updated when Merchant
# stock is ever updated
merchStock = {1: '  Slayer VIP Coupon  Slayer VIP Coupon  ', 41: '  D&D token (daily)  Gift for the Reaper  ',
              81: '  Small goebie burial charm  Menaphite gift offering (small)  ',
              2: '  Unfocused damage enhancer  Unfocused damage enhancer  ', 42: '  Slayer VIP Coupon  Goebie burial charm  ',
              82: '  Barrel of bait  Livid plant (Deep Sea Fishing)  ', 3: '  Gift for the Reaper  Gift for the Reaper  ',
              43: '  Shattered anima  Menaphite gift offering (small)  ', 83: '  Goebie burial charm  Slayer VIP Coupon  ',
              4: '  Tangled fishbowl  Menaphite gift offering (small)  ', 44: '  Silverhawk down  Slayer VIP Coupon  ',
              84: '  Shattered anima  Gift for the Reaper  ', 5: '  Anima crystal  Unstable air rune  ',
              45: '  Tangled fishbowl  Barrel of bait  ', 85: '  Menaphite gift offering (small)  Shattered anima  ',
              6: '  Menaphite gift offering (small)  Broken fishing rod  ',
              46: '  Unstable air rune  Menaphite gift offering (medium)  ',
              86: '  Livid plant (Deep Sea Fishing)  Silverhawk down  ',
              7: '  Small goebie burial charm  Goebie burial charm  ',
              47: '  Broken fishing rod  Livid plant (Deep Sea Fishing)  ',
              87: '  Unstable air rune  Unfocused damage enhancer  ',
              8: '  Menaphite gift offering (medium)  Shattered anima  ', 48: '  Barrel of bait  Unstable air rune  ',
              88: '  Sacred clay (Deep Sea Fishing)  Barrel of bait  ',
              9: '  Shattered anima  Sacred clay (Deep Sea Fishing)  ', 49: '  Tangled fishbowl  Tangled fishbowl  ',
              89: '  Silverhawk down  Small goebie burial charm  ', 10: '  Small goebie burial charm  Silverhawk down  ',
              50: '  Broken fishing rod  Broken fishing rod  ', 90: '  Unstable air rune  Menaphite gift offering (medium)  ',
              11: '  D&D token (daily)  Tangled fishbowl  ', 51: '  Small goebie burial charm  Small goebie burial charm  ',
              91: '  Slayer VIP Coupon  Sacred clay (Deep Sea Fishing)  ',
              12: '  Slayer VIP Coupon  Small goebie burial charm  ',
              52: '  Barrel of bait  Sacred clay (Deep Sea Fishing)  ', 92: '  Unfocused damage enhancer  Tangled fishbowl  ',
              13: '  Sacred clay (Deep Sea Fishing)  Slayer VIP Coupon  ',
              53: '  Menaphite gift offering (medium)  Gift for the Reaper  ',
              93: '  Barrel of bait  Menaphite gift offering (small)  ',
              14: '  Advanced pulse core  Unfocused damage enhancer  ',
              54: '  Sacred clay (Deep Sea Fishing)  Goebie burial charm  ',
              94: '  Gift for the Reaper  Livid plant (Deep Sea Fishing)  ', 15: '  Tangled fishbowl  Broken fishing rod  ',
              55: '  Menaphite gift offering (small)  Menaphite gift offering (medium)  ',
              95: '  Anima crystal  Silverhawk down  ', 16: '  Unstable air rune  Menaphite gift offering (small)  ',
              56: '  Livid plant (Deep Sea Fishing)  Slayer VIP Coupon  ',
              96: '  Menaphite gift offering (small)  Gift for the Reaper  ',
              17: '  Advanced pulse core  Menaphite gift offering (small)  ',
              57: '  Sacred clay (Deep Sea Fishing)  Slayer VIP Coupon  ', 97: '  Gift for the Reaper  Gift for the Reaper  ',
              18: '  Gift for the Reaper  Livid plant (Deep Sea Fishing)  ',
              58: '  Shattered anima  Unfocused damage enhancer  ', 98: '  Goebie burial charm  Goebie burial charm  ',
              19: '  Tangled fishbowl  Unstable air rune  ', 59: '  Silverhawk down  Barrel of bait  ',
              99: '  Shattered anima  Shattered anima  ', 20: '  Broken fishing rod  Gift for the Reaper  ',
              60: '  Unstable air rune  Menaphite gift offering (small)  ',
              100: '  Small goebie burial charm  Slayer VIP Coupon  ',
              21: '  Menaphite gift offering (small)  Sacred clay (Deep Sea Fishing)  ',
              61: '  Unstable air rune  Tangled fishbowl  ',
              101: '  Livid plant (Deep Sea Fishing)  Small goebie burial charm  ',
              22: '  Small goebie burial charm  Advanced pulse core  ', 62: '  Broken fishing rod  Anima crystal  ',
              102: '  Unstable air rune  D&D token (daily)  ',
              23: '  Menaphite gift offering (medium)  Unfocused damage enhancer  ',
              63: '  Barrel of bait  Goebie burial charm  ',
              103: '  Sacred clay (Deep Sea Fishing)  Livid plant (Deep Sea Fishing)  ',
              24: '  Sacred clay (Deep Sea Fishing)  Small goebie burial charm  ',
              64: '  Gift for the Reaper  Sacred clay (Deep Sea Fishing)  ', 104: '  Advanced pulse core  Tangled fishbowl  ',
              25: '  Small goebie burial charm  Small goebie burial charm  ',
              65: '  Broken fishing rod  Sacred clay (Deep Sea Fishing)  ', 105: '  Unstable air rune  Tangled fishbowl  ',
              26: '  D&D token (daily)  D&D token (daily)  ', 66: '  Small goebie burial charm  Advanced pulse core  ',
              106: '  Slayer VIP Coupon  Anima crystal  ',
              27: '  Sacred clay (Deep Sea Fishing)  Sacred clay (Deep Sea Fishing)  ',
              67: '  Gift for the Reaper  Tangled fishbowl  ', 107: '  Advanced pulse core  Small goebie burial charm  ',
              28: '  Shattered anima  Tangled fishbowl  ', 68: '  Goebie burial charm  Small goebie burial charm  ',
              108: '  Gift for the Reaper  Sacred clay (Deep Sea Fishing)  ', 29: '  Advanced pulse core  Shattered anima  ',
              69: '  Sacred clay (Deep Sea Fishing)  Unstable air rune  ', 109: '  Gift for the Reaper  Barrel of bait  ',
              30: '  Gift for the Reaper  Silverhawk down  ', 70: '  Shattered anima  Broken fishing rod  ',
              110: '  Goebie burial charm  Menaphite gift offering (medium)  ',
              31: '  Unstable air rune  Advanced pulse core  ', 71: '  Livid plant (Deep Sea Fishing)  Anima crystal  ',
              111: '  Menaphite gift offering (small)  D&D token (daily)  ', 32: '  Broken fishing rod  Barrel of bait  ',
              72: '  Unstable air rune  Shattered anima  ', 112: '  Small goebie burial charm  Unstable air rune  ',
              33: '  Gift for the Reaper  Barrel of bait  ', 73: '  Shattered anima  Shattered anima  ',
              113: '  Goebie burial charm  Unstable air rune  ', 34: '  Tangled fishbowl  Menaphite gift offering (medium)  ',
              74: '  Silverhawk down  Silverhawk down  ', 114: '  Shattered anima  Broken fishing rod  ',
              35: '  Broken fishing rod  Shattered anima  ', 75: '  Unstable air rune  Unstable air rune  ',
              115: '  Small goebie burial charm  Barrel of bait  ', 36: '  Small goebie burial charm  Unstable air rune  ',
              76: '  Slayer VIP Coupon  Barrel of bait  ', 116: '  D&D token (daily)  Shattered anima  ',
              37: '  Small goebie burial charm  Menaphite gift offering (small)  ',
              77: '  Broken fishing rod  Slayer VIP Coupon  ', 117: '  Unstable air rune  Gift for the Reaper  ',
              38: '  Menaphite gift offering (medium)  D&D token (daily)  ', 78: '  Barrel of bait  Advanced pulse core  ',
              118: '  Sacred clay (Deep Sea Fishing)  Anima crystal  ',
              39: '  Sacred clay (Deep Sea Fishing)  Silverhawk down  ', 79: '  Gift for the Reaper  Broken fishing rod  ',
              119: '  Advanced pulse core  Menaphite gift offering (medium)  ',
              40: '  Shattered anima  Gift for the Reaper  ', 80: '  Goebie burial charm  Menaphite gift offering (small)  ',
              120: '  Gift for the Reaper  Slayer VIP Coupon'}

# today gets today's date which will be used to compare to the first day the merchant's logic was figured out.
today = datetime.today()

# firstDayOfMerch holds the value of the first day the merchant's logic was figured out
firstDayOfMerch = datetime(2018, 3, 11)

# difference holds the day difference of the two previous dates
difference = today - firstDayOfMerch

# remainder holds the value equal to the number key in the dictionary, This will return the correct items.
# 120 is hardcoded because that is how many sets of items that are in the dictionary
remainder = difference.days % 120

# now is used to initialize a date that will compare to reset time
now = datetime.now()

# reset time is hardcoded to 7pm because that is when reset is EST. Daylight savings time WILL effect this. to 20:00
# (8pm)
resetTime = now.replace(hour=19, minute=0, second=0, microsecond=0)

# Formatting for pretty output
print('=' * 45)

# Compare time now to reset time to make sure that the correct items are shown. +1 means it's before reset +2 means
# reset has happened so we need items for the next day.
if now >= resetTime:
    print(merchStock.get(remainder + 2))
else:
    print(merchStock.get(remainder + 1))

# Formatting for pretty output
print('=' * 45)
