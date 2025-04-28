# MosaicRestrictionDTO

Generic Mosaic Restriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal resource identifier. | 
**mosaic_restriction_entry** | [**MosaicGlobalRestrictionEntryWrapperDTO**](MosaicGlobalRestrictionEntryWrapperDTO.md) |  | 

## Example

```python
from mijin_openapi_client.models.mosaic_restriction_dto import MosaicRestrictionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MosaicRestrictionDTO from a JSON string
mosaic_restriction_dto_instance = MosaicRestrictionDTO.from_json(json)
# print the JSON string representation of the object
print(MosaicRestrictionDTO.to_json())

# convert the object into a dict
mosaic_restriction_dto_dict = mosaic_restriction_dto_instance.to_dict()
# create an instance of MosaicRestrictionDTO from a dict
mosaic_restriction_dto_from_dict = MosaicRestrictionDTO.from_dict(mosaic_restriction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


