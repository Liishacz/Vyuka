import random
import time

#uvodni otazka
def otazka():
	print("Je tu obri vyzva! Chci spocitat pruhy na zebre. Jdes do toho se mnou?")

#otázka na počítání pruhů	
	while(True):
		odpoved = input()
		if odpoved.lower() == "ano":
			print("Tak jdeme na to!")
			print('')
			break
		elif odpoved.lower() == "ne":
			print("Skoda, mohla to byt zabava - nechces se rozmyslet?")
		else:
			print("Musis zadat ano, nebo ne, jen tak poznam, ze chces.")

#Kolik má zebra pruhů?
def zebra(cislo_poctu):
	cislo = random.randint(1,26)
	time.sleep(1)


#podmínka počítání pruhů			
	if cislo==22:
		print(f'Pri pokusu {cislo_poctu} si napocital {cislo} pruhu. To je ale malo.')
	elif cislo==25:
		print(f'Pri pokusu {cislo_poctu} si napocital {cislo} pruhu. Spocital jsi vsechny pruhy!')
	else:
		print(f'Nepodarilo se ti spocitat vsechny pruhy, tvuj pokus je {cislo_poctu}, zkusíme to jeste jednou!')

#otazka na věštbu
def vestecka_koule():
	print("Za odmenu ti vyvestim budoucnost, ano?")
	
	while(True):
		odpoved = input()
		if odpoved.lower() == "ano":
			print("Usad se pohodlne na zidli a drz se, bude to jizda!")
			print('')
			break
		elif odpoved.lower() == "ne":
			print("Ty nechces vedet, co te ceka? Tak dobre, ahoj priste.")
			quit()
		else:
			print("Musis zadat ano, nebo ne, jen tak poznam, ze chces.")


#Věštba - definice funkce "úmrtí"
def umrti(poradi_vestby):
	leta = random.randint(18,120)
	time.sleep(1)

#podmínka umrti
	if leta in range(17,55):
		print(f'Při věštbě č. {poradi_vestby} jsem zjistila, že umřete velmi mladý. Okolo roku {leta}.')
	elif leta in range(55,95):
		print(f'Při věštbě č. {poradi_vestby} jsem zjistila, že umřete v průměreném věku. Okolo roku {leta}.')
	else:
		print(f'Při věštbě č. {poradi_vestby} jsem zjistila, že umřete až budete hodně starý. Okolo roku {leta}.')

#Věštba - definice funkce "narození dítěte"
def narozeni(poradi_vestby):
	roky = random.randint(18,45)
	time.sleep(1)

#podminka narozeni
	if roky in range(17,25):
		print(f'Při věštbě č. {poradi_vestby} jsem zjistila, že budete mít dítě velmi mladý. Okolo roku {roky}.')
	elif roky in range(25,40):
		print(f'Při věštbě č. {poradi_vestby} jsem zjistila, že budete mít dítě průměreném věku. Okolo roku {roky}.')
	else:
		print(f'Při věštbě č. {poradi_vestby} jsem zjistila, že budete mít dítě až budete hodně starý. Okolo roku {roky}.')

#definice Mainu - zebra + věštba
def __main__():
	otazka()
	for pocitani in range(1,6):
		zebra(pocitani)
	print('')
	vestecka_koule()
	for vestba in range(1,6):
		umrti(vestba)
	print('')
	for vestba in range(1,6):
		narozeni(vestba)


__main__()