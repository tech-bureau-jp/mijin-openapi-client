# NodeHealthDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_node** | [**NodeStatusEnum**](NodeStatusEnum.md) |  | 
**db** | [**NodeStatusEnum**](NodeStatusEnum.md) |  | 

## Example

```python
from mijin_openapi_client.models.node_health_dto import NodeHealthDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NodeHealthDTO from a JSON string
node_health_dto_instance = NodeHealthDTO.from_json(json)
# print the JSON string representation of the object
print(NodeHealthDTO.to_json())

# convert the object into a dict
node_health_dto_dict = node_health_dto_instance.to_dict()
# create an instance of NodeHealthDTO from a dict
node_health_dto_from_dict = NodeHealthDTO.from_dict(node_health_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


