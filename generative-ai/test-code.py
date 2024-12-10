import json



def genReport(dd):
    dottedline = '-'*70
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:3}'
    print('CLASS REPORT')
    print(dottedline)
    print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    print(dottedline)
    for regid in dd.keys():
        name = dd[regid]['name']
        age  = dd[regid]['age']
        regid = dd[regid]['regid']
        phy = dd[regid]['phy']
        chem = dd[regid]['chem']
        math = dd[regid]['math']
        bio = dd[regid]['bio']
        avg = dd[regid]['avg']
        rank = dd[regid]['rank']
        print(template.format( regid, name, age,phy, chem, math, bio, avg, rank))
    print(dottedline)

def write2file(dd, path):
    pass



path = r"C:\\Users\\mindf\\Desktop\\step\\day_05\\case\\students.csv"
f = open(path, "r")
content = f.readlines()
f.close()

print(content)
print('-'*60 + ' > First Step')



classdict = {}
coldata = content[0]


columns = [item.strip() for item in coldata.split(',')]

for rowdata in content[1:]:
    rows = [item.strip() for item in rowdata.split(',')]
    studdict = dict(zip(columns, rows))
    classdict.setdefault(studdict['regid'], studdict)

print(classdict)
print('-'*60 + ' > Second Step')



for regid in classdict.keys():
    sum_of_subj_marks = 0
    for key in ['phy','chem', 'math', 'bio']:
        sum_of_subj_marks += float(classdict[regid][key])
    classdict[regid]['avg'] = sum_of_subj_marks / 4


print(classdict)
print('-'*60 + ' > Third Step')



avgs = [classdict[regid]['avg'] for regid in classdict.keys()]
avgs = list(set(avgs))
avgs.sort(reverse=True)
print(avgs)

rank = 1
for avg in avgs:
    for regid in classdict.keys():
        if(classdict[regid]['avg'] == avg):
            classdict[regid]['rank'] = rank
    rank += 1

print(classdict)
print('-'*60 + ' > Fourth Step')



path = r"C:\Users\Purushotham\Desktop\oracle-june\day_03\case\students_updated.csv"
f = open(path, "w")
f.write(coldata)
for regid in classdict.keys():
    r = list(zip(*classdict[regid].items()))
    rowdata = ','.join([str(item) for item in r[1]]) + '\n'
    f.write(rowdata)

f.close()

print(classdict)
print('-'*60 + ' > Fifth Step')



genReport(classdict)

with open("report.json", "w") as report:
    json.dump(classdict, report)


