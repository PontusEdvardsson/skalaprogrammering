grundavgift = 60
pris_per_timme = 600
pris_per_km = 14.20

kostnad_a = grundavgift + pris_per_timme * 0.5 + pris_per_km * 14
kostnad_b = grundavgift + pris_per_timme * 0.75 + pris_per_km * 8.5

print("14 km pa 30 minuter kostar", kostnad_a, "kr.")
print("8.5 km pa 45 minuter kostar", kostnad_b, "kr.")
