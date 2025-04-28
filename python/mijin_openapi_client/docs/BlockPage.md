# BlockPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BlockInfoDTO]**](BlockInfoDTO.md) | Array of blocks. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from mijin_openapi_client.models.block_page import BlockPage

# TODO update the JSON string below
json = "{}"
# create an instance of BlockPage from a JSON string
block_page_instance = BlockPage.from_json(json)
# print the JSON string representation of the object
print(BlockPage.to_json())

# convert the object into a dict
block_page_dict = block_page_instance.to_dict()
# create an instance of BlockPage from a dict
block_page_from_dict = BlockPage.from_dict(block_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


