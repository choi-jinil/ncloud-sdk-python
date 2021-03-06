# coding: utf-8

"""
    autoscaling

    OpenAPI spec version: 2018-06-21T02:22:22Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ncloud_autoscaling.model.common_code import CommonCode  # noqa: F401,E501


class ActivityLog(object):
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
        'activity_no': 'str',
        'auto_scaling_group_name': 'str',
        'status': 'CommonCode',
        'status_message': 'str',
        'action_cause': 'str',
        'description': 'str',
        'details': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'activity_no': 'activityNo',
        'auto_scaling_group_name': 'autoScalingGroupName',
        'status': 'status',
        'status_message': 'statusMessage',
        'action_cause': 'actionCause',
        'description': 'description',
        'details': 'details',
        'start_time': 'startTime',
        'end_time': 'endTime'
    }

    def __init__(self, activity_no=None, auto_scaling_group_name=None, status=None, status_message=None, action_cause=None, description=None, details=None, start_time=None, end_time=None):  # noqa: E501
        """ActivityLog - a model defined in Swagger"""  # noqa: E501

        self._activity_no = None
        self._auto_scaling_group_name = None
        self._status = None
        self._status_message = None
        self._action_cause = None
        self._description = None
        self._details = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if activity_no is not None:
            self.activity_no = activity_no
        if auto_scaling_group_name is not None:
            self.auto_scaling_group_name = auto_scaling_group_name
        if status is not None:
            self.status = status
        if status_message is not None:
            self.status_message = status_message
        if action_cause is not None:
            self.action_cause = action_cause
        if description is not None:
            self.description = description
        if details is not None:
            self.details = details
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def activity_no(self):
        """Gets the activity_no of this ActivityLog.  # noqa: E501

        액티비티번호  # noqa: E501

        :return: The activity_no of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._activity_no

    @activity_no.setter
    def activity_no(self, activity_no):
        """Sets the activity_no of this ActivityLog.

        액티비티번호  # noqa: E501

        :param activity_no: The activity_no of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._activity_no = activity_no

    @property
    def auto_scaling_group_name(self):
        """Gets the auto_scaling_group_name of this ActivityLog.  # noqa: E501

        오토스케일링그룹명  # noqa: E501

        :return: The auto_scaling_group_name of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._auto_scaling_group_name

    @auto_scaling_group_name.setter
    def auto_scaling_group_name(self, auto_scaling_group_name):
        """Sets the auto_scaling_group_name of this ActivityLog.

        오토스케일링그룹명  # noqa: E501

        :param auto_scaling_group_name: The auto_scaling_group_name of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._auto_scaling_group_name = auto_scaling_group_name

    @property
    def status(self):
        """Gets the status of this ActivityLog.  # noqa: E501

        상태  # noqa: E501

        :return: The status of this ActivityLog.  # noqa: E501
        :rtype: CommonCode
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ActivityLog.

        상태  # noqa: E501

        :param status: The status of this ActivityLog.  # noqa: E501
        :type: CommonCode
        """

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this ActivityLog.  # noqa: E501

        상태메세지  # noqa: E501

        :return: The status_message of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this ActivityLog.

        상태메세지  # noqa: E501

        :param status_message: The status_message of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._status_message = status_message

    @property
    def action_cause(self):
        """Gets the action_cause of this ActivityLog.  # noqa: E501

        액션원인  # noqa: E501

        :return: The action_cause of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._action_cause

    @action_cause.setter
    def action_cause(self, action_cause):
        """Sets the action_cause of this ActivityLog.

        액션원인  # noqa: E501

        :param action_cause: The action_cause of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._action_cause = action_cause

    @property
    def description(self):
        """Gets the description of this ActivityLog.  # noqa: E501

        설명  # noqa: E501

        :return: The description of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ActivityLog.

        설명  # noqa: E501

        :param description: The description of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def details(self):
        """Gets the details of this ActivityLog.  # noqa: E501

        상세설명  # noqa: E501

        :return: The details of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ActivityLog.

        상세설명  # noqa: E501

        :param details: The details of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def start_time(self):
        """Gets the start_time of this ActivityLog.  # noqa: E501

        시작일시  # noqa: E501

        :return: The start_time of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this ActivityLog.

        시작일시  # noqa: E501

        :param start_time: The start_time of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this ActivityLog.  # noqa: E501

        종료일시  # noqa: E501

        :return: The end_time of this ActivityLog.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ActivityLog.

        종료일시  # noqa: E501

        :param end_time: The end_time of this ActivityLog.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

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
        if not isinstance(other, ActivityLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
