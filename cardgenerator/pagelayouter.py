#
# @file pagelayouter.py
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
# @brief Page Layouter.
# 
# The pagelayouter.py is used by cardgenerator.py
# Its purpose is to render the SVG representation of a single
# page as SVG text.
#
# The PageLayouter's constructor takes parameters for
# * card dimensions (width and height in mm),
# * language ( e.g. 'de' or 'en' ), and
# * card index (the card position inside array cardcontent in cardcontent.py)
#

"""
Example:

  >>> from pagelayouter import PageLayouter
  >>> pl = PageLayouter( width=88, height=63, lang='en', index=10 )
  >>> ( svg, rendered, skipped ) = pl.svg()
  >>> svg[0:60]
  "<?xml version='1.0' encoding='UTF-8' standalone='no'?><svg  "
  >>> len(svg)
  2989

"""

from cardcontent import *
import time

svgTemplate = '''<?xml version='1.0' encoding='UTF-8' standalone='no'?><svg    xmlns:dc='http://purl.org/dc/elements/1.1/'
xmlns:cc='http://creativecommons.org/ns#'
xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'
xmlns:svg='http://www.w3.org/2000/svg'
xmlns='http://www.w3.org/2000/svg'
width='210mm' height='297mm' version='1.1' viewBox='0 0 2100 2970'>
  <metadata>
    <rdf:RDF>
      <cc:Work
         rdf:about='Playing cards for the Scrum Card Game'>
        <dc:format>image/svg+xml</dc:format>
        <dc:type
           rdf:resource='http://purl.org/dc/dcmitype/StillImage' />
        <dc:title>Playing cards for the Scrum Card Game</dc:title>
        <cc:license
           rdf:resource='http://creativecommons.org/licenses/by-sa/4.0' />
        <dc:date>%s</dc:date>
        <dc:creator>
          <cc:Agent>
            <dc:title>Oliver Merkel</dc:title>
          </cc:Agent>
        </dc:creator>
        <dc:rights>
          <cc:Agent>
            <dc:title>
              cc-by-sa-4.0.
              All rights reserved.
              All logos, brands, and trademarks mentioned belong to their respective owners.
            </dc:title>
          </cc:Agent>
        </dc:rights>
        <dc:publisher>
          <cc:Agent>
            <dc:title>Oliver Merkel</dc:title>
          </cc:Agent>
        </dc:publisher>
        <dc:source>https://github.com/OMerkel/Scrum-Card-Game</dc:source>
        <dc:relation>https://github.com/OMerkel/Scrum-Card-Game</dc:relation>
        <dc:language>en</dc:language>
        <dc:contributor>
          <cc:Agent>
            <dc:title>
Oliver Merkel
Timofey Yevgrashyn
Nils Bernert
            </dc:title>
          </cc:Agent>
        </dc:contributor>
        <dc:description>Playing cards for the Scrum Card Game as available on https://github.com/OMerkel/Scrum-Card-Game</dc:description>
        <dc:subject>
          <rdf:Bag>
            <rdf:li>SCRUM</rdf:li>
            <rdf:li>agile</rdf:li>
            <rdf:li>development</rdf:li>
            <rdf:li>game</rdf:li>
            <rdf:li>simulation</rdf:li>
            <rdf:li>lean</rdf:li>
            <rdf:li>card game</rdf:li>
            <rdf:li>training</rdf:li>
            <rdf:li>workshop</rdf:li>
          </rdf:Bag>
        </dc:subject>
      </cc:Work>
      <cc:License
         rdf:about='http://creativecommons.org/licenses/by-sa/4.0'>
        <cc:permits
           rdf:resource='http://creativecommons.org/ns#Reproduction' />
        <cc:permits
           rdf:resource='http://creativecommons.org/ns#Distribution' />
        <cc:requires
           rdf:resource='http://creativecommons.org/ns#Notice' />
        <cc:requires
           rdf:resource='http://creativecommons.org/ns#Attribution' />
        <cc:permits
           rdf:resource='http://creativecommons.org/ns#DerivativeWorks' />
        <cc:requires
           rdf:resource='http://creativecommons.org/ns#ShareAlike' />
      </cc:License>
    </rdf:RDF>
  </metadata>
%s</svg>'''
bulb = '''<g><path d="m 148.7,42.3 c 2.3,0 4.2,-1.9 4.2,-4.2 l 0,-18.8 c 0,-2.4 -1.9,-4.3 -4.2,-4.3 -2.4,0 -4.4,1.9 -4.4,4.3 l 0,18.8 c 0,2.3 2,4.2 4.4,4.2 z" style="fill:#fff;stroke:none" />
<path d="m 98,92 -18.8,0 c -2.4,0 -4.3,1.9 -4.3,4.3 0,2.4 1.9,4.3 4.3,4.3 l 18.8,0 c 2.3,0 4.2,-1.9 4.2,-4.3 0,-2.4 -1.9,-4.3 -4.2,-4.3 z" style="fill:#fff;stroke:none" />
<path d="m 103.2,63.8 -16.3,-9.4 c -2.1,-1.2 -4.7,-0.4 -5.9,1.6 -1.2,2.1 -0.4,4.8 1.6,6 L 99,71.2 c 2,1.2 4.5,0.4 5.8,-1.6 1.2,-2.1 0.4,-4.8 -1.6,-5.9 z" style="fill:#fff;stroke:none" />
<path d="m 122.9,50.3 c 2,-1.2 2.8,-3.9 1.7,-5.9 l -9.1,-16.5 c -1.2,-2 -4,-2.7 -6.1,-1.7 -2,1.2 -2.8,3.9 -1.6,6 l 9.3,16.4 c 1,2.1 3.7,2.8 5.8,1.7 z" style="fill:#fff;stroke:none" />
<path d="m 218.4,92.7 -18.7,-0.6 c -2.4,0 -4.5,2 -4.5,4.3 -0.1,2.3 1.8,4.3 4.3,4.4 l 18.7,0.4 c 2.3,0 4.2,-1.8 4.3,-4.1 0,-2.3 -1.8,-4.5 -4.1,-4.5 z" style="fill:#fff;stroke:none" />
<path d="m 198.9,71.6 16.6,-9 c 2,-1.1 2.9,-3.7 1.7,-5.9 -1.1,-2.1 -3.7,-2.8 -5.8,-1.8 l -16.6,9.1 c -2,1.1 -2.9,3.8 -1.7,5.8 1.1,2.1 3.7,2.9 5.8,1.8 z" style="fill:#fff;stroke:none" />
<path d="m 190.2,26.4 c -2.1,-1.1 -4.8,-0.6 -6,1.4 l -9.6,16.3 c -1.1,2 -0.6,4.7 1.6,5.9 2.1,1.2 4.7,0.6 5.9,-1.4 l 9.6,-16.3 c 1.2,-2 0.6,-4.7 -1.4,-5.9 z" style="fill:#fff;stroke:none" />
<path d="m 125.8,175.8 14.7,11.7 0,4.7 6.2,0 4,0 6.2,0 0,-4.7 14.6,-11.7 0,-12.4 -21.7,11.1 -9,0 0,-0.7 30.7,-17.1 0,-9.2 -45.8,21.9 0,6.3 z" style="fill:#fff;stroke:none" />
<path d="m 139.7,69.7 c -7.5,2.4 -11.3,10.6 -11.3,10.7 -0.6,1.2 -1.9,2 -3.2,2 -0.4,0 -0.9,-0.1 -1.2,-0.2 -1.8,-0.9 -2.7,-2.8 -1.8,-4.5 0.1,-0.4 4.9,-11.1 15.5,-14.5 1.8,-0.6 3.7,0.4 4.2,2.2 0.7,1.8 -0.4,3.8 -2.2,4.3 z m 46.9,17.7 c 0,-20.3 -16,-38.5 -38,-38.5 -21.8,0 -37.7,18.2 -37.7,38.5 -0.3,24.7 20.2,41.7 20.2,41.7 l 0,7 -5.2,0 0,12 4.4,-2.2 9.1,1 -13.5,7 0,10.3 45.8,-21.3 0,-6.8 -5.3,0 0,-7 c 0,0 20.6,-17 20.3,-41.7 z" style="fill:#fff;stroke:none" /></g>'''
warningsign = '''<path d="m 160.9,85.5 -2,40.9 c -0.3,3.5 -1.6,4.9 -3,6.2 -0.7,0.8 -2.2,1.9 -4.1,1.9 -1.8,0 -3.4,-1.1 -4.1,-1.9 -1.6,-1.4 -2.9,-2.8 -3.1,-6.2 l -2,-40.9 c -0.3,-3.1 0.7,-5.2 1.9,-6.5 1.5,-1.6 3.9,-2.5 7.3,-2.5 3.4,0 5.7,1 7.2,2.5 1.2,1.3 2.2,3.4 1.9,6.5 z m -9.1,71.6 c -4.8,0 -8.5,-3.8 -8.5,-8.5 0,-4.7 3.7,-8.5 8.5,-8.5 4.7,0 8.4,3.8 8.4,8.5 0,4.7 -3.7,8.5 -8.4,8.5 z m -61.1,5.2 122,0 L 151.7,56.6 90.6,162.3 Z" style="fill:#fff;stroke:none" />
<path d="m 239.53862,177.6273 c -1.8005,3.0719 -5.18932,5.0824 -8.89559,5.0824 l -157.579946,0 c -3.600606,0 -6.989429,-2.0105 -8.895629,-5.0824 -1.800322,-3.1767 -1.800322,-7.0956 0,-10.2723 L 142.95736,30.8486 c 1.80019,-3.0709 5.29491,-5.0832 9.00147,-5.0832 3.60065,0 7.0954,2.0123 8.78993,5.0832 l 78.78986,136.5064 c 1.80016,3.1767 1.80016,7.0956 0,10.2723 z m 5.29487,-13.4494 -78.68391,-136.4002 c -2.85928,-5.0836 -8.26038,-8.2603 -14.19075,-8.2603 -6.03628,0 -11.54301,3.1767 -14.50818,8.2603 L 58.766525,164.1779 c -3.071106,5.0824 -3.071106,11.4359 0,16.5213 2.859304,5.0821 8.472053,8.2588 14.296559,8.2588 l 157.579946,0 c 5.93038,0 11.33117,-3.1767 14.19046,-8.2588 3.07108,-5.0854 3.07108,-11.4389 0,-16.5213 z" style="fill:#fff;stroke:none" />'''
prioritisation = '''<path d="m 200,182 -96.1,-0 -48,-83.6 48.1,-83.2 96.1,0 48,83.3 z" style="fill:#fff;stroke:none;" /><text xml:space="preserve" x="153" y="130"><tspan x="153" y="130" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:92px;line-height:100%%;font-family:Arial;-inkscape-font-specification:'Arial, Bold';text-align:center;writing-mode:lr;text-anchor:middle;">#%s</tspan></text>'''
estimate = '''<path d="m %s,652 -96.1,-0 -48,-83.6 48.1,-83.2 96.1,0 48,83.3 z" style="fill:#ccc;stroke:none;" /><text x="%s" y="610"><tspan x="%s" y="610" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:120px;line-height:100%%;font-family:Arial;-inkscape-font-specification:'Arial, Bold';text-align:center;writing-mode:lr;text-anchor:middle;fill:#fff">%s</tspan></text>'''
typelabel = '''<text x="%s" y="200"><tspan x="%s" y="200" style="font-style:normal;font-variant:normal;font-weight:bold;font-stretch:normal;font-size:128px;line-height:100%%;font-family:Arial;-inkscape-font-specification:'Arial, Bold';text-align:end;writing-mode:lr;text-anchor:end;fill:#fff">%s</tspan></text>'''
storyBody = '''<switch><foreignObject x="50" y="220" width="%s" height="300"><p xmlns="http://www.w3.org/1999/xhtml" style="font-style:normal;font-weight:normal;font-size:56px;line-height:125%%;font-family:Sans,Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000;stroke:none;">%s</p></foreignObject><text x="50" y="220">Your SVG viewer cannot display html.</text></switch>'''
cardBody = '''<switch><foreignObject x="50" y="170" width="%s" height="470"><p xmlns="http://www.w3.org/1999/xhtml" style="font-style:normal;font-weight:normal;font-size:56px;line-height:120%%;font-family:Sans,Arial;text-align:start;letter-spacing:0px;word-spacing:0px;text-anchor:start;fill:#000;stroke:none;">%s</p></foreignObject><text x="50" y="220">Your SVG viewer cannot display html.</text></switch>'''

class PageLayouter:
  def __init__(self, width, height, lang, index):
    self.width = width
    self.height = height
    self.lang = lang
    self.index = index;
    self.startIndex = index;
    self.pos = { 'x': [
      100 - width if width == 85 else 105 - width,
      110 if width == 85 else 105
    ], 'y': [] }
    offsetY = (297 % height) / 2
    self.maxCardsY = 297 // height
    for n in range(self.maxCardsY):
      self.pos['y'].append( offsetY + n*height )
    self.maxCards = 2 * self.maxCardsY;

  def info(self):
    print('width: ' + str(self.width) + ' height: ' + str(self.height))
    for x in self.pos['x']:
      print( 'x : ' + str(x) )
    for y in self.pos['y']:
      print( 'y : ' + str(y) )

  def getNextCardInfo(self):
    if self.index < len(cardcontent):
      card = cardcontent[self.index]
      cardType = card['type'].lower()
      headerColor = {
        'story' : '#ccc',
        'event' : '#789',
        'problem' : '#f60',
        'solution' : '#1bd',
      }
      headerStyle = "style='fill:%s;stroke:none;stroke-width:0;'" % headerColor[cardType]
      scaleCommon = self.height / 69
      scaleWidth = self.width / 104 / scaleCommon
      content = typelabel % ( 1020 * scaleWidth, 1020 * scaleWidth, card['type'].upper() )
      if 'event' == cardType:
        smileyBase = "<circle cx='150' cy='100' r='80' style='fill:none;stroke:#fff;stroke-width:14;'/><circle cx='122' cy='70' r='12' style='fill:#fff;stroke:none;stroke-width:0;'/><circle cx='178' cy='70' r='12' style='fill:#fff;stroke:none;stroke-width:0;'/>"
        content = content + smileyBase + {
          ':-)' :  "<path d='m 110,102 c 0,52 80,52 80,0'", 
          ':-(' :  "<path d='m 110,142 c 0,-52 80,-52 80,0'",
          ':-|' :  "<path d='m 110,122 l 80,0'",
        }[card['smiley']]  + " style='fill:none;stroke:#fff;stroke-width:8;'/>" + \
          (cardBody % ( 950 * scaleWidth, '<p><b>' + card[self.lang + '_title'].upper() + \
          '</b></p>' + card[self.lang]))
      elif 'solution' == cardType:
        content = content + bulb + \
          (cardBody % ( 950 * scaleWidth, '<p><b>' + card[self.lang + '_title'].upper() + \
          '</b></p>' + card[self.lang]))
      elif 'problem' == cardType:
        content = content + warningsign + \
          (cardBody % ( 950 * scaleWidth, '<p><b>' + card[self.lang + '_title'].upper() + \
          '</b></p>' + card[self.lang]))
      elif 'story' == cardType:
        content = content + prioritisation % card['story_id'] + \
          (estimate % ( 950 * scaleWidth, 903 * scaleWidth, 903 * scaleWidth, card['story_estimate'])) + \
          (storyBody % ( 950 * scaleWidth, card[self.lang]))
      else:
        content = '<text x="160" y="200">Unknown card type (index: %s).</text>' % self.index
      cardContent = ( "<g transform='scale(%s)'>" % scaleCommon )+ content +"</g>"
      result = {
        'header' : "<rect x='0' y='0' width='%s' height='%s' %s />%s" % ( self.width*10, self.height*3, headerStyle, cardContent ),
      }
      self.index = self.index + 1
    else:
      result = None
    return result

  def svg(self):
    now = time.strftime("%c")
    style = "style='fill:#fff;stroke:#ccc;stroke-width:1;'"
    svgRect = ''
    for y in self.pos['y']:
      for x in self.pos['x']:
        card = self.getNextCardInfo() if self.index < self.startIndex + self.maxCardsY * 2 else None
        if not card is None:
          svgRect = svgRect + ( "<g transform='translate(%s,%s)'><rect x='0' y='0' width='%s' height='%s' %s />%s</g>" % ( x*10, y*10, self.width*10, self.height*10, style, card['header'] ) )
    svg = svgTemplate % ( now, svgRect)
    return ( svg, self.maxCards, 0 )
