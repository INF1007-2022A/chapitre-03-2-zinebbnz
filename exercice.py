#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	power= (voltage**2)/resistance
	return power

def orthogonal(v1, v2):

	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	if v1[0] * v2[0] + v1[1] * v2[1] == 0:
		return True


def average(values):

	sum_v=0
	positive_nb=0
	for v in values:
		if v>=0 :

			sum_v+= v
			positive_nb+=1

		else: print('toutes les valeurs sont négatives')

	moyenne= sum_v/positive_nb

	return moyenne
	# La variable v contient une valeur de la liste.

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		if value >= 20:
			billet_de_20 = value // 20

		elif value >= 10:
			billet_de_10 = value // 10

		elif value >= 5:
			billet_de_5 = value // 5

		elif value >= 1:
			billet_de_1= value // 1

	return (billet_de_20, billet_de_10, billet_de_5, billet_de_1);

def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
