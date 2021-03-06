import os
from abstract import module                                                                        

class resultor(module):
    """
    Resultor of the network saves down resultor. The initilizer initializes the directories 
    for storing results.

    Args:
        verbose:  Similar to any 3-level verbose in the toolbox.
        resultor_init_args: ``resultor_params`` is a dictionary of the form 

            .. code-block:: none

                resultor_init_args    =    { 
                    "root"      : "<root directory to save stuff inside>",
                    "results"   : "<results_file_name>.txt",      
                    "errors"    : "<error_file_name>.txt",
                    "costs"     : "<cost_file_name>.txt",
                    "confusion" : "<confusion_file_name>.txt",
                    "network"   : "<network_save_file_name>.pkl"
                    "id"        : id of the resultor
                                }                                                          

            While the filenames are optional, ``root`` must be provided. If a particular file is 
            not provided, that value will not be saved. 

    Returns: 
        yann.modules.resultor: A resultor object
                                                                                                                                            
    """                    
    def __init__( self, resultor_init_args, verbose = 1):  
        if "id" in resultor_init_args.keys(): 
            id = resultor_init_args["id"]
        else:
            id = '-1'
        super(resultor,self).__init__(id = id, type = 'resultor')
            
        if verbose >= 3:
            print "... Creating resultor directories"
            
        for item, value in resultor_init_args.iteritems():            
            if item == "root":
                self.root                   = value                
            elif item == "results":
                self.results_file           = value                  
            elif item == "errors":
                self.error_file             = value
            elif item == "costs":
                self.cost_file              = value
            elif item == "confusion":
                self.confusion_file         = value
            elif item == "network":
                self.network_file           = value

        if not hasattr(self, 'root'): raise Exception('root variable has not been provided. \
                                            Without a root folder, no save can be performed')
        if not os.path.exists(self.root):
            if verbose >= 3:
                print "... Creating a root directory for save files"
            os.makedirs(self.root)
                    
        if verbose >= 3:
            print "... Resultor is initiliazed"
  
    