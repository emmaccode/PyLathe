try:
    import julia
except ImportError:
    print("Julia is not installed!")
try:
    from julia import Lathe
except:
    from julia import Pkg
    Pkg.add("Lathe")
