# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow(object):
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
        'dataset': 'str',
        'document_id': 'str',
        'document_revision_number': 'int',
        'publish_time': 'datetime',
        'forecast_year': 'int',
        'forecast_week': 'int',
        'minimum_possible': 'float',
        'maximum_available': 'float'
    }

    attribute_map = {
        'dataset': 'dataset',
        'document_id': 'documentId',
        'document_revision_number': 'documentRevisionNumber',
        'publish_time': 'publishTime',
        'forecast_year': 'forecastYear',
        'forecast_week': 'forecastWeek',
        'minimum_possible': 'minimumPossible',
        'maximum_available': 'maximumAvailable'
    }

    def __init__(self, dataset=None, document_id=None, document_revision_number=None, publish_time=None, forecast_year=None, forecast_week=None, minimum_possible=None, maximum_available=None):  # noqa: E501
        """InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow - a model defined in Swagger"""  # noqa: E501
        self._dataset = None
        self._document_id = None
        self._document_revision_number = None
        self._publish_time = None
        self._forecast_year = None
        self._forecast_week = None
        self._minimum_possible = None
        self._maximum_available = None
        self.discriminator = None
        if dataset is not None:
            self.dataset = dataset
        if document_id is not None:
            self.document_id = document_id
        if document_revision_number is not None:
            self.document_revision_number = document_revision_number
        if publish_time is not None:
            self.publish_time = publish_time
        if forecast_year is not None:
            self.forecast_year = forecast_year
        if forecast_week is not None:
            self.forecast_week = forecast_week
        if minimum_possible is not None:
            self.minimum_possible = minimum_possible
        if maximum_available is not None:
            self.maximum_available = maximum_available

    @property
    def dataset(self):
        """Gets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param dataset: The dataset of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def document_id(self):
        """Gets the document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param document_id: The document_id of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def document_revision_number(self):
        """Gets the document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: int
        """
        return self._document_revision_number

    @document_revision_number.setter
    def document_revision_number(self, document_revision_number):
        """Sets the document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param document_revision_number: The document_revision_number of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: int
        """

        self._document_revision_number = document_revision_number

    @property
    def publish_time(self):
        """Gets the publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param publish_time: The publish_time of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: datetime
        """

        self._publish_time = publish_time

    @property
    def forecast_year(self):
        """Gets the forecast_year of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The forecast_year of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: int
        """
        return self._forecast_year

    @forecast_year.setter
    def forecast_year(self, forecast_year):
        """Sets the forecast_year of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param forecast_year: The forecast_year of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: int
        """

        self._forecast_year = forecast_year

    @property
    def forecast_week(self):
        """Gets the forecast_week of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The forecast_week of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: int
        """
        return self._forecast_week

    @forecast_week.setter
    def forecast_week(self, forecast_week):
        """Sets the forecast_week of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param forecast_week: The forecast_week of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: int
        """

        self._forecast_week = forecast_week

    @property
    def minimum_possible(self):
        """Gets the minimum_possible of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The minimum_possible of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: float
        """
        return self._minimum_possible

    @minimum_possible.setter
    def minimum_possible(self, minimum_possible):
        """Sets the minimum_possible of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param minimum_possible: The minimum_possible of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: float
        """

        self._minimum_possible = minimum_possible

    @property
    def maximum_available(self):
        """Gets the maximum_available of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501


        :return: The maximum_available of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :rtype: float
        """
        return self._maximum_available

    @maximum_available.setter
    def maximum_available(self, maximum_available):
        """Sets the maximum_available of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.


        :param maximum_available: The maximum_available of this InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow.  # noqa: E501
        :type: float
        """

        self._maximum_available = maximum_available

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
        if issubclass(InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InsightsApiModelsResponsesTransparencyDatasetRowsYearAheadTotalLoadPerBiddingZoneDatasetRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
