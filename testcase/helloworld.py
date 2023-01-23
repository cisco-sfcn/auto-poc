# Example
# -------
#
#   hello world

import logging
from pyats import aetest

logger = logging.getLogger(__name__)

class HelloWorld(aetest.Testcase):

    @aetest.test
    def helloworld(self):
        logger.info('Hello World!')

    @aetest.test
    def failure(self):
        logger.info('failure World!')
        assert 1 == 0

class ByeWorld(aetest.Testcase):

    @aetest.test
    def byeworld(self):
        logger.info('Bye World!')

    @aetest.test
    def failure(self):
        logger.info('failure World!')
        assert 1 == 0

# main()
if __name__ == '__main__':
    # set logger level
    logger.setLevel(logging.INFO)

    aetest.main()