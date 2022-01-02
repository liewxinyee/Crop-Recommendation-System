
from selectbox import SelectBox
import models
from selectbox import SelectCrop
import crops


def envFac():
    model = SelectBox()
    model.add_app("Decision Tree", models.DT)
    model.add_app("Naive Bayes", models.NB)
    model.add_app("Support Vector Machines(SVM)", models.SVM)
    model.add_app("Logistic Regression", models.LR)
    model.add_app("Random Forest", models.RF)
    model.add_app("XGBoost", models.XB)

    model.run()

def selectCrop():
    crop = SelectCrop()
    crop.add_app("Apple", crops.apple)
    crop.add_app("Banana", crops.banana)
    crop.add_app("Blackgram", crops.blackgram)
    crop.add_app("Chickpea", crops.chickpea)
    crop.add_app("Coconut", crops.coconut)
    crop.add_app("Coffee", crops.coffee)
    crop.add_app("Cotton", crops.cotton)
    crop.add_app("Grapes", crops.grapes)
    crop.add_app("Jute", crops.jute)
    crop.add_app("Kidneybeans", crops.kidneybeans)
    crop.add_app("Lentil", crops.lentil)
    crop.add_app("Maize", crops.maize)
    crop.add_app("Mango", crops.mango)
    crop.add_app("Mothbeans", crops.mothbeans)
    crop.add_app("Mungbean", crops.mungbean)
    crop.add_app("Muskmelon", crops.muskmelon)
    crop.add_app("Orange", crops.orange)
    crop.add_app("Papaya", crops.papaya)
    crop.add_app("Pigeonpeas", crops.pigeonpeas)
    crop.add_app("Pomegranate", crops.pomegranate)
    crop.add_app("Rice", crops.rice)
    crop.add_app("Watermelon", crops.watermelon)

    crop.run()



