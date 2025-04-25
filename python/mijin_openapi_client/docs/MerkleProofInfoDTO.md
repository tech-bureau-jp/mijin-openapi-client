# MerkleProofInfoDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merkle_path** | [**List[MerklePathItemDTO]**](MerklePathItemDTO.md) | List of complementary merkle path items needed to recalculate the merkle root. | [optional] 

## Example

```python
from mijin_openapi_client.models.merkle_proof_info_dto import MerkleProofInfoDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MerkleProofInfoDTO from a JSON string
merkle_proof_info_dto_instance = MerkleProofInfoDTO.from_json(json)
# print the JSON string representation of the object
print(MerkleProofInfoDTO.to_json())

# convert the object into a dict
merkle_proof_info_dto_dict = merkle_proof_info_dto_instance.to_dict()
# create an instance of MerkleProofInfoDTO from a dict
merkle_proof_info_dto_from_dict = MerkleProofInfoDTO.from_dict(merkle_proof_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


