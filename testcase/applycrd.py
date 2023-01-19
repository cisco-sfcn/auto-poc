# Example
# -------
#
#   hello world

import logging
from pyats import aetest
from kubeconfig import kubectl
from kubeconfig.exceptions import KubectlCommandError

logger = logging.getLogger(__name__)

class HelloWorld(aetest.Testcase):

    @aetest.test
    def test(self):
        logger.info('Hello World!')
        try:
            kubectl.run(self.kubeconfig_path, cmd)
            self.pod_wait_for_running_and_ready_state()
            log.info('Applied resources from the config file: %s', config_path)
        except KubectlCommandError as ex:
            log.error(ex.message)
            raise ex

# main()
if __name__ == '__main__':
    # set logger level
    logger.setLevel(logging.INFO)

    aetest.main()