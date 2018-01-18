from fechas import calcular_dia_juliano,leer_fecha

dia1,mes1,año1=leer_fecha()
dia2,mes2,año2=leer_fecha()

if año1==año2:
	intervalo=calcular_dia_juliano(dia1,mes1,año1)-calcular_dia_juliano(dia2,mes2,año2)
	print("Han pasado %d dias." % abs(intervalo))