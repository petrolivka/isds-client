import base64
import mimetypes
from pydantic import BaseModel, computed_field
import os


class DmFile(BaseModel):
    file_path: str

    @computed_field
    def dmEncodedContent(self) -> str | None:
        return self._encode_file()

    @computed_field
    def dmMimeType(self) -> str | None:
        return mimetypes.guess_type(self.file_path)[0]

    @computed_field
    def dmFileMetaType(self) -> str | None:
        return "enclosure"

    @computed_field
    def dmFileDescr(self) -> str | None:
        return os.path.basename(self.file_path)

    @computed_field
    def dmFileGuid(self) -> str | None:
        return None

    @computed_field
    def dmUpFileGuid(self) -> str | None:
        return None

    def _encode_file(self):
        with open(self.file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
