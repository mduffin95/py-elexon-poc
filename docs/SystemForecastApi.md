# swagger_client.SystemForecastApi

All URIs are relative to *https://data.elexon.co.uk/bmrs/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecast_system_loss_of_load_get**](SystemForecastApi.md#forecast_system_loss_of_load_get) | **GET** /forecast/system/loss-of-load | Loss of load probability and de-rated margin forecast (LOLPDRM)

# **forecast_system_loss_of_load_get**
> InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse forecast_system_loss_of_load_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)

Loss of load probability and de-rated margin forecast (LOLPDRM)

This endpoint provides the 1h, 2h, 4h, 8h and 12h+ Loss of Load Probability and De-rated Margin forecasts  for each settlement period over a requested time range.                For each forecast horizon at 1, 2, 4 or 8 hours, the returned value is the forecast received that number of hours  before the start of the settlement period.                For the forecast horizon of 12h, the returned value is the most recent forecast received 12 or more hours  before the start of the settlement period. That is, if the most recent forecast was published today at 00:00,  - for 11:30 today, the 12h forecast is the one published yesterday at 23:30 (12h before)  - for 12:00 today, the 12h forecast is the one published today at 00:00 (12h before)  - for 12:30 today, the 12h forecast is the one published today at 00:00 (the latest published)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemForecastApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | 
to = '2013-10-20T19:20:30+01:00' # datetime | 
settlement_period_from = 56 # int | The \"from\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
settlement_period_to = 56 # int | The \"to\" settlement period for the filter. This should be an integer from 1-50 inclusive. (optional)
format = 'format_example' # str | Response data format. Use json/xml to include metadata. (optional)

try:
    # Loss of load probability and de-rated margin forecast (LOLPDRM)
    api_response = api_instance.forecast_system_loss_of_load_get(_from, to, settlement_period_from=settlement_period_from, settlement_period_to=settlement_period_to, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemForecastApi->forecast_system_loss_of_load_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**|  | 
 **to** | **datetime**|  | 
 **settlement_period_from** | **int**| The \&quot;from\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **settlement_period_to** | **int**| The \&quot;to\&quot; settlement period for the filter. This should be an integer from 1-50 inclusive. | [optional] 
 **format** | **str**| Response data format. Use json/xml to include metadata. | [optional] 

### Return type

[**InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse**](InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscLossOfLoadProbabilityDeratedMarginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json, application/xml, text/xml, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

