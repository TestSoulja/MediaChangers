import os
import pathlib

s = os.path.abspath(__file__)
c = s.replace(os.path.basename(os.path.abspath(__file__)), "")

n = 4319
q = n
w = n
e = n

path = pathlib.Path(c+"/Enter/46")
for i, path in enumerate(path.glob('*.png')):
    new_name = c + "/Exit/"+ str(n) + '.png'
    path.rename(new_name)
    n += 1

path = pathlib.Path(c+"/Enter/92")
for i, path in enumerate(path.glob('*.png')):
    new_name = c + "/Exit/"+ str(q) + '_hd.png'
    path.rename(new_name)
    q += 1

path = pathlib.Path(c+"/Enter/184")
for i, path in enumerate(path.glob('*.png')):
    new_name = c + "/Exit/"+ str(w) + '_qd.png'
    path.rename(new_name)
    w += 1

path = pathlib.Path(c+"/Enter/512")
for i, path in enumerate(path.glob('*.png')):
    new_name = c + "/Exit/"+ str(e) + '_xd.png'
    path.rename(new_name)
    e += 1
