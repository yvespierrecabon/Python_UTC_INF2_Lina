l = list(range(0,10,2))
print(l)
print(l[-1])
print(l[-4:4])
print([i for i in l if i %4 == 0])

def carre(n):
    print(n**2)

carre(5)
# carre('a')

notes = {'etu1':12}
print(notes.get('etu1'))
print(notes.get('etu1',0))
print(notes.get('etu2',0))
print(notes.get('etu2'))

def surprise(func):
    def wrapper(*args, **kwargs):
        print(f"Nb args = {len(args)}, Nb kwargs = {len(kwargs)}")
        res = func(*args)
        return res
    return wrapper

@surprise
def fonction(*args):
    if len(args)==1:
        return str(args[0])
    else:
        return str(args[0]) + fonction(*args[1:])

print(fonction(2,'toto'))
print(fonction(1, 2,a=12))