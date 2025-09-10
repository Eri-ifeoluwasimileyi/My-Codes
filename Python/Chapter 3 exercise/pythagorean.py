for first_side in range(1, 21):

	for second_side in range(first_side, 21):

		for hypotenuse in range(second_side, 21):

			if first_side **2 + second_side **2 == hypotenuse **2:
				print(f'Pythagorean triple: {first_side},{second_side},{hypotenuse}')
