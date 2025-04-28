# MosaicGlobalRestrictionEntryRestrictionDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_mosaic_id** | **str** | Mosaic identifier. | 
**restriction_value** | **str** | Restriction value. | 
**restriction_type** | [**MosaicRestrictionTypeEnum**](MosaicRestrictionTypeEnum.md) |  | 

## Example

```python
from mijin_openapi_client.models.mosaic_global_restriction_entry_restriction_dto import MosaicGlobalRestrictionEntryRestrictionDTO

# TODO update the JSON string below
json = "{}"
# create an instance of MosaicGlobalRestrictionEntryRestrictionDTO from a JSON string
mosaic_global_restriction_entry_restriction_dto_instance = MosaicGlobalRestrictionEntryRestrictionDTO.from_json(json)
# print the JSON string representation of the object
print(MosaicGlobalRestrictionEntryRestrictionDTO.to_json())

# convert the object into a dict
mosaic_global_restriction_entry_restriction_dto_dict = mosaic_global_restriction_entry_restriction_dto_instance.to_dict()
# create an instance of MosaicGlobalRestrictionEntryRestrictionDTO from a dict
mosaic_global_restriction_entry_restriction_dto_from_dict = MosaicGlobalRestrictionEntryRestrictionDTO.from_dict(mosaic_global_restriction_entry_restriction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


