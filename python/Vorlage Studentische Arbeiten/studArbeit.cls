%Ver 1 - Standard-Vorlage �bernommen
%Copyright 2013, Lutz Kleinsorge, Lehrstuhl Schiffbau 

\NeedsTeXFormat{LaTeX2e}
\LoadClass[11pt,plainfootsepline,footsepline,parskip=full,toc=bibliography]{scrreprt}
\ProvidesFile{studArbeit}[2013/01 studArbeit-Template]
%\documentclass[11pt,headsepline,plainfootsepline,footsepline,parskip=full,toc=bibliography]{scrreprt}

\RequirePackage[latin1]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage[ngerman]{babel}
\RequirePackage{ae}
\RequirePackage{vmargin}
\setmarginsrb{30mm}% randlinks
        {20mm}% randoben
        {20mm}% randrechts
        {20mm}% randunten
        {15pt}% kopfh�he
        {10mm}% kopfabstand
        {20pt}% f��e
        {10mm}% fu?bstand
\RequirePackage{import}
\RequirePackage[footsepline,plainfootsepline]{scrpage2}
\pagestyle{scrheadings}
\RequirePackage[subfigure]{tocloft}
\RequirePackage{acronym}
\RequirePackage{color}
\RequirePackage{colortbl}
\RequirePackage{moreverb}
\RequirePackage{amsmath}
\RequirePackage{graphicx}
\RequirePackage{url}
\RequirePackage{longtable}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{booktabs}
\RequirePackage{natbib}
\RequirePackage{multirow}
\RequirePackage{pdfpages}
\RequirePackage{paralist}
\RequirePackage{booktabs}

\RequirePackage[center]{subfigure}
\RequirePackage[margin=0pt,font=normalsize,labelfont=normalsize,
format=hang]{caption}
\RequirePackage[breaklinks=true,bookmarksopen,%
pdfstartview=FitH,colorlinks,%
urlcolor=black,linkcolor=black,citecolor=black,%
pdftitle=TypDerArbeit,pdfauthor={Autor}]{hyperref}

% abstand lof
\setlength{\cftfignumwidth}{10mm} 
\definecolor{fms}{RGB}{0,129,199}
\definecolor{uni}{RGB}{0,74,153}

%keine Hurenkinder und Schusterjungen, sowie b�ndiger Abschluss der Seiten
\clubpenalty10000
\widowpenalty10000
\displaywidowpenalty=10000
\raggedbottom
\flushbottom

% TOC
\setcounter{tocdepth}{1}
\tolerance 2000
\emergencystretch 20pt

%Seitenaussehen:
\renewcommand*\chaptermarkformat{}%verhindert die Zahlen vor dem Kapitel in der Kopfzeile

%Define Fields for the titlepage
\def\TitelDeutsch#1{\gdef\@TitelDeutsch{#1}}
\def\TitelEnglisch#1{\gdef\@TitelEnglisch{#1}}
\def\TextAufgabenstellung#1{\gdef\@TextAufgabenstellung{#1}}
\def\ArtDerArbeit#1{\gdef\@ArtDerArbeit{#1}}
\def\Autor#1{\gdef\@Autor{#1}}
\def\AutorMatrikel#1{\gdef\@AutorMatrikel{#1}}
\def\AutorEmail#1{\gdef\@AutorEmail{#1}}
\def\AutorStudiengang#1{\gdef\@AutorStudiengang{#1}}
\def\Bearbeitungszeitraum#1{\gdef\@Bearbeitungszeitraum{#1}}
\def\AusgabeArbeit#1{\gdef\@AusgabeArbeit{#1}}
\def\ErstGutachter#1{\gdef\@ErstGutachter{#1}}
\def\ZweitGutachter#1{\gdef\@ZweitGutachter{#1}}

%Newcommand \titelSeite produces the first page
\newcommand{\titelSeite}{
\thispagestyle{empty} \enlargethispage{20mm}
\vspace*{20mm} 
\begin{flushright}
{\color{uni} \sffamily{\LARGE\@ArtDerArbeit}}\\
{\parindent -15mm\color{uni}\rule{1.1\textwidth}{1mm}}
{\color{uni}\sffamily {\LARGE \textbf{\@TitelDeutsch}}\\[3mm]
{\Large \@TitelEnglisch}}\\
{\parindent -15mm\color{uni}\rule{1.1\textwidth}{1mm}}\\[3mm]
{\color{uni} \sffamily
eingereicht an der \\
Fakult�t f�r Maschinenbau und Schiffstechnik der Universit�t Rostock}\\[10mm]
{\color{uni}\sffamily%\Large
 vorgelegt von: \@Autor \\
 Martikelnummer: \@AutorMatrikel}\\[2mm]
{\color{uni}\sffamily \@AutorStudiengang } \\[10mm]
{\color{uni}\sffamily 
\begin{tabular}{rr}
 Erstgutachter: & \@ErstGutachter \\
 Zweitgutachter: & \@ZweitGutachter \\
\end{tabular}}
\vfill
{\color{uni}\sffamily 
\includegraphics[height=12mm, clip=]{Include/figures/uni-logo}\\
Lehrstuhl Schiffbau\\[2mm]
Rostock, \today }
\end{flushright}
\newpage
\thispagestyle{empty} \enlargethispage{20mm} \vspace*{25mm}%
\normalsize
\phantom{x}
\vfill
\noindent Copyright \copyright\ \the\year, \@Autor\\
Alle Rechte vorbehalten, Text, Bilder und Grafiken sind gesch�tztes
Material.
\\[10mm]
%\begin{tabbing}%
%email: \={\@AutorEmail}\kill
%\@Autor\\
%Universit�t Rostock\\
%Albert-Einstein-Stra�e 2\\
%D-18059 Rostock\\[1mm]
%Tel:  \>+ 49 381 498 9270\\
%FAX:  \>+ 49 381 498 9272\\
%\makeatletter email: \>{\tt \@AutorEmail}%
%\end{tabbing}
%\makeatother
\@Autor\\
\makeatletter{\tt \@AutorEmail}\makeatother \\[5mm]
\vspace{10mm} \noindent \scriptsize Dieses Dokument wurde am \today\
mit dem Satzsystem \LaTeX\ gesetzt. \normalsize
\clearpage
}

\newcommand{\selbst}{
\newpage
% Selbst�ndigkeitserkl�rung
\thispagestyle{empty} \enlargethispage{20mm} \vspace*{25mm}%
\normalsize
%\begin{tabularx}{\textwidth}{|p{20mm}|>{\raggedright}X|p{80mm}|}
%\hline Version & Datum & Kommentar\\\hline\hline%
%\thisdocversion & \thisdocversiondate & \thisdoccomment
%\\\hline
%\end{tabularx}
%\vspace{30mm}
\textbf{\sffamily Eidesstattliche Versicherung.} Ich versichere eidesstattlich durch eingenh�ndige Unterschrift, dass ich die Arbeit selbstst�ndig und ohne Benutzung anderer als der angegebenen Hilfsmittel angefertigt habe. Alle Stellen, die w�rtlich oder sinngem�� aus Ver�ffentlichungen entnommen sind, habe ich als solche kenntlich gemacht. Ich wei�, dass bei Abgabe einer falschen Versicherung die Pr�fung als nicht bestanden zu gelten hat.\\[20mm]%

\begin{tabularx}{\textwidth}{p{50mm}X}
Ort, Datum & \raggedleft Unterschrift
\end{tabularx}
\vspace{30mm}

\textbf{\sffamily Einverst�ndniserkl�rung.} Ich erkl�re mich damit einverstanden, dass ein Exemplar meiner \@ArtDerArbeit\ in der Universit�tsbibliothek der Universit�t Rostock aufbewahrt und f�r die allgemeine Nutzung zug�nglich gemacht wird. Ich nehme zur Kenntnis, dass dies die Wirkung einer Ver�ffentlichung im urheberrechtlichen Sinne hat.\\[20mm]%

\begin{tabularx}{\textwidth}{p{50mm}X}
Ort, Datum & \raggedleft Unterschrift
\end{tabularx}
\clearpage
}
%%% ENDE TITELSEITE
%TableofContents + TOF, etc
\newcommand{\toc}{
\pagenumbering{roman} \setfootsepline{}[\color{white}]
\tableofcontents
\clearpage
\listoffigures
\clearpage
\listoftables}
%Produziert Aufgabenstellung
\newcommand{\aufgabenstellung}{
\clearpage
\thispagestyle{empty}
\begin{center}
\sffamily\textbf{%
Aufgabenstellung\\
{\LARGE\@TitelDeutsch}}\\[5mm]%
\normalsize%
\@ArtDerArbeit\\[2mm]
\@Autor\\
Matrikelnummer: \@AutorMatrikel\\[10mm]
%
\end{center}
\@TextAufgabenstellung
\vfill
\begin{tabbing}
Betreuer: \= Prof. Dr.-Ing Robert Bronsart \kill
Betreuer: \> \@ErstGutachter\\
\> \@ZweitGutachter\\
\end{tabbing}
\begin{tabbing}
Bearbeitungszeitraum: \= 56 Monate \kill
 Ausgabe der Arbeit: \> \@AusgabeArbeit\\
Bearbeitungszeitraum: \> \@Bearbeitungszeitraum\\
\end{tabbing}
\clearpage
}
\newcommand{\start}{
\pagenumbering{arabic} \setfootsepline{0.5pt}[\color{black}]
\clearscrheadfoot %eigentlich unn�tig
\setkomafont{pageheadfoot}{\normalfont}
	\ihead[]{\headmark}
	\chead[]{}
	\ohead[]{\pagemark}
	\ifoot[\@Autor]{\@Autor}
	\cfoot[]{}
	\ofoot[Universit�t Rostock]{Universit�t Rostock}
\pagestyle{scrheadings}

\setlength{\parindent}{0mm} }