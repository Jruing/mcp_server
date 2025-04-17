# weather.py
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# 初始化FastMCP服务
mcp = FastMCP("Weather",prompt="""
这是一个天气查询服务，可以通过城市和地区查询天气
工具列表：
1. 查询天气：get_weather_tools
""")

async def get_weatcher(city:str,area:str) ->  Any:
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://cn.apihz.cn/api/tianqi/tqyb.php?id=88888888&key=88888888&sheng={city}&place={area}")
        return resp.json()
def format_weather(data:Any) -> str:
    info = f"""
地点: {data['place']}
降雨量: {data['precipitation']}
温度: {data['temperature']}
湿度: {data['humidity']}
风向: {data['windDirection']}
风速: {data['windSpeed']}
天气: {data['weather1']}"""
    return info

@mcp.tool()
async def get_weather_tools(city:str,area:str) -> str:
    """
    根据城市和地区查询天气
    Args:
        city: 城市,省或者直辖市
        area: 地区或者地级市
    Returns:
        返回指定地区的天气信息
    """
    data = await get_weatcher(city,area)
    return format_weather(data)
if __name__ == "__main__":
    mcp.run(transport='sse')