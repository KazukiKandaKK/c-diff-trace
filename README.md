# c-diff-trace

A simple diff tool implementation and C file analysis project.

## Contents

- `diff.py` - Python implementation of a diff tool
- `diffchallenge.c` - C source file for analysis
- `a.txt`, `b.txt` - Sample text files for diff testing
- `Dockerfile` - Container setup for development environment

## Usage

### Python diff tool
```bash
python3 diff.py file1 file2
```

### Docker environment
```bash
docker build -t c-diff-trace .
docker run -it c-diff-trace
```
