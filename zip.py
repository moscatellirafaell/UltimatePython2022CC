li_frutas = ['Banana', 'Maçã', 'Morango', 'Mamão']
qtd_frutas = [10, 8, 7, 10]
rep_list = [(f, q) for f, q in zip(li_frutas, qtd_frutas) if q < 10]

for id, frutas in enumerate(zip(li_frutas, qtd_frutas)):
    print(f'{frutas[0]:10}[id:{id}] - qtd: {frutas[1]:2}')

print(f'Reposição: {rep_list}')
