import inflect

p = inflect.engine()

family = []

while True:
        try:
                kname = input("Name: ")
                family.append(kname)
        except EOFError:
                print("Adieu, adieu, to",p.join(family))
                break
