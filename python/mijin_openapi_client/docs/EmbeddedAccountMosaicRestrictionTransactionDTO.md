# EmbeddedAccountMosaicRestrictionTransactionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_public_key** | **str** | Public key. | 
**version** | **int** | Entity version. | 
**network** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | 
**type** | **int** |  | 
**restriction_flags** | [**AccountRestrictionFlagsEnum**](AccountRestrictionFlagsEnum.md) |  | 
**restriction_additions** | **List[str]** | Account restriction additions. | 
**restriction_deletions** | **List[str]** | Account restriction deletions. | 

## Example

```python
from mijin_openapi_client.models.embedded_account_mosaic_restriction_transaction_dto import EmbeddedAccountMosaicRestrictionTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedAccountMosaicRestrictionTransactionDTO from a JSON string
embedded_account_mosaic_restriction_transaction_dto_instance = EmbeddedAccountMosaicRestrictionTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(EmbeddedAccountMosaicRestrictionTransactionDTO.to_json())

# convert the object into a dict
embedded_account_mosaic_restriction_transaction_dto_dict = embedded_account_mosaic_restriction_transaction_dto_instance.to_dict()
# create an instance of EmbeddedAccountMosaicRestrictionTransactionDTO from a dict
embedded_account_mosaic_restriction_transaction_dto_from_dict = EmbeddedAccountMosaicRestrictionTransactionDTO.from_dict(embedded_account_mosaic_restriction_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


