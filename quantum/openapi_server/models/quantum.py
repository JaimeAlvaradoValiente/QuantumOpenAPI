# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.category import Category
from openapi_server import util

from openapi_server.models.category import Category  # noqa: E501

class Quantum(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, category=None, name=None):  # noqa: E501
        """Quantum - a model defined in OpenAPI

        :param id: The id of this Quantum.  # noqa: E501
        :type id: int
        :param category: The category of this Quantum.  # noqa: E501
        :type category: Category
        :param name: The name of this Quantum.  # noqa: E501
        :type name: str
        """
        self.openapi_types = {
            'id': int,
            'category': Category,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'category': 'category',
            'name': 'name'
        }

        self._id = id
        self._category = category
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Quantum':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The quantum of this Quantum.  # noqa: E501
        :rtype: Quantum
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Quantum.


        :return: The id of this Quantum.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Quantum.


        :param id: The id of this Quantum.
        :type id: int
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this Quantum.


        :return: The category of this Quantum.
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Quantum.


        :param category: The category of this Quantum.
        :type category: Category
        """

        self._category = category

    @property
    def name(self):
        """Gets the name of this Quantum.


        :return: The name of this Quantum.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Quantum.


        :param name: The name of this Quantum.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name
