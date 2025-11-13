f1 = open("groups.xml", "r", encoding="utf-8")
data1 = f1.readlines()
f1.close()

f2 = open("login.xml", "r", encoding="utf-8")
data2 = f2.readlines()
f2.close()

all_lines = data1 + data2

unique = []
for l in all_lines:
    if l not in unique:
        unique.append(l)

out = open("result_Tysiak.csv", "w", encoding="utf-8")
for l in unique:
    out.write(l)
out.close()