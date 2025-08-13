#initialize
from flask import Flask, render_template, redirect, url_for
import pandas as pd
import matplotlib.pyplot as plt
import os
app = Flask(__name__)

data_df = pd.DataFrame()


@app.route('/second')
def second_page():
    return render_template('second_page.html')

@app.route('/third')
def third_page():
    return render_template('third_page.html')

@app.route('/pandas')
def Pandas():
    df = pd.read_csv(r'C:\Users\dell\Downloads\academicStress.csv')
    return render_template('Pandas.html',title = "Dataset-1", table = df.head().to_html(index=False,classes="table"))

@app.route('/pandas1')
def pandas2():
    df = pd.read_csv('gta_sa_vehicle_stats.csv')
    df.head()
    return render_template('pandas2.html',title = "Dataset2", table = df.head().to_html(index=False,classes="table"))

@app.route('/pandas2')
def pandas3():
    df = pd.read_csv('sustainability_social_media_posts.csv')
    df.head()
    return render_template('pandas3.html',title = "Dataset-3",table=df.head().to_html(index=True,classes="table"))

@app.route('/pandas3')
def pandas4():
    df = pd.read_csv('ai_financial_market_daily_realistic_synthetic.csv')
    df.head()
    return render_template('pandas4.html',title = "Dataset-4",table=df.head().to_html(index=True,classes="table"))

@app.route('/')
def First_page():
    return render_template('First_page.html')

@app.route('/Home')
def Home_page():
    global data_df
    data_df = pd.read_csv('ai_financial_market_daily_realistic_synthetic.csv').head()
    return render_template("Home_page.html",title = "PANDAS",table = data_df.to_html(index=False, classes="table"))

@app.route('/bar')
def bar():
    if data_df.empty:
        return redirect('/Home')
    plt.figure(figsize=(8,6))
    plt.bar(data_df["AI_Revenue_USD_Mn"], data_df["Company"])
    plt.xlabel("Revenue")
    plt.ylabel("Time")
    plt.grid(False)
    chart_path = os.path.join('static', 'chart.png')
    plt.savefig(chart_path)
    plt.close()

    return render_template('bar.html', chart_url = url_for('static', filename='chart.png'))

    

if(__name__) == '__main__':
    app.run(port=3000,debug=False, host = "0.0.0.0")
    
    #you need this to show the flask app and show web pages.
   # flask is the python library
   # Flask is the class
   # render means to take an html file and send it to the browser so that user can see it as a web page

#render_templates help to load the html file
