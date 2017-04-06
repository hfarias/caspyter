#
# This file was generated using xslt from its XML file
#
# Copyright 2013, Associated Universities Inc., Washington DC
#
import sys
import os
#from casac import *
import casac
import string
import time
import inspect
import gc
import numpy
from odict import odict
from taskmanager import tm
from task_ftw import ftw
class ftw_cli_:
    __name__ = "ftw"
    __async__ = {}
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (ftw_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'field':None, 'spw':None, 'model':None, 'nterms':None, 'reffreq':None, 'wprojplanes':None, 'complist':None, 'incremental':None, 'usescratch':None,  'async':None}


    def result(self, key=None):
	    #### here we will scan the task-ids in __async__
	    #### and add any that have completed...
	    if key is not None and self.__async__.has_key(key) and self.__async__[key] is not None:
	       ret = tm.retrieve(self.__async__[key])
	       if ret['state'] == "done" :
	          self.__async__[key] = None
	       elif ret['state'] == 'crashed' :
		  self.__async__[key] = None
	       return ret
	    return None


    def __call__(self, vis=None, field=None, spw=None, model=None, nterms=None, reffreq=None, wprojplanes=None, complist=None, incremental=None, usescratch=None,  async=None):

        """Insert a source model  a visibility set:

	Detailed Description: 

	
       TASK created by R.J. van Weeren (Dec. 2013, adapted from ft-task)
	
       A source model (souce.model image) or components list is converted into 
       model visibilities that is inserted into the MODEL_DATA column or alternatively 
       is stored  in the header of the MS to be served on the fly when requested.  This is
       needed to use more complicated sources than setjy provides; e.g resolved source 
       or off centered sources in gaincal. Wprojection is included to deal with large FOV.
       If you do not need Wprojection than simply use the task ft. 


	
	Arguments :
		vis:	Name of input visibility file (MS)
		   Default Value: 

		field:	Field selection
		   Default Value: 

		spw:	Spw selection
		   Default Value: 

		model:	Name of input model image(s)
		   Default Value: 

		nterms:	Number of terms used to model the sky frequency dependence
		   Default Value: 1

		reffreq:	Reference frequency (e.g. \'1.5e+9\' or \'1.5GHz\')
		   Default Value: 

		wprojplanes:	Number of w-projection planes for predict 
		   Default Value: 1

		complist:	Name of component list
		   Default Value: 

		incremental:	Add to the existing model visibility?
		   Default Value: False

		usescratch:	If True predicted  visibility  is stored in MODEL_DATA column
		   Default Value: False

	Returns: void

	Example :


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
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals
	#casac = self.__globals__['casac']
	casalog = self.__globals__['casalog']
	#casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'ftw'
        self.__globals__['taskname'] = 'ftw'
        ###
        self.__globals__['update_params'](func=self.__globals__['taskname'],printtext=False,ipython_globals=self.__globals__)
        ###
        ###
        #Handle globals or user over-ride of arguments
        #
	function_signature_defaults=dict(zip(self.__call__.func_code.co_varnames,self.__call__.func_defaults))
	useLocalDefaults = False

        for item in function_signature_defaults.iteritems():
                key,val = item
                keyVal = eval(key)
                if (keyVal == None):
                        #user hasn't set it - use global/default
                        pass
                else:
                        #user has set it - use over-ride
			if (key != 'self') :
			   useLocalDefaults = True

	myparams = {}
	if useLocalDefaults :
	   for item in function_signature_defaults.iteritems():
	       key,val = item
	       keyVal = eval(key)
	       exec('myparams[key] = keyVal')
	       self.parameters[key] = keyVal
	       if (keyVal == None):
	           exec('myparams[key] = '+ key + ' = self.itsdefault(key)')
		   keyVal = eval(key)
		   if(type(keyVal) == dict) :
                      if len(keyVal) > 0 :
		         exec('myparams[key] = ' + key + ' = keyVal[len(keyVal)-1][\'value\']')
		      else :
		         exec('myparams[key] = ' + key + ' = {}')

	else :
            async = self.parameters['async']
            myparams['vis'] = vis = self.parameters['vis']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['model'] = model = self.parameters['model']
            myparams['nterms'] = nterms = self.parameters['nterms']
            myparams['reffreq'] = reffreq = self.parameters['reffreq']
            myparams['wprojplanes'] = wprojplanes = self.parameters['wprojplanes']
            myparams['complist'] = complist = self.parameters['complist']
            myparams['incremental'] = incremental = self.parameters['incremental']
            myparams['usescratch'] = usescratch = self.parameters['usescratch']


	result = None

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
	pathname="file:///home/stsf309/.casa/mytasks/"
        trec = casac.casac.utils().torecord(pathname+'ftw.xml')

        casalog.origin('ftw')
	try :
          #if not trec.has_key('ftw') or not casac.casac.utils().verify(mytmp, trec['ftw']) :
	    #return False

          casac.casac.utils().verify(mytmp, trec['ftw'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']
          saveinputs('ftw', 'ftw.last', myparams, self.__globals__,scriptstr=scriptstr)
          if async :
	    count = 0
	    keybase =  time.strftime("%y%m%d.%H%M%S")
	    key = keybase + "_" + str(count)
	    while self.__async__.has_key(key) :
	       count += 1
	       key = keybase + "_" + str(count)
            result = tm.execute('ftw', vis, field, spw, model, nterms, reffreq, wprojplanes, complist, incremental, usescratch)
	    print "Use: "
	    print "      tm.retrieve(return_value) # to retrieve the status"
	    print 
	    self.rkey = key
	    self.__async__[key] = result
          else :
              tname = 'ftw'
              spaces = ' '*(18-len(tname))
              casalog.post('\n##########################################'+
                           '\n##### Begin Task: ' + tname + spaces + ' #####')
              casalog.post(scriptstr[1][1:]+'\n', 'INFO')
              result = ftw(vis, field, spw, model, nterms, reffreq, wprojplanes, complist, incremental, usescratch)
              casalog.post('##### End Task: ' + tname + '  ' + spaces + ' #####'+
                           '\n##########################################')

	except Exception, instance:
          if(self.__globals__.has_key('__rethrow_casa_exceptions') and self.__globals__['__rethrow_casa_exceptions']) :
             raise
          else :
             #print '**** Error **** ',instance
	     tname = 'ftw'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass

        gc.collect()
        return result
#
#
#
    def paramgui(self, useGlobals=True, ipython_globals=None):
        """
        Opens a parameter GUI for this task.  If useGlobals is true, then any relevant global parameter settings are used.
        """
        import paramgui
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals

        if useGlobals:
	    if ipython_globals == None:
                myf=self.__globals__
            else:
                myf=ipython_globals

            paramgui.setGlobals(myf)
        else:
            paramgui.setGlobals({})

        paramgui.runTask('ftw', myf['_ip'])
        paramgui.setGlobals({})

#
#
#
    def defaults(self, param=None, ipython_globals=None, paramvalue=None, subparam=None):
	if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=sys._getframe(len(inspect.stack())-1).f_globals
        if ipython_globals == None:
            myf=self.__globals__
        else:
            myf=ipython_globals

        a = odict()
        a['vis']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['model']  = ''
        a['nterms']  = 1
        a['wprojplanes']  = 1
        a['complist']  = ''
        a['incremental']  = False
        a['usescratch']  = False

        a['async']=False
        a['nterms'] = {
                    0:odict([{'notvalue':1}, {'reffreq':''}])}

### This function sets the default values but also will return the list of
### parameters or the default value of a given parameter
        if(param == None):
                myf['__set_default_parameters'](a)
        elif(param == 'paramkeys'):
                return a.keys()
        else:
            if(paramvalue==None and subparam==None):
               if(a.has_key(param)):
                  return a[param]
               else:
                  return self.itsdefault(param)
            else:
               retval=a[param]
               if(type(a[param])==dict):
                  for k in range(len(a[param])):
                     valornotval='value'
                     if(a[param][k].has_key('notvalue')):
                        valornotval='notvalue'
                     if((a[param][k][valornotval])==paramvalue):
                        retval=a[param][k].copy()
                        retval.pop(valornotval)
                        if(subparam != None):
                           if(retval.has_key(subparam)):
                              retval=retval[subparam]
                           else:
                              retval=self.itsdefault(subparam)
		     else:
                        retval=self.itsdefault(subparam)
               return retval


#
#
    def check_params(self, param=None, value=None, ipython_globals=None):
      if ipython_globals == None:
          myf=self.__globals__
      else:
          myf=ipython_globals
#      print 'param:', param, 'value:', value
      try :
         if str(type(value)) != "<type 'instance'>" :
            value0 = value
            value = myf['cu'].expandparam(param, value)
            matchtype = False
            if(type(value) == numpy.ndarray):
               if(type(value) == type(value0)):
                  myf[param] = value.tolist()
               else:
                  #print 'value:', value, 'value0:', value0
                  #print 'type(value):', type(value), 'type(value0):', type(value0)
                  myf[param] = value0
                  if type(value0) != list :
                     matchtype = True
            else :
               myf[param] = value
            value = myf['cu'].verifyparam({param:value})
            if matchtype:
               value = False
      except Exception, instance:
         #ignore the exception and just return it unchecked
         myf[param] = value
      return value
#
#
    def description(self, key='ftw', subkey=None):
        desc={'ftw': 'Insert a source model  a visibility set:',
               'vis': 'Name of input visibility file (MS)',
               'field': 'Field selection',
               'spw': 'Spw selection',
               'model': 'Name of input model image(s)',
               'nterms': 'Number of terms used to model the sky frequency dependence',
               'reffreq': 'Reference frequency (e.g. \'1.5e+9\' or \'1.5GHz\')',
               'wprojplanes': 'Number of w-projection planes for predict ',
               'complist': 'Name of component list',
               'incremental': 'Add to the existing model visibility?',
               'usescratch': 'If True predicted  visibility  is stored in MODEL_DATA column',

               'async': 'If true the taskname must be started using ftw(...)'
              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['model']  = ''
        a['nterms']  = 1
        a['reffreq']  = ''
        a['wprojplanes']  = 1
        a['complist']  = ''
        a['incremental']  = False
        a['usescratch']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['nterms']  != 1:
            a['reffreq'] = ''

        if a.has_key(paramname) :
	      return a[paramname]
ftw_cli = ftw_cli_()
