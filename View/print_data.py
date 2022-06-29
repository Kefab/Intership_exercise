def print_data(employee_a, employee_b, number_of_matches):
    
    names = [employee_a.name,employee_b.name]
    names.sort()
    print(f'{names[0]} - {names[1]}: {number_of_matches}')