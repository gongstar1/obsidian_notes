# Agent Skills

Agent Skills 是 Claude Code 中的可扩展技能系统,允许通过预定义的技能快速执行特定任务。

## 概述

Skills 提供了专业化的能力,可以处理特定的任务类型,比如:
- JSON Canvas 文件编辑
- Obsidian Markdown 编辑
- Obsidian Bases 数据库操作
- Git 提交和 PR 管理
- PDF 处理

## 可用 Skills

基于系统配置,当前可用的 skills 包括:

- **json-canvas**: 创建和编辑 JSON Canvas 文件(.canvas)
- **obsidian-bases**: 创建和编辑 Obsidian Bases (.base 文件)
- **obsidian-markdown**: 创建和编辑 Obsidian Flavored Markdown
- **commit**: Git 提交操作
- **review-pr**: PR 代码审查
- **pdf**: PDF 文档处理

## 使用方式

在 Claude Code 中通过 `/skill-name` 语法调用:

```
/commit
/commit -m "Fix bug in authentication"
/review-pr 123
```

## 相关文档

- [[Claude Code]] - Claude Code 的主要文档

---

> [!TIP] 技巧提示
> 技能系统支持自定义扩展。你可以为特定的工作流创建专属的 skill,提高重复性任务的效率。查看 `.obsidian/plugins/` 目录下的相关插件配置来了解更多。
