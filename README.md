# Awesome Codex Skills

将 [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)
的 **158 个专业能力、10 个分类**转换为可独立安装的 Codex skills。

每个 skill 包含标准 `SKILL.md`、`agents/openai.yaml` 和 MIT 许可。
详细专业指引按需放在 `references/guide.md`，检索与安装由
[`va-skill-catalog`](skills/va-skill-catalog/SKILL.md) 提供。
不需要 Claude Code，也不依赖第三方 Python 包。

## 安装与使用

需要 Python 3.9+。这是私有仓库，克隆前需通过 GitHub 身份验证。

```sh
gh repo clone roche-k/awesome-codex-skills
cd awesome-codex-skills

# 查看分类、查找能力
python3 skills/va-skill-catalog/scripts/catalog.py categories
python3 skills/va-skill-catalog/scripts/catalog.py search 'C++'
python3 skills/va-skill-catalog/scripts/catalog.py show cpp-pro

# 安装到 ~/.agents/skills
python3 skills/va-skill-catalog/scripts/catalog.py install cpp-pro python-pro code-reviewer

# 安装到指定项目的 .agents/skills
python3 skills/va-skill-catalog/scripts/catalog.py install backend-developer --project /path/to/project

# 兼容使用 CODEX_HOME/skills 的本地环境
python3 skills/va-skill-catalog/scripts/catalog.py install cpp-pro --dest "${CODEX_HOME:-$HOME/.codex}/skills"
```

在 Codex 中使用 `$va-cpp-pro`、`$va-python-pro` 等名字，或让 Codex
根据请求自动匹配已安装 skill。新安装的能力未出现时，重启 Codex 会话。
标准发现路径、命名与触发机制参见
[OpenAI 官方 skills 文档](https://learn.chatgpt.com/docs/build-skills)。

建议按任务选择能力；一次加载大量相似技能会占用发现列表的上下文预算。
完整安装仍可显式使用 `install --all`，按分类安装使用
`install --category 02-language-specialists`。

## 管理已安装技能

```sh
python3 skills/va-skill-catalog/scripts/catalog.py install --all --dry-run
python3 skills/va-skill-catalog/scripts/catalog.py installed
python3 skills/va-skill-catalog/scripts/catalog.py uninstall cpp-pro --dry-run
python3 skills/va-skill-catalog/scripts/catalog.py uninstall cpp-pro

# 安装目录管理 skill，让 Codex 自己检索这个集合
python3 skills/va-skill-catalog/scripts/catalog.py install skill-catalog
```

安装和卸载都支持 `--dest`、`--project` 和 `--dry-run`。
工具会先检查整批选择，再修改目标目录；默认不覆盖已有 skill。
相同版本可重复安装，未经修改且由本工具管理的版本可以卸载。
更新时先卸载旧版本再安装新版；发现本地修改、额外文件或符号链接时会停止，
保留这些内容供你处理。磁盘错误等运行时故障可能使一批操作只完成一部分，
可根据输出重试剩余操作。

独立安装的目录 skill 自带离线索引。安装其他能力时需指定本地仓库：

```sh
python3 ~/.agents/skills/va-skill-catalog/scripts/catalog.py \
  --source /path/to/awesome-codex-skills install cpp-pro
```

也可以用 Codex 的 `$skill-installer`，指定此私有仓库、
`main` 分支和 `skills/va-<name>` 路径安装单个目录。
手工或其他安装器安装的目录不由本工具自动卸载。

## 分类

| 分类 | 数量 |
| --- | ---: |
| `01-core-development` 核心开发 | 11 |
| `02-language-specialists` 语言与框架 | 30 |
| `03-infrastructure` 基础设施 | 16 |
| `04-quality-security` 质量与安全 | 17 |
| `05-data-ai` 数据与 AI | 13 |
| `06-developer-experience` 开发者体验 | 16 |
| `07-specialized-domains` 专业领域 | 16 |
| `08-business-product` 商业与产品 | 17 |
| `09-meta-orchestration` 工作流与协作 | 11 |
| `10-research-analysis` 研究与分析 | 11 |

完整列表：`python3 skills/va-skill-catalog/scripts/catalog.py list`。
名称统一加 `va-` 前缀，版本号中的点转换为连字符，例如
`powershell-5.1-expert` 对应 `va-powershell-5-1-expert`。
原 `agent-installer` 对应 `va-skill-catalog`；命令仍接受原始名称。

## 转换原则与维护

Claude 的 `tools`、`model` 字段不进入 Codex skill 元数据。
专业内容保留为按需加载的参考，移除了通信协议、假定存在的 context manager、
示例进度指标和完成通知。编排、设计翻译、论文检索与安装能力按 Codex 的实际
执行方式重写，不假定存在某个 MCP、消息总线或后台 agent。
模型、权限和委派由当前 Codex 会话决定。

上游的性能目标、覆盖率和版本号属于历史参考，不能当成已测结果或通用硬门槛。
技能应遵守用户指定的逻辑位置、测试与产物规则，按实际任务选择指引。

`source/categories/` 保留原始输入，仅用于维护和溯源，不作为 Codex skill 安装。
`scripts/convert.py` 包含转换规则和需要重写的能力，生成 `skills/` 下的入口、
参考、UI 元数据、许可与索引。目录工具的 `scripts/catalog.py` 是手工维护的运行代码。

```sh
python3 scripts/convert.py
```

转换使用的上游提交：
[`3097abe2d0d1e83a9023c7a8d054c00aace24990`](https://github.com/VoltAgent/awesome-claude-code-subagents/commit/3097abe2d0d1e83a9023c7a8d054c00aace24990)。
索引记录每份源文件的 SHA-256。更新源文件时同步转换规则中的上游提交，
重新生成并检查实际受影响能力。测试代码与测试产物仅留在项目本地 `test/`，
不属于分发内容或提交内容。

## 许可

沿用上游 [MIT License](LICENSE)，保留 `Copyright (c) 2025 VoltAgent`。
每个 skill 都附带 `LICENSE.txt`，便于独立安装与分发时保留许可声明。
