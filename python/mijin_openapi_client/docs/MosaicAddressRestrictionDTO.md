# MosaicAddressRestrictionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal resource identifier. | 
**mosaic_restriction_entry** | [**MosaicAddressRestrictionEntryWrapperDTO**](MosaicAddressRestrictionEntryWrapperDTO.md) |  | 

## Example

```python
from mijin_openapi_client.models.mosaic_address_restriction_dto import MosaicAddressRestrictionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MosaicAddressRestrictionDTO from a JSON string
mosaic_address_restriction_dto_instance = MosaicAddressRestrictionDTO.from_json(json)
# print the JSON string representation of the object
print(MosaicAddressRestrictionDTO.to_json())

# convert the object into a dict
mosaic_address_restriction_dto_dict = mosaic_address_restriction_dto_instance.to_dict()
# create an instance of MosaicAddressRestrictionDTO from a dict
mosaic_address_restriction_dto_from_dict = MosaicAddressRestrictionDTO.from_dict(mosaic_address_restriction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


