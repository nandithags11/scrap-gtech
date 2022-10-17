"""
The script to scrap Gtech Mulearn colleges 
inorder to study scrapping APIs

"""


import requests


d_response=requests.get("https://learning-circles-api.mulearn.org/districts")
text=d_response.json()
districts=text.get("data")
#print(districts)


for district in districts:
    c_response=requests.get("https://learning-circles-api.mulearn.org/colleges/"+str(district))
    text=c_response.json()
    colleges=text.get("data")
    print(type(colleges))
    for i in colleges:
        print(i.get('name'))
    break