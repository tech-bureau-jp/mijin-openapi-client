# EmbeddedNamespaceMetadataTransactionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_public_key** | **str** | Public key. | 
**version** | **int** | Entity version. | 
**network** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | 
**type** | **int** |  | 
**target_address** | **str** | Address expressed in Base32 format. If the bit 0 of byte 0 is not set (like in 0x90), then it is a regular address. Example: TAOXUJOTTW3W5XTBQMQEX3SQNA6MCUVGXLXR3TA.  Otherwise (e.g. 0x91) it represents a namespace id which starts at byte 1. Example: THBIMC3THGH5RUYAAAAAAAAAAAAAAAAAAAAAAAA  | 
**scoped_metadata_key** | **str** | Metadata key scoped to source, target and type expressed. | 
**target_namespace_id** | **str** | Namespace identifier. | [optional] 
**value_size_delta** | **int** | Change in value size in bytes. | 
**value_size** | **int** | A number that allows uint 32 values. | 
**value** | **str** | Metadata value. If embedded in a transaction, this is calculated as xor(previous-value, value). | 

## Example

```python
from mijin_openapi_client.models.embedded_namespace_metadata_transaction_dto import EmbeddedNamespaceMetadataTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddedNamespaceMetadataTransactionDTO from a JSON string
embedded_namespace_metadata_transaction_dto_instance = EmbeddedNamespaceMetadataTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(EmbeddedNamespaceMetadataTransactionDTO.to_json())

# convert the object into a dict
embedded_namespace_metadata_transaction_dto_dict = embedded_namespace_metadata_transaction_dto_instance.to_dict()
# create an instance of EmbeddedNamespaceMetadataTransactionDTO from a dict
embedded_namespace_metadata_transaction_dto_from_dict = EmbeddedNamespaceMetadataTransactionDTO.from_dict(embedded_namespace_metadata_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


