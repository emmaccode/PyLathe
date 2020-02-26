# PyLathe
## PyLathe has been deprecated in favor of TOPLOADER.py
https://github.com/emmettgb/TopLoader
![Lathe Logo](http://lathe.ai/logo.png)\
Lathe.py is a wrapper of the machine-learning module for Julia, Lathe, ported into Python.
- Ensure you have julia.py installed:
```bash
sudo pip3 install julia
```
- There is a known bug on systems with the Aptitude package manager where the Julia executable will fail to load. Unfortunately the issue is with julia.py trying to access Julia in a directory which Apt does not put Julia.
Install it!\
**Bash**
```bash
sudo pip3 install PyLathe
```
**Python**
```python
from Lathe.Runtime import ClassicEnvironment
env = ClassicEnvironment()
stats = env.importStats()
stats.mean([5,10,15])
>>> 10
models = env.importModels()
m = models.LinearRegression([5,10,15,20],[10,20,30,40])
ypred = models.predict(m, [5,10,15,20])
print(ypred)
>>> [10. 20. 30. 40.]

```
(Yes, it's really that easy)
[Julia Documentation (Python docs coming soon)](http://lathe.ai/doc.html)
