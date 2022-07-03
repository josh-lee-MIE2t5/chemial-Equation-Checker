import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for
from forms import geteqn
from checkBalance import check_eqn_balance

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET')


unbalanced_Elements = []
secondLast = []
last = []

    
@app.route("/Dark", methods=['GET', 'POST'])
def mainpgDark():
    form = geteqn()

    if form.is_submitted():
        reactsAndProds = []
        reactsStr = ""
        prodsStr = ""
        reactsStrNoSpaces = ""
        prodsStrNoSpaces = ""
        reactMolsList = list()
        prodMolsList = list()
        reactsCoef = []
        reactsMol = []
        prodsCoef = []
        prodsMol = []
        finalInput = []

        result = request.form
        for x, y in result.items():
            reactsAndProds.append(y)

        reactsStr = reactsAndProds[0]
        prodsStr = reactsAndProds[1]

        for i in range(0, len(reactsStr)):
            if reactsStr[i] != " ":
                reactsStrNoSpaces += reactsStr[i]
            i += 1

        for i in range(0, len(prodsStr)):
            if prodsStr[i] != " ":
                prodsStrNoSpaces += prodsStr[i]
            i += 1

        reactMolsList = reactsStrNoSpaces.split("+")
        prodMolsList = prodsStrNoSpaces.split("+")

        for i in reactMolsList:
            if i[0].isnumeric():
                if i[1].isnumeric():
                    reactsCoef.append(int(i[0:2]))
                    reactsMol.append(i[2:])
                else:
                    reactsCoef.append(int(i[0]))
                    reactsMol.append(i[1:])
            else:
                reactsCoef.append(1)
                reactsMol.append(i)

        for i in prodMolsList:
            if i[0].isnumeric():
                if i[1].isnumeric():
                    prodsCoef.append(int(i[0:2]))
                    prodsMol.append(i[2:])
                else:
                    prodsCoef.append(int(i[0]))
                    prodsMol.append(i[1:])
            else:
                prodsCoef.append(1)
                prodsMol.append(i)

        reactsCoef = tuple(reactsCoef)
        reactsMol = tuple(reactsMol)
        prodsCoef = tuple(prodsCoef)
        prodsMol = tuple(prodsMol)

        finalInput.append((reactsCoef, reactsMol))
        finalInput.append((prodsCoef, prodsMol))

        y = check_eqn_balance(finalInput[0], finalInput[1])
        placeholderUnbalanced = []
        placeholderLast = []
        placeholderSecondLast = []
        if y:
            for m in y:
                placeholderUnbalanced.append(m)
        if len(placeholderUnbalanced) > 2:
            placeholderSecondLast.append(placeholderUnbalanced.pop(-2))
            placeholderLast.append(placeholderUnbalanced.pop(-1))
        elif len(placeholderUnbalanced) > 1:
            placeholderLast.append(placeholderUnbalanced.pop(-1))
        unbalanced_Elements = placeholderUnbalanced
        last = placeholderLast
        secondLast = placeholderSecondLast

        C=' '
        D=' '
        E=' '
        for i in unbalanced_Elements:
            C+=i
        for i in last:
            D+=i
        for i in secondLast:
            E+=i

        print(C)
        print(D)
        print(E)
        return redirect(url_for('resultDark', a = reactsStrNoSpaces, b = prodsStrNoSpaces, c = C, d = D, e = E))
    
    return render_template('mainDark.html', form=form)

@app.route("/", methods=['GET', 'POST'])
def mainpgLight():
    form = geteqn()

    if form.is_submitted():
        reactsAndProds = []
        reactsStr = ""
        prodsStr = ""
        reactsStrNoSpaces = ""
        prodsStrNoSpaces = ""
        reactMolsList = list()
        prodMolsList = list()
        reactsCoef = []
        reactsMol = []
        prodsCoef = []
        prodsMol = []
        finalInput = []

        result = request.form
        for x, y in result.items():
            reactsAndProds.append(y)

        reactsStr = reactsAndProds[0]
        prodsStr = reactsAndProds[1]

        for i in range(0, len(reactsStr)):
            if reactsStr[i] != " ":
                reactsStrNoSpaces += reactsStr[i]
            i += 1

        for i in range(0, len(prodsStr)):
            if prodsStr[i] != " ":
                prodsStrNoSpaces += prodsStr[i]
            i += 1

        reactMolsList = reactsStrNoSpaces.split("+")
        prodMolsList = prodsStrNoSpaces.split("+")

        for i in reactMolsList:
            if i[0].isnumeric():
                if i[1].isnumeric():
                    reactsCoef.append(int(i[0:2]))
                    reactsMol.append(i[2:])
                else:
                    reactsCoef.append(int(i[0]))
                    reactsMol.append(i[1:])
            else:
                reactsCoef.append(1)
                reactsMol.append(i)

        for i in prodMolsList:
            if i[0].isnumeric():
                if i[1].isnumeric():
                    prodsCoef.append(int(i[0:2]))
                    prodsMol.append(i[2:])
                else:
                    prodsCoef.append(int(i[0]))
                    prodsMol.append(i[1:])
            else:
                prodsCoef.append(1)
                prodsMol.append(i)

        reactsCoef = tuple(reactsCoef)
        reactsMol = tuple(reactsMol)
        prodsCoef = tuple(prodsCoef)
        prodsMol = tuple(prodsMol)

        finalInput.append((reactsCoef, reactsMol))
        finalInput.append((prodsCoef, prodsMol))

        y = check_eqn_balance(finalInput[0], finalInput[1])
        placeholderUnbalanced = []
        placeholderLast = []
        placeholderSecondLast = []
        if y:
            for m in y:
                placeholderUnbalanced.append(m)
        if len(placeholderUnbalanced) > 2:
            placeholderSecondLast.append(placeholderUnbalanced.pop(-2))
            placeholderLast.append(placeholderUnbalanced.pop(-1))
        elif len(placeholderUnbalanced) > 1:
            placeholderLast.append(placeholderUnbalanced.pop(-1))
        unbalanced_Elements = placeholderUnbalanced
        last = placeholderLast
        secondLast = placeholderSecondLast

        C=' '
        D=' '
        E=' '
        for i in unbalanced_Elements:
            C+=i
        for i in last:
            D+=i
        for i in secondLast:
            E+=i

        print(C)
        print(D)
        print(E)
        return redirect(url_for('resultLight', a = reactsStrNoSpaces, b = prodsStrNoSpaces, c = C, d = D, e = E))
    
    return render_template('mainLight.html', form=form)

@app.route("/resultLight/<a>/<b>/<c>/<d>/<e>", methods=['GET', 'POST'])
def resultLight(a, b, c, d, e):
    data = prepareData(c)
    last = prepareLast(d)
    secondLast = prepareSecondLast(e)
    return render_template('resultPgLight.html', reactantSide=a, productSide=b, data=data, last=last, secondLast=secondLast, title = "result")

@app.route("/resultDark/<a>/<b>/<c>/<d>/<e>", methods=['GET', 'POST'])
def resultDark(a, b, c, d, e):
    data = prepareData(c)
    last = prepareLast(d)
    secondLast = prepareSecondLast(e)
    return render_template('resultPgDark.html', reactantSide=a, productSide=b, data=data, last=last, secondLast=secondLast, title = "result")

def prepareData(c):
    data =[]
    c = c.replace(" ", "")
    lowerIndex = []
    if c != "":
        i=0
        if c.isupper():
            for i in c:
                data.append(i)
        else:
            for i in c:
                if i.islower():
                    n = c.find(i)
                    el = c[n-1] + c[n]
                    data.append(el)
                    c = c[0:c.find(el)] + c[c.find(el)+len(el):]
            for i in c:
                data.append(i)
    return data

def prepareLast(d):
    last = []
    d = d.replace(" ", "")
    if d != "":
        last.append(d)
    return last

def prepareSecondLast(e):

    secondLast=[]
    e = e.replace(" ", "")
    if e != "":
        secondLast.append(e)
    return secondLast
if __name__ == '__main__':
    app.run(debug=True)