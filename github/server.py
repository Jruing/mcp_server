# encoding: utf-8
import json
import os

import httpx
from mcp.server.fastmcp import FastMCP

#
mcp = FastMCP("Github 🚀",prompt="""
查询Github仓库的星标，叉，以及最后一次更新时间
工具栏列表：
1. get_repo_info
""")

os.environ["github_token"] = "ghp_xxxxx"
token = os.environ.get("github_token")


@mcp.tool()
async def get_repo_info(owner: str, repo: str):
    """
    获取github仓库信息
    Args：
        owner：仓库作者
        repo: 仓库名称
    Returns:
        返回结果，用中文进行回答,将最后一次更新时间添加8小时后并字段格式化成%Y-%m-%d %H:%M:%S,具体格式如下
    Example：
        {
            "🧛‍作者”：owner,
            "🎁仓库”：repo
            "✨星标数量": stars,
            "🍴Fork数量": forks,
            "⏲️最后一次更新时间": updated_time,
        }

    """
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"https://api.github.com/repos/{owner}/{repo}",
                                headers={"Accept": "application/vnd.github+json",
                                         "Authorization": f"Bearer {token}",
                                         "X-GitHub-Api-Version": "2022-11-28"})
        stars = resp.json()["stargazers_count"]
        forks = resp.json()["forks"]
        updated_time = resp.json()["pushed_at"]
        return {
            "author": owner,
            "repo": repo,
            "stars": stars,
            "forks": forks,
            "updated_time": updated_time,
        }



if __name__ == '__main__':
    mcp.run(transport="sse")
