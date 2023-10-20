# Question 10:
parcours=[dorian]
for i in range(10):
    parcours.append(get_max(get_five_more_close(parcours[i])))
print(parcours)
