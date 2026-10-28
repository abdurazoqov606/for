mevalar = ['olma','anor']
meva=input("meva nomini kirit galvars: ")
if meva in mevalar:
    print("bu meva bor barakalla ")

else:
    mevalar.insert(0,[meva])

print(mevalar)