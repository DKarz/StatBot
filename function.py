from scipy.stats import chi2
alpha  = 5
def calc(a,m,x):
  if m == 1:
    s = 0
    aver = sum(x[0])/len(x[0])
    for i in x[0]:
      s += (i - aver)**2
    s *= 1/(len(x[0])-1)
    s = s**0.5
    df = 1
    ans = chi2.ppf(a/2, df)
    ans1 = chi2.ppf(1-a/2, df)
    print("form:",ans)
    print("to:",ans1)
    if ans1 > s and ans < s:
      print("Do not reject, insignificant")
    else:
      print("Reject, significant")
  else:
    sum1 = []
    sum2 = []
    for row in x:
      sum1.insert(len(sum1),sum(row))
    for i in range(len(x[0])):
      temp = 0
      for j in range(m):
        temp += x[j][i]
      sum2.insert(len(sum2), temp)
    ex = [[]]
    row = 0
    all = sum(sum1)
    for i in range(m):
      for k in range(len(x[i])):
        ex[row].insert(len(x[row]), (sum1[i]*sum2[k])/all)
      ex.insert(len(ex),[])
      row += 1
    ex.pop()
    ch2 = 0
    for i in range(m):
      for j in range(len(x[0])):
        ch2 += (x[i][j] - ex[i][j])**2/ex[i][j]
    output = "chi^2 = " + str(ch2)
    print(output)
    df = (len(x[0])-1)*(m-1)
    ans = chi2.ppf(a/2, df)
    ans1 = chi2.ppf(1-a/2, df)
    print("form:",ans)
    print("to:",ans1)
    if ans1 > ch2 and ans < ch2:
      print("Do not reject, insignificant")
    else:
      print("Reject, significant")
    return output

def perc(O, p, a):
  E = []
  summ = sum(O)
  for i in range(len(O)):
    E.insert(i, (p[i]/100)*summ)
  sum1=0
  for i in range(len(O)):
    sum1+=((O[i]-E[i])**2)/E[i]
  print("chi^2 =", sum1)
  df = len(O)-1
  ans = chi2.ppf(a/2, df)
  ans1 = chi2.ppf(1-a/2, df)
  print("form:",ans)
  print("to:",ans1)
  if ans1 > sum1 and ans < sum1:
    print("Do not reject, insignificant")
  else:
    print("Reject, significant")

def chi1(O, E):
  sum = 0
  for i in range(len(O)):
    sum += ((O[i] - E[i]) ** 2) / E[i]
  return str(sum)

