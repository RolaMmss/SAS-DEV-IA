# **`Exercice`**
# - Créer des classes: boite à outils, marteau, tournevis, clou, visse 
# - Instanciez une boîte à outils, un tournevis, et un marteau.
# - Placez le marteau et le tournevis dans la boîte à outils.
# - Instanciez une visse, et serrez-la avec le tournevis. Affichez la vis avant et après avoir été serrée.
# - Instanciez un clou, puis enfoncez-le avec le marteau. Affichez le clou avant et après avoir été enfoncé.
# - Une boite à outil possède 5 emplacements. (classe attributs)
# - Régulièrement le constructeur des boites à outils sort un nouveau modèle qui permet d'etendre la capacité des boites à outils de 1 emplacement.



class BoiteAOutil:
    emplacement = 5

    def __init__(self, contenu=[]):
        self.contenu = contenu

    def add_tool(self,tool):
        if len(self.contenu) >= self.emplacement:
            print ("la boite est pleine")
        else:
            self.contenu.append(tool)
            print(f"la boite a maintenant {len(self.contenu)} outils")

    @classmethod
    def nouvelle_version(cls):
        cls.emplacement +=1
        print("la capacité de ma boite a augmenté de 1")

class Marteau:
    def __init__(self,poids):
        self.poids = poids

class Tournevis:
    def __init__(self,type_vis):
        self.type_vis = type_vis

class Clou:
    def __init__(self, enfonce=False):
        self.enfonce = enfonce
    
    def enfoncer(self, tool):
        if isinstance(tool, Marteau):
            self.enfonce = True



class Vis:
    def __init__(self, type_vis, serre=False):
        self.type_vis = type_vis
        self.serre = serre
    
    def serrage(self, tool):
        if isinstance(tool, Tournevis):
            if tool.type_vis == self.type_vis:
                self.serre = True


    

ma_boite = BoiteAOutil()
mon_marteau = Marteau(3)
mon_tournevis = Tournevis("cruciforme")
ma_boite.add_tool(mon_marteau)
ma_boite.add_tool(mon_tournevis)
ma_boite.add_tool(mon_tournevis)
ma_boite.add_tool(mon_tournevis)
ma_boite.add_tool(mon_tournevis)
ma_boite.add_tool(mon_tournevis)
BoiteAOutil.nouvelle_version()
ma_boite.add_tool(mon_tournevis)


# print(ma_boite.contenu)

# ma_vis = Vis("cruciforme")

# print(ma_vis.serre)

# ma_vis.serrage(mon_tournevis)

# print(ma_vis.serre)

mon_clou = Clou()

mon_clou.enfoncer(mon_tournevis)

print(ma_boite.emplacement)