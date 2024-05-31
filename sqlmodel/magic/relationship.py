from typing import (
    Any,
    Tuple,
    Dict,
    Type,
)

from ..main import _TSQLModel, Magic


class ManyToMany(Magic):
    def __call__(
        self,
        cls: Type[_TSQLModel],
        name: str,
        bases: Tuple[Type[Any], ...],
        class_dict: Dict[str, Any],
        key: str,
        annotations: Dict[str, Any],
        **kwargs: Any,
    ) -> Any:
        return NotImplemented


class OneToMany(Magic):
    def __call__(
        self,
        cls: Type[_TSQLModel],
        name: str,
        bases: Tuple[Type[Any], ...],
        class_dict: Dict[str, Any],
        key: str,
        annotations: Dict[str, Any],
        **kwargs: Any,
    ) -> Any:
        return NotImplemented


class ManyToOne(Magic):
    def __call__(
        self,
        cls: Type[_TSQLModel],
        name: str,
        bases: Tuple[Type[Any], ...],
        class_dict: Dict[str, Any],
        key: str,
        annotations: Dict[str, Any],
        **kwargs: Any,
    ) -> Any:
        return NotImplemented
