import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging.config import dictConfig
import logging
import inspect


@pytest.mark.usefixtures('setup')
class BaseClass:
    logging_config = dict(
        version=1,
        formatters={
            'f': {'format':
                      '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
        handlers={
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.INFO},
            'fh': {'class': 'logging.FileHandler',
                  'formatter': 'f',
                   'filename': 'logs.log',
                  'level': logging.INFO
            }
        },
        root={
            'handlers': ['h','fh'],
            'level': logging.INFO,
        },
    )

    def get_logger(self, logger_name=None):
        dictConfig(self.logging_config)
        logger_name = logger_name if logger_name else inspect.stack()[1][3]
        return logging.getLogger(logger_name)

    def wait_until_element_is_visible(self, webelement):
        WebDriverWait(self.driver, timeout=10).until(EC.visibility_of(webelement))


