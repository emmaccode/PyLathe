from julia import Lathe
from julia import Pkg
# Classic Environment:
class ClassicEnvironment:
    jl = Lathe
    pacman = Pkg
    def importStats(self):
        return(Lathe.stats)
    def importPreprocess(self):
        return(Lathe.preprocess)
    def importModels(self):
        return(Lathe.models)
    def addPkg(self, pack):
        Pkg.add(pack)
    def Pkg(self):
        return(self.pacman)
