import connexion
import six

from openapi_server.models.quantum import Quantum  # noqa: E501
from openapi_server import util





def find_service_by_category(category):  # noqa: E501
    
    """Finds quantum service by category

    Multiple status values can be provided with comma separated strings # noqa: E501

    :param category: Status values that need to be considered for filter
    :type category: List[str]

    :rtype: List[Quantum]
    """


    
    return 'do some magic!'
