# coding: utf-8

"""
    cdn

    OpenAPI spec version: 2018-06-21T02:27:10Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_cdn.model.common_code import CommonCode  # noqa: F401,E501
from ncloud_cdn.model.global_cdn_rule import GlobalCdnRule  # noqa: F401,E501
from ncloud_cdn.model.global_cdn_service_domain import GlobalCdnServiceDomain  # noqa: F401,E501


class GlobalCdnInstance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cdn_instance_no': 'str',
        'cdn_instance_status': 'CommonCode',
        'cdn_instance_operation': 'CommonCode',
        'cdn_instance_status_name': 'str',
        'create_date': 'str',
        'last_modified_date': 'str',
        'cdn_instance_description': 'str',
        'service_name': 'str',
        'is_available_partial_domain_purge': 'bool',
        'global_cdn_service_domain_list': 'list[GlobalCdnServiceDomain]',
        'global_cdn_rule': 'GlobalCdnRule'
    }

    attribute_map = {
        'cdn_instance_no': 'cdnInstanceNo',
        'cdn_instance_status': 'cdnInstanceStatus',
        'cdn_instance_operation': 'cdnInstanceOperation',
        'cdn_instance_status_name': 'cdnInstanceStatusName',
        'create_date': 'createDate',
        'last_modified_date': 'lastModifiedDate',
        'cdn_instance_description': 'cdnInstanceDescription',
        'service_name': 'serviceName',
        'is_available_partial_domain_purge': 'isAvailablePartialDomainPurge',
        'global_cdn_service_domain_list': 'globalCdnServiceDomainList',
        'global_cdn_rule': 'globalCdnRule'
    }

    def __init__(self, cdn_instance_no=None, cdn_instance_status=None, cdn_instance_operation=None, cdn_instance_status_name=None, create_date=None, last_modified_date=None, cdn_instance_description=None, service_name=None, is_available_partial_domain_purge=None, global_cdn_service_domain_list=None, global_cdn_rule=None):  # noqa: E501
        """GlobalCdnInstance - a model defined in Swagger"""  # noqa: E501

        self._cdn_instance_no = None
        self._cdn_instance_status = None
        self._cdn_instance_operation = None
        self._cdn_instance_status_name = None
        self._create_date = None
        self._last_modified_date = None
        self._cdn_instance_description = None
        self._service_name = None
        self._is_available_partial_domain_purge = None
        self._global_cdn_service_domain_list = None
        self._global_cdn_rule = None
        self.discriminator = None

        if cdn_instance_no is not None:
            self.cdn_instance_no = cdn_instance_no
        if cdn_instance_status is not None:
            self.cdn_instance_status = cdn_instance_status
        if cdn_instance_operation is not None:
            self.cdn_instance_operation = cdn_instance_operation
        if cdn_instance_status_name is not None:
            self.cdn_instance_status_name = cdn_instance_status_name
        if create_date is not None:
            self.create_date = create_date
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if cdn_instance_description is not None:
            self.cdn_instance_description = cdn_instance_description
        if service_name is not None:
            self.service_name = service_name
        if is_available_partial_domain_purge is not None:
            self.is_available_partial_domain_purge = is_available_partial_domain_purge
        if global_cdn_service_domain_list is not None:
            self.global_cdn_service_domain_list = global_cdn_service_domain_list
        if global_cdn_rule is not None:
            self.global_cdn_rule = global_cdn_rule

    @property
    def cdn_instance_no(self):
        """Gets the cdn_instance_no of this GlobalCdnInstance.  # noqa: E501

        CDN인스턴스번호  # noqa: E501

        :return: The cdn_instance_no of this GlobalCdnInstance.  # noqa: E501
        :rtype: str
        """
        return self._cdn_instance_no

    @cdn_instance_no.setter
    def cdn_instance_no(self, cdn_instance_no):
        """Sets the cdn_instance_no of this GlobalCdnInstance.

        CDN인스턴스번호  # noqa: E501

        :param cdn_instance_no: The cdn_instance_no of this GlobalCdnInstance.  # noqa: E501
        :type: str
        """

        self._cdn_instance_no = cdn_instance_no

    @property
    def cdn_instance_status(self):
        """Gets the cdn_instance_status of this GlobalCdnInstance.  # noqa: E501

        CDN인스턴스상태  # noqa: E501

        :return: The cdn_instance_status of this GlobalCdnInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._cdn_instance_status

    @cdn_instance_status.setter
    def cdn_instance_status(self, cdn_instance_status):
        """Sets the cdn_instance_status of this GlobalCdnInstance.

        CDN인스턴스상태  # noqa: E501

        :param cdn_instance_status: The cdn_instance_status of this GlobalCdnInstance.  # noqa: E501
        :type: CommonCode
        """

        self._cdn_instance_status = cdn_instance_status

    @property
    def cdn_instance_operation(self):
        """Gets the cdn_instance_operation of this GlobalCdnInstance.  # noqa: E501

        CDN인스턴스OP  # noqa: E501

        :return: The cdn_instance_operation of this GlobalCdnInstance.  # noqa: E501
        :rtype: CommonCode
        """
        return self._cdn_instance_operation

    @cdn_instance_operation.setter
    def cdn_instance_operation(self, cdn_instance_operation):
        """Sets the cdn_instance_operation of this GlobalCdnInstance.

        CDN인스턴스OP  # noqa: E501

        :param cdn_instance_operation: The cdn_instance_operation of this GlobalCdnInstance.  # noqa: E501
        :type: CommonCode
        """

        self._cdn_instance_operation = cdn_instance_operation

    @property
    def cdn_instance_status_name(self):
        """Gets the cdn_instance_status_name of this GlobalCdnInstance.  # noqa: E501

        CDN인스턴스상태명  # noqa: E501

        :return: The cdn_instance_status_name of this GlobalCdnInstance.  # noqa: E501
        :rtype: str
        """
        return self._cdn_instance_status_name

    @cdn_instance_status_name.setter
    def cdn_instance_status_name(self, cdn_instance_status_name):
        """Sets the cdn_instance_status_name of this GlobalCdnInstance.

        CDN인스턴스상태명  # noqa: E501

        :param cdn_instance_status_name: The cdn_instance_status_name of this GlobalCdnInstance.  # noqa: E501
        :type: str
        """

        self._cdn_instance_status_name = cdn_instance_status_name

    @property
    def create_date(self):
        """Gets the create_date of this GlobalCdnInstance.  # noqa: E501

        생성일자  # noqa: E501

        :return: The create_date of this GlobalCdnInstance.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this GlobalCdnInstance.

        생성일자  # noqa: E501

        :param create_date: The create_date of this GlobalCdnInstance.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this GlobalCdnInstance.  # noqa: E501

        UPTIME  # noqa: E501

        :return: The last_modified_date of this GlobalCdnInstance.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this GlobalCdnInstance.

        UPTIME  # noqa: E501

        :param last_modified_date: The last_modified_date of this GlobalCdnInstance.  # noqa: E501
        :type: str
        """

        self._last_modified_date = last_modified_date

    @property
    def cdn_instance_description(self):
        """Gets the cdn_instance_description of this GlobalCdnInstance.  # noqa: E501

        CDN인스턴스설명  # noqa: E501

        :return: The cdn_instance_description of this GlobalCdnInstance.  # noqa: E501
        :rtype: str
        """
        return self._cdn_instance_description

    @cdn_instance_description.setter
    def cdn_instance_description(self, cdn_instance_description):
        """Sets the cdn_instance_description of this GlobalCdnInstance.

        CDN인스턴스설명  # noqa: E501

        :param cdn_instance_description: The cdn_instance_description of this GlobalCdnInstance.  # noqa: E501
        :type: str
        """

        self._cdn_instance_description = cdn_instance_description

    @property
    def service_name(self):
        """Gets the service_name of this GlobalCdnInstance.  # noqa: E501

        서비스이름  # noqa: E501

        :return: The service_name of this GlobalCdnInstance.  # noqa: E501
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """Sets the service_name of this GlobalCdnInstance.

        서비스이름  # noqa: E501

        :param service_name: The service_name of this GlobalCdnInstance.  # noqa: E501
        :type: str
        """

        self._service_name = service_name

    @property
    def is_available_partial_domain_purge(self):
        """Gets the is_available_partial_domain_purge of this GlobalCdnInstance.  # noqa: E501


        :return: The is_available_partial_domain_purge of this GlobalCdnInstance.  # noqa: E501
        :rtype: bool
        """
        return self._is_available_partial_domain_purge

    @is_available_partial_domain_purge.setter
    def is_available_partial_domain_purge(self, is_available_partial_domain_purge):
        """Sets the is_available_partial_domain_purge of this GlobalCdnInstance.


        :param is_available_partial_domain_purge: The is_available_partial_domain_purge of this GlobalCdnInstance.  # noqa: E501
        :type: bool
        """

        self._is_available_partial_domain_purge = is_available_partial_domain_purge

    @property
    def global_cdn_service_domain_list(self):
        """Gets the global_cdn_service_domain_list of this GlobalCdnInstance.  # noqa: E501


        :return: The global_cdn_service_domain_list of this GlobalCdnInstance.  # noqa: E501
        :rtype: list[GlobalCdnServiceDomain]
        """
        return self._global_cdn_service_domain_list

    @global_cdn_service_domain_list.setter
    def global_cdn_service_domain_list(self, global_cdn_service_domain_list):
        """Sets the global_cdn_service_domain_list of this GlobalCdnInstance.


        :param global_cdn_service_domain_list: The global_cdn_service_domain_list of this GlobalCdnInstance.  # noqa: E501
        :type: list[GlobalCdnServiceDomain]
        """

        self._global_cdn_service_domain_list = global_cdn_service_domain_list

    @property
    def global_cdn_rule(self):
        """Gets the global_cdn_rule of this GlobalCdnInstance.  # noqa: E501


        :return: The global_cdn_rule of this GlobalCdnInstance.  # noqa: E501
        :rtype: GlobalCdnRule
        """
        return self._global_cdn_rule

    @global_cdn_rule.setter
    def global_cdn_rule(self, global_cdn_rule):
        """Sets the global_cdn_rule of this GlobalCdnInstance.


        :param global_cdn_rule: The global_cdn_rule of this GlobalCdnInstance.  # noqa: E501
        :type: GlobalCdnRule
        """

        self._global_cdn_rule = global_cdn_rule

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GlobalCdnInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
