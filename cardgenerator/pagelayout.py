#
# @file pagelayout.py
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
# @brief Page Layout.
# 
# The array pagelayout holds the supported card sizes in millimeter
# for dimensions width and height of a card. Mind the cards are
# rendered onto page size DIN-A4 (210mm x 297mm) in portrait mode
# using double columns.
# Any issue when trying to add more card sizes?
# Need help? Contact me... You are welcome.
#

pagelayout = [
  { 'width': 104, 'height': 69 },
  { 'width': 88, 'height': 63 },
  { 'width': 85, 'height': 54 }
]
