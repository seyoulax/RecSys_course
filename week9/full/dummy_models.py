import os
from pathlib import Path

import torch
import onnx
import numpy as np
import onnxruntime as ort


class ALS(torch.nn.Module):
    def __init__(self, num_users: int, num_items: int, factors: int) -> None:
        super().__init__()
        self._embeddings = torch.nn.ModuleDict(
            {
                "user": torch.nn.Embedding(num_users, factors),
                "item": torch.nn.Embedding(num_items, factors),
            }
        )

    def forward(self, users: torch.Tensor) -> torch.Tensor:
        scores = self.get_scores(users)
        return torch.sort(-scores).indices

    def get_scores(self, users: torch.Tensor, items: torch.Tensor = None) -> torch.Tensor:
        # users ~ (num users)
        # items ~ (num items)
        # emb_users ~ (num users, hidden size)
        # emb_items ~ (num items, hidden size)
        emb_users = self._embeddings["user"](users)
        emb_items = (
            self._embeddings["item"](items)
            if items is not None
            else self._embeddings["item"].weight
        )
        # scores ~ (num users, num items)
        return torch.einsum("uh,ih->ui", emb_users, emb_items)


def main() -> None:
    model = ALS(10, 11, factors=32)
    model.eval()
    for param in model.parameters():
        param.requires_grad_(False)
    dummy_users = torch.randint(low=0, high=10, size=(4,))
    path = str(Path(os.getcwd()) / "models_storage" / "als" / "1"/ "model.onnx")
    torch.onnx.export(
        model,
        args=(dummy_users,),
        f=path,
        opset_version=12,
        input_names=["users"],
        output_names=["recommendations"],
        dynamic_axes={
            "users": {0: "num_users"},
            "recommendations": {0: "num_users", 1: "num_items"},
        },
    )
    model = onnx.load(path)
    ort_session = ort.InferenceSession(path)
    outputs = ort_session.run(
        None,
        {"users": np.random.randint(low=0, high=5, size=(1,))},
    )
    print(onnx.checker.check_model(model))
    print(onnx.helper.printable_graph(model.graph))
    print(outputs)


if __name__ == "__main__":
    main()
