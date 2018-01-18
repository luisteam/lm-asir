val=float(input("Cantidad total: "))
val2=float(input("Cantidad entregada: "))
cambio=val2-val
print("Cantidad a devolver: %.2f €" % (cambio))

bil50=cambio/50
bil20=cambio/20
mon2=cambio/2
mon50=cambio/0.50
mon20=cambio/0.20
mon10=cambio/0.10
mon05=cambio/0.05
mon02=cambio/0.02
mon01=cambio/0.01

if bil50 >= 1:
	if bil50 >=2:
		print("%d billetes de 50€" % (bil50))
	else:
		print("%d billete de 50€" % (bil50))
	
	bil500=cambio-(int(bil50)*50)
	bil501=bil500/20
	if bil501 >=1:
		if bil501 >=2:
			print("%d billetes de 20€" % (bil501))
		else:
			print("%d billete de 20€" % (bil501))
	bil502=bil500-(int(bil501)*20)
	bil503=bil502/2
	if bil503 >=1:
		if bil503 >=2:
			print("%d monedas de 2€" % (bil503))
		else:
			print("%d moneda de 2€" % (bil503))
	bil504=bil502-(int(bil503)*2)
	bil505=bil504/0.50
	if bil505 >=1:
		if bil505 >=2:
			print("%d monedas de 0.50€" % (bil505))
		else:
			print("%d moneda de 0.50€" % (bil505))
	bil506=bil504-(int(bil505)*0.50)
	bil507=bil506/0.20
	if bil507 >=1:
		if bil507 >=2:
			print("%d monedas de 0.20€" % (bil507))
		else:
			print("%d moneda de 0.20€" % (bil507))
	bil508=bil506-(int(bil507)*0.20)
	bil509=bil508/0.10
	if bil509 >=1:
		if bil509 >=2:
			print("%d monedas de 0.10€" % (bil509))
		else:
			print("%d moneda de 0.10€" % (bil509))
	bil510=bil508-(int(bil509)*0.10)
	bil511=bil510/0.05
	if bil511 >=1:
		if bil511 >=2:
			print("%d monedas de 0.05€" % (bil511))
		else:
			print("%d moneda de 0.05€" % (bil511))
	bil512=bil510-(int(bil511)*0.05)
	bil513=bil512/0.02
	if bil513 >=1:
		if bil513 >=2:
			print("%d monedas de 0.02€" % (bil513))
		else:
			print("%d moneda de 0.02€" % (bil513))
	bil514=bil512-(int(bil513)*0.02)
	bil515=bil514/0.01
	if bil515 >=1:
		if bil515 >=2:
			print("%d monedas de 0.01€" % (bil515))
		else:
			print("%d moneda de 0.01€" % (bil515))

elif bil20 >=1:
	if bil20 >=2:
		print("%d billetes de 20€" % (bil20))
	else:
		print("%d billete de 20€" % (bil20))
	bil202=cambio-(int(bil20)*20)
	bil203=bil202/2
	if bil203 >=1:
		if bil203 >=2:
			print("%d monedas de 2€" % (bil203))
		else:
			print("%d moneda de 2€" % (bil203))
	bil204=bil202-(int(bil203)*2)
	bil205=bil204/0.50
	if bil205 >=1:
		if bil205 >=2:
			print("%d monedas de 0.50€" % (bil205))
		else:
			print("%d moneda de 0.50€" % (bil205))
	bil206=bil204-(int(bil205)*0.50)
	bil207=bil206/0.20
	if bil207 >=1:
		if bil207 >=2:
			print("%d monedas de 0.20€" % (bil207))
		else:
			print("%d moneda de 0.20€" % (bil207))
	bil208=bil206-(int(bil207)*0.20)
	bil209=bil208/0.10
	if bil209 >=1:
		if bil209 >=2:
			print("%d monedas de 0.10€" % (bil209))
		else:
			print("%d moneda de 0.10€" % (bil209))
	bil210=bil208-(int(bil209)*0.10)
	bil211=bil210/0.05
	if bil211 >=1:
		if bil211 >=2:
			print("%d monedas de 0.05€" % (bil211))
		else:
			print("%d moneda de 0.05€" % (bil211))
	bil212=bil210-(int(bil211)*0.05)
	bil213=bil212/0.02
	if bil213 >=1:
		if bil213 >=2:
			print("%d monedas de 0.02€" % (bil213))
		else:
			print("%d moneda de 0.02€" % (bil213))
	bil214=bil212-(int(bil213)*0.02)
	bil215=bil214/0.01
	if bil215 >=1:
		if bil215 >=2:
			print("%d monedas de 0.01€" % (bil215))
		else:
			print("%d moneda de 0.01€" % (bil215))

elif mon2 >=1:
	if mon2 >=2:
		print("%d monedas de 2€" % (mon2))
	else:
		print("%d moneda de 2€" % (mon2))
	bil204=cambio-(int(mon2)*2)
	bil205=bil204/0.50
	if bil205 >=1:
		if bil205 >=2:
			print("%d monedas de 0.50€" % (bil205))
		else:
			print("%d moneda de 0.50€" % (bil205))
	bil206=bil204-(int(bil205)*0.50)
	bil207=bil206/0.20
	if bil207 >=1:
		if bil207 >=2:
			print("%d monedas de 0.20€" % (bil207))
		else:
			print("%d moneda de 0.20€" % (bil207))
	bil208=bil206-(int(bil207)*0.20)
	bil209=bil208/0.10
	if bil209 >=1:
		if bil209 >=2:
			print("%d monedas de 0.10€" % (bil209))
		else:
			print("%d moneda de 0.10€" % (bil209))
	bil210=bil208-(int(bil209)*0.10)
	bil211=bil210/0.05
	if bil211 >=1:
		if bil211 >=2:
			print("%d monedas de 0.05€" % (bil211))
		else:
			print("%d moneda de 0.05€" % (bil211))
	bil212=bil210-(int(bil211)*0.05)
	bil213=bil212/0.02
	if bil213 >=1:
		if bil213 >=2:
			print("%d monedas de 0.02€" % (bil213))
		else:
			print("%d moneda de 0.02€" % (bil213))
	bil214=bil212-(int(bil213)*0.02)
	bil215=bil214/0.01
	if bil215 >=1:
		if bil215 >=2:
			print("%d monedas de 0.01€" % (bil215))
		else:
			print("%d moneda de 0.01€" % (bil215))

elif mon50 >=1:
	if mon50 >=2:
		print("%d monedas de 0.50€" % (mon50))
	else:
		print("%d moneda de 0.50€" % (mon50))
	bil206=cambio-(int(mon50)*0.50)
	bil207=bil206/0.20
	if bil207 >=1:
		if bil207 >=2:
			print("%d monedas de 0.20€" % (bil207))
		else:
			print("%d moneda de 0.20€" % (bil207))
	bil208=bil206-(int(bil207)*0.20)
	bil209=bil208/0.10
	if bil209 >=1:
		if bil209 >=2:
			print("%d monedas de 0.10€" % (bil209))
		else:
			print("%d moneda de 0.10€" % (bil209))
	bil210=bil208-(int(bil209)*0.10)
	bil211=bil210/0.05
	if bil211 >=1:
		if bil211 >=2:
			print("%d monedas de 0.05€" % (bil211))
		else:
			print("%d moneda de 0.05€" % (bil211))
	bil212=bil210-(int(bil211)*0.05)
	bil213=bil212/0.02
	if bil213 >=1:
		if bil213 >=2:
			print("%d monedas de 0.02€" % (bil213))
		else:
			print("%d moneda de 0.02€" % (bil213))
	bil214=bil212-(int(bil213)*0.02)
	bil215=bil214/0.01
	if bil215 >=1:
		if bil215 >=2:
			print("%d monedas de 0.01€" % (bil215))
		else:
			print("%d moneda de 0.01€" % (bil215))

elif mon20 >=1:
	if mon20 >=2:
		print("%d monedas de 0.20€" % (mon20))
	else:
		print("%d moneda de 0.20€" % (mon20))
	bil208=cambio-(int(mon20)*0.20)
	bil209=bil208/0.10
	if bil209 >=1:
		if bil209 >=2:
			print("%d monedas de 0.10€" % (bil209))
		else:
			print("%d moneda de 0.10€" % (bil209))
	bil210=bil208-(int(bil209)*0.10)
	bil211=bil210/0.05
	if bil211 >=1:
		if bil211 >=2:
			print("%d monedas de 0.05€" % (bil211))
		else:
			print("%d moneda de 0.05€" % (bil211))
	bil212=bil210-(int(bil211)*0.05)
	bil213=bil212/0.02
	if bil213 >=1:
		if bil213 >=2:
			print("%d monedas de 0.02€" % (bil213))
		else:
			print("%d moneda de 0.02€" % (bil213))
	bil214=bil212-(int(bil213)*0.02)
	bil215=bil214/0.01
	if bil215 >=1:
		if bil215 >=2:
			print("%d monedas de 0.01€" % (bil215))
		else:
			print("%d moneda de 0.01€" % (bil215))

elif mon10 >=1:
	if mon10 >=2:
		print("%d monedas de 0.10€" % (mon10))
	else:
		print("%d moneda de 0.10€" % (mon10))
	bil210=cambio-(int(mon10)*0.10)
	bil211=bil210/0.05
	if bil211 >=1:
		if bil211 >=2:
			print("%d monedas de 0.05€" % (bil211))
		else:
			print("%d moneda de 0.05€" % (bil211))
	bil212=bil210-(int(bil211)*0.05)
	bil213=bil212/0.02
	if bil213 >=1:
		if bil213 >=2:
			print("%d monedas de 0.02€" % (bil213))
		else:
			print("%d moneda de 0.02€" % (bil213))
	bil214=bil212-(int(bil213)*0.02)
	bil215=bil214/0.01
	if bil215 >=1:
		if bil215 >=2:
			print("%d monedas de 0.01€" % (bil215))
		else:
			print("%d moneda de 0.01€" % (bil215))

elif mon05 >=1:
	if mon05 >=2:
		print("%d monedas de 0.05€" % (mon05))
	else:
		print("%d moneda de 0.05€" % (mon5))
	bil212=cambio-(int(mon05)*0.05)
	bil213=bil212/0.02
	if bil213 >=1:
		if bil213 >=2:
			print("%d monedas de 0.02€" % (bil213))
		else:
			print("%d moneda de 0.02€" % (bil213))
	bil214=bil212-(int(bil213)*0.02)
	bil215=bil214/0.01
	if bil215 >=1:
		if bil215 >=2:
			print("%d monedas de 0.01€" % (bil215))
		else:
			print("%d moneda de 0.01€" % (bil215))

elif mon02 >=1:
	if mon02 >=2:
		print("%d monedas de 0.02€" % (mon02))
	else:
		print("%d moneda de 0.02€" % (mon02))
	bil212=cambio-(int(mon02)*0.02)
	bil213=bil212/0.01
	if bil213 >=1:
		if bil213 >=2:
			print("%d monedas de 0.01€" % (bil213))
		else:
			print("%d moneda de 0.01€" % (bil213))

elif mon01 >=1:
	if mon01 >=2:
		print("%d monedas de 0.01€" % (mon01))
	else:
		print("%d moneda de 0.01€" % (mon01))