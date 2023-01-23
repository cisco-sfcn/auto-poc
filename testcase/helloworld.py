# Example
# -------
#
#   hello world

import logging
from pyats import aetest

logger = logging.getLogger(__name__)

class Success(aetest.Testcase):

    @aetest.test
    def helloworld(self):
        logger.info('Hello World!')

    @aetest.test
    def successTC(self):
        assert 1 == 1


class Failure(aetest.Testcase):

    @aetest.test
    def helloworld(self):
        logger.info('Hello World!')

    @aetest.test
    def failureTC(self):
        assert 1 == 0

# main()
if __name__ == '__main__':
    # set logger level
    logger.setLevel(logging.INFO)

    aetest.main()