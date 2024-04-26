res = 0
score = 0
rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
for _ in range(20):
    _, point, rate = input().split()
    p = float(point)
    if rate != 'P':
      score += p
      res += p*grade[rating.index(rate)]
    
print('%.6f' % (res / score))