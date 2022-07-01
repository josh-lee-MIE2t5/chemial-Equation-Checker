import os 
from tabnanny import check
from turtle import title
from flask import Flask, redirect, render_template, request, url_for
from forms import geteqn
from checkBalance import check_eqn_balance


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET']

unbalanced_Elements = []
secondLast = []
last = []


@app.route("/", methods=['GET', 'POST'])
def mainpg():
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
        print(y)
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

        return redirect(url_for('result', a = reactsStrNoSpaces, b = prodsStrNoSpaces, c = C, d = D, e = E))
    return render_template('index.html', form=form)


@app.route("/result/<a>/<b>/<c>/<d>/<e>", methods=['GET', 'POST'])
def result(a, b, c, d, e):
    data =[]
    last =[]
    secondLast = []
    c = c.replace(" ", "")
    d = d.replace(" ", "")
    e = e.replace(" ", "")

    # print(c)
    # print(d)
    # print(e)

    if c != "":
        for i in range(len(c)):
            if i == len(c)-1:
                data.append(c[i])
                i+=1
            elif i == len(c)-2:
                if c[i:i+1].isupper():
                    data.append(c[i])
                    i+=1
                else:
                    data.append(c[i:])
                    i+=2
            else:
                if c[i:i+1].isupper():
                    data.append(c[i])
                    i+=1
                else:
                    data.append(c[i:i+1])
                    i+=2

    if d != "":
        last.append(d)
    if e != "":
        secondLast.append(e)
        
    # print(data)
    # print(last)
    # print(secondLast)
    return render_template('resultPg.html', reactantSide=a, productSide=b, data=data, last=last, secondLast=secondLast)


if __name__ == '__main__':
    app.run(debug=True)
