# coding: utf-8

"""
    clouddb

    OpenAPI spec version: 2018-07-02T10:10:19Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ncloud_clouddb.api_client import ApiClient


class V2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_cloud_db_instance(self, create_cloud_db_instance_request, **kwargs):  # noqa: E501
        """create_cloud_db_instance  # noqa: E501

        CloudDB인스턴스생성  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_cloud_db_instance(create_cloud_db_instance_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateCloudDBInstanceRequest create_cloud_db_instance_request: createCloudDBInstanceRequest (required)
        :return: CreateCloudDBInstanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_cloud_db_instance_with_http_info(create_cloud_db_instance_request, **kwargs)  # noqa: E501
        else:
            (data) = self.create_cloud_db_instance_with_http_info(create_cloud_db_instance_request, **kwargs)  # noqa: E501
            return data

    def create_cloud_db_instance_with_http_info(self, create_cloud_db_instance_request, **kwargs):  # noqa: E501
        """create_cloud_db_instance  # noqa: E501

        CloudDB인스턴스생성  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_cloud_db_instance_with_http_info(create_cloud_db_instance_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreateCloudDBInstanceRequest create_cloud_db_instance_request: createCloudDBInstanceRequest (required)
        :return: CreateCloudDBInstanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['create_cloud_db_instance_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_cloud_db_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_cloud_db_instance_request' is set
        if ('create_cloud_db_instance_request' not in params or
                params['create_cloud_db_instance_request'] is None):
            raise ValueError("Missing the required parameter `create_cloud_db_instance_request` when calling `create_cloud_db_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('responseFormatType', 'json'))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_cloud_db_instance_request' in params:
            body_params = params['create_cloud_db_instance_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-ncp-iam']  # noqa: E501

        return self.api_client.call_api(
            '/createCloudDBInstance', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateCloudDBInstanceResponse',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_cloud_db_server_instance(self, delete_cloud_db_server_instance_request, **kwargs):  # noqa: E501
        """delete_cloud_db_server_instance  # noqa: E501

        CloudDB서버인스턴스삭제  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_cloud_db_server_instance(delete_cloud_db_server_instance_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param DeleteCloudDBServerInstanceRequest delete_cloud_db_server_instance_request: deleteCloudDBServerInstanceRequest (required)
        :return: DeleteCloudDBServerInstanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_cloud_db_server_instance_with_http_info(delete_cloud_db_server_instance_request, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_cloud_db_server_instance_with_http_info(delete_cloud_db_server_instance_request, **kwargs)  # noqa: E501
            return data

    def delete_cloud_db_server_instance_with_http_info(self, delete_cloud_db_server_instance_request, **kwargs):  # noqa: E501
        """delete_cloud_db_server_instance  # noqa: E501

        CloudDB서버인스턴스삭제  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_cloud_db_server_instance_with_http_info(delete_cloud_db_server_instance_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param DeleteCloudDBServerInstanceRequest delete_cloud_db_server_instance_request: deleteCloudDBServerInstanceRequest (required)
        :return: DeleteCloudDBServerInstanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delete_cloud_db_server_instance_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cloud_db_server_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delete_cloud_db_server_instance_request' is set
        if ('delete_cloud_db_server_instance_request' not in params or
                params['delete_cloud_db_server_instance_request'] is None):
            raise ValueError("Missing the required parameter `delete_cloud_db_server_instance_request` when calling `delete_cloud_db_server_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('responseFormatType', 'json'))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'delete_cloud_db_server_instance_request' in params:
            body_params = params['delete_cloud_db_server_instance_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-ncp-iam']  # noqa: E501

        return self.api_client.call_api(
            '/deleteCloudDBServerInstance', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteCloudDBServerInstanceResponse',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud_db_config_group_list(self, get_cloud_db_config_group_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_config_group_list  # noqa: E501

        CloudDB설정그룹리스트조회  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_config_group_list(get_cloud_db_config_group_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBConfigGroupListRequest get_cloud_db_config_group_list_request: getCloudDBConfigGroupListRequest (required)
        :return: GetCloudDBConfigGroupListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_db_config_group_list_with_http_info(get_cloud_db_config_group_list_request, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_db_config_group_list_with_http_info(get_cloud_db_config_group_list_request, **kwargs)  # noqa: E501
            return data

    def get_cloud_db_config_group_list_with_http_info(self, get_cloud_db_config_group_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_config_group_list  # noqa: E501

        CloudDB설정그룹리스트조회  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_config_group_list_with_http_info(get_cloud_db_config_group_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBConfigGroupListRequest get_cloud_db_config_group_list_request: getCloudDBConfigGroupListRequest (required)
        :return: GetCloudDBConfigGroupListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_cloud_db_config_group_list_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud_db_config_group_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'get_cloud_db_config_group_list_request' is set
        if ('get_cloud_db_config_group_list_request' not in params or
                params['get_cloud_db_config_group_list_request'] is None):
            raise ValueError("Missing the required parameter `get_cloud_db_config_group_list_request` when calling `get_cloud_db_config_group_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('responseFormatType', 'json'))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_cloud_db_config_group_list_request' in params:
            body_params = params['get_cloud_db_config_group_list_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-ncp-iam']  # noqa: E501

        return self.api_client.call_api(
            '/getCloudDBConfigGroupList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCloudDBConfigGroupListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud_db_image_product_list(self, get_cloud_db_image_product_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_image_product_list  # noqa: E501

        CloudDB이미지상품리스트  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_image_product_list(get_cloud_db_image_product_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBImageProductListRequest get_cloud_db_image_product_list_request: getCloudDBImageProductListRequest (required)
        :return: GetCloudDBImageProductListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_db_image_product_list_with_http_info(get_cloud_db_image_product_list_request, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_db_image_product_list_with_http_info(get_cloud_db_image_product_list_request, **kwargs)  # noqa: E501
            return data

    def get_cloud_db_image_product_list_with_http_info(self, get_cloud_db_image_product_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_image_product_list  # noqa: E501

        CloudDB이미지상품리스트  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_image_product_list_with_http_info(get_cloud_db_image_product_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBImageProductListRequest get_cloud_db_image_product_list_request: getCloudDBImageProductListRequest (required)
        :return: GetCloudDBImageProductListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_cloud_db_image_product_list_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud_db_image_product_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'get_cloud_db_image_product_list_request' is set
        if ('get_cloud_db_image_product_list_request' not in params or
                params['get_cloud_db_image_product_list_request'] is None):
            raise ValueError("Missing the required parameter `get_cloud_db_image_product_list_request` when calling `get_cloud_db_image_product_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('responseFormatType', 'json'))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_cloud_db_image_product_list_request' in params:
            body_params = params['get_cloud_db_image_product_list_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-ncp-iam']  # noqa: E501

        return self.api_client.call_api(
            '/getCloudDBImageProductList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCloudDBImageProductListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud_db_instance_list(self, get_cloud_db_instance_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_instance_list  # noqa: E501

        CloudDB인스턴스리스트조회  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_instance_list(get_cloud_db_instance_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBInstanceListRequest get_cloud_db_instance_list_request: getCloudDBInstanceListRequest (required)
        :return: GetCloudDBInstanceListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_db_instance_list_with_http_info(get_cloud_db_instance_list_request, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_db_instance_list_with_http_info(get_cloud_db_instance_list_request, **kwargs)  # noqa: E501
            return data

    def get_cloud_db_instance_list_with_http_info(self, get_cloud_db_instance_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_instance_list  # noqa: E501

        CloudDB인스턴스리스트조회  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_instance_list_with_http_info(get_cloud_db_instance_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBInstanceListRequest get_cloud_db_instance_list_request: getCloudDBInstanceListRequest (required)
        :return: GetCloudDBInstanceListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_cloud_db_instance_list_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud_db_instance_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'get_cloud_db_instance_list_request' is set
        if ('get_cloud_db_instance_list_request' not in params or
                params['get_cloud_db_instance_list_request'] is None):
            raise ValueError("Missing the required parameter `get_cloud_db_instance_list_request` when calling `get_cloud_db_instance_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('responseFormatType', 'json'))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_cloud_db_instance_list_request' in params:
            body_params = params['get_cloud_db_instance_list_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-ncp-iam']  # noqa: E501

        return self.api_client.call_api(
            '/getCloudDBInstanceList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCloudDBInstanceListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_cloud_db_product_list(self, get_cloud_db_product_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_product_list  # noqa: E501

        CloudDB상품리스트조회  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_product_list(get_cloud_db_product_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBProductListRequest get_cloud_db_product_list_request: getCloudDBProductListRequest (required)
        :return: GetCloudDBProductListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_cloud_db_product_list_with_http_info(get_cloud_db_product_list_request, **kwargs)  # noqa: E501
        else:
            (data) = self.get_cloud_db_product_list_with_http_info(get_cloud_db_product_list_request, **kwargs)  # noqa: E501
            return data

    def get_cloud_db_product_list_with_http_info(self, get_cloud_db_product_list_request, **kwargs):  # noqa: E501
        """get_cloud_db_product_list  # noqa: E501

        CloudDB상품리스트조회  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cloud_db_product_list_with_http_info(get_cloud_db_product_list_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param GetCloudDBProductListRequest get_cloud_db_product_list_request: getCloudDBProductListRequest (required)
        :return: GetCloudDBProductListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['get_cloud_db_product_list_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_cloud_db_product_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'get_cloud_db_product_list_request' is set
        if ('get_cloud_db_product_list_request' not in params or
                params['get_cloud_db_product_list_request'] is None):
            raise ValueError("Missing the required parameter `get_cloud_db_product_list_request` when calling `get_cloud_db_product_list`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('responseFormatType', 'json'))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'get_cloud_db_product_list_request' in params:
            body_params = params['get_cloud_db_product_list_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-ncp-iam']  # noqa: E501

        return self.api_client.call_api(
            '/getCloudDBProductList', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetCloudDBProductListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def reboot_cloud_db_server_instance(self, reboot_cloud_db_server_instance_request, **kwargs):  # noqa: E501
        """reboot_cloud_db_server_instance  # noqa: E501

        CloudDB서버인스턴스재부팅  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reboot_cloud_db_server_instance(reboot_cloud_db_server_instance_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param RebootCloudDBServerInstanceRequest reboot_cloud_db_server_instance_request: rebootCloudDBServerInstanceRequest (required)
        :return: RebootCloudDBServerInstanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.reboot_cloud_db_server_instance_with_http_info(reboot_cloud_db_server_instance_request, **kwargs)  # noqa: E501
        else:
            (data) = self.reboot_cloud_db_server_instance_with_http_info(reboot_cloud_db_server_instance_request, **kwargs)  # noqa: E501
            return data

    def reboot_cloud_db_server_instance_with_http_info(self, reboot_cloud_db_server_instance_request, **kwargs):  # noqa: E501
        """reboot_cloud_db_server_instance  # noqa: E501

        CloudDB서버인스턴스재부팅  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.reboot_cloud_db_server_instance_with_http_info(reboot_cloud_db_server_instance_request, async=True)
        >>> result = thread.get()

        :param async bool
        :param RebootCloudDBServerInstanceRequest reboot_cloud_db_server_instance_request: rebootCloudDBServerInstanceRequest (required)
        :return: RebootCloudDBServerInstanceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['reboot_cloud_db_server_instance_request']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reboot_cloud_db_server_instance" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'reboot_cloud_db_server_instance_request' is set
        if ('reboot_cloud_db_server_instance_request' not in params or
                params['reboot_cloud_db_server_instance_request'] is None):
            raise ValueError("Missing the required parameter `reboot_cloud_db_server_instance_request` when calling `reboot_cloud_db_server_instance`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        query_params.append(('responseFormatType', 'json'))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reboot_cloud_db_server_instance_request' in params:
            body_params = params['reboot_cloud_db_server_instance_request']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-ncp-iam']  # noqa: E501

        return self.api_client.call_api(
            '/rebootCloudDBServerInstance', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RebootCloudDBServerInstanceResponse',  # noqa: E501
            auth_settings=auth_settings,
            _async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
