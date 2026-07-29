from typing import Dict, List


class Task:
    def __init__(self, id: str, duree: int):
        if isinstance(id, str):
            self.id = id
        else:
            raise TypeError("l'identifiant doit être une chaine de caractères")
        try:
            self.set_duree(duree)
        except  ValueError:
            print("La durée doit être un nombre entier positif")

    def get_id(self):
        return self.id

    def get_duree(self):
        return self.duree

    def set_duree(self, duree:int):
        if duree >0:
            self.duree = duree

    def __str__(self):
        return f"{self.id}.upper() : durée={self.duree}"


class PriorityTask(Task):
    def __init__(self, id: str, duree: int, priority):
        super().__init__(id, duree)
        if 0 <= priority <= 100:
            self.priority:int = priority
        else:
            raise ValueError('La priorité est un nombre entier compris entr 0 et 100')
        
    def get_priority(self):
        return self.priority

    def set_priority(self, priority:int):
        if 0 <= priority <= 100:
            self.priority = priority
        else:
            raise ValueError("La priorité est un nombre entier compris entre 0 et 100")
            
    def __str__(self):
        return f"{super().__str__()}, priorité={self.priority}"

class Constraint():
    def __init__(self):
        self.dico:Dict[str,List[str]] = {}


    def add_constraint(self,id1:str, id2:str)->None:
        if id1 not in self.dico.keys():
            self.dico[id1] = [id2]
        else:
            if id2 not in self.dico[id1]:
                self.dico[id1].append(id2)
            else:
                erreur = f"l'ID {id2} est déjà dans la liste de précédence de {id1}"
                raise ValueError(erreur)


    def print_constraint(self, id:str) -> None:
        if id not in self.dico.keys():
            print(f"{id} -> _")
        else:
            print(f"{id} -> ", end=" ")
            for id_ in self.dico[id]:
                print(f"{id_} ", end="")
            print()






def main():
    try:
        T2 = Task('T2', 100)
        T3 = PriorityTask('T3', 100, 50)
        T4 = PriorityTask('T4', 100, 60)

        constraint = Constraint()
        constraint.add_constraint('T3', T4.get_id())
        constraint.add_constraint('T3', T2.get_id())
        constraint.add_constraint('T3', T2.get_id())
        for key, value in constraint.dico.items():
            print(f"{key} = {value}")
        constraint.print_constraint('T2')
        constraint.print_constraint('T3')
    except TypeError as e:
        print(f"Erreur de type : {e}")
    except ValueError as e:
        print(f"Valeur invalide : {e}")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


if __name__ == "__main__":
    main()
