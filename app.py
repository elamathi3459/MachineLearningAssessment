# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 12:14:56 2022

@author: Elamathi
"""
import logging
logging.basicConfig(level="DEBUG")
from flask import Flask, render_template, request
from ast import literal_eval
app = Flask(__name__, template_folder='templates')
@app.route("/",methods=['GET'])
def Home():
    return render_template('hindex.html')

def isRectangle(x1, y1, x2, y2, x3, y3, x4, y4):
    cx=(x1+x2+x3+x4)/4
    cy=(y1+y2+y3+y4)/4
    dd1=(cx-x1)**2+(cy-y1)**2
    dd2=(cx-x2)**2+(cy-y2)**2
    dd3=(cx-x3)**2+(cy-y3)**2
    dd4=(cx-x4)**2+(cy-y4)**2
    return dd1==dd2 and dd1==dd3 and dd1==dd4
@app.route("/predict", methods=['POST'])
def predict():
    #Getting the corner points
    if request.method == 'POST':
        cornerPoints = str(request.form['cornerPoints'])
        row=int(request.form['row'])
        col=int(request.form['col'])
        a = literal_eval(cornerPoints)
        l=isRectangle(a[0][0],a[0][1],a[1][0],a[1][1],a[2][0],a[2][1],a[3][0],a[3][1])
        if l is True:
            ans=[]
            topleft_x= min(a[0][0],a[1][0],a[2][0],a[3][0])
            topleft_y= max(a[0][1],a[1][1],a[2][1],a[3][1])
            img_height= max(a[0][1],a[1][1],a[2][1],a[3][1])-min(a[0][1],a[1][1],a[2][1],a[3][1])
            img_width= max(a[0][0],a[1][0],a[2][0],a[3][0])-min(a[0][0],a[1][0],a[2][0],a[3][0])
            for i in range (0,row):
                ans_row =[]
                for j in range (0,col):
                    ans_row.append([round(topleft_x+(img_width*j/(col-1)),1),round(topleft_y-(img_height*i/(row-1)),1)])
                ans.append(ans_row)
            
            return render_template('hindex.html',prediction_text=ans, row_num=row, col_num=col)
        else:
            return render_template('hindex.html', error='Error in the points')
    else:
        return render_template('hindex.html')

if __name__=="__main__":
        logging.debug("Starting Flask Server")
        from api import *
        app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True)
    
        
