# TransactionStatementDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **str** | Height of the blockchain. | 
**source** | [**SourceDTO**](SourceDTO.md) |  | 
**receipts** | [**List[TransactionStatementDTOReceiptsInner]**](TransactionStatementDTOReceiptsInner.md) | Array of receipts. | 

## Example

```python
from mijin_openapi_client.models.transaction_statement_dto import TransactionStatementDTO

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionStatementDTO from a JSON string
transaction_statement_dto_instance = TransactionStatementDTO.from_json(json)
# print the JSON string representation of the object
print(TransactionStatementDTO.to_json())

# convert the object into a dict
transaction_statement_dto_dict = transaction_statement_dto_instance.to_dict()
# create an instance of TransactionStatementDTO from a dict
transaction_statement_dto_from_dict = TransactionStatementDTO.from_dict(transaction_statement_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


