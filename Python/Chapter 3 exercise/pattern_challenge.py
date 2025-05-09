stars = 10

for rows in range(1, stars + 1):
    
    first_pattern = '*' * rows

   
    second_pattern = '*' * (stars - rows + 1)

    
    third_pattern = (rows - 1) + '*' * (stars - rows + 1)

  
    fourth_pattern=  (stars - rows) + '*' * rows

    
    print(f'{first_pattern:<10}   {second_pattern:<10}   {third_pattern:<10}   {fourth_pattern}', end='')

	
