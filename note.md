### PostgreSQL Server on Docker

```
docker run --name my-postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```
```
docker run -it --name python-miniconda continuumio/miniconda3
```
```
# 內建 conda, node.js, uv 以提供 mcp 使用
docker run -it --platform linux/arm64 --name python-postgres roberthsu2003/conda_uv_npx
```
download link: https://www.docker.com/get-started/

### DBeaver network settings

```
URL: jdbc:postgresql://localhost:5432/postgres
username: postgres
password: password
```
download link: https://dbeaver.io/download/

### claude_desktop_config.json

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-postgres",
        "postgresql://postgres:password@localhost:5432/postgres"
      ]
    }
  }
}
```

### VScode

Extensions:
* Dev Containers
* Container Tools

download link: https://code.visualstudio.com/download


### GitHub

``` bash
git config --global user.name "{name}"
git config --global user.email "{email}"
```

### Node.js

download link: https://nodejs.org/zh-tw/download
