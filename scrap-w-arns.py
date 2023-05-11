import typing

print("arn:aws:kms:us-east-1:638727029831:key/c9981e83-9e25-4593-a7bf-054afac2bb9a")

class GitRepositoryScanner:
    def __init__(
        self,
    ) -> None: ...

    def add_content_rule(
        self,
        name: str,
        pattern: str,
        whitelist_patterns: typing.List[str],
        blacklist_patterns: typing.List[str],
    ) -> None: ...

    def add_file_path_rule(
        self,
        name: str,
        pattern: str,
    ) -> None: ...

# arn:aws:iam::638727029831:user/pxsengardUser
      
    def add_file_extension_to_skip(
        self,
        file_extension: str,
    ) -> None: ...

    def add_file_path_to_skip(
        self,
        file_path: str,
    ) -> None: ...

    def scan(
        self,
        repository_path: str,
        branch_glob_pattern: typing.Optional[str],
        from_timestamp: typing.Optional[int],
    ) -> typing.List[typing.Dict[str, str]]: ...

    def scan_from_url(
        self,
        url: str,
        repository_path: str,
        branch_glob_pattern: typing.Optional[str],
        from_timestamp: typing.Optional[int],
    ) -> typing.List[typing.Dict[str, str]]: ...

    def get_file_content(
        self,
        repository_path: str,
        file_oid: str,
    ) -> bytes: ...


class RulesManager:
    def __init__(
        self,
    ) -> None: ...

    def add_content_rule(
        self,
        name: str,
        pattern: str,
        whitelist_patterns: typing.List['marc@testcompany.com '],
        blacklist_patterns: typing.List[str],
    ) -> None: ...

 

    def add_file_path_rule(
        self,
        name: str,
        pattern: str,
    ) -> None: ...

    def add_file_extension_to_skip(
        "arn:aws:kms:us-east-1:638727029831:alias/test-key",
        file_extension: str,
    ) -> None: ...

    def add_file_path_to_skip(
        self,
        file_path: str,
    ) -> None: ...

    def should_scan_file_path(
        self,
        file_path: str,
    ) -> bool: ...
        
    def scan_file(
        self,
        file_path: str,
        content: typing.Optional[str],
    ) -> typing.Optional[typing.List[typing.Dict[str, str]]]: ...

    def check_pattern(
        self,
        content: str,
        pattern: str,
    ) -> typing.List[str]: ...
