import csv
points = 0
with open('quis.csv') as myFile:
  reader = csv.reader(myFile, delimiter=';')
  dict_reader = csv.DictReader(myFile, delimiter=';')
  for row in reader:
    data = dict(Вопрос=row[0],a=row[1],b=row[2],c=row[3])
    print(data)
    right = dict(righ=row[4])
    print(right)
    answer = str(input('Введите ответ на вопрос: '))
    if data.get(answer)  == right.get('righ'):
      points = points + 5
  print('У вас ', points, ' баллов!')
  if points >= 40 and points < 50:
    print('У вас оценка D.')
  elif points >= 50 and points < 70:
    print('У вас оценка C.')
  elif points >= 70 and points < 90:
    print('У вас оценка B.')
  elif points >= 90:
    print('У вас оценка A.')
  else:
    print('Похоже, вы недобрали проходной балл. В следующий раз получится!')
    



