#!/usr/bin/env python3
"""
Generate Python protobuf / gRPC stubs from the zqnt-protos submodule.

Output: zqnt_utils/generated/zqnt/
Usage:  python scripts/gen_protos.py
"""

import sys
from pathlib import Path

try:
    from grpc_tools import protoc
except ImportError:
    sys.exit("grpcio-tools is required: pip install grpcio-tools")

ROOT = Path(__file__).resolve().parent.parent
PROTO_DIR = ROOT / "zqnt-protos"
OUT_DIR = ROOT / "zqnt_utils" / "generated" / "zqnt"

WELL_KNOWN_PROTOS = Path(protoc.__file__).parent / "_proto"


def ensure_init_files(directory: Path) -> None:
    for dirpath in [directory.parent, directory]:
        init = dirpath / "__init__.py"
        if not init.exists():
            init.write_text("")


def run() -> None:
    if not PROTO_DIR.exists():
        sys.exit("zqnt-protos submodule not found – run: git submodule update --init")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ensure_init_files(OUT_DIR)

    proto_files = sorted(PROTO_DIR.glob("*.proto"))
    if not proto_files:
        sys.exit("No .proto files found in zqnt-protos/")

    print(f"Generating {len(proto_files)} proto file(s) -> {OUT_DIR.relative_to(ROOT)}")

    args = [
        "grpc_tools.protoc",
        f"--proto_path={PROTO_DIR}",
        f"--proto_path={WELL_KNOWN_PROTOS}",
        f"--python_out={OUT_DIR}",
        f"--pyi_out={OUT_DIR}",
        f"--grpc_python_out={OUT_DIR}",
        f"--mypy_grpc_out={OUT_DIR}",
        *[str(p) for p in proto_files],
    ]

    rc = protoc.main(args)
    if rc != 0:
        sys.exit(f"protoc failed with exit code {rc}")

    # grpc_tools generates absolute imports; rewrite them to relative so the
    # package works when installed as zqnt_utils.generated.zqnt.*
    _fix_imports(OUT_DIR)

    print("Done.")


def _fix_imports(directory: Path) -> None:
    """
    grpc_tools emits `import common_pb2 as common__pb2` (bare module import).
    Rewrite to `from . import common_pb2 as common__pb2` so the package
    works correctly when installed.
    """
    import re

    bare_import = re.compile(r"^import (\w+_pb2) as (\w+)$", re.MULTILINE)

    for py_file in [*directory.glob("*.py"), *directory.glob("*.pyi")]:
        src = py_file.read_text()
        patched = bare_import.sub(r"from . import \1 as \2", src)
        if patched != src:
            py_file.write_text(patched)
            print(f"  fixed imports in {py_file.name}")


if __name__ == "__main__":
    run()
