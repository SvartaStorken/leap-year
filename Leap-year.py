import array as arr

leap_year = arr.array('i')

print("year")
End_year = int(input())
End_year += 3

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



#leap_year = arr.array('i', [2016])



#leap_year.append(2020)
#leap_year.append(2024)

#print(leap_year[0])
#print(leap_year[1])
#print(leap_year[2])

print(leap_year)