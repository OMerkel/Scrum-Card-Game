#
# @file cardtype.py
# @author Oliver Merkel <Merkel(dot)Oliver(at)web(dot)de>
# @date 2016 November 23rd
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
# @brief Card Type Titles in target languages
#
# The array cardTypeTitles holds the Card Type Titles
# in various target languages.
#
# Usually in German 'de' in SCRUM, lean, agile
# environments the domain terminology is used as
# in English 'en' language without any specific
# translation.
#
# If you insist to translate domain terminology
# then uncomment the unwanted and comment the
# intended language block for 'de' below.
#
# Mind the file is supposed to be UTF-8 encoded.
# This way special language characters are supported.
#

cardTypeTitle = {
  'de': {
    'story' : 'story',
    'event' : 'event',
    'problem' : 'problem',
    'solution' : 'solution',
  },
#   'de': {
#     'story' : 'Anforderung',
#     'event' : 'Ereignis',
#     'problem' : 'Problem',
#     'solution' : 'Lösung',
#   },
  'en': {
    'story' : 'story',
    'event' : 'event',
    'problem' : 'problem',
    'solution' : 'solution',
  },
  'es': {
    'story' : 'requisito',
    'event' : 'evento',
    'problem' : 'problema',
    'solution' : 'solución',
  },
}
