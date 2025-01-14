import base64
import mimetypes
from typing import Optional
import uuid
from pydantic import BaseModel, Field, computed_field
import os


class DmFile(BaseModel):
    file_path: str = Field(..., description="File path")

    @computed_field
    def dmEncodedContent(self) -> str | None:
        return self._encode_file()

    @computed_field
    def dmMimeType(self) -> str | None:
        if not self.file_path:
            return None
        return mimetypes.guess_type(self.file_path)[0]

    @computed_field
    def dmFileMetaType(self) -> str | None:
        return "enclosure"

    @computed_field
    def dmFileDescr(self) -> str | None:
        if not self.file_path:
            return None
        return os.path.basename(self.file_path)

    @computed_field
    def dmFileGuid(self) -> str | None:
        if not self.file_path:
            return None
        return str(uuid.uuid4())

    @computed_field
    def dmUpFileGuid(self) -> str | None:
        if not self.file_path:
            return None
        return str(uuid.uuid4())

    def _encode_file(self):
        if not self.file_path:
            return None
        with open(self.file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
