# 1.2 Practice

#1
# 身体质量指数（BMI，Body Mass Index）是国际上常用的衡量人体肥胖程度和是否健康的重要标准，
# 计算公式为：BMI=体重/身高的平方（国际单位kg/㎡）。

weight, height = eval(input())

bmi = weight / height ** 2
print('Your BMI is {0:.1f}'.format(bmi))
if bmi < 18.5:
    print('too thin')
elif bmi < 24:
    print('normal')
elif bmi < 28:
    print('overweight')
else:
    print('fat')
    

