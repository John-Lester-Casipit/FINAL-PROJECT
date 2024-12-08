prelim=eval(input('Enter your grade in prelim :'))
midterm=eval(input('Enter your grade in midterm :'))
semifinal=eval(input('Enter your grade in semifinal :'))
final=eval(input('Enter your grade in final :'))
quiz=eval(input('Enter your grade in quiz :'))
proj=eval(input('Enter your grade in project :'))

if (prelim >= 65 and prelim <=100) and (midterm >= 65 and midterm <=100) and (semifinal >=65 and semifinal <=100) and (final >= 65 and final <=100) and (quiz >= 65 and quiz <=100) and (proj >= 65 and proj <=100):
	
	grade = (prelim * .15) + (midterm * .15) + (semifinal * .15) + (final * .15) + (quiz * .25) + (proj * .15)

	if grade >= 75:
		print('CONGRATULATONS, YOU PASSED WITH AN AVERAGE GRADE OF',grade,)

	else:
		print('SORRY YOU FAILED')
		print(f'your average is {grade}')
else:
	print('INVALID GRADE')

	