from turtle import title
from flask import Flask, render_template, request, url_for
from forms import geteqn
from checkBalance import check_eqn_balance


app = Flask(__name__)
app.config['SECRET_KEY'] = 'e8a474d0dc43876787c5abd844d6cf25'

unbalanced_Elements = []
secondLast = []
last = []

@app.route("/", methods=['GET', 'POST'])
def mainpg():
    form = geteqn()

    if form.is_submitted():
        reactsAndProds = []
        reactsStr = str
        prodsStr = str
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
        finalInput.append((prodsCoef,prodsMol))

        y = check_eqn_balance(finalInput[0], finalInput[1])
        placeholderUnbalanced = []
        placeholderLast = []
        placeholderSecondLast = []
        if y:
            for m in y:
                placeholderUnbalanced.append(m)
        if len(placeholderUnbalanced)>2:
            placeholderSecondLast.append(placeholderUnbalanced.pop(-2))
            placeholderLast.append(placeholderUnbalanced.pop(-1))
        elif len(placeholderUnbalanced)>1:
            placeholderLast.append(placeholderUnbalanced.pop(-1))
        unbalanced_Elements = placeholderUnbalanced
        last = placeholderLast
        secondLast = placeholderSecondLast
        return render_template('resultPg.html', reactantSide = reactsStrNoSpaces, productSide = prodsStrNoSpaces, data = unbalanced_Elements, last = last, secondLast = secondLast)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)