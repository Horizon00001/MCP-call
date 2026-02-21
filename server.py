from fastmcp import FastMCP
import subprocess
import os
mcp = FastMCP(name="server")

@mcp.tool
def return_hello():
    return "hello"

@mcp.tool
def run_script(script_path: str) -> None:
    if not os.path.exists(script_path):
        return f"错误：脚本文件 {script_path} 不存在"
    result = subprocess.run(
        [script_path],
        shell=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode == 0:
        return result.stdout

if __name__ == "__main__":
    mcp.run(transport="stdio")