# TransactionStatusEnum

List of status errors that can be returned via the status channel after announcing a transaction: * Success * Neutral * Failure * Failure_Core_Past_Deadline - Validation failed because the deadline passed. * Failure_Core_Future_Deadline - Validation failed because the deadline is too far in the future. * Failure_Core_Insufficient_Balance - Validation failed because the account has an insufficient balance. * Failure_Core_Too_Many_Transactions - Validation failed because there are too many transactions in a block. * Failure_Core_Nemesis_Account_Signed_After_Nemesis_Block - Validation failed because an entity originated from the nemesis account after the nemesis block. * Failure_Core_Wrong_Network - Validation failed because the entity has the wrong network specified. * Failure_Core_Invalid_Address - Validation failed because an address is invalid. * Failure_Core_Invalid_Version - Validation failed because entity version is invalid. * Failure_Core_Invalid_Transaction_Fee - Validation failed because a transaction fee is invalid. * Failure_Core_Block_Harvester_Ineligible - Validation failed because a block was harvested by an ineligible harvester. * Failure_Core_Zero_Address - Validation failed because an address is zero. * Failure_Core_Zero_Public_Key - Validation failed because a public key is zero. * Failure_Core_Nonzero_Internal_Padding - Validation failed because internal padding is nonzero. * Failure_Core_Address_Collision - Validation failed because an address collision is detected. * Failure_Core_Importance_Block_Mismatch - Validation failed because the block does not match the schema of an importance block. * Failure_Core_Unexpected_Block_Type - Validation failed because the block type is unexpected. * Failure_Core_Block_Explicit_Transactions_Hash_Mismatch - Validation failed because a block did not have the expected transactions hash at a specified height. * Failure_Core_Invalid_Link_Action - Validation failed because link action is invalid. * Failure_Core_Link_Already_Exists - Validation failed because main account is already linked to another account. * Failure_Core_Inconsistent_Unlink_Data - Validation failed because unlink data is not consistent with existing account link. * Failure_Core_Invalid_Link_Range - Validation failed because link range is invalid. * Failure_Core_Too_Many_Links - Validation failed because main account has too many links of the specified type. * Failure_Core_Link_Start_Epoch_Invalid - Validation failed because the start epoch is invalid. * Failure_Hash_Already_Exists * Failure_Signature_Not_Verifiable - Validation failed because the verification of the signature failed. * Failure_AccountLink_Link_Already_Exists - Validation failed because main account is already linked to another account. * Failure_AccountLink_Inconsistent_Unlink_Data - Validation failed because unlink data is not consistent with existing account link. * Failure_AccountLink_Unknown_Link - Validation failed because main account is not linked to another account. * Failure_AccountLink_Remote_Account_Ineligible - Validation failed because link is attempting to convert ineligible account to remote. * Failure_AccountLink_Remote_Account_Signer_Prohibited - Validation failed because remote is not allowed to sign a transaction. * Failure_AccountLink_Remote_Account_Participant_Prohibited - Validation failed because remote is not allowed to participate in the transaction. * Failure_Aggregate_Too_Many_Transactions - Validation failed because aggregate has too many transactions. * Failure_Aggregate_No_Transactions - Validation failed because aggregate does not have any transactions. * Failure_Aggregate_Too_Many_Cosignatures - Validation failed because aggregate has too many cosignatures. * Failure_Aggregate_Redundant_Cosignatures - Validation failed because redundant cosignatures are present. * Failure_Aggregate_Ineligible_Cosignatories - Validation failed because at least one cosignatory is ineligible. * Failure_Aggregate_Missing_Cosignatures - Validation failed because at least one required cosignature is missing. * Failure_Aggregate_Transactions_Hash_Mismatch - Validation failed because the aggregate transactions hash does not match the calculated value. * Failure_LockHash_Invalid_Mosaic_Id - Validation failed because lock does not allow the specified mosaic. * Failure_LockHash_Invalid_Mosaic_Amount - Validation failed because lock does not allow the specified amount. * Failure_LockHash_Hash_Already_Exists - Validation failed because hash is already present in cache. * Failure_LockHash_Unknown_Hash - Validation failed because hash is not present in cache. * Failure_LockHash_Inactive_Hash - Validation failed because hash is inactive. * Failure_LockHash_Invalid_Duration - Validation failed because duration is too long. * Failure_LockSecret_Invalid_Hash_Algorithm - Validation failed because hash algorithm for lock type secret is invalid. * Failure_LockSecret_Hash_Already_Exists - Validation failed because hash is already present in cache. * Failure_LockSecret_Proof_Size_Out_Of_Bounds - Validation failed because proof is too small or too large. * Failure_LockSecret_Secret_Mismatch - Validation failed because secret does not match proof. * Failure_LockSecret_Unknown_Composite_Key - Validation failed because composite key is unknown. * Failure_LockSecret_Inactive_Secret - Validation failed because secret is inactive. * Failure_LockSecret_Hash_Algorithm_Mismatch - Validation failed because hash algorithm does not match. * Failure_LockSecret_Invalid_Duration - Validation failed because duration is too long. * Failure_Metadata_Value_Too_Small - Validation failed because the metadata value is too small. * Failure_Metadata_Value_Too_Large - Validation failed because the metadata value is too large. * Failure_Metadata_Value_Size_Delta_Too_Large - Validation failed because the metadata value size delta is larger in magnitude than the value size. * Failure_Metadata_Value_Size_Delta_Mismatch - Validation failed because the metadata value size delta does not match expected value based on the current state. * Failure_Metadata_Value_Change_Irreversible - Validation failed because a metadata value change (truncation) is irreversible. * Failure_Mosaic_Invalid_Duration - Validation failed because the duration has an invalid value. * Failure_Mosaic_Invalid_Name - Validation failed because the name is invalid. * Failure_Mosaic_Name_Id_Mismatch - Validation failed because the name and id don't match. * Failure_Mosaic_Expired - Validation failed because the parent is expired. * Failure_Mosaic_Owner_Conflict - Validation failed because the parent owner conflicts with the child owner. * Failure_Mosaic_Id_Mismatch - Validation failed because the id is not the expected id generated from signer and nonce. * Failure_Mosaic_Parent_Id_Conflict - Validation failed because the existing parent id does not match the supplied parent id. * Failure_Mosaic_Invalid_Property - Validation failed because a mosaic property is invalid. * Failure_Mosaic_Invalid_Flags - Validation failed because the mosaic flags are invalid. * Failure_Mosaic_Invalid_Divisibility - Validation failed because the mosaic divisibility is invalid. * Failure_Mosaic_Invalid_Supply_Change_Action - Validation failed because the mosaic supply change action is invalid. * Failure_Mosaic_Invalid_Supply_Change_Amount - Validation failed because the mosaic supply change amount is invalid. * Failure_Mosaic_Invalid_Id - Validation failed because the mosaic id is invalid. * Failure_Mosaic_Modification_Disallowed - Validation failed because mosaic modification is not allowed. * Failure_Mosaic_Modification_No_Changes - Validation failed because mosaic modification would not result in any changes. * Failure_Mosaic_Supply_Immutable - Validation failed because the mosaic supply is immutable. * Failure_Mosaic_Supply_Negative - Validation failed because the resulting mosaic supply is negative. * Failure_Mosaic_Supply_Exceeded - Validation failed because the resulting mosaic supply exceeds the maximum allowed value. * Failure_Mosaic_Non_Transferable - Validation failed because the mosaic is not transferable. * Failure_Mosaic_Max_Mosaics_Exceeded - Validation failed because the credit of the mosaic would exceed the maximum of different mosaics an account is allowed to own. * Failure_Mosaic_Required_Property_Flag_Unset - Validation failed because the mosaic has at least one required property flag unset. * Failure_Multisig_Account_In_Both_Sets - Validation failed because account is specified to be both added and removed. * Failure_Multisig_Multiple_Deletes - Validation failed because multiple removals are present. * Failure_Multisig_Redundant_Modification - Validation failed because a modification is redundant. * Failure_Multisig_Unknown_Multisig_Account - Validation failed because account is not in multisig cache. * Failure_Multisig_Not_A_Cosignatory - Validation failed because account to be removed is not present. * Failure_Multisig_Already_A_Cosignatory - Validation failed because account to be added is already a cosignatory. * Failure_Multisig_Min_Setting_Out_Of_Range - Validation failed because new minimum settings are out of range. * Failure_Multisig_Min_Setting_Larger_Than_Num_Cosignatories - Validation failed because min settings are larger than number of cosignatories. * Failure_Multisig_Invalid_Modification_Action - Validation failed because the modification action is invalid. * Failure_Multisig_Max_Cosigned_Accounts - Validation failed because the cosignatory already cosigns the maximum number of accounts. * Failure_Multisig_Max_Cosignatories - Validation failed because the multisig account already has the maximum number of cosignatories. * Failure_Multisig_Loop - Validation failed because a multisig loop is created. * Failure_Multisig_Max_Multisig_Depth - Validation failed because the max multisig depth is exceeded. * Failure_Multisig_Operation_Prohibited_By_Account - Validation failed because an operation is not permitted by a multisig account. * Failure_Namespace_Invalid_Duration - Validation failed because the duration has an invalid value. * Failure_Namespace_Invalid_Name - Validation failed because the name is invalid. * Failure_Namespace_Name_Id_Mismatch - Validation failed because the name and id don't match. * Failure_Namespace_Expired - Validation failed because the parent is expired. * Failure_Namespace_Owner_Conflict - Validation failed because the parent owner conflicts with the child owner. * Failure_Namespace_Id_Mismatch - Validation failed because the id is not the expected id generated from signer and nonce. * Failure_Namespace_Invalid_Registration_Type - Validation failed because the namespace registration type is invalid. * Failure_Namespace_Root_Name_Reserved - Validation failed because the root namespace has a reserved name. * Failure_Namespace_Too_Deep - Validation failed because the resulting namespace would exceed the maximum allowed namespace depth. * Failure_Namespace_Unknown_Parent - Validation failed because the namespace parent is unknown. * Failure_Namespace_Already_Exists - Validation failed because the namespace already exists. * Failure_Namespace_Already_Active - Validation failed because the namespace is already active. * Failure_Namespace_Eternal_After_Nemesis_Block - Validation failed because an eternal namespace was received after the nemesis block. * Failure_Namespace_Max_Children_Exceeded - Validation failed because the maximum number of children for a root namespace was exceeded. * Failure_Namespace_Alias_Invalid_Action - Validation failed because alias action is invalid. * Failure_Namespace_Unknown - Validation failed because namespace does not exist. * Failure_Namespace_Alias_Already_Exists - Validation failed because namespace is already linked to an alias. * Failure_Namespace_Unknown_Alias - Validation failed because namespace is not linked to an alias. * Failure_Namespace_Alias_Inconsistent_Unlink_Type - Validation failed because unlink type is not consistent with existing alias. * Failure_Namespace_Alias_Inconsistent_Unlink_Data - Validation failed because unlink data is not consistent with existing alias. * Failure_Namespace_Alias_Invalid_Address - Validation failed because aliased address is invalid. * Failure_RestrictionAccount_Invalid_Restriction_Flags - Validation failed because the account restriction flags are invalid. * Failure_RestrictionAccount_Invalid_Modification_Action - Validation failed because a modification action is invalid. * Failure_RestrictionAccount_Invalid_Modification_Address - Validation failed because a modification address is invalid. * Failure_RestrictionAccount_Modification_Operation_Type_Incompatible - Validation failed because the operation type is incompatible. *Note*: This indicates that the existing restrictions have a different operation type than that specified in the notification. * Failure_RestrictionAccount_Redundant_Modification - Validation failed because a modification is redundant. * Failure_RestrictionAccount_Invalid_Modification - Validation failed because a value is not in the container. * Failure_RestrictionAccount_Modification_Count_Exceeded - Validation failed because the transaction has too many modifications. * Failure_RestrictionAccount_No_Modifications - Validation failed because the transaction has no modifications. * Failure_RestrictionAccount_Values_Count_Exceeded - Validation failed because the resulting account restriction has too many values. * Failure_RestrictionAccount_Invalid_Value - Validation failed because the account restriction value is invalid. * Failure_RestrictionAccount_Address_Interaction_Prohibited - Validation failed because the addresses involved in the transaction are not allowed to interact. * Failure_RestrictionAccount_Mosaic_Transfer_Prohibited - Validation failed because the mosaic transfer is prohibited by the recipient. * Failure_RestrictionAccount_Operation_Type_Prohibited - Validation failed because the operation type is not allowed to be initiated by the signer. * Failure_RestrictionMosaic_Invalid_Restriction_Type - Validation failed because the mosaic restriction type is invalid. * Failure_RestrictionMosaic_Previous_Value_Mismatch - Validation failed because specified previous value does not match current value. * Failure_RestrictionMosaic_Previous_Value_Must_Be_Zero - Validation failed because specified previous value is nonzero. * Failure_RestrictionMosaic_Max_Restrictions_Exceeded - Validation failed because the maximum number of restrictions would be exceeded. * Failure_RestrictionMosaic_Cannot_Delete_Nonexistent_Restriction - Validation failed because nonexistent restriction cannot be deleted. * Failure_RestrictionMosaic_Unknown_Global_Restriction - Validation failed because required global restriction does not exist. * Failure_RestrictionMosaic_Invalid_Global_Restriction - Validation failed because mosaic has invalid global restriction. * Failure_RestrictionMosaic_Account_Unauthorized - Validation failed because account lacks proper permissions to move mosaic. * Failure_Transfer_Message_Too_Large - Validation failed because the message is too large. * Failure_Transfer_Out_Of_Order_Mosaics - Validation failed because mosaics are out of order. * Failure_Chain_Unlinked - Validation failed because a block was received that did not link with the existing chain. * Failure_Chain_Block_Not_Hit - Validation failed because a block was received that is not a hit. * Failure_Chain_Block_Inconsistent_State_Hash - Validation failed because a block was received that has an inconsistent state hash. * Failure_Chain_Block_Inconsistent_Receipts_Hash - Validation failed because a block was received that has an inconsistent receipts hash. * Failure_Chain_Block_Invalid_Vrf_Proof - Validation failed because the Vrf proof is invalid. * Failure_Chain_Block_Unknown_Signer - Validation failed because the block signer is unknown. * Failure_Chain_Unconfirmed_Cache_Too_Full - Validation failed because the unconfirmed cache is too full. * Failure_Consumer_Empty_Input - Validation failed because the consumer input is empty. * Failure_Consumer_Block_Transactions_Hash_Mismatch - Validation failed because the block transactions hash does not match the calculated value. * Neutral_Consumer_Hash_In_Recency_Cache - Validation failed because an entity hash is present in the recency cache. * Failure_Consumer_Remote_Chain_Too_Many_Blocks - Validation failed because the chain part has too many blocks. * Failure_Consumer_Remote_Chain_Improper_Link - Validation failed because the chain is internally improperly linked. * Failure_Consumer_Remote_Chain_Duplicate_Transactions - Validation failed because the chain part contains duplicate transactions. * Failure_Consumer_Remote_Chain_Unlinked - Validation failed because the chain part does not link to the current chain. * Failure_Consumer_Remote_Chain_Difficulties_Mismatch - Validation failed because the remote chain difficulties do not match the calculated difficulties. * Failure_Consumer_Remote_Chain_Score_Not_Better - Validation failed because the remote chain score is not better. * Failure_Consumer_Remote_Chain_Too_Far_Behind - Validation failed because the remote chain is too far behind. * Failure_Consumer_Remote_Chain_Too_Far_In_Future - Validation failed because the remote chain timestamp is too far in the future. * Failure_Consumer_Batch_Signature_Not_Verifiable - Validation failed because the verification of the signature failed during a batch operation. * Failure_Consumer_Remote_Chain_Improper_Importance_Link - Validation failed because the remote chain has an improper importance link. * Failure_Extension_Partial_Transaction_Cache_Prune - Validation failed because the partial transaction was pruned from the temporal cache. * Failure_Extension_Partial_Transaction_Dependency_Removed - Validation failed because the partial transaction was pruned from the temporal cache due to its dependency being removed. * Failure_Extension_Read_Rate_Limit_Exceeded - Validation failed because socket read rate limit was exceeded. 

## Enum

* `SUCCESS` (value: `'Success'`)

* `NEUTRAL` (value: `'Neutral'`)

* `FAILURE` (value: `'Failure'`)

* `FAILURE_CORE_PAST_DEADLINE` (value: `'Failure_Core_Past_Deadline'`)

* `FAILURE_CORE_FUTURE_DEADLINE` (value: `'Failure_Core_Future_Deadline'`)

* `FAILURE_CORE_INSUFFICIENT_BALANCE` (value: `'Failure_Core_Insufficient_Balance'`)

* `FAILURE_CORE_TOO_MANY_TRANSACTIONS` (value: `'Failure_Core_Too_Many_Transactions'`)

* `FAILURE_CORE_NEMESIS_ACCOUNT_SIGNED_AFTER_NEMESIS_BLOCK` (value: `'Failure_Core_Nemesis_Account_Signed_After_Nemesis_Block'`)

* `FAILURE_CORE_WRONG_NETWORK` (value: `'Failure_Core_Wrong_Network'`)

* `FAILURE_CORE_INVALID_ADDRESS` (value: `'Failure_Core_Invalid_Address'`)

* `FAILURE_CORE_INVALID_VERSION` (value: `'Failure_Core_Invalid_Version'`)

* `FAILURE_CORE_INVALID_TRANSACTION_FEE` (value: `'Failure_Core_Invalid_Transaction_Fee'`)

* `FAILURE_CORE_BLOCK_HARVESTER_INELIGIBLE` (value: `'Failure_Core_Block_Harvester_Ineligible'`)

* `FAILURE_CORE_ZERO_ADDRESS` (value: `'Failure_Core_Zero_Address'`)

* `FAILURE_CORE_ZERO_PUBLIC_KEY` (value: `'Failure_Core_Zero_Public_Key'`)

* `FAILURE_CORE_NONZERO_INTERNAL_PADDING` (value: `'Failure_Core_Nonzero_Internal_Padding'`)

* `FAILURE_CORE_ADDRESS_COLLISION` (value: `'Failure_Core_Address_Collision'`)

* `FAILURE_CORE_IMPORTANCE_BLOCK_MISMATCH` (value: `'Failure_Core_Importance_Block_Mismatch'`)

* `FAILURE_CORE_UNEXPECTED_BLOCK_TYPE` (value: `'Failure_Core_Unexpected_Block_Type'`)

* `FAILURE_CORE_BLOCK_EXPLICIT_TRANSACTIONS_HASH_MISMATCH` (value: `'Failure_Core_Block_Explicit_Transactions_Hash_Mismatch'`)

* `FAILURE_CORE_INVALID_LINK_ACTION` (value: `'Failure_Core_Invalid_Link_Action'`)

* `FAILURE_CORE_LINK_ALREADY_EXISTS` (value: `'Failure_Core_Link_Already_Exists'`)

* `FAILURE_CORE_INCONSISTENT_UNLINK_DATA` (value: `'Failure_Core_Inconsistent_Unlink_Data'`)

* `FAILURE_CORE_INVALID_LINK_RANGE` (value: `'Failure_Core_Invalid_Link_Range'`)

* `FAILURE_CORE_TOO_MANY_LINKS` (value: `'Failure_Core_Too_Many_Links'`)

* `FAILURE_CORE_LINK_START_EPOCH_INVALID` (value: `'Failure_Core_Link_Start_Epoch_Invalid'`)

* `FAILURE_HASH_ALREADY_EXISTS` (value: `'Failure_Hash_Already_Exists'`)

* `FAILURE_SIGNATURE_NOT_VERIFIABLE` (value: `'Failure_Signature_Not_Verifiable'`)

* `FAILURE_ACCOUNT_LINK_LINK_ALREADY_EXISTS` (value: `'Failure_AccountLink_Link_Already_Exists'`)

* `FAILURE_ACCOUNT_LINK_INCONSISTENT_UNLINK_DATA` (value: `'Failure_AccountLink_Inconsistent_Unlink_Data'`)

* `FAILURE_ACCOUNT_LINK_UNKNOWN_LINK` (value: `'Failure_AccountLink_Unknown_Link'`)

* `FAILURE_ACCOUNT_LINK_REMOTE_ACCOUNT_INELIGIBLE` (value: `'Failure_AccountLink_Remote_Account_Ineligible'`)

* `FAILURE_ACCOUNT_LINK_REMOTE_ACCOUNT_SIGNER_PROHIBITED` (value: `'Failure_AccountLink_Remote_Account_Signer_Prohibited'`)

* `FAILURE_ACCOUNT_LINK_REMOTE_ACCOUNT_PARTICIPANT_PROHIBITED` (value: `'Failure_AccountLink_Remote_Account_Participant_Prohibited'`)

* `FAILURE_AGGREGATE_TOO_MANY_TRANSACTIONS` (value: `'Failure_Aggregate_Too_Many_Transactions'`)

* `FAILURE_AGGREGATE_NO_TRANSACTIONS` (value: `'Failure_Aggregate_No_Transactions'`)

* `FAILURE_AGGREGATE_TOO_MANY_COSIGNATURES` (value: `'Failure_Aggregate_Too_Many_Cosignatures'`)

* `FAILURE_AGGREGATE_REDUNDANT_COSIGNATURES` (value: `'Failure_Aggregate_Redundant_Cosignatures'`)

* `FAILURE_AGGREGATE_INELIGIBLE_COSIGNATORIES` (value: `'Failure_Aggregate_Ineligible_Cosignatories'`)

* `FAILURE_AGGREGATE_MISSING_COSIGNATURES` (value: `'Failure_Aggregate_Missing_Cosignatures'`)

* `FAILURE_AGGREGATE_TRANSACTIONS_HASH_MISMATCH` (value: `'Failure_Aggregate_Transactions_Hash_Mismatch'`)

* `FAILURE_LOCK_HASH_INVALID_MOSAIC_ID` (value: `'Failure_LockHash_Invalid_Mosaic_Id'`)

* `FAILURE_LOCK_HASH_INVALID_MOSAIC_AMOUNT` (value: `'Failure_LockHash_Invalid_Mosaic_Amount'`)

* `FAILURE_LOCK_HASH_HASH_ALREADY_EXISTS` (value: `'Failure_LockHash_Hash_Already_Exists'`)

* `FAILURE_LOCK_HASH_UNKNOWN_HASH` (value: `'Failure_LockHash_Unknown_Hash'`)

* `FAILURE_LOCK_HASH_INACTIVE_HASH` (value: `'Failure_LockHash_Inactive_Hash'`)

* `FAILURE_LOCK_HASH_INVALID_DURATION` (value: `'Failure_LockHash_Invalid_Duration'`)

* `FAILURE_LOCK_SECRET_INVALID_HASH_ALGORITHM` (value: `'Failure_LockSecret_Invalid_Hash_Algorithm'`)

* `FAILURE_LOCK_SECRET_HASH_ALREADY_EXISTS` (value: `'Failure_LockSecret_Hash_Already_Exists'`)

* `FAILURE_LOCK_SECRET_PROOF_SIZE_OUT_OF_BOUNDS` (value: `'Failure_LockSecret_Proof_Size_Out_Of_Bounds'`)

* `FAILURE_LOCK_SECRET_SECRET_MISMATCH` (value: `'Failure_LockSecret_Secret_Mismatch'`)

* `FAILURE_LOCK_SECRET_UNKNOWN_COMPOSITE_KEY` (value: `'Failure_LockSecret_Unknown_Composite_Key'`)

* `FAILURE_LOCK_SECRET_INACTIVE_SECRET` (value: `'Failure_LockSecret_Inactive_Secret'`)

* `FAILURE_LOCK_SECRET_HASH_ALGORITHM_MISMATCH` (value: `'Failure_LockSecret_Hash_Algorithm_Mismatch'`)

* `FAILURE_LOCK_SECRET_INVALID_DURATION` (value: `'Failure_LockSecret_Invalid_Duration'`)

* `FAILURE_METADATA_VALUE_TOO_SMALL` (value: `'Failure_Metadata_Value_Too_Small'`)

* `FAILURE_METADATA_VALUE_TOO_LARGE` (value: `'Failure_Metadata_Value_Too_Large'`)

* `FAILURE_METADATA_VALUE_SIZE_DELTA_TOO_LARGE` (value: `'Failure_Metadata_Value_Size_Delta_Too_Large'`)

* `FAILURE_METADATA_VALUE_SIZE_DELTA_MISMATCH` (value: `'Failure_Metadata_Value_Size_Delta_Mismatch'`)

* `FAILURE_METADATA_VALUE_CHANGE_IRREVERSIBLE` (value: `'Failure_Metadata_Value_Change_Irreversible'`)

* `FAILURE_MOSAIC_INVALID_DURATION` (value: `'Failure_Mosaic_Invalid_Duration'`)

* `FAILURE_MOSAIC_INVALID_NAME` (value: `'Failure_Mosaic_Invalid_Name'`)

* `FAILURE_MOSAIC_NAME_ID_MISMATCH` (value: `'Failure_Mosaic_Name_Id_Mismatch'`)

* `FAILURE_MOSAIC_EXPIRED` (value: `'Failure_Mosaic_Expired'`)

* `FAILURE_MOSAIC_OWNER_CONFLICT` (value: `'Failure_Mosaic_Owner_Conflict'`)

* `FAILURE_MOSAIC_ID_MISMATCH` (value: `'Failure_Mosaic_Id_Mismatch'`)

* `FAILURE_MOSAIC_PARENT_ID_CONFLICT` (value: `'Failure_Mosaic_Parent_Id_Conflict'`)

* `FAILURE_MOSAIC_INVALID_PROPERTY` (value: `'Failure_Mosaic_Invalid_Property'`)

* `FAILURE_MOSAIC_INVALID_FLAGS` (value: `'Failure_Mosaic_Invalid_Flags'`)

* `FAILURE_MOSAIC_INVALID_DIVISIBILITY` (value: `'Failure_Mosaic_Invalid_Divisibility'`)

* `FAILURE_MOSAIC_INVALID_SUPPLY_CHANGE_ACTION` (value: `'Failure_Mosaic_Invalid_Supply_Change_Action'`)

* `FAILURE_MOSAIC_INVALID_SUPPLY_CHANGE_AMOUNT` (value: `'Failure_Mosaic_Invalid_Supply_Change_Amount'`)

* `FAILURE_MOSAIC_INVALID_ID` (value: `'Failure_Mosaic_Invalid_Id'`)

* `FAILURE_MOSAIC_MODIFICATION_DISALLOWED` (value: `'Failure_Mosaic_Modification_Disallowed'`)

* `FAILURE_MOSAIC_MODIFICATION_NO_CHANGES` (value: `'Failure_Mosaic_Modification_No_Changes'`)

* `FAILURE_MOSAIC_SUPPLY_IMMUTABLE` (value: `'Failure_Mosaic_Supply_Immutable'`)

* `FAILURE_MOSAIC_SUPPLY_NEGATIVE` (value: `'Failure_Mosaic_Supply_Negative'`)

* `FAILURE_MOSAIC_SUPPLY_EXCEEDED` (value: `'Failure_Mosaic_Supply_Exceeded'`)

* `FAILURE_MOSAIC_NON_TRANSFERABLE` (value: `'Failure_Mosaic_Non_Transferable'`)

* `FAILURE_MOSAIC_MAX_MOSAICS_EXCEEDED` (value: `'Failure_Mosaic_Max_Mosaics_Exceeded'`)

* `FAILURE_MOSAIC_REQUIRED_PROPERTY_FLAG_UNSET` (value: `'Failure_Mosaic_Required_Property_Flag_Unset'`)

* `FAILURE_MULTISIG_ACCOUNT_IN_BOTH_SETS` (value: `'Failure_Multisig_Account_In_Both_Sets'`)

* `FAILURE_MULTISIG_MULTIPLE_DELETES` (value: `'Failure_Multisig_Multiple_Deletes'`)

* `FAILURE_MULTISIG_REDUNDANT_MODIFICATION` (value: `'Failure_Multisig_Redundant_Modification'`)

* `FAILURE_MULTISIG_UNKNOWN_MULTISIG_ACCOUNT` (value: `'Failure_Multisig_Unknown_Multisig_Account'`)

* `FAILURE_MULTISIG_NOT_A_COSIGNATORY` (value: `'Failure_Multisig_Not_A_Cosignatory'`)

* `FAILURE_MULTISIG_ALREADY_A_COSIGNATORY` (value: `'Failure_Multisig_Already_A_Cosignatory'`)

* `FAILURE_MULTISIG_MIN_SETTING_OUT_OF_RANGE` (value: `'Failure_Multisig_Min_Setting_Out_Of_Range'`)

* `FAILURE_MULTISIG_MIN_SETTING_LARGER_THAN_NUM_COSIGNATORIES` (value: `'Failure_Multisig_Min_Setting_Larger_Than_Num_Cosignatories'`)

* `FAILURE_MULTISIG_INVALID_MODIFICATION_ACTION` (value: `'Failure_Multisig_Invalid_Modification_Action'`)

* `FAILURE_MULTISIG_MAX_COSIGNED_ACCOUNTS` (value: `'Failure_Multisig_Max_Cosigned_Accounts'`)

* `FAILURE_MULTISIG_MAX_COSIGNATORIES` (value: `'Failure_Multisig_Max_Cosignatories'`)

* `FAILURE_MULTISIG_LOOP` (value: `'Failure_Multisig_Loop'`)

* `FAILURE_MULTISIG_MAX_MULTISIG_DEPTH` (value: `'Failure_Multisig_Max_Multisig_Depth'`)

* `FAILURE_MULTISIG_OPERATION_PROHIBITED_BY_ACCOUNT` (value: `'Failure_Multisig_Operation_Prohibited_By_Account'`)

* `FAILURE_NAMESPACE_INVALID_DURATION` (value: `'Failure_Namespace_Invalid_Duration'`)

* `FAILURE_NAMESPACE_INVALID_NAME` (value: `'Failure_Namespace_Invalid_Name'`)

* `FAILURE_NAMESPACE_NAME_ID_MISMATCH` (value: `'Failure_Namespace_Name_Id_Mismatch'`)

* `FAILURE_NAMESPACE_EXPIRED` (value: `'Failure_Namespace_Expired'`)

* `FAILURE_NAMESPACE_OWNER_CONFLICT` (value: `'Failure_Namespace_Owner_Conflict'`)

* `FAILURE_NAMESPACE_ID_MISMATCH` (value: `'Failure_Namespace_Id_Mismatch'`)

* `FAILURE_NAMESPACE_INVALID_REGISTRATION_TYPE` (value: `'Failure_Namespace_Invalid_Registration_Type'`)

* `FAILURE_NAMESPACE_ROOT_NAME_RESERVED` (value: `'Failure_Namespace_Root_Name_Reserved'`)

* `FAILURE_NAMESPACE_TOO_DEEP` (value: `'Failure_Namespace_Too_Deep'`)

* `FAILURE_NAMESPACE_UNKNOWN_PARENT` (value: `'Failure_Namespace_Unknown_Parent'`)

* `FAILURE_NAMESPACE_ALREADY_EXISTS` (value: `'Failure_Namespace_Already_Exists'`)

* `FAILURE_NAMESPACE_ALREADY_ACTIVE` (value: `'Failure_Namespace_Already_Active'`)

* `FAILURE_NAMESPACE_ETERNAL_AFTER_NEMESIS_BLOCK` (value: `'Failure_Namespace_Eternal_After_Nemesis_Block'`)

* `FAILURE_NAMESPACE_MAX_CHILDREN_EXCEEDED` (value: `'Failure_Namespace_Max_Children_Exceeded'`)

* `FAILURE_NAMESPACE_ALIAS_INVALID_ACTION` (value: `'Failure_Namespace_Alias_Invalid_Action'`)

* `FAILURE_NAMESPACE_UNKNOWN` (value: `'Failure_Namespace_Unknown'`)

* `FAILURE_NAMESPACE_ALIAS_ALREADY_EXISTS` (value: `'Failure_Namespace_Alias_Already_Exists'`)

* `FAILURE_NAMESPACE_UNKNOWN_ALIAS` (value: `'Failure_Namespace_Unknown_Alias'`)

* `FAILURE_NAMESPACE_ALIAS_INCONSISTENT_UNLINK_TYPE` (value: `'Failure_Namespace_Alias_Inconsistent_Unlink_Type'`)

* `FAILURE_NAMESPACE_ALIAS_INCONSISTENT_UNLINK_DATA` (value: `'Failure_Namespace_Alias_Inconsistent_Unlink_Data'`)

* `FAILURE_NAMESPACE_ALIAS_INVALID_ADDRESS` (value: `'Failure_Namespace_Alias_Invalid_Address'`)

* `FAILURE_RESTRICTION_ACCOUNT_INVALID_RESTRICTION_FLAGS` (value: `'Failure_RestrictionAccount_Invalid_Restriction_Flags'`)

* `FAILURE_RESTRICTION_ACCOUNT_INVALID_MODIFICATION_ACTION` (value: `'Failure_RestrictionAccount_Invalid_Modification_Action'`)

* `FAILURE_RESTRICTION_ACCOUNT_INVALID_MODIFICATION_ADDRESS` (value: `'Failure_RestrictionAccount_Invalid_Modification_Address'`)

* `FAILURE_RESTRICTION_ACCOUNT_MODIFICATION_OPERATION_TYPE_INCOMPATIBLE` (value: `'Failure_RestrictionAccount_Modification_Operation_Type_Incompatible'`)

* `FAILURE_RESTRICTION_ACCOUNT_REDUNDANT_MODIFICATION` (value: `'Failure_RestrictionAccount_Redundant_Modification'`)

* `FAILURE_RESTRICTION_ACCOUNT_INVALID_MODIFICATION` (value: `'Failure_RestrictionAccount_Invalid_Modification'`)

* `FAILURE_RESTRICTION_ACCOUNT_MODIFICATION_COUNT_EXCEEDED` (value: `'Failure_RestrictionAccount_Modification_Count_Exceeded'`)

* `FAILURE_RESTRICTION_ACCOUNT_NO_MODIFICATIONS` (value: `'Failure_RestrictionAccount_No_Modifications'`)

* `FAILURE_RESTRICTION_ACCOUNT_VALUES_COUNT_EXCEEDED` (value: `'Failure_RestrictionAccount_Values_Count_Exceeded'`)

* `FAILURE_RESTRICTION_ACCOUNT_INVALID_VALUE` (value: `'Failure_RestrictionAccount_Invalid_Value'`)

* `FAILURE_RESTRICTION_ACCOUNT_ADDRESS_INTERACTION_PROHIBITED` (value: `'Failure_RestrictionAccount_Address_Interaction_Prohibited'`)

* `FAILURE_RESTRICTION_ACCOUNT_MOSAIC_TRANSFER_PROHIBITED` (value: `'Failure_RestrictionAccount_Mosaic_Transfer_Prohibited'`)

* `FAILURE_RESTRICTION_ACCOUNT_OPERATION_TYPE_PROHIBITED` (value: `'Failure_RestrictionAccount_Operation_Type_Prohibited'`)

* `FAILURE_RESTRICTION_MOSAIC_INVALID_RESTRICTION_TYPE` (value: `'Failure_RestrictionMosaic_Invalid_Restriction_Type'`)

* `FAILURE_RESTRICTION_MOSAIC_PREVIOUS_VALUE_MISMATCH` (value: `'Failure_RestrictionMosaic_Previous_Value_Mismatch'`)

* `FAILURE_RESTRICTION_MOSAIC_PREVIOUS_VALUE_MUST_BE_ZERO` (value: `'Failure_RestrictionMosaic_Previous_Value_Must_Be_Zero'`)

* `FAILURE_RESTRICTION_MOSAIC_MAX_RESTRICTIONS_EXCEEDED` (value: `'Failure_RestrictionMosaic_Max_Restrictions_Exceeded'`)

* `FAILURE_RESTRICTION_MOSAIC_CANNOT_DELETE_NONEXISTENT_RESTRICTION` (value: `'Failure_RestrictionMosaic_Cannot_Delete_Nonexistent_Restriction'`)

* `FAILURE_RESTRICTION_MOSAIC_UNKNOWN_GLOBAL_RESTRICTION` (value: `'Failure_RestrictionMosaic_Unknown_Global_Restriction'`)

* `FAILURE_RESTRICTION_MOSAIC_INVALID_GLOBAL_RESTRICTION` (value: `'Failure_RestrictionMosaic_Invalid_Global_Restriction'`)

* `FAILURE_RESTRICTION_MOSAIC_ACCOUNT_UNAUTHORIZED` (value: `'Failure_RestrictionMosaic_Account_Unauthorized'`)

* `FAILURE_TRANSFER_MESSAGE_TOO_LARGE` (value: `'Failure_Transfer_Message_Too_Large'`)

* `FAILURE_TRANSFER_OUT_OF_ORDER_MOSAICS` (value: `'Failure_Transfer_Out_Of_Order_Mosaics'`)

* `FAILURE_CHAIN_UNLINKED` (value: `'Failure_Chain_Unlinked'`)

* `FAILURE_CHAIN_BLOCK_NOT_HIT` (value: `'Failure_Chain_Block_Not_Hit'`)

* `FAILURE_CHAIN_BLOCK_INCONSISTENT_STATE_HASH` (value: `'Failure_Chain_Block_Inconsistent_State_Hash'`)

* `FAILURE_CHAIN_BLOCK_INCONSISTENT_RECEIPTS_HASH` (value: `'Failure_Chain_Block_Inconsistent_Receipts_Hash'`)

* `FAILURE_CHAIN_BLOCK_INVALID_VRF_PROOF` (value: `'Failure_Chain_Block_Invalid_Vrf_Proof'`)

* `FAILURE_CHAIN_BLOCK_UNKNOWN_SIGNER` (value: `'Failure_Chain_Block_Unknown_Signer'`)

* `FAILURE_CHAIN_UNCONFIRMED_CACHE_TOO_FULL` (value: `'Failure_Chain_Unconfirmed_Cache_Too_Full'`)

* `FAILURE_CONSUMER_EMPTY_INPUT` (value: `'Failure_Consumer_Empty_Input'`)

* `FAILURE_CONSUMER_BLOCK_TRANSACTIONS_HASH_MISMATCH` (value: `'Failure_Consumer_Block_Transactions_Hash_Mismatch'`)

* `NEUTRAL_CONSUMER_HASH_IN_RECENCY_CACHE` (value: `'Neutral_Consumer_Hash_In_Recency_Cache'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_TOO_MANY_BLOCKS` (value: `'Failure_Consumer_Remote_Chain_Too_Many_Blocks'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_IMPROPER_LINK` (value: `'Failure_Consumer_Remote_Chain_Improper_Link'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_DUPLICATE_TRANSACTIONS` (value: `'Failure_Consumer_Remote_Chain_Duplicate_Transactions'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_UNLINKED` (value: `'Failure_Consumer_Remote_Chain_Unlinked'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_DIFFICULTIES_MISMATCH` (value: `'Failure_Consumer_Remote_Chain_Difficulties_Mismatch'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_SCORE_NOT_BETTER` (value: `'Failure_Consumer_Remote_Chain_Score_Not_Better'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_TOO_FAR_BEHIND` (value: `'Failure_Consumer_Remote_Chain_Too_Far_Behind'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_TOO_FAR_IN_FUTURE` (value: `'Failure_Consumer_Remote_Chain_Too_Far_In_Future'`)

* `FAILURE_CONSUMER_BATCH_SIGNATURE_NOT_VERIFIABLE` (value: `'Failure_Consumer_Batch_Signature_Not_Verifiable'`)

* `FAILURE_CONSUMER_REMOTE_CHAIN_IMPROPER_IMPORTANCE_LINK` (value: `'Failure_Consumer_Remote_Chain_Improper_Importance_Link'`)

* `FAILURE_EXTENSION_PARTIAL_TRANSACTION_CACHE_PRUNE` (value: `'Failure_Extension_Partial_Transaction_Cache_Prune'`)

* `FAILURE_EXTENSION_PARTIAL_TRANSACTION_DEPENDENCY_REMOVED` (value: `'Failure_Extension_Partial_Transaction_Dependency_Removed'`)

* `FAILURE_EXTENSION_READ_RATE_LIMIT_EXCEEDED` (value: `'Failure_Extension_Read_Rate_Limit_Exceeded'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


