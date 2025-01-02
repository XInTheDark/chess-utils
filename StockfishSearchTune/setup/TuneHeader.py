_input = input()

t = [int(x.strip()) for x in _input.split(',') if x.strip() != '']

print("int ", end="")
for i in range(len(t)):
    name = f"a{i+1}"
    value = t[i]
    print(f"{name}={value}{', ' if i < len(t)-1 else ';'}", end="")
print()

print("TUNE(", end="")
for i in range(len(t)):
    name = f"a{i+1}"
    print(f"{name}{', ' if i < len(t)-1 else ''}", end="")
print(");")
