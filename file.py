from typing import Literal
from pydantic import BaseModel


class File(BaseModel):
    binary_file_content_id: str
    datasource_name: str
    type: Literal["txt", "py"]
    path: str  # eg: /index.html
    status: Literal["new", "deleted"] = "new"
