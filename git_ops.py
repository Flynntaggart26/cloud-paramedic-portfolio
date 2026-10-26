import os
os.chdir(r"C:\Users\Lenovo\AppData\Local\Cline\cloud-paramedic-portfolio")
os.system("git add -A")
os.system('git commit -q -m "Final: Complete modern UI with all sections"')
os.system("git push -u origin main")
print("Done")