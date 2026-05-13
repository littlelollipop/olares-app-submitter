# Olares 应用提交技能

一个全面的技能包，帮助开发者将应用提交到 Olares 应用市场。提供创建 OAC（Olares Application Chart）包、提交 PR、通过 GitBot 校验的完整工作流程指导。

## 🌟 功能特点

- ✅ **完整的 OAC 包创建指南** - 分步说明如何创建符合规范的 OAC 包
- ✅ **PR 提交流程** - 正确的 PR 命名规范和提交流程
- ✅ **GitBot 错误解决方案** - 20+ 个实际测试发现的 GitBot 校验错误及解决方案
- ✅ **本地验证脚本** - 提交前本地验证 OAC 包的 Python 脚本
- ✅ **详尽的文档** - OAC 规范和下机指南的详细参考文档

## 📦 安装方法

### 方法 1：通过 Git 克隆

```bash
# 克隆此仓库到本地
git clone https://github.com/LittleLollipop/olares-app-submitter.git
```

### 方法 2：下载 ZIP

1. 访问 https://github.com/LittleLollipop/olares-app-submitter
2. 点击 "Code" → "Download ZIP"
3. 解压到你想放置的位置

## 🚀 使用方法

### 基本用法

当你需要向 Olares 应用市场提交应用时，将技能文件提供给你的 AI 助手：

```
请阅读 SKILL.md 和 references/ 文件，帮助我将应用提交到 Olares 应用市场。
```

AI 助手会引导你完成流程。

### 工作流程步骤

1. **创建 OAC 包**
   - 使用提供的模板：`Chart.yaml` 和 `OlaresManifest.yaml`
   - 创建 `owners` 文件，包含你的 GitHub 用户名
   - 确保所有必需字段都存在

2. **本地验证（可选）**
   ```bash
   python3 /path/to/olares-app-submitter/scripts/validate_oac.py /path/to/your-app
   ```

3. **提交 PR**
   - Fork `https://github.com/beclab/apps`
   - 将你的 OAC 目录添加到 Fork 后的仓库
   - 创建 Draft PR，标题遵循规范：`[NEW][your-app][1.0.0] 标题`
   - 点击 "Ready for review" 触发 GitBot 校验

4. **修复 GitBot 错误**
   - 查看 PR 评论中的 GitBot 校验结果
   - 参考 `references/gitbot-errors.md` 了解常见错误及解决方案
   - 修复问题并推送新的 commit 触发重新校验

## 📁 文件结构

```
olares-app-submitter/
├── SKILL.md                          # 技能定义和工作流程指南
├── README.md                         # 英文 README
├── README_zh.md                      # 中文 README（本文件）
├── references/                       # 参考文档
│   ├── oac-specification.md         # OAC 包规范
│   ├── olares-submit-guide.md      # 详细提交指南
│   └── gitbot-errors.md           # 20+ 个 GitBot 错误解决方案
└── scripts/                          # 实用脚本
    └── validate_oac.py             # 本地 OAC 包验证器
```

## 📚 文档说明

### OlaresManifest.yaml 中的必需字段

**`metadata.icon` 字段** - GitBot 校验需要：
```yaml
metadata:
  name: your-app
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png
```

**`entrances` 字段** - 定义应用入口点：
```yaml
entrances:
- name: yourapp
  port: 80
  host: yourapp
  title: Your App Title
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png
  openMethod: window
```

### 模板限制

- **镜像字段必须硬编码** - 不能在 `templates/deployment.yaml` 中使用 Helm 模板占位符如 `{{ .Values.image.tag }}`
- **必须设置所有容器资源** - 必须为内存和 CPU 定义 `requests` 和 `limits`

### 目录命名规则

- 只允许的字符：`a-z`, `A-Z`, `0-9`, 空格, `. , ! ? ; : ' " -`
- 最大长度：30 个字符
- **不允许使用连字符 (`-`)** - 使用下划线 (`_`) 代替

### PR 提交规则

- **一个 PR = 一个目录** - 不能在单个 PR 中修改多个应用目录
- PR 标题必须与目录名完全一致

## 🔍 在不同 AI 助手中使用此技能

这是一个**通用技能包**，任何 AI 助手都可以使用。方法如下：

### 对于 Claude 用户（通过 Claude API 或 Claude.ai）

直接给 Claude 提供技能文件：
```
请阅读 SKILL.md 和 references/ 文件，帮助我将应用提交到 Olares 应用市场。
```

或者将技能目录作为上下文上传。

### 对于 GPT 用户（通过 GPTs 或 Assistants API）

1. 上传 `SKILL.md` 和 `references/*.md` 作为知识文件
2. 指示 GPT："按照 SKILL.md 中的工作流程帮助提交应用到 Olares"

### 对于其他 AI 助手

任何能够读取 Markdown 的 AI 都可以使用此技能：
1. 读取 `SKILL.md` 了解工作流程
2. 遇到错误时参考 `references/gitbot-errors.md`
3. 使用 `scripts/validate_oac.py` 进行本地验证（需要 Python）

## 📖 参考资料

- [Olares 官方文档](https://docs.olares.cn/zh/developer/develop/submit/)
- [官方应用仓库](https://github.com/beclab/apps)
- [OAC 打包指南](https://docs.olares.cn/zh/developer/develop/package/chart.html)

## 🤝 贡献

发现了新的 GitBot 错误？请帮助改进这个技能：

1. Fork 本仓库
2. 将新的错误和解决方案添加到 `references/gitbot-errors.md`
3. 提交 Pull Request

## 📝 许可证

MIT 许可证 - 欢迎自由使用和修改此技能。

---

## 📊 实际测试结果

**提交成功的 PR**: [#2185](https://github.com/beclab/apps/pull/2185)（已合并 ✅）

**发现的错误**: 测试过程中发现 10 个错误，全部记录在 `references/gitbot-errors.md` 中

**价值**: 本技能提供 GitBot 校验错误的实际解决方案，帮助开发者节省试错时间。
