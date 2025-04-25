# BalanceTransferReceiptDTO

Receipt stored when a state change that triggered a mosaic transfer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Version of the receipt. | 
**type** | [**ReceiptTypeEnum**](ReceiptTypeEnum.md) |  | 
**mosaic_id** | **str** | Mosaic identifier. | 
**amount** | **str** | Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative). | 
**sender_address** | **str** | Address encoded using a 32-character set. | 
**recipient_address** | **str** | Address encoded using a 32-character set. | 

## Example

```python
from mijin_openapi_client.models.balance_transfer_receipt_dto import BalanceTransferReceiptDTO

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceTransferReceiptDTO from a JSON string
balance_transfer_receipt_dto_instance = BalanceTransferReceiptDTO.from_json(json)
# print the JSON string representation of the object
print(BalanceTransferReceiptDTO.to_json())

# convert the object into a dict
balance_transfer_receipt_dto_dict = balance_transfer_receipt_dto_instance.to_dict()
# create an instance of BalanceTransferReceiptDTO from a dict
balance_transfer_receipt_dto_from_dict = BalanceTransferReceiptDTO.from_dict(balance_transfer_receipt_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


