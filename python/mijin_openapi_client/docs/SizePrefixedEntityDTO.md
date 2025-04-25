# SizePrefixedEntityDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | A number that allows uint 32 values. | 

## Example

```python
from mijin_openapi_client.models.size_prefixed_entity_dto import SizePrefixedEntityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SizePrefixedEntityDTO from a JSON string
size_prefixed_entity_dto_instance = SizePrefixedEntityDTO.from_json(json)
# print the JSON string representation of the object
print(SizePrefixedEntityDTO.to_json())

# convert the object into a dict
size_prefixed_entity_dto_dict = size_prefixed_entity_dto_instance.to_dict()
# create an instance of SizePrefixedEntityDTO from a dict
size_prefixed_entity_dto_from_dict = SizePrefixedEntityDTO.from_dict(size_prefixed_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


