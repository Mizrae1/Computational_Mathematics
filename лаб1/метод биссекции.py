an = 0 #Левая граница (будем считать известной)
bn = 1 #Правая граница (будем считать известной)
epsilon = 0.1 

def function(x):
	"========Функция расчета f(x) = x^3 - 3x^2 + 12x - 12 = 0 ===================="
	f = x ** 3 - 3 * x ** 2 - 24 * x + 10 
	return f

def border(fab, func):
	"========Функция замены границы на посчитанную медиану========================"
	global bn, an
	if fab > 0 and func == 1:
		bn = median
		return bn
	if fab < 0 and func == 1:
		an = median
		return an
	if fab > 0 and func == 0:
		an = median
		return an
	if fab < 0 and func == 0:
		bn = median
		return bn	

def check(module, epsilon, fab, fbn):
	"========Функция проверки конца алгоритма====================================="
	if module < epsilon :
		print("========================================================================")
		print("При границах: a = ", "%.5f" % an, "и b = ", "%.5f" % bn, ", |an - bn| -", "%.5f" % module, "< 0.001")
		print("========================================================================")
		exit()

	if abs(fan) < epsilon :
		print("========================================================================")
		print("При границах: a = ", "%.5f" % an, "и b = ", "%.5f" % bn, ", |f(a)| -", "%.5f" % abs(fan), "< 0.001")
		print("========================================================================")
		exit()

	if abs(fbn) < epsilon :
		print("========================================================================")
		print("При границах: a = ", "%.5f" % an, "и b = ", "%.5f" % bn, ", |f(b)| -", "%.5f" % abs(fbn), "< 0.001")
		print("========================================================================")
		exit()

fan = function(an)
fbn = function(bn)
module = abs(an - bn)

#========Проверка фунции f(x) на возрастанеи(убывание) =======================
if (fan < 0) and (fbn > 0):
	func = 1
else:
	func = 0

#========Шапка таблицы с полученными данными==================================
print("An           |Bn           |f(An)         |f(Bn)        ||an - bn|")
n = 1
median = (an + bn) / 2
while (module > epsilon) and (abs(fan) > epsilon) and (abs(fbn) > epsilon):
	fan = function(an)
	fbn = function(bn)
	module = abs(an - bn)
#========Таблица с полученными данным=========================================
#	print("%.5f" % an, "     ", "%.5f" % bn, "     ", "%.5f" % fan,"     ","%.5f" % fbn,"     ", "%.5f" % module)
	print("  ",n, "Итерация\nМедиана = (", "%.3f" % an, "+", "%.3f" % bn, ") / 2 =","%.5f" % median, "\nF(a) = ", "%.3f" % fan, "\nF(b) = ", "%.3f" % fbn,"\n|an - bn| = ", "%.5f" % module)
	n += 1
	check(module,epsilon, fan, fbn)
	median = (an + bn) / 2 # Считаем медиану
	fab = function(median)
	border(fab, func)