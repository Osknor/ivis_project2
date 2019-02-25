import xlrd
import json
import csv
lander = ['Argentina', 'Australia', 'Brazil', 'Chile', 'China', 'Colombia', 'Egypt', 'Georgia', 'India', 'Iraq', 'Japan', 'Jordan', 'Mexico', 'Moldova', 'Morocco', 'New Zealand', 'Peru','Poland', 'Romania', 'Russian Federation', 'Serbia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Taiwan', 'Turkey', 'Ukraine', 'United States', 'Uruguay']
array =  [
["Be_willing_to_fight_in_war_for_your_country.xls", 1,"war"],
["Having_a_strong_leader (1).xls", 2,"leader"],
["How_proud_of_nationality.xls", 2,"proud"],
["Interested_in_politics.xls", 2 ,"politics"],
["Men_make_better_political_leaders.xls", 2, "better"],
["More_emphasis_on_technology.xls", 1, "tech" ],
["Most_people_can_be_trusted (1).xls", 1, "trust" ],
["When_jobs_are_scare_men_should_have_more_right_to_a_job_tha.xls", 1, "jobs"]
]
tomarray = []
objektet = [0]*len(lander)
header = ["country","location"]
for item in array:
    header.append(item[2])
with open('countries.txt', newline='') as countries:
    dat = csv.DictReader(countries)
    dit = list(dat)
    print(dit)
    for i in range(0,len(lander)):
        objektet[i] = {"country":lander[i]}
        for j in range(len(dit)):
            if dit[j]['name'] == lander[i]:
                objektet[i].update({"location":{"latitude":dit[j]['latitude'],"longitude":dit[j]['longitude']}})
        for item in array:
            objektet[i].update({item[2]:"No data"})
for bok in array:
    inteurug = True
    workbook = xlrd.open_workbook("2005/"+bok[0])
    worksheet = workbook.sheet_by_index(0)
    indexet = 8
    tomarray.append(worksheet.row(3)[1].value)
    while inteurug:
        var1 = worksheet.row(indexet)[0].value
        print(var1 == 'Uruguay')
        print(var1)
        if var1 == 'Uruguay':
            inteurug = False
        if var1 == 'Russia':
            var1 ='Russian Federation'
        var2 = worksheet.row(indexet)[2].value
        if (bok[1] == 2):
            var2 += worksheet.row(indexet)[3].value
        indexet += 1
        objektet[lander.index(var1)].update({bok[2]:var2})
        print(var1)


with open('20055.csv', mode='w', newline='') as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=header)

    writer.writeheader()
    for item in objektet:
        writer.writerow(item)

        
with open('2005.json', 'w') as outfile:
    json.dump(objektet, outfile)
print(objektet)
print(tomarray)