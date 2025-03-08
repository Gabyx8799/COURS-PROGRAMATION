from flask import Flask, render_template,session,redirect
import os 
from questions import questions
from resultats import resultats
app= Flask("App Quizz")
app.secret_key = os.urandom(24)




@app.route("/")
def index():
        session["numero_question"] = 0
        session["score"] = {"Perso1" : 0, "Perso2" : 0, "Perso3":0, "Perso4":0}
        return render_template("index.html")
@app.route("/question")
def question():
        global questions
        nb_question = session["numero_question"]
        if nb_question < len(questions):
                
        
                enonce_question= questions[nb_question]["enonce"]
                questions_copy = questions[nb_question].copy()
                questions_copy.pop("enonce") 
                reponses = list(questions_copy.values())
                clefs= list(questions_copy.keys())
                session["clefs"]= clefs
                return render_template("questions.html",question = enonce_question,reponses=reponses)
        else:
                global resultats
                score_trie = sorted(session["score"],
                key=session["score"].get,reverse=True)
                nom_vainqueur = score_trie[0]
                description = resultats[nom_vainqueur]


                return render_template("resultats.html",nom_vainqueur =  nom_vainqueur, description=description)

@app.route("/reponse/<numero>") 
def reponse(numero):
        session["numero_question"] += 1
        clef_gagnant = session["clefs"][int(numero)]
        session["score"][clef_gagnant] += 1
        return redirect("/question")


app.run(host = '0.0.0.0',port = 81 )

# git config --global user.name "Gabyx8799"
# git config --global user.email "samakgaby@gmail.com"


