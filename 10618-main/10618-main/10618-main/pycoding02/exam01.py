math = float(input('수학 점수:'))
kor = float(input('국어 점수:'))
info = float(input('정보 점수:'))
total=float(math+kor+info)
aver=float((math+kor+info)/3)

if aver >= 90 :
  print('등급A') 
elif aver >= 80 :
  print('등급B')
elif aver < 80 and math >= 30 and kor >=30 and info >=30:
  print('등급C')
elif aver < 80 and math <30 or kor <30 or info <30:
  print('등급F')
