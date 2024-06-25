# import tk
# import tkinter as tk
# from tkinter import messagebox
# class QuizApp:
#     def __init__(self, root): #constructeur
#         self.root = root
#         self.root.title("Intellilearn")  # fenetre principale
#         self.score = 0
#         self.question_num = 1
#
#         self.questions = ("Welche Dimensionen gehören zum magischen Viereck des Projektmanagements? :",
#             "Welche Herausforderungen treten häufig bei einer Software auf?:",
#             "Welche Begriffe gehören zu den organisatorischen Erfolgsfaktoren ?",
#             "Welche Eigenschaften hat eine Software? :",
#             "Welche Definition beschreibt ein Programm? :",
#             "Was ist wichtig bei der Erfassung von Anforderungen? :",
#             "Was ist die Konsequenz, wenn man kein Architeckturentwurf macht? :",
#             "Was sind die Kernaufgaben der Architektur? :",
#             "Warum werden Aufgaben im Betrieb und in der Evolution oft falsch unterschätzt? :",
#             "Nach was kann man Software kategorisieren? :",
#             "Auf welche Art erfolgt die Erbringung des Nutzers? :",
#             "Welche der folgenden Perspektiven gehören zum Ansichtenmodell? :",
#             "Welche Qualitätseigenschaften können von Kunden erwartet werden? :",
#             "Was ist das Ziel eines Vorgehensmodell? :",
#             "Ein Vorgehensmodell ist… :",
#             "Welche Folgen gehören zu dem Traditionellen Vorgehensmodell? :",
#             "Zu den Nachteilen des Wasserfall Modells gehören … ",
#             "Welche der folgenden Eigenschaften gehören zu dm Spiral Modell? :",
#             "Nach welchen Prinzipien ist das V-Modell XT ausgerichtet? :",
#             "Welche Rollen gehören zum Scrum? :",
#             "Welche ist die grundlegende Idee des Scrums? :",
#             "Wie lange dauert ein Sprint ca.? :",
#             "Welche Vorteile weist der Scum auf? :",
#             "Welche Definition passt zu der eines Modells? :",
#             "Was ist bei der Modellbildung wichtig? :",
#             "Was wird zur Modellierung von Daten verwendet? :",
#             "Welches Zeichen nutzt man für ein Privates Attribut in einer Notationsübersicht? :",
#             "Welche Art von Modellierungen gibt es? :",
#             "Wie nennt man dieses Symbol: ◆) ? :")
#
#         self.options = (("Qualität","Radius","Kommunikation"),
#            ("Ungenügende Planung","Schreibfehler","bessere Strucktur"),
#            ("Ressourcenverfügbarkeit","klare Anforderungen","Motivation"),
#            ("Software ist materiell","Software ist konkret","Software ist Befähigung"),
#            ("Verarbeitungsvorschrift auf einer Rechenanlage","Von Umgebung abgegrenztes Gebilde","Die Rechenanlage einer Umgebung"),
#            ("Die Analyse, um herauszufinden was der Hersteller will","Die Spezifikation, um die Anforderungen festzulegen","Der Test, um die Qualität des Codes sicherzustellen"),
#            ("Man spart Zeit in der Wartung" , "Man benötigt mehr Zeit in der Wartung",	"Es gibt keine Konseuqenzen"),
#            ("Analyse","Managementaufgaben","Wartung"),
#            ("weil es nicht wichtig ist","…weil es noch weit weg in der Zukunft ist","weil sie andere Sachen priorisieren"),
#            ("Grad der Systeme",	"Bearbeitung",	"Lizenzmodell"),
#            ("Anwenderinteraktion",	"Datenspeicherung",	"Datenerkennung"),
#            ("Fokussicht", "Plattformanbhängige Komponentensicht","Innensicht "),
#            ("Qualität in  Kompetenz","Qualität in Bearbeitung",	"Qualität in der Vermarktung"),
#            ("Systematisierung der Softwareentwicklung",	"Qualitative Ergebnisse","Schnelle Verarbeitung"),
#            ("…ein Spielplan","… eine Herausforderung","… ein Prozess zur Speicherung von Daten"),
#            ("viele verschiedene Ansätze","nur ein einzigen Ansatz",	"keine Gemeinsamkeiten"),
#            ("… eine schwere Projektorganisation","…Komplexität" ,"…ein schweres Controlling"),
#            ("aufwändige Planung","Schnelle Feedback-Zyklen","einfache Organisation"),
#            ("unstruckturierte Reihenfolgen","Iterative Entwicklung", "Alphabetische Reihenfolge"),
#            ("Creative Owner","Product  Master", "Team"),
#            ("Selbstorganisierte Teams",	"das Team muss einem strickten Plan befolgen","Nutzung abgesprochener Schritte"),
#            ("max. 10 Tage",	"max. 20 Tage",	"max. 30 Tage"),
#            ("einfache Strucktur", "'eigene' Terminologie",	"schwer zu verstehen"),
#            ("eine Komplizierte Idee","eine mathematische Ansicht","eine Abstraktion"),
#            ("Fomalisierung von Datenstruckturen","Erfassung von Ideen","Modellinerung der Daten"),
#            ("UML-Klassendiagramm",	"MLU-Klassendiagramm ","ULM-Klassendiagramm"),
#            ("'+'",	"'#'",	"'-'"),
#            ("Modellierung von Zuständen", "Modellierung von Eigenschaften", "Modellierung von Signalen"),
#            ("Assoziaton","Aggregation", "Komposition"))
#
#         self.answers =(  "Qualität",
#             "Ungenügende Planung",
#             "Ressourcenverfügbarkeit",
#             "Software ist Befähigung",
#             "Verarbeitungsvorschrift auf einer Rechenanlage",
#             "Die Spezifikation, um die Anforderungen festzulegen",
#             "Man benötigt mehr Zeit in der Wartung",
#             "Analyse",
#             "…weil es noch weit weg in der Zukunft ist",
#             "Grad der Systeme",
#             "Anwenderinteraktion",
#             "Fokussicht",
#             "Qualität in Kompetenz",
#             "Systematisierung der Softwareentwicklung",
#             "…ein Spielplan",
#             "viele verschiedene Ansätze",
#             "… eine schwere Projektorganisation",
#             "aufwändige Planung",
#             "Iterative Entwicklung",
#             "Product Master",
#             "Selbstorganisierte Teams",
#             "max. 10 Tage",
#             "einfache Struktur",
#             "eine Abstraktion",
#             "Modellierung der Daten",
#             "UML-Klassendiagramm",
#             "'-'",
#             "Modellierung von Zuständen",
#             "Aggregation")
#
#
#         self.correct_answers = [0, 0, 0]  # Index von Korrekte Antworten
#
#         self.question_label = tk.Label(root, text="", wraplength=500) #je cree un widget pour afficher une classe ou un object
#         self.question_label.pack(pady=20)
#
#         self.buttons = [tk.Button(root, text="", command=lambda opt=i: self.check_answer(opt)) for i in range(3)]
#         for button in self.buttons:
#             button.pack(fill="x", pady=5)
#
#         self.next_button = tk.Button(root, text="NEXT", command=self.next_question)
#         self.next_button.pack(pady=20)
#
#         self.display_question()
#
#
#     def display_question(self):
#         self.question_label.config(text=self.questions[self.question_num])
#         for i, option in enumerate(self.options[self.question_num]):
#             self.buttons[i].config(text=opti2on)
#
#
#     def check_Answer(self, selected_option):
#         if selected_option == self.correct_answers[self.question_num]:
#             self.score += 1
#             self.next_question()
#
#     def next_question(self):
#         self.question_num += 1
#         if self.question_num < len(self.questions):
#             self.display_question()
#         else:
#             self.end_quiz()
#
#
#     def end_quiz(self):
#         messagebox.showinfo("quiz done", f"High score is {self.score} / {len(self.questions)}")
#         self.root.destroy()
#
#
# # Création de la fenêtre principale Tkinter
# root = tk.Tk()
# app = QuizApp(root)
# root.mainloop()
