# HashLockTransactionDTO

Transaction to lock funds before sending an aggregate bonded transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | A number that allows uint 32 values. | 
**signature** | **str** | Entity&#39;s signature generated by the signer. | 
**signer_public_key** | **str** | Public key. | 
**version** | **int** | Entity version. | 
**network** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | 
**type** | **int** |  | 
**max_fee** | **str** | Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative). | 
**deadline** | **str** | Duration expressed in number of blocks. | 
**mosaic_id** | **str** | Mosaic identifier. If the most significant bit of byte 0 is set, a namespaceId (alias) is used instead of the real mosaic identifier.  | 
**amount** | **str** | Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative). | 
**duration** | **str** | Duration expressed in number of blocks. | 
**hash** | **str** |  | 

## Example

```python
from mijin_openapi_client.models.hash_lock_transaction_dto import HashLockTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HashLockTransactionDTO from a JSON string
hash_lock_transaction_dto_instance = HashLockTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(HashLockTransactionDTO.to_json())

# convert the object into a dict
hash_lock_transaction_dto_dict = hash_lock_transaction_dto_instance.to_dict()
# create an instance of HashLockTransactionDTO from a dict
hash_lock_transaction_dto_from_dict = HashLockTransactionDTO.from_dict(hash_lock_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


