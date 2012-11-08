 # -*- coding: utf8 -*-
import subprocess
import os
import time
 
##################################
#       Hantera kontonummer      #
##################################
#Öppnar en fil där man kan läsa in betydelsen av kontonummer
kontofil = open("AutoVerifikatKonton.txt", "r")
#Skapar en hemagjord "2-delad dictionary"
kontnummer=[]
kontnamn=[]
for rad in kontofil.readlines():
	komponenter=rad.split(";")
	kontnummer.append(komponenter[0])
	kontnamn.append(komponenter[1].strip())

#En funktion som kollar om kontonummret finns och i så fall returnerar rätt konto-namn (linjär sökning)
def kontonamn(knummer):
	for i in range(0,len(kontnummer)):
		if (knummer == kontnummer[i]):
			return kontnamn[i]
	return ""
 
 
 
 
##################################
#        Konto-info rader        #
##################################
#Variabler för total kredit och debit
global totkred
global totdeb
#Funktion för att sätta totalen till 0
def resetkreddeb():
	global totkred
	global totdeb
	totkred=0
	totdeb=0
	
#Funktion för att hitta rätt om det är kredit eller debet
def kontcalc(kontoinf):
	global totkred
	global totdeb
	Nummer=""
	Namn=""
	RS=""
	Kred=""
	Projekt=""
	Deb=""	
	#Om det inte står något på konto, returnera tomt
	if (kontoinf == ""):
		return[Namn,Nummer,RS,Projekt,Deb,Kred]
	kontoinf=kontoinf.split(" ")
	#Skriv kontonummret och försök slå upp kontonamnet
	Nummer=kontoinf[1]
	Namn=kontonamn(Nummer)
	#Om det är debet
	if (kontoinf[0].upper() == "D"):
		Deb=kontoinf[2]
		totdeb += float(Deb)
		#Testa om det finns ett resultatställe (måste inte finnas, men måste finnas om det finns ett projekt) samt ett projekt (måste inte finnas)
		#Dock ser syntaxen ut sådan att om man försöker ange ett Projekt utan ett resultatställe så kommer projektet att hamna på plats [3] och behandlas som ett resultatställe.
		try:
			RS=kontoinf[3]
		except IndexError:
			RS=""
		try:
			Projekt=kontoinf[4]
		except IndexError:
			Projekt=""
	#Om det är kredit
	elif(kontoinf[0].upper() == "K"):
		Kred=kontoinf[2]
		#Testa om det finns ett resultatställe (måste inte finnas, men måste finnas om det finns ett projekt) samt ett projekt (måste inte finnas)
		#Dock ser syntaxen ut sådan att om man försöker ange ett Projekt utan ett resultatställe så kommer projektet att hamna på plats [3] och behandlas som ett resultatställe.
		try:
			RS=kontoinf[3]
		except IndexError:
			RS=""
		#Testa om det finns ett projekt (det måste inte finnas ett projekt)
		try:
			Projekt=kontoinf[4]
		except IndexError:
			Projekt="";
		totkred += float(Kred)
	#Om det är bugg, varken K eller D, så retuneras tomt
	return[Namn,Nummer,RS,Projekt,Deb,Kred]



##################################
#    Hantera namnförkortningar   #
##################################
#Öppnar en fil där man kan läsa in betydelsen av namnförkortningar
namnfil = open("AutoVerifikatNamn.txt", "r")
#Skapar en hemagjord "3-delad dictionary"
kortnamn=[]
fullnamn=[]
titel=[]
for rad in namnfil.readlines():
	komponenter=rad.split(";")
	kortnamn.append(komponenter[0].upper()) #Upper case för att göra case-okänslig
	fullnamn.append(komponenter[1])
	titel.append(komponenter[2].strip())

#En funktion som kollar om förkortningen finns och i så fall returnerar rätt namn och titel
def person(forkortning):
	#Gör upper case för att göra case-okänslig
	forkortning=forkortning.upper()
	for i in range(0,len(kortnamn)):
		if (forkortning == kortnamn[i]):
			return [fullnamn[i], titel[i]]
	return ["Signatur", "Namnförtydligande och titel"]
	
##################################
# Fixa med specifikationstexten  #
##################################	
specifikation=[]

#Funktion för att sätte default ingentext
def resetspec():
	global specifikation
	specifikation=[" \\\\ \\hline \\\\ ",
	" \\\\ \\hline \\\\ ",
	" \\\\ \\hline \\\\ ",
	" \\\\ \\hline \\\\ ",
	" \\\\ \\hline \\\\ "]

#Funktion för att sätta ihop den faktiska specifikationen för ett verifikat
def byggspecifikation(text):
	for i in range(len(text)):
		if text[i] is not "" and i<5:
			specifikation[i] = text[i]+"\\\\ \\hline \\\\"
	enStrang=""
	for snutt in specifikation:
		enStrang+=snutt
	return enStrang
	
	
	

##################################
#  Fördefinierade TeX kommandon  #
##################################
#Förbereder en lista med alla variabler som ska sättas
#Observera att \\ är för att Python ska registrera det andra \ som ett tecken i en string
texvariabler=[]
#Metod för att resetta all texvariabler mellan körningarna av olika verifikat
def resettex():
	global texvariabler
	texvariabler=[
	"\\newcommand{\\vernr}{",
	"\\newcommand{\\verdate}{",
	"\\newcommand{\\bokdate}{",
	"\\newcommand{\\sakattestNamn}{",
	"\\newcommand{\\sakattestTitel}{",
	"\\newcommand{\\ekattestNamn}{",
	"\\newcommand{\\ekattestTitel}{",
	"\\newcommand{\\kontonamnA}{",
	"\\newcommand{\\KontoA}{",
	"\\newcommand{\\RSA}{",
	"\\newcommand{\\ProjektA}{",
	"\\newcommand{\\DebetA}{",
	"\\newcommand{\\KreditA}{",
	"\\newcommand{\\kontonamnB}{",
	"\\newcommand{\\KontoB}{",
	"\\newcommand{\\RSB}{",
	"\\newcommand{\\ProjektB}{",
	"\\newcommand{\\DebetB}{",
	"\\newcommand{\\KreditB}{",
	"\\newcommand{\\kontonamnC}{",
	"\\newcommand{\\KontoC}{",
	"\\newcommand{\\RSC}{",
	"\\newcommand{\\ProjektC}{",
	"\\newcommand{\\DebetC}{",
	"\\newcommand{\\KreditC}{",
	"\\newcommand{\\kontonamnD}{",
	"\\newcommand{\\KontoD}{",
	"\\newcommand{\\RSD}{",
	"\\newcommand{\\ProjektD}{",
	"\\newcommand{\\DebetD}{",
	"\\newcommand{\\KreditD}{",
	"\\newcommand{\\kontonamnE}{",
	"\\newcommand{\\KontoE}{",
	"\\newcommand{\\RSE}{",
	"\\newcommand{\\ProjektE}{",
	"\\newcommand{\\DebetE}{",
	"\\newcommand{\\KreditE}{",
	"\\newcommand{\\TotalDebet}{",
	"\\newcommand{\\TotalKredit}{",
	"\\newcommand{\\Specifikation}{\\tabularnewline "]



##################################
#    Bygger TeX av indatafilen   #
##################################
#Öppnar själva TeX mallen och läser in texten i en enhet
texmallfil = open("AutoVerifikatMall.tex", "r")
texmall=texmallfil.read()

#Öppnar en fil med indata. All data ligger på en rad och seppareras med ;
indatafil = open("AutoVerifikatIndata.txt", "r")
errorlogtext=""

#En rad = fullständigt verifikat
for rad in indatafil.readlines():
	#Resetar Texvariablerna mellan varje verifikat
	resettex()
	#Resetar total kredit och debit mellan varje verifikat
	resetkreddeb()
	#Resetar specifikationstexten mellan varja verifikat
	resetspec()
	#Ta bort sista \endline
	rad=rad.strip()
	#Kollar om raden är tom
	if(rad==""):
		continue
	#Kollar om raden är "utkommenterad"
	if(rad[0]=="#"):
		continue
	#Plockar ut alla komponenter ur varje rad.
	delar=rad.split(";")
	vernummer=delar[0]
	#Hjälputskrift, för att man ska fatta vad som händer om något går fel.
	print('Processar verifikat ' +vernummer)
	verdatum=delar[1]
	bokdatum=delar[2]
	sakatest=delar[3]
	ekatest=delar[4]
	kontoEtt=delar[5]
	kontoTva=delar[6]
	kontoTre=delar[7]
	kontoFyra=delar[8]
	kontoFem=delar[9]
	text=delar[10].split("|")
	
	#Lägg in rätt saker på rätt plats
	#verifikationsnummer
	texvariabler[0]+=vernummer+"}"
	#verifikationsdatum
	texvariabler[1]+=verdatum+"}"
	#bokföringsdatum
	texvariabler[2]+=bokdatum+"}"
	#Sakatest
	temp=person(sakatest.upper()) #Upper case för att gör case-okänslig
	texvariabler[3]+=temp[0]+"}"
	texvariabler[4]+=temp[1]+"}"
	#Ekonomisk atest
	temp=person(ekatest.upper()) #Upper case för att gör case-okänslig
	texvariabler[5]+=temp[0]+"}"
	texvariabler[6]+=temp[1]+"}"
	#Konto 1
	temp=kontcalc(kontoEtt)
	texvariabler[7]+=temp[0]+"}"
	texvariabler[8]+=temp[1]+"}"
	texvariabler[9]+=temp[2]+"}"
	texvariabler[10]+=temp[3]+"}"
	texvariabler[11]+=temp[4]+"}"
	texvariabler[12]+=temp[5]+"}"
	#Konto 2
	temp=kontcalc(kontoTva)
	texvariabler[13]+=temp[0]+"}"
	texvariabler[14]+=temp[1]+"}"
	texvariabler[15]+=temp[2]+"}"
	texvariabler[16]+=temp[3]+"}"
	texvariabler[17]+=temp[4]+"}"
	texvariabler[18]+=temp[5]+"}"
	#Konto 3
	temp=kontcalc(kontoTre)
	texvariabler[19]+=temp[0]+"}"
	texvariabler[20]+=temp[1]+"}"
	texvariabler[21]+=temp[2]+"}"
	texvariabler[22]+=temp[3]+"}"
	texvariabler[23]+=temp[4]+"}"
	texvariabler[24]+=temp[5]+"}"
	#Konto 4
	temp=kontcalc(kontoFyra)
	texvariabler[25]+=temp[0]+"}"
	texvariabler[26]+=temp[1]+"}"
	texvariabler[27]+=temp[2]+"}"
	texvariabler[28]+=temp[3]+"}"
	texvariabler[29]+=temp[4]+"}"
	texvariabler[30]+=temp[5]+"}"
	#Konto 5
	temp=kontcalc(kontoFem)
	texvariabler[31]+=temp[0]+"}"
	texvariabler[32]+=temp[1]+"}"
	texvariabler[33]+=temp[2]+"}"
	texvariabler[34]+=temp[3]+"}"
	texvariabler[35]+=temp[4]+"}"
	texvariabler[36]+=temp[5]+"}"
	texvariabler[37]+=str(totdeb)+"}"
	texvariabler[38]+=str(totkred)+"}"
	#Specifikationen
	temp=byggspecifikation(text)
	texvariabler[39]+=temp+"}"

		
	#Lägg ihop alla texvariabler i en sträng för att klistra in i dokumentet
	texkommandon=""
	for variabel in texvariabler:
		texkommandon += variabel+"\n"
	texkommandon += "\n"
	
	#Skriv hela kalaset till en fil, filnamn = verifikatnummer
	slutfil = open(vernummer+".tex","w")
	slutfil.write(str(texkommandon+texmall))
	slutfil.close()
	
	#Ropa på Xelatex två gånger för att kompilera allt och får referenser bra. Om TeX-kompileringen går bra så slippe användaren se all TeX kod. Men TeX-error kastas ut i terminalen.
	#Tot debet och kredit (måste vara lika, annars VARNA!)
	if(totdeb != totkred):
		print('VARNING: Verifikat ' +vernummer+ ' har inte debet och kredit lika!\n')
		errorlogtext += 'Verifikat ' +vernummer+ ' har inte debet och kredit lika och har därför inte kompilerats.\n\n'
	else:
		with open(os.devnull, "w") as fnull:
			subprocess.call(["xelatex", vernummer+".tex"], stdout = fnull)
			subprocess.call(["xelatex", vernummer+".tex"], stdout = fnull)
		#Städa bort TeX relaterat skoj
		os.remove(vernummer +".aux")
		os.remove(vernummer +".log")
		os.remove(vernummer +".out")
		print('\n')

if (errorlogtext != ""):
	#Om det faktiskt finns några problem, skriv en error fil.
	logfil = open('ErrorReport.txt','w')
	logfil.write(str(errorlogtext))
	logfil.close()
else:
	#Det finns inga fel att skriva, kolla om det finns en gammal Logfil och ta bort den i sådana fall
	if(os.path.exists('ErrorReport.txt')):
				os.remove('ErrorReport.txt')

print('Klar!')