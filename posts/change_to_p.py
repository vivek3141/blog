with open("ml.txt","r") as f:
    text = f.read()
with open("ml.txt","w") as f:
    f.write(text.replace("\n","<p></p>"))
