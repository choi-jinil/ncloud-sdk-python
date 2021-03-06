# coding: utf-8

"""
    cdn

    OpenAPI spec version: 2018-07-04T02:02:10Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GlobalCdnRule(object):
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
        'protocol_type_code': 'str',
        'service_domain_type_code': 'str',
        'origin_url': 'str',
        'origin_path': 'str',
        'origin_http_port': 'int',
        'origin_https_port': 'int',
        'forward_host_header_type_code': 'str',
        'forward_host_header': 'str',
        'cache_key_host_name_type_code': 'str',
        'is_gzip_compression_use': 'bool',
        'caching_option_type_code': 'str',
        'is_error_contents_response_use': 'bool',
        'caching_ttl_time': 'str',
        'is_query_string_ignore_use': 'bool',
        'is_remove_vary_header_use': 'bool',
        'is_large_file_optimization_use': 'bool',
        'gzip_response_type_code': 'str',
        'is_referrer_domain_use': 'bool',
        'referrer_domain_list': 'list[str]',
        'is_referrer_domain_restrict_use': 'bool',
        'is_secure_token_use': 'bool',
        'secure_token_password': 'str',
        'is_reissue_secure_token_password': 'bool',
        'certificate_name': 'str',
        'is_access_log_use': 'bool',
        'access_log_file_storage_container_name': 'str'
    }

    attribute_map = {
        'protocol_type_code': 'protocolTypeCode',
        'service_domain_type_code': 'serviceDomainTypeCode',
        'origin_url': 'originUrl',
        'origin_path': 'originPath',
        'origin_http_port': 'originHttpPort',
        'origin_https_port': 'originHttpsPort',
        'forward_host_header_type_code': 'forwardHostHeaderTypeCode',
        'forward_host_header': 'forwardHostHeader',
        'cache_key_host_name_type_code': 'cacheKeyHostNameTypeCode',
        'is_gzip_compression_use': 'isGzipCompressionUse',
        'caching_option_type_code': 'cachingOptionTypeCode',
        'is_error_contents_response_use': 'isErrorContentsResponseUse',
        'caching_ttl_time': 'cachingTtlTime',
        'is_query_string_ignore_use': 'isQueryStringIgnoreUse',
        'is_remove_vary_header_use': 'isRemoveVaryHeaderUse',
        'is_large_file_optimization_use': 'isLargeFileOptimizationUse',
        'gzip_response_type_code': 'gzipResponseTypeCode',
        'is_referrer_domain_use': 'isReferrerDomainUse',
        'referrer_domain_list': 'referrerDomainList',
        'is_referrer_domain_restrict_use': 'isReferrerDomainRestrictUse',
        'is_secure_token_use': 'isSecureTokenUse',
        'secure_token_password': 'secureTokenPassword',
        'is_reissue_secure_token_password': 'isReissueSecureTokenPassword',
        'certificate_name': 'certificateName',
        'is_access_log_use': 'isAccessLogUse',
        'access_log_file_storage_container_name': 'accessLogFileStorageContainerName'
    }

    def __init__(self, protocol_type_code=None, service_domain_type_code=None, origin_url=None, origin_path=None, origin_http_port=None, origin_https_port=None, forward_host_header_type_code=None, forward_host_header=None, cache_key_host_name_type_code=None, is_gzip_compression_use=None, caching_option_type_code=None, is_error_contents_response_use=None, caching_ttl_time=None, is_query_string_ignore_use=None, is_remove_vary_header_use=None, is_large_file_optimization_use=None, gzip_response_type_code=None, is_referrer_domain_use=None, referrer_domain_list=None, is_referrer_domain_restrict_use=None, is_secure_token_use=None, secure_token_password=None, is_reissue_secure_token_password=None, certificate_name=None, is_access_log_use=None, access_log_file_storage_container_name=None):  # noqa: E501
        """GlobalCdnRule - a model defined in Swagger"""  # noqa: E501

        self._protocol_type_code = None
        self._service_domain_type_code = None
        self._origin_url = None
        self._origin_path = None
        self._origin_http_port = None
        self._origin_https_port = None
        self._forward_host_header_type_code = None
        self._forward_host_header = None
        self._cache_key_host_name_type_code = None
        self._is_gzip_compression_use = None
        self._caching_option_type_code = None
        self._is_error_contents_response_use = None
        self._caching_ttl_time = None
        self._is_query_string_ignore_use = None
        self._is_remove_vary_header_use = None
        self._is_large_file_optimization_use = None
        self._gzip_response_type_code = None
        self._is_referrer_domain_use = None
        self._referrer_domain_list = None
        self._is_referrer_domain_restrict_use = None
        self._is_secure_token_use = None
        self._secure_token_password = None
        self._is_reissue_secure_token_password = None
        self._certificate_name = None
        self._is_access_log_use = None
        self._access_log_file_storage_container_name = None
        self.discriminator = None

        if protocol_type_code is not None:
            self.protocol_type_code = protocol_type_code
        if service_domain_type_code is not None:
            self.service_domain_type_code = service_domain_type_code
        if origin_url is not None:
            self.origin_url = origin_url
        if origin_path is not None:
            self.origin_path = origin_path
        if origin_http_port is not None:
            self.origin_http_port = origin_http_port
        if origin_https_port is not None:
            self.origin_https_port = origin_https_port
        if forward_host_header_type_code is not None:
            self.forward_host_header_type_code = forward_host_header_type_code
        if forward_host_header is not None:
            self.forward_host_header = forward_host_header
        if cache_key_host_name_type_code is not None:
            self.cache_key_host_name_type_code = cache_key_host_name_type_code
        if is_gzip_compression_use is not None:
            self.is_gzip_compression_use = is_gzip_compression_use
        if caching_option_type_code is not None:
            self.caching_option_type_code = caching_option_type_code
        if is_error_contents_response_use is not None:
            self.is_error_contents_response_use = is_error_contents_response_use
        if caching_ttl_time is not None:
            self.caching_ttl_time = caching_ttl_time
        if is_query_string_ignore_use is not None:
            self.is_query_string_ignore_use = is_query_string_ignore_use
        if is_remove_vary_header_use is not None:
            self.is_remove_vary_header_use = is_remove_vary_header_use
        if is_large_file_optimization_use is not None:
            self.is_large_file_optimization_use = is_large_file_optimization_use
        if gzip_response_type_code is not None:
            self.gzip_response_type_code = gzip_response_type_code
        if is_referrer_domain_use is not None:
            self.is_referrer_domain_use = is_referrer_domain_use
        if referrer_domain_list is not None:
            self.referrer_domain_list = referrer_domain_list
        if is_referrer_domain_restrict_use is not None:
            self.is_referrer_domain_restrict_use = is_referrer_domain_restrict_use
        if is_secure_token_use is not None:
            self.is_secure_token_use = is_secure_token_use
        if secure_token_password is not None:
            self.secure_token_password = secure_token_password
        if is_reissue_secure_token_password is not None:
            self.is_reissue_secure_token_password = is_reissue_secure_token_password
        if certificate_name is not None:
            self.certificate_name = certificate_name
        if is_access_log_use is not None:
            self.is_access_log_use = is_access_log_use
        if access_log_file_storage_container_name is not None:
            self.access_log_file_storage_container_name = access_log_file_storage_container_name

    @property
    def protocol_type_code(self):
        """Gets the protocol_type_code of this GlobalCdnRule.  # noqa: E501

        프로토콜구분코드  # noqa: E501

        :return: The protocol_type_code of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._protocol_type_code

    @protocol_type_code.setter
    def protocol_type_code(self, protocol_type_code):
        """Sets the protocol_type_code of this GlobalCdnRule.

        프로토콜구분코드  # noqa: E501

        :param protocol_type_code: The protocol_type_code of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._protocol_type_code = protocol_type_code

    @property
    def service_domain_type_code(self):
        """Gets the service_domain_type_code of this GlobalCdnRule.  # noqa: E501

        서비스도메인구분코드  # noqa: E501

        :return: The service_domain_type_code of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._service_domain_type_code

    @service_domain_type_code.setter
    def service_domain_type_code(self, service_domain_type_code):
        """Sets the service_domain_type_code of this GlobalCdnRule.

        서비스도메인구분코드  # noqa: E501

        :param service_domain_type_code: The service_domain_type_code of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._service_domain_type_code = service_domain_type_code

    @property
    def origin_url(self):
        """Gets the origin_url of this GlobalCdnRule.  # noqa: E501

        원본URL  # noqa: E501

        :return: The origin_url of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._origin_url

    @origin_url.setter
    def origin_url(self, origin_url):
        """Sets the origin_url of this GlobalCdnRule.

        원본URL  # noqa: E501

        :param origin_url: The origin_url of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._origin_url = origin_url

    @property
    def origin_path(self):
        """Gets the origin_path of this GlobalCdnRule.  # noqa: E501

        원본경로  # noqa: E501

        :return: The origin_path of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._origin_path

    @origin_path.setter
    def origin_path(self, origin_path):
        """Sets the origin_path of this GlobalCdnRule.

        원본경로  # noqa: E501

        :param origin_path: The origin_path of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._origin_path = origin_path

    @property
    def origin_http_port(self):
        """Gets the origin_http_port of this GlobalCdnRule.  # noqa: E501

        원본HTTP포트  # noqa: E501

        :return: The origin_http_port of this GlobalCdnRule.  # noqa: E501
        :rtype: int
        """
        return self._origin_http_port

    @origin_http_port.setter
    def origin_http_port(self, origin_http_port):
        """Sets the origin_http_port of this GlobalCdnRule.

        원본HTTP포트  # noqa: E501

        :param origin_http_port: The origin_http_port of this GlobalCdnRule.  # noqa: E501
        :type: int
        """

        self._origin_http_port = origin_http_port

    @property
    def origin_https_port(self):
        """Gets the origin_https_port of this GlobalCdnRule.  # noqa: E501

        원본HTTPS포트  # noqa: E501

        :return: The origin_https_port of this GlobalCdnRule.  # noqa: E501
        :rtype: int
        """
        return self._origin_https_port

    @origin_https_port.setter
    def origin_https_port(self, origin_https_port):
        """Sets the origin_https_port of this GlobalCdnRule.

        원본HTTPS포트  # noqa: E501

        :param origin_https_port: The origin_https_port of this GlobalCdnRule.  # noqa: E501
        :type: int
        """

        self._origin_https_port = origin_https_port

    @property
    def forward_host_header_type_code(self):
        """Gets the forward_host_header_type_code of this GlobalCdnRule.  # noqa: E501

        포워드호스트헤더구분코드  # noqa: E501

        :return: The forward_host_header_type_code of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._forward_host_header_type_code

    @forward_host_header_type_code.setter
    def forward_host_header_type_code(self, forward_host_header_type_code):
        """Sets the forward_host_header_type_code of this GlobalCdnRule.

        포워드호스트헤더구분코드  # noqa: E501

        :param forward_host_header_type_code: The forward_host_header_type_code of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._forward_host_header_type_code = forward_host_header_type_code

    @property
    def forward_host_header(self):
        """Gets the forward_host_header of this GlobalCdnRule.  # noqa: E501

        포워드호스트헤더  # noqa: E501

        :return: The forward_host_header of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._forward_host_header

    @forward_host_header.setter
    def forward_host_header(self, forward_host_header):
        """Sets the forward_host_header of this GlobalCdnRule.

        포워드호스트헤더  # noqa: E501

        :param forward_host_header: The forward_host_header of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._forward_host_header = forward_host_header

    @property
    def cache_key_host_name_type_code(self):
        """Gets the cache_key_host_name_type_code of this GlobalCdnRule.  # noqa: E501

        캐쉬키호스트명구분코드  # noqa: E501

        :return: The cache_key_host_name_type_code of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._cache_key_host_name_type_code

    @cache_key_host_name_type_code.setter
    def cache_key_host_name_type_code(self, cache_key_host_name_type_code):
        """Sets the cache_key_host_name_type_code of this GlobalCdnRule.

        캐쉬키호스트명구분코드  # noqa: E501

        :param cache_key_host_name_type_code: The cache_key_host_name_type_code of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._cache_key_host_name_type_code = cache_key_host_name_type_code

    @property
    def is_gzip_compression_use(self):
        """Gets the is_gzip_compression_use of this GlobalCdnRule.  # noqa: E501

        GZIP압축사용여부  # noqa: E501

        :return: The is_gzip_compression_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_gzip_compression_use

    @is_gzip_compression_use.setter
    def is_gzip_compression_use(self, is_gzip_compression_use):
        """Sets the is_gzip_compression_use of this GlobalCdnRule.

        GZIP압축사용여부  # noqa: E501

        :param is_gzip_compression_use: The is_gzip_compression_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_gzip_compression_use = is_gzip_compression_use

    @property
    def caching_option_type_code(self):
        """Gets the caching_option_type_code of this GlobalCdnRule.  # noqa: E501

        캐싱옵션구분코드  # noqa: E501

        :return: The caching_option_type_code of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._caching_option_type_code

    @caching_option_type_code.setter
    def caching_option_type_code(self, caching_option_type_code):
        """Sets the caching_option_type_code of this GlobalCdnRule.

        캐싱옵션구분코드  # noqa: E501

        :param caching_option_type_code: The caching_option_type_code of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._caching_option_type_code = caching_option_type_code

    @property
    def is_error_contents_response_use(self):
        """Gets the is_error_contents_response_use of this GlobalCdnRule.  # noqa: E501

        오류내용응답사용여부  # noqa: E501

        :return: The is_error_contents_response_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_error_contents_response_use

    @is_error_contents_response_use.setter
    def is_error_contents_response_use(self, is_error_contents_response_use):
        """Sets the is_error_contents_response_use of this GlobalCdnRule.

        오류내용응답사용여부  # noqa: E501

        :param is_error_contents_response_use: The is_error_contents_response_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_error_contents_response_use = is_error_contents_response_use

    @property
    def caching_ttl_time(self):
        """Gets the caching_ttl_time of this GlobalCdnRule.  # noqa: E501

        TTL캐싱  # noqa: E501

        :return: The caching_ttl_time of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._caching_ttl_time

    @caching_ttl_time.setter
    def caching_ttl_time(self, caching_ttl_time):
        """Sets the caching_ttl_time of this GlobalCdnRule.

        TTL캐싱  # noqa: E501

        :param caching_ttl_time: The caching_ttl_time of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._caching_ttl_time = caching_ttl_time

    @property
    def is_query_string_ignore_use(self):
        """Gets the is_query_string_ignore_use of this GlobalCdnRule.  # noqa: E501

        쿼리스트링무시여부  # noqa: E501

        :return: The is_query_string_ignore_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_query_string_ignore_use

    @is_query_string_ignore_use.setter
    def is_query_string_ignore_use(self, is_query_string_ignore_use):
        """Sets the is_query_string_ignore_use of this GlobalCdnRule.

        쿼리스트링무시여부  # noqa: E501

        :param is_query_string_ignore_use: The is_query_string_ignore_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_query_string_ignore_use = is_query_string_ignore_use

    @property
    def is_remove_vary_header_use(self):
        """Gets the is_remove_vary_header_use of this GlobalCdnRule.  # noqa: E501

        헤더제거사용여부  # noqa: E501

        :return: The is_remove_vary_header_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_remove_vary_header_use

    @is_remove_vary_header_use.setter
    def is_remove_vary_header_use(self, is_remove_vary_header_use):
        """Sets the is_remove_vary_header_use of this GlobalCdnRule.

        헤더제거사용여부  # noqa: E501

        :param is_remove_vary_header_use: The is_remove_vary_header_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_remove_vary_header_use = is_remove_vary_header_use

    @property
    def is_large_file_optimization_use(self):
        """Gets the is_large_file_optimization_use of this GlobalCdnRule.  # noqa: E501

        대용량파일최적화사용여부  # noqa: E501

        :return: The is_large_file_optimization_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_large_file_optimization_use

    @is_large_file_optimization_use.setter
    def is_large_file_optimization_use(self, is_large_file_optimization_use):
        """Sets the is_large_file_optimization_use of this GlobalCdnRule.

        대용량파일최적화사용여부  # noqa: E501

        :param is_large_file_optimization_use: The is_large_file_optimization_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_large_file_optimization_use = is_large_file_optimization_use

    @property
    def gzip_response_type_code(self):
        """Gets the gzip_response_type_code of this GlobalCdnRule.  # noqa: E501

        GZIP응답구분코드  # noqa: E501

        :return: The gzip_response_type_code of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._gzip_response_type_code

    @gzip_response_type_code.setter
    def gzip_response_type_code(self, gzip_response_type_code):
        """Sets the gzip_response_type_code of this GlobalCdnRule.

        GZIP응답구분코드  # noqa: E501

        :param gzip_response_type_code: The gzip_response_type_code of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._gzip_response_type_code = gzip_response_type_code

    @property
    def is_referrer_domain_use(self):
        """Gets the is_referrer_domain_use of this GlobalCdnRule.  # noqa: E501

        레퍼러도메인사용여부  # noqa: E501

        :return: The is_referrer_domain_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_referrer_domain_use

    @is_referrer_domain_use.setter
    def is_referrer_domain_use(self, is_referrer_domain_use):
        """Sets the is_referrer_domain_use of this GlobalCdnRule.

        레퍼러도메인사용여부  # noqa: E501

        :param is_referrer_domain_use: The is_referrer_domain_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_referrer_domain_use = is_referrer_domain_use

    @property
    def referrer_domain_list(self):
        """Gets the referrer_domain_list of this GlobalCdnRule.  # noqa: E501

        레퍼러도메인리스트  # noqa: E501

        :return: The referrer_domain_list of this GlobalCdnRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._referrer_domain_list

    @referrer_domain_list.setter
    def referrer_domain_list(self, referrer_domain_list):
        """Sets the referrer_domain_list of this GlobalCdnRule.

        레퍼러도메인리스트  # noqa: E501

        :param referrer_domain_list: The referrer_domain_list of this GlobalCdnRule.  # noqa: E501
        :type: list[str]
        """

        self._referrer_domain_list = referrer_domain_list

    @property
    def is_referrer_domain_restrict_use(self):
        """Gets the is_referrer_domain_restrict_use of this GlobalCdnRule.  # noqa: E501

        레퍼러도메인제한사용여부  # noqa: E501

        :return: The is_referrer_domain_restrict_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_referrer_domain_restrict_use

    @is_referrer_domain_restrict_use.setter
    def is_referrer_domain_restrict_use(self, is_referrer_domain_restrict_use):
        """Sets the is_referrer_domain_restrict_use of this GlobalCdnRule.

        레퍼러도메인제한사용여부  # noqa: E501

        :param is_referrer_domain_restrict_use: The is_referrer_domain_restrict_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_referrer_domain_restrict_use = is_referrer_domain_restrict_use

    @property
    def is_secure_token_use(self):
        """Gets the is_secure_token_use of this GlobalCdnRule.  # noqa: E501

        보안토큰사용여부  # noqa: E501

        :return: The is_secure_token_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_secure_token_use

    @is_secure_token_use.setter
    def is_secure_token_use(self, is_secure_token_use):
        """Sets the is_secure_token_use of this GlobalCdnRule.

        보안토큰사용여부  # noqa: E501

        :param is_secure_token_use: The is_secure_token_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_secure_token_use = is_secure_token_use

    @property
    def secure_token_password(self):
        """Gets the secure_token_password of this GlobalCdnRule.  # noqa: E501

        보안토큰비밀번호  # noqa: E501

        :return: The secure_token_password of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._secure_token_password

    @secure_token_password.setter
    def secure_token_password(self, secure_token_password):
        """Sets the secure_token_password of this GlobalCdnRule.

        보안토큰비밀번호  # noqa: E501

        :param secure_token_password: The secure_token_password of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._secure_token_password = secure_token_password

    @property
    def is_reissue_secure_token_password(self):
        """Gets the is_reissue_secure_token_password of this GlobalCdnRule.  # noqa: E501

        보안토큰재발급여부  # noqa: E501

        :return: The is_reissue_secure_token_password of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_reissue_secure_token_password

    @is_reissue_secure_token_password.setter
    def is_reissue_secure_token_password(self, is_reissue_secure_token_password):
        """Sets the is_reissue_secure_token_password of this GlobalCdnRule.

        보안토큰재발급여부  # noqa: E501

        :param is_reissue_secure_token_password: The is_reissue_secure_token_password of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_reissue_secure_token_password = is_reissue_secure_token_password

    @property
    def certificate_name(self):
        """Gets the certificate_name of this GlobalCdnRule.  # noqa: E501

        인증서이름  # noqa: E501

        :return: The certificate_name of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._certificate_name

    @certificate_name.setter
    def certificate_name(self, certificate_name):
        """Sets the certificate_name of this GlobalCdnRule.

        인증서이름  # noqa: E501

        :param certificate_name: The certificate_name of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._certificate_name = certificate_name

    @property
    def is_access_log_use(self):
        """Gets the is_access_log_use of this GlobalCdnRule.  # noqa: E501

        엑세스로그사용여부  # noqa: E501

        :return: The is_access_log_use of this GlobalCdnRule.  # noqa: E501
        :rtype: bool
        """
        return self._is_access_log_use

    @is_access_log_use.setter
    def is_access_log_use(self, is_access_log_use):
        """Sets the is_access_log_use of this GlobalCdnRule.

        엑세스로그사용여부  # noqa: E501

        :param is_access_log_use: The is_access_log_use of this GlobalCdnRule.  # noqa: E501
        :type: bool
        """

        self._is_access_log_use = is_access_log_use

    @property
    def access_log_file_storage_container_name(self):
        """Gets the access_log_file_storage_container_name of this GlobalCdnRule.  # noqa: E501

        엑세스로그파일스토리지인스턴스이름  # noqa: E501

        :return: The access_log_file_storage_container_name of this GlobalCdnRule.  # noqa: E501
        :rtype: str
        """
        return self._access_log_file_storage_container_name

    @access_log_file_storage_container_name.setter
    def access_log_file_storage_container_name(self, access_log_file_storage_container_name):
        """Sets the access_log_file_storage_container_name of this GlobalCdnRule.

        엑세스로그파일스토리지인스턴스이름  # noqa: E501

        :param access_log_file_storage_container_name: The access_log_file_storage_container_name of this GlobalCdnRule.  # noqa: E501
        :type: str
        """

        self._access_log_file_storage_container_name = access_log_file_storage_container_name

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
        if not isinstance(other, GlobalCdnRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
