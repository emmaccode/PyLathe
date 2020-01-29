try:
    import julia
except ImportError:
    print("Julia is not installed!")

class ClassicEnvironment:
    jl = ""
    stats = ""
    preprocess = ""
    models = ""
    def __init__(self):
        try:
            self.jl = julia.Julia()
        except:
            print(""""Julia could not be loaded! There are
            several likely causes..""")
            print("1. You don't have Julia installed.")
            print("2. You don't have PyCall.JL")
            print("""3. There is a known bug with Debian/Ubuntu where julia.py
             is unable to find Julia.""")
        print("Julia initialized from: ")
        print(self.jl)
        self.jl.include("JL/Lathe.jl")
    def importStats(self):
        self.stats = self.jl.Lathe.stats
        return(self.stats)
    def importPreprocess(self):
        self.preprocess = self.jl.Lathe.preprocess
        return(self.preprocess)
    def importModels(self):
        self.models = self.jl.Lathe.models
        return(self.models)
