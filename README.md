# Scrum-Card-Game

Scrum Card Game: Scrum Sprint Simulation played as a multi-player card game

<table><tbody>
<tr><td><img alt='The main game material of Scrum Card Game' src='scrum_card_game-rules/docbook/src/docbkx/media/game_material_de.jpg' width='80%' /></td><td>The main game material of Scrum Card Game,<br /><a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0'><img alt='Creative Commons License' style='border-width:0' src='res/cc_by_sa-88x31.png' /></a>This image is licensed under a <a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0'>Creative Commons Attribution-ShareAlike 4.0 International License</a>.</td></tr>
</tbody></table>

## Abstract

A card game has been created in this project to support learners of agile framework SCRUM.
The card game is used so that players experience work in a simulated SCRUM sprint scenario.
It allows reflection of many questions and topics that happen in real life while working in
a SCRUM team, too. Players act in a collaborative team environment during game play.
This game is typically played during a training or workshop.

__Keywords__ _SCRUM, agile, software development framework, education, training, card game, learning, simulation, multi-player, team work_

## Motivation

The concept to simulate real life scenarios in game play turns out to be an approach for
several authors in the agile domain. The intention of such an approach is to ease
understanding of underlying methods and strategies for learners of the agile software
development domain. The proposal of using such a card game follows the idea that a
simulated game scenario is helpful for experienced players to either exploit situations
not experienced so far and explore or test strategies when encoutering real life
situations similar or close to the ones as simulated in game play.

## Related Work

Various proposals to simulate real life agile scenarios in game play already exist.
Major differences among these simulation games can be seen in terms of game material,
simulated roles per player, amount of players, effort of preparation and set up,
abstraction or detail level of game aspects covering the
simulated agile real life domain. By skipping such aspects the game moves from
generalization to specialization of covered subjects or vice versa. Such that the choice
of aspects leads to a training of either wider or deeper knowledge in the game scope.

[BNH03] describes the card game ___Problems and Programmers___ as a competitive game.
Each player acts in the role of a project leader given
same project tasks but solved independently from each other. Thus it restricts team play
and the player will hardly gain more experience in team collaboration and team
retrospectives with acting in and responsibility of different roles. Still it
covers project phases from setting up requirements, design phase, implementation,
integration, and maintenance. The game play follows a classic waterfall model. It does
hardly cover agile self organizing, iterative, and retrospective recurring aspects.

In [FeSo10] the card game ___PlayScrum___ is presentedcovering the scope of learning
Scrum agile method. It claims to be the predecessor of ___Problems and Programmers___.
Again it is missing collaboration of participating players. Instead each player slips
into the role of a Scrum Master following the practices of Scrum. A die is used to
determine the amount of cards to be drawn from a card pile on a player's turn.
The team working on open tasks from a Backlog is represented in an abstract way by
so called developer cards the Scrum Master controls. Having that said this means that
team experiences by human players in different roles working in collaboration are
not performed and shared amongst the participants.

## Print and Play

This repository's subdirectories contain PDF files with rules and
cards to print and play the game. Different variants of card
sizes are available. To make the cards durable you could laminate
the cards.

* <a href='https://github.com/OMerkel/Scrum-Card-Game/releases'>Get the latest release in English or German!</a>
* Additionally the repository's root holds subdirectories with names reflecting which card size related files can be found in there.

The card designs of the Scrum Card Game are available in PDF and SVG. If you can get blank business cards
available as office supplies then you can print the PDF onto the blank cards.
Another option is to print the cards on normal paper and then cut the cards manually. Heavy
weight paper shall be used for enhanced durability. For better protection the cards could be laminated.
The lamination foil should be non glare if possible and available. In case you plan to create own card
texts or modify the existing ones you should go for an alternative approach like putting the cards into
business card pouches for single cards. The cards are kept in the protecting pouches while playing and
the cards can be easily removed from the pouch as intended, be modified and placed back.

Using card size of standard business cards (85mm x 54mm) will allow to use business card pouches
for card protection. To ease printing and finishing of cards a business card size of
85mm x 54mm is chosen in files of directory named '85x54mm-business card size'.

Instead of searching for business card pouches in office supplies
you could find similar articles in game stores stocking Trading Card
Games (TCGs). TCG players often protect their cards with card
sleeves or card protectors. The ones that match the business cards
in size are called Standard American Board Game Sleeves
(87mm x 56mm, 3-1/2 x 2-1/4 inch).

<table><tbody>
<tr><td><img alt='Using Standard Card Size Sleeves and Deck Box' src='res/Standard Card Size Sleeves and Deck Box.jpg' width='80%' /></td><td>Using Standard Card Size Sleeves and Deck Box,<br /><a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0'><img alt='Creative Commons License' style='border-width:0' src='res/cc_by_sa-88x31.png' /></a>This image is licensed under a <a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0'>Creative Commons Attribution-ShareAlike 4.0 International License</a>.</td></tr>
</tbody></table>

More common and popular for TCGs is a so called Standard Card Size
(88mm x 63mm, 3-1/2 x 2-1/2 inch) with sleeve protectors a bit
bigger than that (91mm x 66mm). In case you can get these in different
variants then non glare sleeves are recommended.

## How to...

In case you want to generate components like rules text or the cards separately or on your own.

### Generate the Rules as PDF

Rules are maintained in [Docbook](http://docbook.org) format.
Related files can be found in `Scrum-Card-Game/scrum_card_game-rules/docbook/src/docbkx` .
The simplest way to generate the PDFs from Docbook using this repository is to install and use [Maven](https://maven.apache.org).

Invocation to generate the PDFs from Docbook looks like

```
cd scrum_card_game-rules/docbook
mvn docbkx:generate-pdf
```

### Generate the Playing Cards

To just generate the cards with already existing card defintions [Python](https://www.python.org) is needed.

```
cd cardgenerator
python cardgenerator.py
```

The cards get generated in the same directory as [SVG](https://www.w3.org/Graphics/SVG)
(Scalable Vector Graphics, W3C standard).

### Modify the existing Playing Cards or create new ones

Cards are maintained in [Python](https://www.python.org) files. Python script files are separated
from files that hold the card description data. This split of script files and pure data files is
done although the card description data files are simple Python files, too.
Thus this is done to not mix data with scripts.

The card descriptions can be found in `cardgenerator/cardcontent.py` covering all languages.
The syntax follows Python [JSON](http://json.org) (JavaScript Object Notation,
ECMA-404 The JSON Data Interchange Standard) format.

Card types supported by the `cardgenerator.py` are

1. 'type' : 'story'
2. 'type' : 'event'
3. 'type' : 'solution'
4. 'type' : 'problem'

Event cards describe positive, neutral, or negative impact on the game result by smilies.
Smilies supported by the `cardgenerator.py` are

1. 'smiley' : ':-)'
2. 'smiley' : ':-|'
3. 'smiley' : ':-('

Titles and text fields should stay at a reasonable text length.

### Volunteer translating the Playing Cards

Any help in translating the cards into other languages is highly appreciated. If you want
to volunteer and see any bigger technical issues on your side and already followed the
descriptions then simply get in touch with a maintainer of the Scrum Card Game GitHub
repository. You are welcome!

Translation (new texts and text replacements to improve existing texts) is mainly done by
modification of the file `cardgenerator/cardcontent.py`. Editing is done in any text
editor that supports files in UTF-8 format. Which is usually the case in all major
up-to-date text editors.

Adding a translation is simply done by adding the appropriate line per card entry.
Language ID shall be in lower case. If an aphostroph ' is needed in your text then
simply use double quotes surrounding your text.

If you scroll around in the file you will see that card content is defined in there
and each card definition holds at least English and German text (if not even some more)
directly beside each other.

E.g. like
```
cardcontent = [
...
  {
    'type' : 'event',
    'smiley' : ':-)',
    'en_title' : 'GURU',
    'en' : 'A guru visited your office. You may immediately remove one problem card from the current story.',
    'de_title' : 'GURU', 
    'de' : 'Ein Guru war zu Besuch im Büro. Du darfst sofort eine Problemkarte von der aktuellen Story weglegen.', 
  },
...
```

Now if you want to add a new language like Spanish, then this can be done with just
adding in the curly braces

```
    'es_title' : 'GURU', 
    'es' : 'Un gurú ha venido a verte. Puedes eliminar una tarjeta de Problema inmediatamente.',
```

or Russian

```
    'ru_title' : ' гуру', 
    'ru' : 'Мимо проходил гуру. Вы можете убрать все Проблемы с одной задачи.',
```

For card texts not translated so far you should eventually create dummy texts entries
for your language to assist upcoming translation steps.

And that's it! Some additional changes are needed in the scripts section currently.
As soon as you contribute a four eye review of your changes is performed.
The ```cardgenerator/cardgenerator.py``` holds a line defining which translations
shall be generated. It shall look like:

```
 for lang in [ 'de', 'en' ]:
```

If a preferred language is missing simply add it. If a language is intended to be skipped
then remove it. Any information missing? Just ask... You are welcome.

### Concatenate PDFs into one PDF if needed

A possible cover page can be found as `scrum_card_game-rules/scrum_card_game-cover.pdf`

SVGs can be converted to PDF or PS (Postscript) in various ways and with various tools.

In case you insist to have rules and cards in a single combined PDF file a free tool
like [GhostScript](http://ghostscript.com) could be used.

Concatenating multiple PDFs into a combined one could be achieved as follows

```
gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=scrum_card_game-104x69mm-en.pdf scrum_card_game-cover.pdf scrum_card_game-rules-en.pdf scrum_card_game-104x69mm-en-0_svg.pdf scrum_card_game-104x69mm-en-1_svg.pdf...
```

Here the PDFs `scrum_card_game-cover.pdf scrum_card_game-rules-en.pdf scrum_card_game-104x69mm-en-0_svg.pdf scrum_card_game-104x69mm-en-1_svg.pdf...` get concatenated into `scrum_card_game-104x69mm-en.pdf`.

Windows users might find GhostScript versions in 32bit and 64bit as `gswin32.exe` and `gswin64.exe` with similar command line arguments in place.

## Links

* http://scrumcardgame.com/scrum-card-game-rules
* http://docbook.org
* https://maven.apache.org
* https://www.python.org
* http://json.org
* https://www.w3.org/Graphics/SVG
* http://ghostscript.com

## References

* __[FeSo10]__ João M. Fernandes, Sónia M. Sousa, "[PlayScrum - A Card Game to Learn the Scrum Agile Method](https://pdfs.semanticscholar.org/ec4b/3b68875c27a01da0edffc652e610ef4615d4.pdf)", Proceedings of Second International Conference on Games and Virtual Worlds for Serious Applications, VS-GAMES2010, Portugal, March 2010.
* __[BNH03]__ Alex Baker, Emily Oh Navarro, André van der Hoek, "[An Experimental Card Game for Teaching Software Engineering](http://www.ics.uci.edu/~emilyo/papers/CSEET2003.pdf)", Proceedings of CSEET 2003, 16th Conference on Software Engineering Education and Training, p.216, ISBN:0-7695-1869-9, IEEE Computer Society Washington, DC, USA, 2003
    * [Problems and Programmers](https://boardgamegeek.com/boardgame/21999/problems-and-programmers) @ https://boardgamegeek.com

## Legal / License

<a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0'><img alt='Creative Commons License' style='border-width:0' src='res/cc_by_sa-88x31.png' /></a><br />This work is licensed under a <a rel='license' href='http://creativecommons.org/licenses/by-sa/4.0'>Creative Commons Attribution-ShareAlike 4.0 International License</a>.

_All logos, brands, and trademarks mentioned belong to their respective owners._
