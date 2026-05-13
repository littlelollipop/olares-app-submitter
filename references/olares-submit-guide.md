# Olares 应用提交详细指南

本文档提供将应用提交到 Olares 应用市场的详细步骤和注意事项。

## 前置条件

在提交应用前，请确保：
1. 应用已在 Olares OS 上完成开发和测试
2. 应用已打包为符合规范的 OAC（Olares Application Chart）格式
3. 拥有有效的 GitHub 账号
4. 了解 Git 基本操作（Fork、Commit、PR）

## 步骤一：Fork 官方仓库

1. 访问官方应用仓库：`https://github.com/beclab/apps`
2. 点击右上角 "Fork" 按钮
3. 选择你的 GitHub 账号作为 Fork 目标
4. 等待 Fork 完成（会跳转到你的 Fork 仓库页面）

## 步骤二：添加 OAC 包到 Fork 仓库

### 方式 A：使用 Git 命令行（推荐）

```bash
# 1. 克隆你的 Fork 仓库到本地
git clone https://github.com/你的用户名/apps.git
cd apps

# 2. 添加上游仓库（可选，用于同步官方更新）
git remote add upstream https://github.com/beclab/apps.git

# 3. 创建新分支（推荐）
git checkout -b add-my-app

# 4. 将你的 OAC 目录复制到 apps/ 目录下
cp -r /path/to/your-app ./

# 5. 提交更改
git add your-app/
git commit -m "Add new app: your-app"

# 6. 推送到你的 Fork 仓库
git push origin add-my-app
```

### 方式 B：使用 GitHub Web 界面

1. 在你的 Fork 仓库页面，点击 "Add file" -> "Create new file"
2. 在文件名中输入：`your-app/Chart.yaml`
3. 复制粘贴你的 Chart.yaml 内容
4. 点击 "Commit new file"
5. 重复以上步骤，创建 `OlaresManifest.yaml`、`owners` 等文件

**注意**：Web 界面方式仅适合小型 OAC 包，大型 OAC 包建议使用 Git 命令行。

## 步骤三：创建 Pull Request

1. 在你的 Fork 仓库页面，会看到 "Compare & pull request" 按钮，点击它
2. 填写 PR 标题（**必须严格遵守命名规范**）

**PR 标题格式**：
```
[PR类型][应用目录名][版本号] 标题
```

**示例**：
```
[NEW][my-ai-app][1.0.0] 提交我的 AI 应用
```

3. 填写 PR 描述（按照 PR 模板要求填写）
4. **重要**：先创建为 "Draft PR"（点击 "Create draft pull request"）
5. 确认所有内容无误后，点击 "Ready for review" 按钮（这会触发 GitBot 自动检查）

## 步骤四：等待 GitBot 校验

PR 提交后会自动触发 GitBot 校验，请在 PR 页面查看校验状态。

### GitBot 状态标签说明

| 状态标签 | 说明 | 后续操作 |
|----------|------|----------|
| 无标签 | 标题格式校验中 | 等待标签出现 |
| PR 类型标签（如 `NEW`） | 标题格式校验通过 | 不得修改 PR 类型 |
| `waiting to submit` | 存在待修复问题 | 根据 GitBot 评论修改代码，提交新 commit 会触发重新检查 |
| `closed` | 存在不可修复错误 | 不得重新打开，需关闭此 PR 并创建新 PR |
| `waiting to merge` | 所有检查通过 | 等待 GitBot 自动合并（通常几分钟内） |
| `merged` | PR 已合并到 main 分支 | 等待约 1 小时，应用会出现在 Olares 应用市场 |

### 常见 PR 检查项

GitBot 会自动检查以下项目（包括但不限于）：
1. PR 标题格式是否正确
2. OAC 目录结构是否完整
3. `Chart.yaml` 和 `OlaresManifest.yaml` 格式是否正确
4. 版本号是否符合语义化版本规范
5. 版本号是否高于仓库已有版本
6. `owners` 文件是否包含提交者 GitHub 用户名
7. 应用图标、宣传图等资产是否符合规格
8. 是否存在安全漏洞或恶意代码

## 步骤五：PR 合并后

1. PR 合并后，等待约 1 小时
2. 访问 Olares 应用市场：`https://market.olares.com/`
3. 搜索你的应用名称，确认已上架
4. 测试应用安装和功能是否正常

## 更新已有应用

如果需要更新已上架的应用：

1. 修改 OAC 包内容（升级版本号、更新配置等）
2. 提交 `UPDATE` 类型的 PR：
   ```
   [UPDATE][your-app][1.0.1] 更新应用：修复 Bug
   ```
3. **重要**：新版本号必须高于仓库现有版本号
4. 不得包含 `.suspend` 或 `.remove` 文件

## 暂停或移除应用

### 暂停应用（SUSPEND）

暂停后，新用户无法在市场中找到并安装该应用，但已安装的用户可继续使用。

1. 确保版本号与仓库现有版本一致
2. 在 OAC 目录中创建 `.suspend` 空文件
3. 提交 `SUSPEND` 类型的 PR：
   ```
   [SUSPEND][your-app][1.0.1] 暂停应用分发
   ```

### 移除应用（REMOVE）

移除后，新用户无法在市场中找到并安装该应用，已安装的用户可继续使用。此操作不可逆转（OAC 名称无法复用）。

1. 清空 OAC 目录的所有文件
2. 仅保留 `.remove` 空文件
3. 提交 `REMOVE` 类型的 PR：
   ```
   [REMOVE][your-app][1.0.1] 移除应用
   ```

## 注意事项

1. **同一时间只能有一个打开的 PR**：同一个应用目录不能同时存在多个打开的 Draft/正式 PR
2. **版本号管理**：Olares 市场不支持版本回滚，应用问题需通过提交更高版本修复
3. **所有者权限**：修改已有应用的 PR 提交者必须是 `owners` 文件中列出的 GitHub 用户
4. **PR 被关闭后**：不得重新打开，需修改内容后提交新 PR

## 参考资料

- Olares 官方提交指南：`https://docs.olares.cn/zh/developer/develop/submit/`
- 官方应用仓库：`https://github.com/beclab/apps`
- OAC 打包指南：`https://docs.olares.cn/zh/developer/develop/package/chart.html`
- GitBot 校验规则：参考 `references/gitbot-errors.md`
