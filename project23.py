records = {
    "Aran": {"Math": 85, "Science": 90},
    "Mia": {"Math": 78, "Science": 82},
    "Leo": {"Math": 92, "Science": 88},
    "Mia_duplicate": {"Math": 78, "Science": 82}
}

print("Original records:", records)
print("Total records:", len(records))

print("Aran's marks:", records.get("Aran"))
print("Unknown student:", records.get("Zoe", "Not found"))

records["Zoe"] = {"Math": 70, "Science": 75}
records["Aran"]["Math"] = 88

removed = records.pop("Mia_duplicate")
print("Removed duplicate:", removed)

del records["Zoe"]

print("Total records after cleaning:", len(records))

for name, subjects in records.items():
    print(name, "->", subjects)