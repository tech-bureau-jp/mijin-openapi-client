# MosaicMetadataTransactionDTO

Transaction to create or modify a multisig account.

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
**target_address** | **str** | Address expressed in Base32 format. If the bit 0 of byte 0 is not set (like in 0x90), then it is a regular address. Example: TAOXUJOTTW3W5XTBQMQEX3SQNA6MCUVGXLXR3TA.  Otherwise (e.g. 0x91) it represents a namespace id which starts at byte 1. Example: THBIMC3THGH5RUYAAAAAAAAAAAAAAAAAAAAAAAA  | 
**scoped_metadata_key** | **str** | Metadata key scoped to source, target and type expressed. | 
**target_mosaic_id** | **str** | Mosaic identifier. If the most significant bit of byte 0 is set, a namespaceId (alias) is used instead of the real mosaic identifier.  | 
**value_size_delta** | **int** | Change in value size in bytes. | 
**value_size** | **int** | A number that allows uint 32 values. | 
**value** | **str** | Metadata value. If embedded in a transaction, this is calculated as xor(previous-value, value). | 

## Example

```python
from mijin_openapi_client.models.mosaic_metadata_transaction_dto import MosaicMetadataTransactionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MosaicMetadataTransactionDTO from a JSON string
mosaic_metadata_transaction_dto_instance = MosaicMetadataTransactionDTO.from_json(json)
# print the JSON string representation of the object
print(MosaicMetadataTransactionDTO.to_json())

# convert the object into a dict
mosaic_metadata_transaction_dto_dict = mosaic_metadata_transaction_dto_instance.to_dict()
# create an instance of MosaicMetadataTransactionDTO from a dict
mosaic_metadata_transaction_dto_from_dict = MosaicMetadataTransactionDTO.from_dict(mosaic_metadata_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


