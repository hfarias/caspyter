import os
import time

casa = { 'build': {
             'time': '',
             'version': 'casanova',
             'number': ''
         },
         'source': {
             'url': '',
             'revision': ''
         },
         'helpers': {
             'logger': 'casalogger',
             'viewer': 'casaviewer',
             'info': None,
             'dbus': None,
             'ipcontroller': None,
             'ipengine': None
         },
         'dirs': {
             'rc': '',
             'data': None,
             'recipes': '',
             'root': None,
             'pipeline': None
         },
         'flags': { },
         'files': { 
             'logfile': os.getcwd( ) + '/casapy-'+time.strftime("%Y%m%d-%H%M%S", time.gmtime())+'.log'
         },
         'state' : {
             'startup': True,
             'unwritable': set( )
         }
       }


## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
## set up casa root
## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
if os.environ.has_key('CASAPATH') :
    __casapath__ = os.environ['CASAPATH'].split(' ')[0]
    if not os.path.exists(__casapath__ + "/data") :
        print "DEBUG: CASAPATH = %s" % (__casapath__)
        raise RuntimeError, "Unable to find the data repository directory in your CASAPATH. Please fix."
    else :
        casa['dirs']['root'] = __casapath__
        casa['dirs']['data'] = __casapath__ + "/data"
else :
    __casapath__ = casac.__file__
    while __casapath__ and __casapath__ != "/" :
        if os.path.exists( __casapath__ + "/data") :
            break
        __casapath__ = os.path.dirname(__casapath__)
    if not os.path.exists(__casapath__ + "/data") :
        raise RuntimeError, "casa path could not be determined"
    else :
        casa['dirs']['root'] = __casapath__
        casa['dirs']['data'] = __casapath__ + "/data"

## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
## setup pipeline path (if it exists)
## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
if os.path.exists(casa['dirs']['root']+"/pipeline"):
    casa['dirs']['pipeline'] = casa['dirs']['root']+"/pipeline"


## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
## setup helper paths...
## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
##
## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
## try to set casapyinfo path...
## ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
if os.path.exists( __casapath__ + "/bin/casapyinfo") :
    casa['helpers']['info'] = __casapath__ + "/bin/casapyinfo"


import __builtin__
__builtin__.globalcasa = casa
