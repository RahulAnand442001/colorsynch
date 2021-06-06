import os
from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import colorgram 


def extract_colors(fileName:str):
    colors=[]
    extracted_colors=colorgram.extract(fileName,15)
    for color in extracted_colors:
        colors.append(tuple(color.rgb))
    return colors

app =Flask(__name__)


@app.route("/",methods=["GET","POST"])
def Home():
    if request.method=="POST":
        img_file=request.files["image"]
        img_file_name = img_file.filename
        if img_file_name != "":
            img_file.save(secure_filename(img_file_name))
            colors=extract_colors(fileName=img_file_name)
            os.remove(img_file_name)
            return render_template("index.html",photo=True,colors=colors)            
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)

