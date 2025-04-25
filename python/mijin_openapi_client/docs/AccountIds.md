# AccountIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_keys** | **List[str]** | Array of public keys. | [optional] 
**addresses** | **List[str]** | Array of addresses. | [optional] 

## Example

```python
from mijin_openapi_client.models.account_ids import AccountIds

# TODO update the JSON string below
json = "{}"
# create an instance of AccountIds from a JSON string
account_ids_instance = AccountIds.from_json(json)
# print the JSON string representation of the object
print(AccountIds.to_json())

# convert the object into a dict
account_ids_dict = account_ids_instance.to_dict()
# create an instance of AccountIds from a dict
account_ids_from_dict = AccountIds.from_dict(account_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


