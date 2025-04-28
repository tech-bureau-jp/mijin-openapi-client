# ResolutionStatementInfoDTO

A resolution statement keeps the relation between a namespace alias used in a transaction and the real address or mosaicId. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal resource identifier. | 
**meta** | [**StatementMetaDTO**](StatementMetaDTO.md) |  | 
**statement** | [**ResolutionStatementDTO**](ResolutionStatementDTO.md) |  | 

## Example

```python
from mijin_openapi_client.models.resolution_statement_info_dto import ResolutionStatementInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ResolutionStatementInfoDTO from a JSON string
resolution_statement_info_dto_instance = ResolutionStatementInfoDTO.from_json(json)
# print the JSON string representation of the object
print(ResolutionStatementInfoDTO.to_json())

# convert the object into a dict
resolution_statement_info_dto_dict = resolution_statement_info_dto_instance.to_dict()
# create an instance of ResolutionStatementInfoDTO from a dict
resolution_statement_info_dto_from_dict = ResolutionStatementInfoDTO.from_dict(resolution_statement_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


