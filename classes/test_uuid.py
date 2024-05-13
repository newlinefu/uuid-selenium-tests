from uuid import UUID


class TestUuid:
    def __init__(self, uuid: str, version: int):
        self.uuid = uuid
        self.version = version

    def is_valid_uuid(self):
        try:
            uuid_obj = UUID(self.uuid, version=self.version)
        except ValueError:
            return False
        return str(uuid_obj) == self.uuid
