import array as arr

leap_year = arr.array('i')

print("year")
End_year = int(input())
End_year += 4

print(str(End_year))

year_count = 0
year_count += 1
year = 2016
while year < End_year:
    if year_count == 1:
        leap_year.append(year)
        print(leap_year)
    if year_count == 4:
        year_count = 0
    year_count += 1
    if year == End_year:
        break
    year += 1

print(leap_year)