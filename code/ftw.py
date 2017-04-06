#
# This file was generated using xslt from its XML file
#
# Copyright 2009, Associated Universities Inc., Washington DC
#
import sys
import os
from  casac import *
import string
from taskinit import casalog
#from taskmanager import tm
import task_ftw
def ftw(vis='', field='', spw='', model='', nterms=1, reffreq='', wprojplanes=1, complist='', incremental=False, usescratch=False):

        """Insert a source model  a visibility set:

       A source model (souce.model image) or components list is converted into a
       model visibility that is inserted into the MODEL_DATA column. 
       Wprojection is included to deal with large FOV.
       If you do not need Wprojection than simply use the task ft.
       
       TASK created by R. J. van Weeren (adapted from ft-task)


               

       Keyword arguments:
       vis -- Name of input visibility file
              default: none; example: vis='ngc5921.ms'
       field -- Field name list
               default: '' ==> all
               NOTE: BUT, only one source can be specified in a multi-source vis.
               field = '1328+307'  specifies source '1328+307'
               field = '4' specified field with index 4
       spw -- Spw selection
               default: spw = '' (all spw)
       model -- Name of input model image
               default: '' ==> None;
               example: model='/usr/lib/casapy/data/nrao/VLA/CalModels/3C286_X.im'
               Note: The model visibilities are scaled from the model frequency
                     to the observed frequency of the data.
       nterms -- Number of terms used to model the sky frequency dependence
                 default: 1  ==> one model image is required
                 example : nterms=3  represents a 2nd order Taylor-polynomial in frequency
                           and should be used in conjuction with coefficient model images as 
		           model=['xxx.model.tt0','xxx.model.tt1', 'xxx.model.tt2']
             reffreq -- Reference-frequency about which this Taylor-expansion is defined.
	                default: '' ==> reads the reference frequency from the model image
                        example : reffreq = '1.5GHz'
       wprojplanes is the number of pre-computed w-planes used for
                   the W-Projection algorithm.  wprojplanes=1 disables
       complist -- Name of component list
               default: None; ; example: complist='test.cl'
               component lists are difficult to make.
       incremental -- Add model visibility to the existing model visibilties stored in the MS
               default: False; example: incremental=True
       usescratch  -- if True model visibilities will be stored in the scratch column 
                            MODEL_DATA; when false the model visibilities will be generated 
                            on the fly (this mode may save some disk space equivalent to 
			    the volume of the observed data). 
                            default: False; example usescratch=True


     



 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['model'] = model
        mytmp['nterms'] = nterms
        mytmp['reffreq'] = reffreq
        mytmp['wprojplanes'] = wprojplanes
        mytmp['complist'] = complist
        mytmp['incremental'] = incremental
        mytmp['usescratch'] = usescratch
	pathname='file:///'+os.environ.get('CASAPATH').split()[0]+'/xml/'
        trec = casac.utils().torecord(pathname+'ftw.xml')

        casalog.origin('ftw')
        if trec.has_key('ftw') and casac.utils().verify(mytmp, trec['ftw']) :
	    result = task_ftw.ftw(vis, field, spw, model, nterms, reffreq, wprojplanes, complist, incremental, usescratch)

	else :
	  result = False
        return result
