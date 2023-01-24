# Example
# -------
#
#   Pinging 8.8.8.8


import logging
from pyats import aetest

logger = logging.getLogger(__name__)

class InternetAvailability(aetest.Testcase):

    @aetest.test
    def ping(self, destination='8.8.8.8'):
        logger.info('ping -c 3 8.8.8.8')
        try:
            result = self.ping(destination)
        except Exception as ex:
            logger.error(ex.message)
            raise ex

class Failure(aetest.Testcase):

    @aetest.test
    def helloworld(self):
        logger.info('Hello World!')

    @aetest.test
    def failureTC(self):
        assert 1 == 0


class PingTestcase(aetest.Testcase):

    @aetest.test.loop(destination=('8.8.8.8', '172.17.10.2'))
    def ping(self, destination):
        try:
            result = self.ping(destination)

        except Exception as e:
            self.failed('Ping {} is failed with error: {}'.format(
                destination,
                str(e),
            ),
                goto=['exit'])
        else:
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')

            logger.info('Ping {} with success rate of {}%'.format(
                destination,
                success_rate,
            )
            )


# main()
if __name__ == '__main__':
    # set logger level
    logger.setLevel(logging.INFO)

    aetest.main()