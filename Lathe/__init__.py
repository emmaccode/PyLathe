import models
import stats
import preprocess
import julia
jl = julia.Julia()
jl.include("JL/Lathe.jl")
tester = jl.Lathe.stats.mean([5,10,15])
if tester != 10:
    print("FATAL ERROR!!! : Mean test failed!")
    print("Something is wrong with your Lathe.jl Julia package!")
else:
    print("Everything seems to be in order.")
