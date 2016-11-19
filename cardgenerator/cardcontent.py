#
# @file cardcontent.py
# @author Oliver Merkel <Merkel(dot)Oliver(at)web(dot)de>
# @date 2016 November 18th
#
# @section LICENSE
#
# Copyright 2016, Oliver Merkel <Merkel(dot)Oliver(at)web(dot)de>
# All rights reserved.
#
# Released under the MIT license.
#
# @section DESCRIPTION
#
# @brief Card Content.
# 
# The array cardcontent holds the data for each card of the
# Scrum Card Game independent from its layout. The file needs
# to be in UTF-8 format, not ANSI / ASCII, when used in your
# text editor or IDE. Adding a translation is simply done by
# adding the appropriate line per card entry. language ID
# shall be in lower case. If an aphostroph ' is needed in
# your text then simply use double quotes surrounding your
# text. Any other issues when trying to add translation?
# Need help? Contact me... You are welcome.
#
# Initial card texts have been adopted by provisions from
#   Timofey Yevgrashyn (initial author),
#   Nils Bernert (German translation),
#   Oliver Merkel (German translation, English and German text review,
#     corrections, and new texts).
#

cardcontent = [
  {
    'type' : 'story',
    'story_id' : 1,
    'story_estimate' : 24,
    'en' : 'Users can exchange emails securely with predefined recipients.',
    'de' : 'Benutzer können E-Mails mit vordefinierten Empfängern sicher versenden.', 
  },
  {
    'type' : 'story',
    'story_id' : 2,
    'story_estimate' : 21,
    'en' : 'Users can send large files securely.',
    'de' : 'Benutzer können große Dateien sicher versenden.', 
  },
  {
     'type' : 'story',
    'story_id' : 3,
    'story_estimate' : 27,
    'en' : 'Users can set time limits on emails for reading.',
    'de' : 'Benutzer können festlegen, wie lange eine E-Mail lesbar bleibt.', 
  },
  {
    'type' : 'story',
    'story_id' : 4,
    'story_estimate' : 30,
    'en' : 'Users can send emails securely to unspecified recipients.',
    'de' : 'Benutzer können E-Mails an beliebige Benutzer sicher versenden.', 
  },
  {
    'type' : 'story',
    'story_id' : 5,
    'story_estimate' : 16,
    'en' : 'Administrators of organizations can monitor emails.',
    'de' : 'Administratoren von Organisationen können E-Mails überwachen.', 
  },
  {
    'type' : 'story',
    'story_id' : 6,
    'story_estimate' : 24,
    'en' : 'Each organization can set security policies and define recipients groups.',
    'de' : 'Jede Organisation kann Sicherheitsrichtlinien erlassen und Empfängergruppen definieren.', 
  },
  {
    'type' : 'story',
    'story_id' : 7,
    'story_estimate' : 43,
    'en' : 'Users can manage their emails effectively.',
    'de' : 'Benutzer können ihre E-Mails effektiv verwalten.', 
  },
  {
    'type' : 'story',
    'story_id' : 8,
    'story_estimate' : 23,
    'en' : 'Users and administrators can backup emails securely.',
    'de' : 'Administratoren und Benutzer können sichere Backups von E-Mails erstellen.', 
  },
  {
    'type' : 'story',
    'story_id' : 9,
    'story_estimate' : 36,
    'en' : 'Users and administrators can delete emails completely.',
    'de' : 'Benutzer und Administratoren können E-Mails komplett löschen.', 
  },
  {
    'type' : 'story',
    'story_id' : 10,
    'story_estimate' : 68,
    'en' : 'Users can access emails from mobile.',
    'de' : 'Benutzer haben Zugriff auf E-Mails über mobile Endgeräte.', 
  },
  {
    'type' : 'story',
    'story_id' : 11,
    'story_estimate' : 28,
    'en' : 'Users can send short messages securely to each other.',
    'de' : 'Benutzer können einander sicher Kurznachrichten schicken.', 
  },
  {
    'type' : 'story',
    'story_id' : 12,
    'story_estimate' : 24,
    'en' : 'Users don’t want to receive spam-letters.',
    'de' : 'Benutzer bekommen keine Spam-E-Mails.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'GOOD RECRUIT',
    'en' : 'New recruit is really good. You may roll 2 dice now and add these to the last roll.',
    'de_title' : 'GUTER NEULING', 
    'de' : 'Der neue Kollege ist exzellent. Du darfst beide Würfel nochmal würfeln und hinzuaddieren.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'HOME OFFICE',
    'en' : 'You have worked well at home. Add 2 points to the last roll.',
    'de_title' : 'HEIMARBEIT', 
    'de' : 'Du konntest im Home-Office konzentriert arbeiten. Zähle zwei Punkte zum letzten Würfelergebnis hinzu.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'BROWN BAG MEETING',
    'en' : 'Discussion during lunch time led to a splendid idea. Work on the current card is instantly resolved.',
    'de_title' : 'BROWN-BAG MEETING', 
    'de' : 'Während des Teammittagessens kam die Lösungsidee. Die Arbeit an der aktuellen Karte ist sofort abgeschlossen.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'GURU',
    'en' : 'A guru visited your office. You may immediately remove one problem card from the current story.',
    'de_title' : 'GURU', 
    'de' : 'Ein Guru war zu Besuch im Büro. Du darfst sofort eine Problemkarte von der aktuellen Story weglegen.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'DOING WELL',
    'en' : 'Things are going incredibly well. Add 4 to the last roll.',
    'de_title' : 'FORTSCHRITT', 
    'de' : 'Du bist im Flow. Zähle vier Punkte zum letzten Wurf hinzu.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'VISIBLE EFFORT',
    'en' : 'The boss acknowledges your effort. You may add 3 points to the previous result.',
    'de_title' : 'SICHTBARE LEISTUNG', 
    'de' : 'Der Chef kommt vorbei und bewundert Eure Arbeit. Zähle drei Punkte zum letzten Wurf hinzu.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'FAIRY',
    'en' : 'A fairy helped you. A card in progress is instantly finished.',
    'de_title' : 'GUTE FEE', 
    'de' : 'Eine gute Fee hat im Projekt ausgeholfen. Die Arbeit an einer Karte in-Progress ist sofort abgeschlossen.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-(',
    'en_title' : 'SICK AT HOME',
    'en' : 'You are sick at home. Skip your next turn.',
    'de_title' : 'KRANKMELDUNG', 
    'de' : 'Du bleibst krank zu Hause und musst einen Tag aussetzen.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-(',
    'en_title' : 'HEALTH PROBLEM',
    'en' : 'You have caught a cold. Skip your next turn.',
    'de_title' : 'GESUNDHEITSPROBLEM', 
    'de' : 'Leider hast Du Dich erkältet und musst einen Tag aussetzen.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-(',
    'en_title' : 'HARD DRIVE CRASHED',
    'en' : 'Hard drive crashed. Remove all progress from a card in progress.',
    'de_title' : 'FESTPLATTENCRASH', 
    'de' : 'Festplattencrash! Sämtlicher Fortschritt bei einer der laufenden Stories geht verloren.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-(',
    'en_title' : 'EMERGENCY CALL',
    'en' : 'An emergency call informs about an incident in the office. Everyone skips next turn.',
    'de_title' : 'NOTRUF', 
    'de' : 'Ein Notruf informiert über einen Zwischenfall im Betrieb. Das ganze Team muss eine Runde aussetzen.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-(',
    'en_title' : 'BUSINESS TRIP',
    'en' : 'You are sent on a business trip. Skip next turn.',
    'de_title' : 'GESCHÄFTSREISE', 
    'de' : 'Du gehst auf Geschäftsreise und musst einen kompletten Tag aussetzen.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-(',
    'en_title' : 'REQUIREMENTS CHANGE',
    'en' : 'PO decided to make changes to the project. So this story will take 4 hours more.',
    'de_title' : 'ANFORDERUNGSÄNDERUNG', 
    'de' : 'Der PO ändert die aktuelle Story im laufenden Sprint. Die Fertigstellung der Story benötigt zusätzliche vier Stunden.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-(',
    'en_title' : 'EXTRA COST',
    'en' : 'Your work costs more than planned. Add 6 hours to the story estimation.',
    'de_title' : 'ZUSATZKOSTEN', 
    'de' : 'Die Aufgabe ist komplexer als gedacht. Zähle sechs Stunden Aufwand zur aktuellen Aufgabe hinzu.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-|',
    'en_title' : 'BIRTHDAY',
    'en' : "It is your birthday today. Subtract 1 point from everybody's dice roll today.",
    'de_title' : 'GEBURTSTAG', 
    'de' : 'Du hast heute Geburtstag und hast Kuchen mitgebracht. Ziehe heute einen Punkt von jedem Wurf des Teams ab.', 
  },
  {
    'type' : 'event',
    'smiley' : ':-|',
    'en_title' : 'OVERTIME',
    'en' : 'You have worked overtime. Draw another card and follow its instruction.',
    'de_title' : 'ÜBERSTUNDEN', 
    'de' : 'Du hast Überstunden geleistet. Ziehe noch eine Karte und befolge die Anweisungen.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'GET SOME REST',
    'en' : 'Get some rest to refresh your mind.',
    'de_title' : 'MACH MAL PAUSE', 
    'de' : 'Mache mal eine Pause, um auf neue Gedanken zu kommen.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'CONSULTING',
    'en' : 'Involve a skilled team member from other team to consult you.',
    'de_title' : 'BERATUNG', 
    'de' : 'Holt Euch jemand erfahrenen aus einem anderen Team zur Beratung.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'EXTRA MEMBER',
    'en' : 'Add another member to the team. Throw dice once at any moment you want.',
    'de_title' : 'TEAMZUWACHS', 
    'de' : 'Ihr holt einen neuen Kollegen in Euer Team. Würfle einmalig zusätzlich bei Bedarf.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'COMMUNICATION',
    'en' : 'Enhance communication.',
    'de_title' : 'KOMMUNIKATION', 
    'de' : 'Ihr konzentriert Euch auf den Erfahrungsaustausch und verbessert Eure Kommunikation.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'SPECIALIST',
    'en' : 'Engage a specialist.',
    'de_title' : 'SPEZIALIST', 
    'de' : 'Ihr setzt Euch mit einem Spezialisten zusammen.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'AUTOMATED TESTING',
    'en' : 'Introduce automated testing.',
    'de_title' : 'TESTAUTOMATISIERUNG', 
    'de' : 'Es wird ein automatisiertes Testverfahren eingeführt.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'TL-SUPPORT',
    'en' : 'Your team lead is ready to take a part of the work.',
    'de_title' : 'TL-UNTERSTÜTZUNG', 
    'de' : 'Euer Team-Lead übernimmt einen Teil der Arbeiten.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'SHARE GOALS',
    'en' : 'Get the team together and share the key project goals.',
    'de_title' : 'VISUALISIERUNG DER ZIELE', 
    'de' : 'Ihr macht einen Workshop und sprecht über die Vision und die Ziele des Projekts.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'DEEP INSIGHT',
    'en' : 'Apply your deep domain knowledge.',
    'de_title' : 'TIEFENEINBLICK', 
    'de' : 'Wende Deine tiefen Fachkenntnisse an.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'LESSONS LEARNT',
    'en' : 'Apply experience destilled from former retrospectives.',
    'de_title' : 'GEWONNENE ERKENNTNISSE', 
    'de' : 'Wende Erfahrungen an, die aus früheren Retrospektiven kamen.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'COLLABORATION',
    'en' : 'Get the team together with PO and exchange information.',
    'de_title' : 'KOLLABORATION', 
    'de' : 'Ihr macht ein Refinement und klärt wichtige Fragen mit dem PO.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'PAIR PROGRAMMING',
    'en' : 'Apply pair programming.',
    'de_title' : 'PAIR-PROGRAMMING', 
    'de' : 'Ihr wendet Pair-Programming an.', 
  },
  {
    'type' : 'solution',
    'en_title' : 'ENHANCE SKILLS',
    'en' : 'Get training for raising the level of your skill.',
    'de_title' : 'WISSENSTRANSFER', 
    'de' : 'Ihr macht einen Wissenstransfer und steigert damit Eure Fähigkeiten.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'TECHNICAL OBSTACLE',
    'en' : 'Your work is blocked by a technical obstacle.',
    'de_title' : 'TECHNISCHES HINDERNIS', 
    'de' : 'Ein technisches Problem verhindert die Weiterarbeit.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'BAD QUALITY',
    'en' : 'You cannot finish the story because the quality is inadequate.',
    'de_title' : 'NIEDRIGE CODEQUALITÄT', 
    'de' : 'Die Codequalität ist schlecht. Es geht einfach nicht weiter.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'UNCLEAR SPEC',
    'en' : 'The specification is not clear enough for you.',
    'de_title' : 'UNKLARE SPEZIFIKATION', 
    'de' : 'Die Anforderungen der aktuellen Story sind unklar.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'UNSATISFIED USERS',
    'en' : 'You feel that users are not satisfied.',
    'de_title' : 'UNZUFRIEDENER KUNDE', 
    'de' : 'Ihr erfahrt, dass die Kunden mit der aktuellen Lösung nicht zufrieden sind.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'DATA IS MISSING',
    'en' : "You can't work with the story, as you don't have important data from PO.",
    'de_title' : 'FEHLENDE INFORMATION', 
    'de' : 'Ihr könnt an der aktuellen Story nicht weiter arbeiten, weil Euch wichtige Information fehlt.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'BAD COMMUNICATION',
    'en' : "You cannot communicate well with other team members. They just don't get you.",
    'de_title' : 'SCHLECHTE KOMMUNIKATION', 
    'de' : 'Irgendwie kannst Du das aktuelle Problem für die Kollegen im Team nicht verständlich erklären.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'POOR SKILLS',
    'en' : 'You are not skilled enough to finish the work.',
    'de_title' : 'DÜRFTIGES WISSEN', 
    'de' : 'Euch fehlt die Fähigkeit, um diese Herausforderung zu lösen.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'UNSTABLE SYSTEM',
    'en' : 'System is very unstable. You have to test with major difficulties.',
    'de_title' : 'INSTABILES SYSTEM', 
    'de' : 'Das System stürzt dauernd ab. Tests sind nur unzureichend möglich.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'BAD MOOD',
    'en' : 'Today you are upset. So you are too lazy to work.',
    'de_title' : 'GENERVT', 
    'de' : 'Du bist so genervt, dass Du nicht weiter an dieser Story arbeiten kannst.', 
  },
  {
    'type' : 'problem',
    'en_title' : 'INTEGRATION ISSUES',
    'en' : "Your colleague provided you with the component, which is different from what you expected. Your work is blocked.",
    'de_title' : 'INTEGRATIONSPROBLEM', 
    'de' : 'Eine Zulieferung eines Kollegen ist anders, als Ihr es erwartet habt. Das blockiert die Arbeit.', 
  },
]
