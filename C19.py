# Continental-Summary-of-Covid-19-Pandemic
>>> Continents = {'Africa', 'Asia', 'America', 'Europe', 'Oceania'}
>>> print(Continents)
{'America', 'Europe', 'Asia', 'Africa', 'Oceania'}
>>> Africa = {'Total Cases: 49,421, Discharged Cases: 19080, Deaths: 1561, Active Cases: 28851, MIN: Nigeria: 7839, MAX: South Africa: 23615, MEAN: 16474'}
>>> Asia = {'Total Cases: 385,740, Discharged Cases: 258989, Deaths: 13352, Active Cases: 113352, MIN: China: 82985, MAX Turkey: 157814, MEAN: 128580'}
>>> America = {'Total Cases: 2158857, Discharged Cases: 655342, Deaths: 130326, Active Cases: 1374132, MIN: Brazil: 370060, MAX: USA: 1703118, MEAN: 719619'}
>>> Europe = {'Total Cases: 866065, Discharged Cases: 457737, Deaths: 63531, Active Cases: 344981, MIN: Italy: 230158, MAX: Russia: 353427, MEAN: 288688'}
>>> Oceania = {'Total Cases: 8788, Discharged Cases: 8125, Active Cases: 535, MIN: Guam: 166, MAX: Australia: 7118, MEAN: 2929'}
>>> Input_Continents = ['Which continent Covid-19 summary will you like to see?:']
>>> print(Input_Continents)
['Which continent Covid-19 summary will you like to see?:']
>>> if Input_Continents is Africa:
	print(Africa)
elif Input_Continents is Asia:
	print(Asia)
elif Input_Continents is America:
	print(America)
elif Input_Continents is Europe:
	print(Europe)
elif Input_Continents is Oceania:
	print(Oceania)
else:
	stop
