from typing import Any

_logger: Any

def get_test_modules(module: Any): ...
def _get_tests_modules(path: Any, module: Any): ...
def make_suite(module_name: Any, position: str = ...): ...
def run_suite(suite: Any, module_name: Any): ...
def unwrap_suite(test: Any) -> None: ...