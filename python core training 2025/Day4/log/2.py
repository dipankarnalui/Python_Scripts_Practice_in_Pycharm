import logging as log

#change the default log level to DEBUG
log.basicConfig(level = log.DEBUG)  # now default level 10

log.debug("msg-1")     # debug is    10>=10  default is 10
log.info("msg-2")      # info  is    20>=10  
log.warning("msg-3")   # warning is  30>=10
log.error("msg-4")     # error   is  40>=10
log.critical("msg-5")  # critical is 50>=10



