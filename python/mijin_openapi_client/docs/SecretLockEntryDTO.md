# SecretLockEntryDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The version of the state | 
**owner_address** | **str** | Address encoded using a 32-character set. | 
**mosaic_id** | **str** | Mosaic identifier. | 
**amount** | **str** | Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative). | 
**end_height** | **str** | Height of the blockchain. | 
**status** | [**LockStatus**](LockStatus.md) |  | 
**hash_algorithm** | [**LockHashAlgorithmEnum**](LockHashAlgorithmEnum.md) |  | 
**secret** | **str** | Secret. | 
**recipient_address** | **str** | Address encoded using a 32-character set. | 
**composite_hash** | **str** |  | 

## Example

```python
from mijin_openapi_client.models.secret_lock_entry_dto import SecretLockEntryDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SecretLockEntryDTO from a JSON string
secret_lock_entry_dto_instance = SecretLockEntryDTO.from_json(json)
# print the JSON string representation of the object
print(SecretLockEntryDTO.to_json())

# convert the object into a dict
secret_lock_entry_dto_dict = secret_lock_entry_dto_instance.to_dict()
# create an instance of SecretLockEntryDTO from a dict
secret_lock_entry_dto_from_dict = SecretLockEntryDTO.from_dict(secret_lock_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


