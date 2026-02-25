#!/usr/bin/env python3
"""
MCP 服务器示例

这是一个基于 FastMCP 的简单 MCP 服务器，提供两个工具：
1. return_hello - 返回问候语 "hello"
2. run_script - 运行指定路径的 Python 脚本

配置说明：
在 Trae 中配置 MCP 服务器时，需要设置：
- 名称: test
- 命令: python
- 参数: 本文件的绝对路径
"""

# 导入必要的库
from fastmcp import FastMCP  # 导入 FastMCP 库
import subprocess  # 用于执行外部脚本
import os  # 用于文件路径检查

# 创建 MCP 服务器实例
# name 参数指定服务器名称，在 Trae 中使用时需要对应
mcp = FastMCP(name="server")


@mcp.tool
def return_hello():
    """返回问候语
    
    Returns:
        str: 问候语 "hello"
    """
    return "hello"


@mcp.tool
def run_script(script_path: str) -> None:
    """运行指定路径的 Python 脚本
    
    Args:
        script_path (str): 脚本文件的绝对路径
        
    Returns:
        str: 脚本的输出内容（如果执行成功）
        str: 错误信息（如果脚本不存在或执行失败）
    """
    # 检查脚本文件是否存在
    if not os.path.exists(script_path):
        return f"错误：脚本文件 {script_path} 不存在"
    
    # 执行脚本
    result = subprocess.run(
        [script_path],  # 要执行的命令
        shell=True,  # 使用 shell 执行
        capture_output=True,  # 捕获输出
        text=True,  # 输出为文本格式
        timeout=30,  # 超时时间 30 秒
    )
    
    # 检查执行结果
    if result.returncode == 0:
        return result.stdout  # 返回脚本输出


if __name__ == "__main__":
    """主函数：启动 MCP 服务器
    
    使用 stdio 传输方式，这是 Trae 配置中需要的传输类型
    """
    mcp.run(transport="stdio")
