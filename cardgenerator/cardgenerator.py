#
# @file cardgenerator.py
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
# @brief Card Generator.
# 
# When cardgenerator.py is started it processes
#
# * the card content specifications from cardcontent.py
# * the card sizes as defined in pagelayout.py
#
# A set of SVG (Scaleable Vector Graphics) gets rendered
# in DIN-A4 page format (width='210mm' height='297mm') and
# will be written to disk as SVG files.
# The SVGs will be generated for a predefined set of languages
# and card sizes.
#

"""
Example:

  >>> from cardgenerator import CardGenerator
  >>> CardGenerator().start()
  Generated 7 files in language de and card size 104x69mm
  Generated 7 files in language en and card size 104x69mm
  Generated 7 files in language de and card size 88x63mm
  Generated 7 files in language en and card size 88x63mm
  Generated 6 files in language de and card size 85x54mm
  Generated 6 files in language en and card size 85x54mm
  >>>
"""

from pagelayout import pagelayout 
from pagelayouter import PageLayouter
from cardcontent import cardcontent

class CardGenerator(Exception):
  def __init__(self):
    pass

  def start(self):
    for pl in pagelayout:
      w = pl['width']
      h = pl['height']
      for lang in [ 'de', 'en' ]:
        index = 0
        fileIndex = 0
        amountCards = len(cardcontent)
        while index < amountCards:
          layouter = PageLayouter( w, h, lang, index )
          # layouter.info()
          ( svg, renderedCards, skippedCards ) = layouter.svg()
          filename = 'scrum card game-%sx%smm-%s-%s.svg' % ( w, h, lang, fileIndex )
          with open(filename, 'w+', encoding='utf8') as f:
            f.write(svg)
          index = index + renderedCards + skippedCards
          fileIndex = fileIndex + 1
        print('Generated %s files in language %s and card size %sx%smm' \
          % ( fileIndex, lang, w, h))

if '__main__' == __name__:
  CardGenerator().start()
