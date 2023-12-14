from emplacement import * 

class EmplacementVoiture(Emplacement):
    def __init__(self, numero_place, type_emplacement):
        super().__init__(numero_place)
        self.type_emplacement = type_emplacement

