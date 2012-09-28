def readfromfile(dfile):
	dfile = open(dfile, "r")
	read = dfile.read()
	listofdata = []
#Skapar en lista där de olika raderna i textfilen blir elementen
	d,read = read.split("@verifikationsnummer")
	d,read = read.split("@verifikationsdatum")
	listofdata.append(d)
	d,read = read.split("@bokföringsdatum")
	listofdata.append(d)
	d,read = read.split("@sakattest")
	listofdata.append(d)
	d,read = read.split("@ekonomiskattest")
	listofdata.append(d)
	d,read = read.split("@konto1")
	listofdata.append(d)
	d,read = read.split("@konto2")
	listofdata.append(d)
	d,read = read.split("@konto3")
	listofdata.append(d)
	d,read = read.split("@konto4")
	listofdata.append(d)
	d,read = read.split("@konto5")
	listofdata.append(d)
	d,read = read.split("@beskrivning")
	listofdata.append(d)

#Lägger till hela beskrivningen som en sträng sist i listan
	listofdata.append(read)

#Tar bort alla radbrytningstecken (\n)
	for i in range(len(listofdata)):
		listofdata[i] = listofdata[i].strip()

#Gör listor i listan av kontoelementen
	listofdata[5] = listofdata[5].split()
	listofdata[6] = listofdata[6].split()
	listofdata[7] = listofdata[7].split()
	listofdata[8] = listofdata[8].split()
	listofdata[9] = listofdata[9].split()
	listofdata[-1] = listofdata[-1].split("@")

#Lägger till element i listan så att den totalt har 5 element	
	while len(listofdata[-1]) <= 4:
		listofdata[-1].append("")
	while len(listofdata[5]) <= 3:
		listofdata[5].append("")
	while len(listofdata[6]) <= 3:
		listofdata[6].append("")
	while len(listofdata[7]) <= 3:
		listofdata[7].append("")
	while len(listofdata[8]) <= 3:
		listofdata[8].append("")
	while len(listofdata[9]) <= 3:
		listofdata[9].append("")

	return listofdata



#Använd nedan utkommenterade två rader för att skriva ut listan som genereras från textfilen	
#testvar = readfromfile("indata.txt")
#print(testvar)

latexhuvud = """
\\documentclass[a4paper,10pt]{letter}
\\usepackage{epsf,graphicx,epsfig,graphicx}
\\usepackage[swedish]{babel}
\\usepackage[utf8]{inputenc}
\\setlength{\\parskip}{5pt}
\\setlength{\\parindent}{0pt}
\\addtolength{\\leftmargin}{-2cm}
\\addtolength{\\topmargin}{-3cm}
\\addtolength{\\textheight}{4.5cm}

\\renewcommand{\\rmdefault}{cmr}

\\newcommand{\\comments}[1]{}
"""

latexifyllning = """
\\newcommand{\\vernr}[1]{@verifikatnummer@}
\\newcommand{\\verdate}[1]{@verifikationsdatum@}
\\newcommand{\\bokdate}[1]{@bokföringsdatum@}

\\newcommand{\\kontonamnA}[1]{@kontonamn1@}
\\newcommand{\\KontoA}[1]{@konto1@}
\\newcommand{\\RSA}[1]{@rs1@}
\\newcommand{\\ProjektA}[1]{@projekt1@}
\\newcommand{\\DebetA}[1]{@debet1@}
\\newcommand{\\KreditA}[1]{@kredit1@}

\\newcommand{\\kontonamnB}[1]{@kontonamn2@}
\\newcommand{\\KontoB}[1]{@konto2@}
\\newcommand{\\RSB}[1]{@rs2@}
\\newcommand{\\ProjektB}[1]{@projekt2@}
\\newcommand{\\DebetB}[1]{@debet2@}
\\newcommand{\\KreditB}[1]{@kredit2@}

\\newcommand{\\kontonamnC}[1]{@kontonamn3@}
\\newcommand{\\KontoC}[1]{@konto3@}
\\newcommand{\\RSC}[1]{@rs3@}
\\newcommand{\\ProjektC}[1]{@projekt3@}
\\newcommand{\\DebetC}[1]{@debet3@}
\\newcommand{\\KreditC}[1]{@kredit3@}

\\newcommand{\\kontonamnD}[1]{@kontonamn4@}
\\newcommand{\\KontoD}[1]{@konto4@}
\\newcommand{\\RSD}[1]{@rs4@}
\\newcommand{\\ProjektD}[1]{@projekt4@}
\\newcommand{\\DebetD}[1]{@debet4@}
\\newcommand{\\KreditD}[1]{@kredit4@}

\\newcommand{\\kontonamnE}[1]{@kontonamn5@}
\\newcommand{\\KontoE}[1]{@konto5@}
\\newcommand{\\RSE}[1]{@rs5@}
\\newcommand{\\ProjektE}[1]{@projekt5@}
\\newcommand{\\DebetE}[1]{@debet5@}
\\newcommand{\\KreditE}[1]{@kredit5@}

\\newcommand{\\TotalDebet}[1]{@totald@}
\\newcommand{\\TotalKredit}[1]{@totalk@}
"""

latexverifikationstabell = """
\\begin{document}
\\begin{letter}

\\thispagestyle{empty}
\\begin{tabular}{@{} l l}
  \\includegraphics{F.pdf}
  \\hspace{0.1cm}
  \\includegraphics{logo.pdf}
\\end{tabular}


\\vspace{5mm}

\\begin{Large}{\\bf VERIFIKATION}\\end{Large}
\\flushleft
\\vspace{0.5cm}

\\begin{tabular}{llp{5mm}ll}
Verifikationsnr:&
\\large{\\vernr{}}
&&Verifikationsdatum:&\\large{\\verdate{}}\\\\ \\\\ &&&Bokföringsdatum:&
\\large{\\bokdate{}}\\\\
\\end{tabular}

\\vspace{2.5\\baselineskip}
"""

latexspecifikation = """
Specifikation:
\\begin{tabular}{p{12cm}}
\\\\ @rad1@ \\\\
    \\hline 
\\vspace{@parameter2@} @rad2@ \\\\
    \\hline
\\vspace{@parameter3@} @rad3@ \\\\
    \\hline
\\vspace{@parameter4@} @rad4@ \\\\
    \\hline
\\vspace{@parameter5@} @rad5@ \\\\
    \\hline
\\vspace{.6pt}
\\vspace{.6\\baselineskip} \\\\
\\end{tabular}
"""

latextabell = """
\\begin{center}
  \\begin{tabular}{|p{4.5cm}|p{.8cm}|p{.4cm}|p{1.0cm}|p{1.6cm}|p{1.6cm}|}
    \\hline
        \\vspace{0pt}\\large{Kontonamn} &\\vspace{0pt}\\small{Konto}& \\vspace{0pt}\\small{RS} & \\vspace{0pt}\\small{Projekt} & \\vspace{0pt}\\large{Debet} & \\vspace{0pt}\\large{Kredit} \\\\
    \\hline
    \\hline

{\\raisebox{-5pt}{\\normalsize{\\kontonamnA{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\KontoA{}}}} 
&\\centering {\\raisebox{-6pt}{\\large{\\RSA{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\ProjektA{}}}}
&\\hfill     {\\raisebox{-6pt}{\\large{\\DebetA{}}}} 
&\\hfill     {\\raisebox{-6pt}{\\large{\\KreditA{}}}} 
		\\vspace{6pt}
		\\\\
    \\hline
{\\raisebox{-5pt}{\\normalsize{\\kontonamnB{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\KontoB{}}}} 
&\\centering {\\raisebox{-6pt}{\\large{\\RSB{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\ProjektB{}}}}
&\\hfill     {\\raisebox{-6pt}{\\large{\\DebetB{}}}} 
&\\hfill     {\\raisebox{-6pt}{\\large{\\KreditB{}}}} 
		\\vspace{6pt}
		\\\\
    \\hline
{\\raisebox{-5pt}{\\normalsize{\\kontonamnC{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\KontoC{}}}} 
&\\centering {\\raisebox{-6pt}{\\large{\\RSC{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\ProjektC{}}}}
&\\hfill     {\\raisebox{-6pt}{\\large{\\DebetC{}}}} 
&\\hfill     {\\raisebox{-6pt}{\\large{\\KreditC{}}}} 
		\\vspace{6pt}
		\\\\
    \\hline
{\\raisebox{-5pt}{\\normalsize{\\kontonamnD{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\KontoD{}}}} 
&\\centering {\\raisebox{-6pt}{\\large{\\RSD{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\ProjektD{}}}}
&\\hfill     {\\raisebox{-6pt}{\\large{\\DebetD{}}}} 
&\\hfill     {\\raisebox{-6pt}{\\large{\\KreditB{}}}} 
		\\vspace{6pt}
		\\\\
    \\hline
{\\raisebox{-5pt}{\\normalsize{\\kontonamnE{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\KontoE{}}}} 
&\\centering {\\raisebox{-6pt}{\\large{\\RSE{}}}}
&\\centering {\\raisebox{-6pt}{\\large{\\ProjektE{}}}}
&\\hfill     {\\raisebox{-6pt}{\\large{\\DebetE{}}}} 
&\\hfill     {\\raisebox{-6pt}{\\large{\\KreditE{}}}} 
		\\vspace{6pt}
		\\\\
    \\hline
        \\multicolumn{4}{|r|}{\\raisebox{-5pt}{TOTALT}} &\\hfill{\\raisebox{-6pt}{\\large{\\TotalDebet{}}}}
							\\vspace{.6\\baselineskip} &\\hfill{\\raisebox{-6pt}{\\large{\\TotalKredit{}}}} \\\\
    \\hline  
  \\end{tabular}
\\end{center}


\\vspace{1cm}
"""

#       \\vspace{.6\\baselineskip}&& & & & \\\\


latexunderskrift ="""
Kvitto/faktura finns på baksidan.
\\vspace{0.5cm}\\\\
\\begin{tabular}{p{6.2cm}p{6.2cm}}
Sakattest & Ekonomisk attest\\\\
\\vspace{1cm} \\\\
\\rule{5.2cm}{0.5pt} & \\rule{5.2cm}{0.5pt} \\\\
@Signatur1@ & @Signatur2@\\\\
@SakTitel@ \\
\\vspace{0.6cm} \\\\
@Rule1@ &  @Rule2@ \\\\
@Namnförtydligande1@ & @Namnförtydligande2@\\\\
\\end{tabular}"""


latexfot = """
\\flushbottom
\\vspace{.2cm}
  \\fontsize{8pt}{8pt}
  \\selectfont
  \\begin{tabular}{p{2cm}p{2.5cm}p{2cm}p{2cm}p{2.6cm}}
    \\hline
    {\\em adress} & 
    {\\em besöksadress} & 
    {\\em org.nr}   & {\\em e-post} & {\\em hemsida} \\\\
    \\parbox[t]{3cm}{Fysiksektionen \\\\ THS \\\\ 100 44 Stockholm} & 
    Brinellvägen 26A &
    802411-8948  &
	& http://www.f.kth.se/
  \\end{tabular}
\\end{letter}
\\end{document}
"""


#Skriver över vald sträng i inläst variabel med element från listan
indata = readfromfile("indata.txt")
latexifyllning = latexifyllning.replace("@verifikatnummer@", indata[0])
latexifyllning = latexifyllning.replace("@verifikationsdatum@", indata[1])
latexifyllning = latexifyllning.replace("@bokföringsdatum@", indata[2])
if indata[-1][0] != "":
	latexspecifikation = latexspecifikation.replace("@rad1@", indata[-1][0])
else:
	latexspecifikation = latexspecifikation.replace("@rad1@","" )
if indata[-1][1] != "":
	latexspecifikation = latexspecifikation.replace("@rad2@", indata[-1][1])
	latexspecifikation = latexspecifikation.replace("@parameter2@", ".6pt")
else:
	latexspecifikation = latexspecifikation.replace("@rad2@","" )
	latexspecifikation = latexspecifikation.replace("@parameter2@",".6\\baselineskip")
if indata[-1][2] != "":
	latexspecifikation = latexspecifikation.replace("@rad3@", indata[-1][2])
	latexspecifikation = latexspecifikation.replace("@parameter3@", ".6pt")
else:
	latexspecifikation = latexspecifikation.replace("@rad3@","" )
	latexspecifikation = latexspecifikation.replace("@parameter3@",".6\\baselineskip")
if indata[-1][3] != "":
	latexspecifikation = latexspecifikation.replace("@rad4@", indata[-1][3])
	latexspecifikation = latexspecifikation.replace("@parameter4@", ".6pt")
else:
	latexspecifikation = latexspecifikation.replace("@rad4@","" )
	latexspecifikation = latexspecifikation.replace("@parameter4@",".6\\baselineskip")
if indata[-1][4] != "":
	latexspecifikation = latexspecifikation.replace("@rad5@", indata[-1][4])
	latexspecifikation = latexspecifikation.replace("@parameter5@", ".6pt")
else:
	latexspecifikation = latexspecifikation.replace("@rad5@","" )
	latexspecifikation = latexspecifikation.replace("@parameter5@",".6\\baselineskip")


#Byter namn som står under Ekonomisk attest. Vid tom input används den generella.
#I if-satsen behöver man bara byta ut namnet och titeln, det andra är grafiskt. 

#Ekonomisk attest Peter Fjellander, FN-Kassör
if indata[4] == "PF":
	latexunderskrift = latexunderskrift.replace("@Signatur2@","Peter Fjellander, FN-kassör 2012")
	latexunderskrift = latexunderskrift.replace("@Namnförtydligande2@", "")
	latexunderskrift = latexunderskrift.replace("@Rule2@", "")

#Ekonomisk attest Marcus Ahlström, Kassör
if indata[4] == "MA":
	latexunderskrift = latexunderskrift.replace("@Signatur2@","Marcus Ahlström, Kassör 2012")
	latexunderskrift = latexunderskrift.replace("@Namnförtydligande2@", "")
	latexunderskrift = latexunderskrift.replace("@Rule2@", "")

#Nedanstående kod ger upphov till den generella blanketten som ifylles manuellt om indata saknas.
else:
	latexunderskrift = latexunderskrift.replace("@Signatur2@","Signatur")
	latexunderskrift = latexunderskrift.replace("@Namnförtydligande2@", "Namnförtydligande och titel")
	latexunderskrift = latexunderskrift.replace("@Rule2@", " \\rule{5.2cm}{0.5pt}")

#Sakattest Ksenia Chechet, Projektledare FArm
if indata[3] == "KC":
	latexunderskrift = latexunderskrift.replace("@Signatur1@","Ksenia Chechet")
	latexunderskrift = latexunderskrift.replace("@SakTitel@","Projektledare FArm 2012")
	latexunderskrift = latexunderskrift.replace("@Namnförtydligande1@", "")
	latexunderskrift = latexunderskrift.replace("@Rule1@", "")

#Sakattest Didrik Lundberg, Ordförande FN
if indata[3] == "DL":
	latexunderskrift = latexunderskrift.replace("@Signatur1@","Didrik Lundberg")
	latexunderskrift = latexunderskrift.replace("@SakTitel@","Ordförande FN 2012")
	latexunderskrift = latexunderskrift.replace("@Namnförtydligande1@", "")
	latexunderskrift = latexunderskrift.replace("@Rule1@", "")


#Nedanstående kod ger upphov till den generella blanketten som ifylles manuellt om indata saknas.
else:
	latexunderskrift = latexunderskrift.replace("@Signatur1@","Signatur")
	latexunderskrift = latexunderskrift.replace("@SakTitel@","")
	latexunderskrift = latexunderskrift.replace("@Namnförtydligande1@", "Namnförtydligande och titel")
	latexunderskrift = latexunderskrift.replace("@Rule1@", " \\rule{5.2cm}{0.5pt}")
#Konto 1
latexifyllning = latexifyllning.replace("@konto1@", indata[5][0][1:])
if indata[5][0][0] == ("d" or "D"):
	latexifyllning = latexifyllning.replace("@debet1@", indata[5][1])
	latexifyllning = latexifyllning.replace("@kredit1@", "")
elif indata[5][0][0] == ("k" or "K"):
	latexifyllning = latexifyllning.replace("@kredit1@", indata[5][1])
	latexifyllning = latexifyllning.replace("@debet1@", "")
latexifyllning = latexifyllning.replace("@rs1@", indata[5][2])
latexifyllning = latexifyllning.replace("@projekt1@", indata[5][3])

#Konto 2
latexifyllning = latexifyllning.replace("@konto2@", indata[6][0][1:])
if indata[6][0][0] == ("d" or "D"):
	latexifyllning = latexifyllning.replace("@debet2@", indata[6][1])
	latexifyllning = latexifyllning.replace("@kredit2@", "")
elif indata[6][0][0] == ("k" or "K"):
	latexifyllning = latexifyllning.replace("@kredit2@", indata[6][1])
	latexifyllning = latexifyllning.replace("@debet2@", "")
latexifyllning = latexifyllning.replace("@rs2@", indata[6][2])
latexifyllning = latexifyllning.replace("@projekt2@", indata[6][3])

#Konto 3
latexifyllning = latexifyllning.replace("@konto3@", indata[7][0][1:])
if indata[7][0] != "":
	if indata[7][0][0] == ("d" or "D"):
		latexifyllning = latexifyllning.replace("@debet3@", indata[7][1])
		latexifyllning = latexifyllning.replace("@kredit3@", "")
	elif indata[7][0][0] == ("k" or "K"):
		latexifyllning = latexifyllning.replace("@kredit3@", indata[7][1])
		latexifyllning = latexifyllning.replace("@debet3@", "")
else:
	latexifyllning = latexifyllning.replace("@debet3@", "")
	latexifyllning = latexifyllning.replace("@kredit3@", "")
latexifyllning = latexifyllning.replace("@rs3@", indata[7][2])
latexifyllning = latexifyllning.replace("@projekt3@", indata[7][3])

#Konto 4
latexifyllning = latexifyllning.replace("@konto4@", indata[8][0][1:])
if indata[8][0] != "":
	if indata[8][0][0] == ("d" or "D"):
		latexifyllning = latexifyllning.replace("@debet4@", indata[8][1])
		latexifyllning = latexifyllning.replace("@kredit4@", "")
	elif indata[8][0][0] == ("k" or "K"):
		latexifyllning = latexifyllning.replace("@kredit4@", indata[8][1])
		latexifyllning = latexifyllning.replace("@debet4@", "")
else:
	latexifyllning = latexifyllning.replace("@debet4@", "")
	latexifyllning = latexifyllning.replace("@kredit4@", "")
latexifyllning = latexifyllning.replace("@rs4@", indata[8][2])
latexifyllning = latexifyllning.replace("@projekt4@", indata[8][3])

#Konto 5
latexifyllning = latexifyllning.replace("@konto5@", indata[9][0][1:])
if indata[9][0] != "":
	if indata[9][0][0] == ("d" or "D"):
		latexifyllning = latexifyllning.replace("@debet5@", indata[9][1])
		latexifyllning = latexifyllning.replace("@kredit5@", "")
	elif indata[9][0][0] == ("k" or "K"):
		latexifyllning = latexifyllning.replace("@kredit5@", indata[9][1])
		latexifyllning = latexifyllning.replace("@debet5@", "")
else:
	latexifyllning = latexifyllning.replace("@debet5@", "")
	latexifyllning = latexifyllning.replace("@kredit5@", "")
latexifyllning = latexifyllning.replace("@rs5@", indata[9][2])
latexifyllning = latexifyllning.replace("@projekt5@", indata[9][3])

#Bestämmer om beloppet hör till D eller K och lägger till det i respektive lista
tempdebetsumma = []
tempkreditsumma = []
if indata[5][0][0] == ("d" or "D"):
	tempdebetsumma.append(indata[5][1])
if indata[5][0][0] == ("k" or "K"):
	tempkreditsumma.append(indata[5][1])
if indata[6][0][0] == ("d" or "D"):
	tempdebetsumma.append(indata[6][1])
if indata[6][0][0] == ("k" or "K"):
	tempkreditsumma.append(indata[6][1])
if indata[7][0] != "":
	if indata[7][0][0] == ("d" or "D"):
		tempdebetsumma.append(indata[7][1])
	elif indata[7][0][0] == ("k" or "K"):
		tempkreditsumma.append(indata[7][1])
if indata[8][0] != "":
	if indata[8][0][0] == ("d" or "D"):
		tempdebetsumma.append(indata[8][1])
	elif indata[8][0][0] == ("k" or "K"):
		tempkreditsumma.append(indata[8][1])	
if indata[9][0] != "":
	if indata[9][0][0] == ("d" or "D"):
		tempdebetsumma.append(indata[9][1])
	elif indata[9][0][0] == ("k" or "K"):
		tempkreditsumma.append(indata[9][1])

#Gör flyttal av elementen så att det går att addera dem.
debetsumma = []
kreditsumma = []
for i in tempdebetsumma:
	debetsumma.append(float(i))
for i in tempkreditsumma:
	kreditsumma.append(float(i))
 
latexifyllning = latexifyllning.replace("@totald@", str(sum(debetsumma)))
latexifyllning = latexifyllning.replace("@totalk@", str(sum(kreditsumma)))



#Kontonamnsersättning
konton = [[1944,"FN Bank"],[2894, "Övriga kortfristiga skulder "]]

kontonamnslista = []
for i in konton:
	if str(i[0]) in str(indata[5][0][1:]):
		kontonamnslista.append(i[1])
	if str(i[0]) in str(indata[6][0][1:]):
		kontonamnslista.append(i[1])
	if str(i[0]) in str(indata[7][0][1:]):
		kontonamnslista.append(i[1])
	if str(i[0]) in str(indata[8][0][1:]):
		kontonamnslista.append(i[1])
	if str(i[0]) in str(indata[9][0][1:]):
		kontonamnslista.append(i[1])

#Utökar listan så att de kontonamn som inte finns ersätts med ""
while len(kontonamnslista) <= 4:
	kontonamnslista.append("")


#Ersätter kontonamnen
latexifyllning = latexifyllning.replace("@kontonamn1@", kontonamnslista[0])
latexifyllning = latexifyllning.replace("@kontonamn2@", kontonamnslista[1])
latexifyllning = latexifyllning.replace("@kontonamn3@", kontonamnslista[2])
latexifyllning = latexifyllning.replace("@kontonamn4@", kontonamnslista[3])
latexifyllning = latexifyllning.replace("@kontonamn5@", kontonamnslista[4])



#Lägger ihop alla variabler med TeX-kod
dokument = latexhuvud + latexifyllning + latexverifikationstabell + latexspecifikation + latextabell + latexunderskrift + latexfot

#Öppnar TeX-dokument och skriver all kod.
s = open(indata[0]+".tex","w")
s.write(str(dokument))
