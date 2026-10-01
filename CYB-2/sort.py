import os
path=input("file name (q to quit): ")
while path!="q" and (not os.path.isfile(path)):
  path=input("retry, file not found: ")
if path=="q":
  print("understood, quitting...")
  exit
f=open(path,"r").read().replace("\n\n\n","\n\n").replace("\n\n\n","\n\n").split("\n\n")
for i in range(len(f)):
  f[i]=f[i].split("\n")
  title=""
  if "=" not in f[i][0]:
    title=f[i][0]+"\n"
    f[i]=f[i][1:]
  f[i]=title+("\n".join(sorted(f[i])))
f=sorted(f)
f="\n\n".join(f)
wf=open(path,"w")
wf.write(f)
wf.close()
print("sorted "+path)