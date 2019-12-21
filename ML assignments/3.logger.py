import logging
logging.basicConfig(filename="Yashwant.log",format='%(asctime)s %(message)s',filemode='a')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("Debugging....")
logger.info("Information of file!")
logger.warning("Alert!!")
logger.error("Error Message!")
logger.critical("Critical Warning!!")
