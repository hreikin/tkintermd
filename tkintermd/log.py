import logging

##################################### LOGS #####################################
# Initialize the logger and specify the level of logging. This will log "DEBUG" 
# and higher messages to file and log "WARNING" and higher messages to the console.

def create_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s][tkintermd][%(asctime)s]: %(message)s',
                        datefmt='%H:%M:%S',
                        filename='debug.log',
                        filemode='a')

    # Define a "handler" which writes "WARNING" messages or higher to the "sys.stderr".
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)

    # Set a format which is simpler for console messages.
    formatter = logging.Formatter('[%(levelname)s][tkintermd]: %(message)s', datefmt='%H:%M:%S')

    # Tell the console "handler" to use this format.
    console.setFormatter(formatter)

    # Add the "handler" to the "root logger".
    log = logging.getLogger(__name__)
    log.addHandler(console)

    return log

# Example Usage
#
#     import tkintermd.log as logg
#
#     logger = log.create_logger()
#     logger.debug("DEBUG")
#     logger.info("INFO")
#     logger.exception("EXCEPTION")
#     logger.warning("WARNING")
#     logger.error("ERROR")
#     logger.critical("CRITICAL")

################################################################################