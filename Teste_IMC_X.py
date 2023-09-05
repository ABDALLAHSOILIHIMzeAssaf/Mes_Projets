# Créé par mzeabdallahsoilihi, le 05/12/2022 en Python 3.7
print ("Bonjour, nous allons calculer votre IMC.")

masse = input("Entrer la masse en kg: ")
masse = float(masse)
taille = input ("entrer la taille en métre: ")
taille = float(taille)

imc = masse/taille**2
float = (imc)
print ("votre imc est de", imc)

if imc < 18.5 :
    print ("vous êtes maigre")
if imc > 40 :
    print ("vous êtes en situation d'obésité massive")
else:
    if imc > 24.9 and imc < 29.9 :
        print ("vous êtes en surpoids")
    if imc > 29.9 and imc < 40 :
        print ("vous êtes en situation d'obésité")
    if imc > 18.5 and imc < 24.9 :
        print ("exellent vous avez une masse normale")