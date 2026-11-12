import re

p = '/home/tapaswi/Mines_Geology/Objective_book/Sayeed_Chapter2_PhysicalGeology/masterclass_data_ch2.py'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any string literal containing \tau or \text that is not prefixed with r
text = text.replace('"Centrifugal', 'r"Centrifugal')

with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved cleanly!")
