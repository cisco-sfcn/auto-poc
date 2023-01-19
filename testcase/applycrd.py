# Example
# -------
#
#   hello world

import logging
from pyats import aetest
from kubeconfig import kubectl
from kubeconfig.exceptions import KubectlCommandError

logger = logging.getLogger(__name__)


class ApplyCRD(aetest.Testcase):

    @aetest.test
    def test(self):
        logger.info('ApplyCRD!')
        try:
            kubectl.run(subcmd_args="kubectl get ns")
            logger.info('Applied resources from the config file: %s', config_path)
        except KubectlCommandError as ex:
            logger.error(ex.message)
            raise ex


# main()
if __name__ == '__main__':
    # set logger level
    logger.setLevel(logging.INFO)

    aetest.main()
