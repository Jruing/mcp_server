# mcp_server
MCP学习笔记
## 简介
> MCP 是一种开放协议，它标准化了应用程序如何为 LLM 提供上下文。将 MCP 想象成 AI 应用程序的 USB-C 端口。正如 USB-C 提供了一种将设备连接到各种外围设备和配件的标准化方式一样，MCP 也提供了一种将 AI 模型连接到不同数据源和工具的标准化方式

## 基础环境
- Python3.8+
- httpx
- mcp[all]
- Cherry Studio(MCP客户端)


## 安装
```shell
pip install mcp[all]
pip intall httpx
```
## 功能列表
[x] Github: 根据用户及仓库名称获取该仓库的star数量，fork数量，及最后一次更新时间

[x] 天气预报: 根据城市加地区查询该地区的天气预报