# MCP Server 示例项目

这是一个基于 FastMCP 的简单 MCP 服务器示例项目。

## 文件说明

| 文件          | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| `server.py` | MCP 服务器主文件，定义了两个工具：return_hello 和 run_script |
| `script.py` | 示例脚本文件，用于测试 run_script 工具                       |
| `test.py`   | 简单的测试文件                                               |

## 工具列表及调用方法

### 1. return_hello

返回问候语 "hello"。

**在 IDE 中调用：**

```
使用 server 的 ping
```

### 2. run_script

运行指定路径的 Python 脚本。

**在 IDE 中调用：**

```
使用 run_script，script_path="C:/Users/LENOVO/test.py"
```

**参数说明：**

- `script_path` (str): 脚本文件的绝对路径

**返回值：**

- 脚本输出内容（如果执行成功）
- 错误信息（如果脚本不存在或执行失败）

## 在 Trae 中配置 MCP

### 1. 打开 Trae 设置

在 Trae 中，点击左下角的设置图标，选择 **设置**，然后搜索 "MCP"。

### 2. 添加 MCP 服务器

在 MCP 设置中，点击 **添加 MCP 服务器**，填写以下信息：

| 配置项 | 值                                |
| ------ | --------------------------------- |
| 名称   | `mcp_test` (或其他你喜欢的名称) |
| 类型   | `stdio`                         |
| 命令   | `python`                        |
| 参数   | `server.py` 的绝对路径          |

**示例配置：**

```json
{
  "mcpServers": {
    "mcp_test": {
      "command": "python",
      "args": [
        "文件路径请填server.py 所在的绝对路径"
      ]
    }
  }
}
```

### 3. 验证配置

配置完成后，在 Trae 的 AI 对话中输入：

```
使用 mcp_test 的 return_hello
```

如果返回 `hello`，说明配置成功。

## 使用方法

### 启动 MCP 服务器

```bash
python server.py
```

### 直接运行脚本

```bash
python script.py
```

## 依赖

- Python 3.x
- fastmcp

## 安装依赖

```bash
pip install fastmcp
```

## 项目结构

```
day26/
├── server.py      # MCP 服务器
├── script.py      # 示例脚本
├── test.py        # 测试文件
└── README.md      # 项目说明
```
