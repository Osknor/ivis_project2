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
objektet = [[-1]*9]*(len(lander)+1)
print(objektet)
tomarray = []

objektet[0][0] = "country"
for i in range(len(array)):
    objektet[0][i+1] = array[i][2]
for i in range(len(lander)):
    objektet[i+1][0] = lander[i]
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
        objektet[lander.index(var1)+1][array.index(bok)] = var2
        print(var1)


with open('2005.csv', mode='w') as outie:
    csvn = csv.writer(outie, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for row in objektet:
    csvn.writerow(row)

#with open('2005.json', 'w') as outfile:
#    json.dump(objektet, outfile)
print(objektet)
print(json.loads(objektet),"ble")
