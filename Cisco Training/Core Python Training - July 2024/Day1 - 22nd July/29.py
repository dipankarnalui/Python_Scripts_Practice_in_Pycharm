data="north-sales-10-20-30-40-50-blr-chn"
print("Total = ",sum(list(map(int,[x for x in data.split("-") if x.isdigit()]))))

