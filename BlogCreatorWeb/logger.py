import logging as lg

def get_log(fname):
    """
    This function is used for setting up log and log configuration
    """

    try:
        logger = lg.getLogger(fname)
        formatter = lg.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
        filehandler = lg.FileHandler(fname+".log")
        filehandler.setFormatter(formatter)
        filehandler.setLevel(lg.INFO)
        logger.setLevel(lg.INFO)
        logger.addHandler(filehandler)
        lg.shutdown()
    except Exception as e:
        print(e)
    else:
        return logger