info = {}

info["Name"] = "Sandy"
info["Occupation"] = "Hacker"

print(info)

info["Occupation"] = "Manager"

print(info)

print(info.get("job",None))

print(info.pop("job",None))

print(info.pop("Occupation"))

print(info)