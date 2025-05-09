# coding: utf-8

"""
    Catapult REST Endpoints

    OpenAPI Specification of catapult-rest

    The version of the OpenAPI document: 1.0.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ChainPropertiesDTO(BaseModel):
    """
    Chain related configuration properties.
    """ # noqa: E501
    enable_verifiable_state: Optional[StrictBool] = Field(default=None, description="Set to true if block chain should calculate state hashes so that state is fully verifiable at each block.", alias="enableVerifiableState")
    enable_verifiable_receipts: Optional[StrictBool] = Field(default=None, description="Set to true if block chain should calculate receipts so that state changes are fully verifiable at each block.", alias="enableVerifiableReceipts")
    currency_mosaic_id: Optional[StrictStr] = Field(default=None, description="Mosaic id used as primary chain currency.", alias="currencyMosaicId")
    harvesting_mosaic_id: Optional[StrictStr] = Field(default=None, description="Mosaic id used to provide harvesting ability.", alias="harvestingMosaicId")
    block_generation_target_time: Optional[StrictStr] = Field(default=None, description="Targeted time between blocks.", alias="blockGenerationTargetTime")
    block_time_smoothing_factor: Optional[StrictStr] = Field(default=None, description="A higher value makes the network more biased.", alias="blockTimeSmoothingFactor")
    block_finalization_interval: Optional[StrictStr] = Field(default=None, description="Number of blocks between successive finalization attempts.", alias="blockFinalizationInterval")
    importance_grouping: Optional[StrictStr] = Field(default=None, description="Number of blocks that should be treated as a group for importance purposes.", alias="importanceGrouping")
    importance_activity_percentage: Optional[StrictStr] = Field(default=None, description="Percentage of importance resulting from fee generation and beneficiary usage.", alias="importanceActivityPercentage")
    max_rollback_blocks: Optional[StrictStr] = Field(default=None, description="Maximum number of blocks that can be rolled back.", alias="maxRollbackBlocks")
    max_difficulty_blocks: Optional[StrictStr] = Field(default=None, description="Maximum number of blocks to use in a difficulty calculation.", alias="maxDifficultyBlocks")
    default_dynamic_fee_multiplier: Optional[StrictStr] = Field(default=None, description="Default multiplier to use for dynamic fees.", alias="defaultDynamicFeeMultiplier")
    max_transaction_lifetime: Optional[StrictStr] = Field(default=None, description="Maximum lifetime a transaction can have before it expires.", alias="maxTransactionLifetime")
    max_block_future_time: Optional[StrictStr] = Field(default=None, description="Maximum future time of a block that can be accepted.", alias="maxBlockFutureTime")
    initial_currency_atomic_units: Optional[StrictStr] = Field(default=None, description="Initial currency atomic units available in the network.", alias="initialCurrencyAtomicUnits")
    max_mosaic_atomic_units: Optional[StrictStr] = Field(default=None, description="Maximum atomic units (total-supply * 10 ^ divisibility) of a mosaic allowed in the network.", alias="maxMosaicAtomicUnits")
    total_chain_importance: Optional[StrictStr] = Field(default=None, description="Total whole importance units available in the network.", alias="totalChainImportance")
    min_harvester_balance: Optional[StrictStr] = Field(default=None, description="Minimum number of harvesting mosaic atomic units needed for an account to be eligible for harvesting.", alias="minHarvesterBalance")
    max_harvester_balance: Optional[StrictStr] = Field(default=None, description="Maximum number of harvesting mosaic atomic units needed for an account to be eligible for harvesting.", alias="maxHarvesterBalance")
    min_voter_balance: Optional[StrictStr] = Field(default=None, description="Minimum number of harvesting mosaic atomic units needed for an account to be eligible for voting.", alias="minVoterBalance")
    max_voting_keys_per_account: Optional[StrictStr] = Field(default=None, description="Maximum number of voting keys that can be registered at once per account.", alias="maxVotingKeysPerAccount")
    min_voting_key_lifetime: Optional[StrictStr] = Field(default=None, description="Minimum number of finalization rounds for which voting key can be registered.", alias="minVotingKeyLifetime")
    max_voting_key_lifetime: Optional[StrictStr] = Field(default=None, description="Maximum number of finalization rounds for which voting key can be registered.", alias="maxVotingKeyLifetime")
    harvest_beneficiary_percentage: Optional[StrictStr] = Field(default=None, description="Percentage of the harvested fee that is collected by the beneficiary account.", alias="harvestBeneficiaryPercentage")
    harvest_network_percentage: Optional[StrictStr] = Field(default=None, description="Percentage of the harvested fee that is collected by the network.", alias="harvestNetworkPercentage")
    harvest_network_fee_sink_address: Optional[StrictStr] = Field(default=None, description="Address encoded using a 32-character set.", alias="harvestNetworkFeeSinkAddress")
    block_prune_interval: Optional[StrictStr] = Field(default=None, description="Number of blocks between cache pruning.", alias="blockPruneInterval")
    max_transactions_per_block: Optional[StrictStr] = Field(default=None, description="Maximum number of transactions per block.", alias="maxTransactionsPerBlock")
    __properties: ClassVar[List[str]] = ["enableVerifiableState", "enableVerifiableReceipts", "currencyMosaicId", "harvestingMosaicId", "blockGenerationTargetTime", "blockTimeSmoothingFactor", "blockFinalizationInterval", "importanceGrouping", "importanceActivityPercentage", "maxRollbackBlocks", "maxDifficultyBlocks", "defaultDynamicFeeMultiplier", "maxTransactionLifetime", "maxBlockFutureTime", "initialCurrencyAtomicUnits", "maxMosaicAtomicUnits", "totalChainImportance", "minHarvesterBalance", "maxHarvesterBalance", "minVoterBalance", "maxVotingKeysPerAccount", "minVotingKeyLifetime", "maxVotingKeyLifetime", "harvestBeneficiaryPercentage", "harvestNetworkPercentage", "harvestNetworkFeeSinkAddress", "blockPruneInterval", "maxTransactionsPerBlock"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ChainPropertiesDTO from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChainPropertiesDTO from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enableVerifiableState": obj.get("enableVerifiableState"),
            "enableVerifiableReceipts": obj.get("enableVerifiableReceipts"),
            "currencyMosaicId": obj.get("currencyMosaicId"),
            "harvestingMosaicId": obj.get("harvestingMosaicId"),
            "blockGenerationTargetTime": obj.get("blockGenerationTargetTime"),
            "blockTimeSmoothingFactor": obj.get("blockTimeSmoothingFactor"),
            "blockFinalizationInterval": obj.get("blockFinalizationInterval"),
            "importanceGrouping": obj.get("importanceGrouping"),
            "importanceActivityPercentage": obj.get("importanceActivityPercentage"),
            "maxRollbackBlocks": obj.get("maxRollbackBlocks"),
            "maxDifficultyBlocks": obj.get("maxDifficultyBlocks"),
            "defaultDynamicFeeMultiplier": obj.get("defaultDynamicFeeMultiplier"),
            "maxTransactionLifetime": obj.get("maxTransactionLifetime"),
            "maxBlockFutureTime": obj.get("maxBlockFutureTime"),
            "initialCurrencyAtomicUnits": obj.get("initialCurrencyAtomicUnits"),
            "maxMosaicAtomicUnits": obj.get("maxMosaicAtomicUnits"),
            "totalChainImportance": obj.get("totalChainImportance"),
            "minHarvesterBalance": obj.get("minHarvesterBalance"),
            "maxHarvesterBalance": obj.get("maxHarvesterBalance"),
            "minVoterBalance": obj.get("minVoterBalance"),
            "maxVotingKeysPerAccount": obj.get("maxVotingKeysPerAccount"),
            "minVotingKeyLifetime": obj.get("minVotingKeyLifetime"),
            "maxVotingKeyLifetime": obj.get("maxVotingKeyLifetime"),
            "harvestBeneficiaryPercentage": obj.get("harvestBeneficiaryPercentage"),
            "harvestNetworkPercentage": obj.get("harvestNetworkPercentage"),
            "harvestNetworkFeeSinkAddress": obj.get("harvestNetworkFeeSinkAddress"),
            "blockPruneInterval": obj.get("blockPruneInterval"),
            "maxTransactionsPerBlock": obj.get("maxTransactionsPerBlock")
        })
        return _obj


