# coding: utf-8

"""
    Universal DDI Anycast API

    Anycast capability enables HA (High Availability) configuration of Universal DDI applications that run on equipment located on customer's premises (on-prem hosts). Anycast supports DNS, as well as DNS-forwarding services.  Anycast-enabled application setups use multiple on-premises installations for one particular application type. Multiple application instances are configured to use the same endpoint address. Anycast capability is collocated with such application instance, monitoring the local application instance and advertising to the upstream router (a customer equipment) a per-instance, local route to the common application endpoint address, as long as the local application instance is available. Depending on the type of the upstream router, the customer may configure local route advertisement via either BGP (Boarder Gateway Protocol) or OSPF (Open Shortest Path First) routing protocols. Both protocols may be enabled as well. Multiple routes to the common application service address provide redundancy without the need to reconfigure application clients.  Should an application instance become unavailable, the local route advertisements stop, resulting in withdrawal of the route (in the upstream router) to the application instance that has gone out of service and ensuring that subsequent application requests thus get routed to the remaining available application instances.  

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from anycast.models.onprem_host_ref import OnpremHostRef
from anycast.models.protobuf_field_mask import ProtobufFieldMask
from typing import Optional, Set
from typing_extensions import Self


class AnycastConfig(BaseModel):
    """
    AnycastConfig
    """

  # noqa: E501
    account_id: Optional[StrictInt] = None
    anycast_ip_address: Optional[StrictStr] = None
    anycast_ipv6_address: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    description: Optional[StrictStr] = None
    fields: Optional[ProtobufFieldMask] = None
    id: Optional[StrictInt] = None
    is_configured: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    onprem_hosts: Optional[List[OnpremHostRef]] = None
    runtime_status: Optional[StrictStr] = None
    service: Optional[StrictStr] = None
    tags: Optional[Dict[str, Any]] = None
    updated_at: Optional[datetime] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = [
        "account_id", "anycast_ip_address", "anycast_ipv6_address",
        "created_at", "description", "fields", "id", "is_configured", "name",
        "onprem_hosts", "runtime_status", "service", "tags", "updated_at"
    ]

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
        """Create an instance of AnycastConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "id",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of fields
        if self.fields:
            _dict['fields'] = self.fields.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in onprem_hosts (list)
        _items = []
        if self.onprem_hosts:
            for _item in self.onprem_hosts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['onprem_hosts'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnycastConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "account_id":
            obj.get("account_id"),
            "anycast_ip_address":
            obj.get("anycast_ip_address"),
            "anycast_ipv6_address":
            obj.get("anycast_ipv6_address"),
            "created_at":
            obj.get("created_at"),
            "description":
            obj.get("description"),
            "fields":
            ProtobufFieldMask.from_dict(obj["fields"])
            if obj.get("fields") is not None else None,
            "id":
            obj.get("id"),
            "is_configured":
            obj.get("is_configured"),
            "name":
            obj.get("name"),
            "onprem_hosts":
            [OnpremHostRef.from_dict(_item) for _item in obj["onprem_hosts"]]
            if obj.get("onprem_hosts") is not None else None,
            "runtime_status":
            obj.get("runtime_status"),
            "service":
            obj.get("service"),
            "tags":
            obj.get("tags"),
            "updated_at":
            obj.get("updated_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
