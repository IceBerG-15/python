# Candidate Elimination
#dataset
dataset = [
    ['japan','honda','blue','2020','eco','yes'],
    ['japan','toyota','blue','2019','eco','yes'],
    ['usa','audi','blue','2018','eco','no'],
    ['japan','honda','white','2023','eco','yes'],
    ['japan','toyota','green','2016','eco','yes']
]
def candidate(dataset):
    specific_hypo = dataset[0][:-1]
    general_hypo = [['?' for _ in range(len(specific_hypo))] for _ in range(len(specific_hypo))]
    for data in dataset:
        if data[-1] == 'yes':
            for i in range(len(specific_hypo)):
                if data[i] != specific_hypo[i]:
                    specific_hypo[i] = '?'
                    general_hypo[i][i] = '?'
        else:
            for i in range(len(specific_hypo)):
                if data[i] != specific_hypo[i]:
                    general_hypo[i][i] = specific_hypo[i]
                else:
                    general_hypo[i][i] = '?'
    return specific_hypo,general_hypo

specific,general = candidate(dataset)
print('specific: ',specific)
print('general: ')
for i in general:
    print(i)
    
    