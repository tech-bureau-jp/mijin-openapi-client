# AccountsNamesDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_names** | [**List[AccountNamesDTO]**](AccountNamesDTO.md) | Array of account names. | 

## Example

```python
from mijin_openapi_client.models.accounts_names_dto import AccountsNamesDTO

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsNamesDTO from a JSON string
accounts_names_dto_instance = AccountsNamesDTO.from_json(json)
# print the JSON string representation of the object
print(AccountsNamesDTO.to_json())

# convert the object into a dict
accounts_names_dto_dict = accounts_names_dto_instance.to_dict()
# create an instance of AccountsNamesDTO from a dict
accounts_names_dto_from_dict = AccountsNamesDTO.from_dict(accounts_names_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


