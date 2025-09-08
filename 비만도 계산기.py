a = float(input("당신의 키를 입력해 주세요"))
b = float(input("당신의 몸무게를 입력해 주세요"))
c = b/((0.01*a)**2)
print(f'당신의 비만도는 {c} 입니다')

if c < 18.5 :
    print("저체중 입니다")
elif c <= 22.9 :
    print("정상체중 입니다")
elif c <= 24.9 :
    print("과체중 입니다")
elif c <=29.9 :
    print("경도비만 입니다")
elif c <= 34.9 :
    print("중증도 비만입니다")
else :
    print("고도 비만입니다")