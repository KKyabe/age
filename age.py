drive = input('你有沒有開過車?')
if drive != ('有') and drive != ('沒有'):
	print('只能輸入有/沒有')
#	raise SystemExit
else:
	age = input('你幾歲?')
	age = int(age)
	if drive == '有':
		if age < 18:
			print('未成年開什麼車!')
		else:
			print('好沒事')
	elif drive == '沒有':
		if age >= 18:
			print('那你怎麼不去考= =')
		if age < 18:
			print('乖乖等18歲')



