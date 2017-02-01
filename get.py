def get_persons_closest_to_average(table):
    average = []
    all_year = 0
    for row in table:
        row[2] = int(row[2])
        average.append(row[2])
        years_added = sum(average)
    avg = years_added / sum(1 for line in table)
    closest = min(average, key=lambda x: abs(x - avg))
    closest_names = []
    for row in table:
        if row[2] == closest:
            closest_names.append(row[1])
    ui.print_result(closest_names, "\nThe closest person(s) to the average age:\n")
    return(closest_names)
