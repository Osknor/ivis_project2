import xlrd
import json
import csv
import math
lander = ['Argentina', 'Australia', 'Brazil', 'Chile', 'China', 'Colombia', 'Egypt', 'Georgia', 'India', 'Iraq', 'Japan', 'Jordan', 'Mexico', 'Moldova', 'Morocco', 'New Zealand','Nigeria','Pakistan','Peru','Philippines','Poland', 'Romania', 'Russian Federation', 'Serbia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Taiwan', 'Turkey', 'Ukraine', 'United States', 'Uruguay']

array =  [
["cell_phone_per_100.xlsx", 1,"cells","Call phones per 100"],
["indicator CDIAC carbon_dioxide_emissions_per_capita.xlsx", 1,"co2","Carbon dioxide emissions per capita"],
["indicator SI_POV_GINI.xlsx", 1,"inequality","GINI inequality index"],
["indicator total health expenditure perc of GDP.xlsx", 1 ,"health","Total health spending % CGP"],
["indicator wdi urbanpopulation.xlsx", 1, "urban","Urban population (percent of total)"],
["population_growth.xlsx", 1, "growth","Annual population growth"],
["Years in school, women 25 to 34 as percent of men.xlsx", 1, "menwo" ,"Year in school 25 to 34 women / men"],
]
tomarray = []
forsta = [0]*len(lander)
andra = [0]*len(lander)
tredje = [0]*len(lander)
fjarde = [0]*len(lander)
objektet = [forsta,andra,tredje,fjarde]
print(objektet)

header = ["country","year"]
for item in array:
    header.append(item[2])
years = [1995,2000,2005,2010]

for year in range(0,4):
    for i in range(0,len(lander)):
        objektet[year][i] = {"country":lander[i]}
        objektet[year][i].update({"year":years[year]})
        for item in array:
            objektet[year][i].update({item[2]:"No data"})


for gong in range(0,len(array)):
    workbook = xlrd.open_workbook("../../../Gapminder/"+array[gong][0])
    worksheet = workbook.sheet_by_index(0)
    print(worksheet.row(1))
    ararray = [0]*(len(worksheet.row(0)))
    print(len(ararray))
    for i in range(0,len(ararray)):
        try:
            ararray[i] = int(worksheet.row(0)[i].value)
        except:
            ararray[i] = 0

    print(worksheet.col(0))
    landerarray = [0]*len(worksheet.col(0))
    for i in range(0,len(landerarray)):
        landerarray[i] = worksheet.col(0)[i].value
    for land in lander:
        for inter in range(0,len(landerarray)):
            if land == landerarray[inter]:
               rowen =  worksheet.row(inter)
               counter = 0
               for oren in years:
                   for ar in range(0,len(ararray)):
                        try:  
                            if oren == ararray[ar+counter]:
                                if (worksheet.row(inter)[ar].value != 0 and worksheet.row(inter)[ar].value != ""):
                                    print('träff')
                                    objektet[years.index(oren)][lander.index(land)].update({array[gong][2]:(worksheet.row(inter)[ar].value)})
                                    counter = 0
                                elif(counter <4):
                                    counter += 1
                                else:
                                    counter = 0
                        except:
                            print("lol")        

print(ararray)
print(landerarray)
objektet
""" for year in range(0,4):
    for bok in array:
        inteurug = True
        workbook = xlrd.open_workbook("../../../Gapminder/"+bok[0])
        worksheet = workbook.sheet_by_index(0)
        
        tomarray.append(worksheet.row(3)[1].value)
        while inteurug:
            var1 = worksheet.row(indexet)[0].value
            print(var1 == 'Uruguay')
            print(var1)
            if var1 == 'Venezuela':
                inteurug = False
            if var1 == 'Russia':
                var1 ='Russian Federation'
            var2 = worksheet.row(indexet)[2].value
            if (bok[1] == 2):
                var2 += worksheet.row(indexet)[3].value
            indexet += 1
            if var1 in lander:
                objektet[lander.index(var1)].update({bok[2]:var2})
            else:
                print(var1)

"""
with open('gap.csv', mode='w', newline='') as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=header)

    writer.writeheader()
    for item in objektet:
        for subitem in item:
            writer.writerow(subitem)
"""
        
with open('2005.json', 'w') as outfile:
    json.dump(objektet, outfile)
print(objektet)
print(tomarray) """