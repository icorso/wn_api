import json
import logging
import os

import sys
from datetime import datetime
from logging.handlers import RotatingFileHandler
from pprint import pprint

LOGFILE = str(os.path.dirname(os.path.abspath(__file__))) + "/wnapi.log"


def session_logging(log_level=logging.INFO):
    def decorator(func):
        def wrapper(*args, **kwargs):
            logger = logging.getLogger('')
            logger.setLevel(log_level)
            fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

            ch = logging.StreamHandler(sys.stdout)
            ch.setFormatter(fmt)
            logger.addHandler(ch)

            fh = RotatingFileHandler(LOGFILE, maxBytes=(1048576 * 3), backupCount=2)
            fh.setFormatter(fmt)
            logger.addHandler(fh)

            res = func(*args, **kwargs)
            request = kwargs.get('request')
            is_silence = kwargs.get('silence')

            start_time = datetime.now()
            if not is_silence:
                if request and hasattr(request, 'hashes'):
                    logger.log(log_level, '\nHash string: %s' % request.hashes)
                if request and hasattr(request, 'hash_string'):
                    logger.log(log_level, '\nRequest %s hash string: %s' % (request.__class__.__name__, request.hash_string))
                logger.log(log_level, '\nSession:\n%s' % args[0]._session)

                if res and hasattr(res, 'hash_string'):
                    logger.log(log_level, '\nResponse hash string: %s' % res.hash_string)
                if 'gateway' in str(type(res)) or 'boarding.' in str(type(res)) or 'paylink' in str(type(res)):
                    logger.log(log_level, '\nResponse:\n%s' % res.xml(is_hashable=False))
                elif 'rest' in str(type(res)):
                    if 'xml' in args[0].content_type:
                        logger.log(log_level, '\nResponse (%s):\n%s' % (res.__class__, res.xml(is_hashable=False)))
                    else:
                        logger.log(log_level, '\nResponse (%s):\n%s' % (res.__class__, res.json(is_hashable=False)))
                elif 'HppSerializable' in str(type(res)):
                    logger.log(log_level, '\nRequest:\n%s' % pprint(args[0]._session.params))
                    logger.log(log_level, '\nResponse:\n%s' % res.to_xml())
                else:
                    logger.log(log_level, '\nResponse:\n%s' % str(res))

            logger.log(log_level, 'Execution time: %s %s' % (res.__class__, str(datetime.now() - start_time)))
            logger.removeHandler(fh)
            logger.removeHandler(ch)

            return res

        return wrapper

    return decorator
