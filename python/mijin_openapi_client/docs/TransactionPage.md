# TransactionPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TransactionInfoDTO]**](TransactionInfoDTO.md) | Array of transactions. | 
**pagination** | [**Pagination**](Pagination.md) |  | 

## Example

```python
from mijin_openapi_client.models.transaction_page import TransactionPage

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionPage from a JSON string
transaction_page_instance = TransactionPage.from_json(json)
# print the JSON string representation of the object
print(TransactionPage.to_json())

# convert the object into a dict
transaction_page_dict = transaction_page_instance.to_dict()
# create an instance of TransactionPage from a dict
transaction_page_from_dict = TransactionPage.from_dict(transaction_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


