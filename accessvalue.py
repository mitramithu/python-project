##accessing the values of dictionary inside a list

list=[{'yellow':'marigold','white':'lily'},{'red':'apple','yellow':'mango'}]
list[0]['white']='jasmine'
list[1]['yellow']='papaya'
print(list)

##2. using loop
for d in list:
    for key in d:
        print (d[key])

for d in list:
    for values in d:
        print(d[values])



##accessing the values of list inside dictionary

country={'India':['tamil nadu','kerala'],'united states':['new york','texas']}
print(country['India'])
print(country['India'][0])
print(country['united states'][1])



