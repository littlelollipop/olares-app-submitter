---
name: olares-app-submitter
description: 帮助开发者将应用提交到 Olares 应用市场。支持 OAC 包创建、PR 提交流程、GitBot 校验规则检查、常见错误解决方案。适用于需要将自研应用发布到 Olares 市场的开发者。
agent_created: true
---

# Olares 应用提交技能

此技能提供将应用提交到 Olares 应用市场的完整工作流程和指导。

## 目的

简化 Olares 应用市场提交流程，帮助开发者正确创建 OAC（Olares Application Chart）包，并成功通过 GitBot 校验，最终将应用上架到 Olares 应用市场。

## 使用场景

在以下场景中使用此技能：
- 需要将自研应用发布到 Olares 应用市场
- 需要创建符合 Olares 规范的 OAC 包
- PR 被 GitBot 拒绝，需要排查错误原因
- 需要更新已上架的 Olares 应用版本
- 需要暂停或移除已上架的应用

## 工作流程

### 1. 创建 OAC 包

OAC（Olares Application Chart）是 Helm Chart 的扩展格式，是提交到 Olares 市场的标准打包格式。

**目录结构**：
```
your-app/
├── Chart.yaml          # Helm 标准配置
├── OlaresManifest.yaml # Olares 扩展元数据
├── owners              # 所有者 GitHub 用户名列表
├── .suspend            # （可选）暂停分发标记
├── .remove             # （可选）移除应用标记
└── ...                 # 其他 Helm Chart 标准文件
```

**快速开始**：
1. 复制 `assets/Chart.yaml.template` 和 `assets/OlaresManifest.yaml.template` 作为模板
2. 根据应用信息填写模板中的占位符
3. 创建 `owners` 文件，每行一个 GitHub 用户名
4. 确保 `Chart.yaml` 的 `version` 与 `OlaresManifest.yaml` 的 `metadata.version` 完全一致

参考 `references/oac-specification.md` 了解完整的 OAC 规范。

### 2. 提交 PR 到官方仓库

**PR 命名规范**（必须严格遵守）：
```
[PR类型][应用目录名][版本号] 标题
```

**PR 类型**：
| 类型 | 说明 |
|------|------|
| `NEW` | 提交全新应用 |
| `UPDATE` | 更新已有应用 |
| `SUSPEND` | 暂停应用分发 |
| `REMOVE` | 完全移除应用 |

**提交步骤**：
1. Fork 官方仓库：`https://github.com/beclab/apps`
2. 将 OAC 目录添加到 Fork 后的仓库对应位置
3. 创建 Draft PR，标题严格遵循命名规范
4. 填写 PR 模板中的所有必填项
5. 点击 "Ready for review" 触发 GitBot 自动检查

参考 `references/olares-submit-guide.md` 了解详细的提交流程。

### 3. 通过 GitBot 校验

PR 提交后会自动触发 GitBot 校验，常见状态：
- `waiting to submit`：存在待修复问题，修改后提交 commit 会触发重新检查
- `closed`：存在不可修复错误，需关闭后重新提交新 PR
- `waiting to merge`：所有检查通过，等待自动合并
- `merged`：已合并，稍后同步到应用市场

**常见错误及解决方案**参考 `references/gitbot-errors.md`（已收录 20+ 个实际测试发现的 GitBot 校验错误及解决方案）。

### 4. 验证 OAC 包（可选）

使用 `scripts/validate_oac.py` 在提交前本地验证 OAC 包的合规性：

```bash
python3 ~/.workbuddy/skills/olares-app-submitter/scripts/validate_oac.py /path/to/your-app
```

## 注意事项

1. **版本号管理**：每次修改必须升级版本号，且新版本必须高于仓库中已有版本
2. **跨平台兼容**：此技能尽量使用标准格式（Markdown、YAML、Python），避免依赖特定平台功能
3. **资产要求**：应用图标、宣传截图等资产需符合 `references/oac-specification.md` 中的规格要求
4. **所有者权限**：修改已有应用的 PR 提交者必须是 `owners` 文件中列出的 GitHub 用户

## 参考资料

- Olares 官方文档：`https://docs.olares.cn/zh/developer/develop/submit/`
- 官方应用仓库：`https://github.com/beclab/apps`
- OAC 打包指南：`https://docs.olares.cn/zh/developer/develop/package/chart.html`
