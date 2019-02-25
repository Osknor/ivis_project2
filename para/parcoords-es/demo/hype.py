import xlrd
import json
import csv
lander = ['Argentina', 'Australia', 'Brazil', 'Chile', 'China', 'Colombia', 'Egypt', 'Georgia', 'India', 'Iraq', 'Japan', 'Jordan', 'Mexico', 'Moldova', 'Morocco', 'New Zealand','Nigeria','Pakistan','Peru','Philippines','Poland', 'Romania', 'Russian Federation', 'Serbia', 'Slovenia', 'South Africa', 'South Korea', 'Spain', 'Sweden', 'Taiwan', 'Turkey', 'Ukraine', 'United States', 'Uruguay']

array =  [
["1.xls", 1,"war","Be_willing_to_fight_in_war_for_your_country.xls"],
["2.xls", 2,"leader","Having_a_strong_leader (1)"],
["3.xls", 2,"proud","How_proud_of_nationality.xls"],
["4.xls", 2 ,"politics","Interested_in_politics.xls"],
["5.xls", 2, "better","Men_make_better_political_leaders.xls"],
["6.xls", 1, "tech","More_emphasis_on_technology.xls"],
["7.xls", 1, "trust" ,"Most_people_can_be_trusted (1).xls"],
["8.xls", 1, "jobs","When_jobs_are_scare_men_should_have_more_right_to_a_job_tha.xls"]
]
tomarray = []
objektet = [0]*len(lander)
header = ["country","longitude","latitude","continent"]
for item in array:
    header.append(item[2])
with open('../../../countries.txt', newline='') as countries:
    dat = csv.DictReader(countries)
    dit = list(dat)
    print(dit)
    with open('actualcont.csv',newline='') as continents:
        fat = csv.DictReader(continents)
        fit = list(fat)
        print(fit[0])
        for i in range(0,len(lander)):
            objektet[i] = {"country":lander[i]}
            for j in range(len(dit)):
                if dit[j]['name'] == lander[i] or (dit[j]['name'] == 'Russia' and lander[i]== 'Russian Federation'):
                    objektet[i].update({"latitude":dit[j]['latitude']})
                    objektet[i].update({"longitude":dit[j]['longitude']})
            for j in range(len(fit)):
                if fit[j]['country'] == lander[i] or (fit[j]['country'] == 'Russia' and lander[i]== 'Russian Federation'):
                    objektet[i].update({"continent":fit[j]['continent']})
            for item in array:
                objektet[i].update({item[2]:"No data"})
for bok in array:
    inteurug = True
    workbook = xlrd.open_workbook("../../../1995/"+bok[0])
    worksheet = workbook.sheet_by_index(0)
    indexet = 8
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


with open('20000.csv', mode='w', newline='') as csv_file:

    writer = csv.DictWriter(csv_file, fieldnames=header)

    writer.writeheader()
    for item in objektet:
        writer.writerow(item)

        
with open('2005.json', 'w') as outfile:
    json.dump(objektet, outfile)
print(objektet)
print(tomarray)