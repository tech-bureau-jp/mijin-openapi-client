# NetworkConfigurationDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**NetworkPropertiesDTO**](NetworkPropertiesDTO.md) |  | 
**chain** | [**ChainPropertiesDTO**](ChainPropertiesDTO.md) |  | 
**plugins** | [**PluginsPropertiesDTO**](PluginsPropertiesDTO.md) |  | 

## Example

```python
from mijin_openapi_client.models.network_configuration_dto import NetworkConfigurationDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConfigurationDTO from a JSON string
network_configuration_dto_instance = NetworkConfigurationDTO.from_json(json)
# print the JSON string representation of the object
print(NetworkConfigurationDTO.to_json())

# convert the object into a dict
network_configuration_dto_dict = network_configuration_dto_instance.to_dict()
# create an instance of NetworkConfigurationDTO from a dict
network_configuration_dto_from_dict = NetworkConfigurationDTO.from_dict(network_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


