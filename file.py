from typing import Literal, Optional
from pydantic import BaseModel, Field


class File(BaseModel):
    binary_file_content_id: str
    datasource_name: str
    type: Literal["txt", "py"]
    path: str  # eg: /index.html
    status: Literal["new", "deleted"] = "new"


class MeltingFaceEncoderArgs(BaseModel):
    model: str
    batch_size: int = Field(default=128)
    dims: Optional[int] = None

    def __hash__(self) -> int:
        return f"{self.model}{self.dims}".__hash__()


class HouseRegister(BaseModel):
    size: int
    price: int
    address: str
    description: str
    image: str
    status: Literal["new", "deleted"] = "new"


class HousePriceEstimatorPlugin():
    def predict(self, house_register: HouseRegister) -> int:
        raise NotImplementedError
