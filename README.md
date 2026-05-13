# Olares App Submitter Skill

English | [中文](#olares-应用提交技能)

> **Universal Skill Declaration**: This is a **platform-agnostic skill** designed for ALL AI assistants (WorkBuddy, Claude, GPT, Copilot, etc.). It contains no platform-specific dependencies and can be used by any AI that can read Markdown documentation.

A comprehensive skill that helps developers submit applications to the Olares App Store. This skill provides complete workflow guidance for creating OAC (Olares Application Chart) packages, submitting PRs, and passing GitBot validation.

## 🌟 Features

- ✅ **Complete OAC Package Creation Guide** - Step-by-step instructions for creating compliant OAC packages
- ✅ **PR Submission Workflow** - Proper PR naming conventions and submission steps
- ✅ **GitBot Error Solutions** - 20+ real-world GitBot validation errors with solutions (discovered through actual testing)
- ✅ **Local Validation Script** - Python script to validate OAC packages before submission
- ✅ **Comprehensive Documentation** - Detailed references for OAC specification and submission guide

## 📦 Installation

### Option 1: Install via WorkBuddy (Recommended)

```bash
# In WorkBuddy, use the /skills command to browse and install skills
/skills
# Then search for "olares-app-submitter" and install
```

### Option 2: Manual Installation

```bash
# Clone this repository to your WorkBuddy skills directory
cd ~/.workbuddy/skills/
git clone https://github.com/YOUR_USERNAME/olares-app-submitter.git
```

## 🚀 Usage

### Basic Usage

When you need to submit an app to Olares App Store, simply tell WorkBuddy:

```
Please help me submit my app to Olares App Store
```

WorkBuddy will automatically load this skill and guide you through the process.

### Workflow Steps

1. **Create OAC Package**
   - Use the provided templates: `Chart.yaml` and `OlaresManifest.yaml`
   - Create `owners` file with your GitHub username
   - Ensure all required fields are present

2. **Validate Locally (Optional)**
   ```bash
   python3 ~/.workbuddy/skills/olares-app-submitter/scripts/validate_oac.py /path/to/your-app
   ```

3. **Submit PR**
   - Fork `https://github.com/beclab/apps`
   - Add your OAC directory to the forked repo
   - Create a Draft PR with proper naming: `[NEW][your-app][1.0.0] Title`
   - Click "Ready for review" to trigger GitBot validation

4. **Fix GitBot Errors**
   - Check PR comments for GitBot validation results
   - Refer to `references/gitbot-errors.md` for common errors and solutions
   - Fix issues and push new commits to trigger re-validation

## 📁 File Structure

```
olares-app-submitter/
├── SKILL.md                          # Skill definition and workflow guide
├── README.md                         # This file
├── references/                       # Reference documentation
│   ├── oac-specification.md         # OAC package specification
│   ├── olares-submit-guide.md      # Detailed submission guide
│   └── gitbot-errors.md           # 20+ GitBot error solutions
└── scripts/                          # Utility scripts
    └── validate_oac.py             # Local OAC package validator
```

## 🔍 Key Findings from Real-World Testing

During actual testing, we discovered several **hidden requirements** not documented in the official Olares documentation:

### 1. Hidden Required Fields in OlaresManifest.yaml

**`metadata.icon` field** - Officially undocumented, but GitBot requires it:
```yaml
metadata:
  name: your-app
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png  # REQUIRED but not in official docs
```

**`entrances` field** - Must define app entrance points:
```yaml
entrances:
- name: yourapp
  port: 80
  host: yourapp
  title: Your App Title
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png
  openMethod: window
```

### 2. Template Restrictions

- **Image field must be hardcoded** - Cannot use Helm template placeholders like `{{ .Values.image.tag }}` in `templates/deployment.yaml`
- **All container resources must be set** - Must define both `requests` and `limits` for memory and CPU

### 3. Directory Naming Rules

- Only allowed characters: `a-z`, `A-Z`, `0-9`, space, `. , ! ? ; : ' " -`
- Maximum length: 30 characters
- **Hyphens (`-`) are NOT allowed** - Use underscores (`_`) instead

### 4. PR Submission Rules

- **One PR = One directory** - Cannot modify multiple app directories in a single PR
- PR title must exactly match the directory name

## 📖 References

- [Olares Official Documentation](https://docs.olares.cn/zh/developer/develop/submit/)
- [Official Apps Repository](https://github.com/beclab/apps)
- [OAC Packaging Guide](https://docs.olares.cn/zh/developer/develop/package/chart.html)

## 🤝 Contributing

Found a new GitBot error? Please help improve this skill by:

1. Fork this repository
2. Add the new error and solution to `references/gitbot-errors.md`
3. Submit a Pull Request

## 📦 Using This Skill with Different AI Assistants

This is a **universal skill** that can be used by any AI assistant. Here's how:

### For WorkBuddy Users

```bash
# Install via WorkBuddy
/skills
# Search for "olares-app-submitter" and install
```

### For Claude Users (via Claude API or Claude.ai)

Simply provide the skill files to Claude:
```
Please read the SKILL.md and references/ files to help me submit my app to Olares App Store.
```

Or upload the skill directory as context.

### For GPT Users (via GPTs or Assistants API)

1. Upload `SKILL.md` and `references/*.md` as knowledge files
2. Instruct the GPT: "Follow the workflow in SKILL.md to help submit an app to Olares"

### For Other AI Assistants

Any AI that can read Markdown can use this skill:
1. Read `SKILL.md` for workflow overview
2. Reference `references/gitbot-errors.md` when encountering errors
3. Use `scripts/validate_oac.py` for local validation (Python required)

## 📝 License

MIT License - feel free to use and modify this skill.

---

# Olares 应用提交技能

[English](#olares-app-submitter-skill) | 中文

> **通用技能声明**: 这是一个**平台无关的技能包**，适用于所有 AI 助手（WorkBuddy、Claude、GPT、Copilot 等）。不包含任何平台特定依赖，任何能够读取 Markdown 文档的 AI 都可以使用。

一个全面的技能包，帮助开发者将应用提交到 Olares 应用市场。提供创建 OAC（Olares Application Chart）包、提交 PR、通过 GitBot 校验的完整工作流程指导。

## 🌟 功能特点

- ✅ **完整的 OAC 包创建指南** - 分步说明如何创建符合规范的 OAC 包
- ✅ **PR 提交流程** - 正确的 PR 命名规范和提交流程
- ✅ **GitBot 错误解决方案** - 20+ 个实际测试发现的 GitBot 校验错误及解决方案
- ✅ **本地验证脚本** - 提交前本地验证 OAC 包的 Python 脚本
- ✅ **详尽的文档** - OAC 规范和下机指南的详细参考文档

## 📦 安装方法

### 方法 1：通过 WorkBuddy 安装（推荐）

```bash
# 在 WorkBuddy 中，使用 /skills 命令浏览和安装技能
/skills
# 然后搜索 "olares-app-submitter" 并安装
```

### 方法 2：手动安装

```bash
# 将此仓库克隆到你的 WorkBuddy 技能目录
cd ~/.workbuddy/skills/
git clone https://github.com/YOUR_USERNAME/olares-app-submitter.git
```

## 🚀 使用方法

### 基本用法

当你需要向 Olares 应用市场提交应用时，只需告诉 WorkBuddy：

```
请帮我将我的应用提交到 Olares 应用市场
```

WorkBuddy 会自动加载此技能并引导你完成流程。

### 工作流程步骤

1. **创建 OAC 包**
   - 使用提供的模板：`Chart.yaml` 和 `OlaresManifest.yaml`
   - 创建 `owners` 文件，包含你的 GitHub 用户名
   - 确保所有必需字段都存在

2. **本地验证（可选）**
   ```bash
   python3 ~/.workbuddy/skills/olares-app-submitter/scripts/validate_oac.py /path/to/your-app
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
├── README.md                         # 本文件
├── references/                       # 参考文档
│   ├── oac-specification.md         # OAC 包规范
│   ├── olares-submit-guide.md      # 详细提交指南
│   └── gitbot-errors.md           # 20+ 个 GitBot 错误解决方案
└── scripts/                          # 实用脚本
    └── validate_oac.py             # 本地 OAC 包验证器
```

## 🔍 实际测试的重要发现

在实际测试过程中，我们发现了几个**官方 Olares 文档中未说明的隐藏要求**：

### 1. OlaresManifest.yaml 中的隐藏必需字段

**`metadata.icon` 字段** - 官方文档未说明，但 GitBot 要求必须提供：
```yaml
metadata:
  name: your-app
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png  # 必须提供，但官方文档模板中没有
```

**`entrances` 字段** - 必须定义应用入口点：
```yaml
entrances:
- name: yourapp
  port: 80
  host: yourapp
  title: Your App Title
  icon: https://app.cdn.olares.com/appstore/your-app/icon.png
  openMethod: window
```

### 2. 模板限制

- **镜像字段必须硬编码** - 不能在 `templates/deployment.yaml` 中使用 Helm 模板占位符如 `{{ .Values.image.tag }}`
- **必须设置所有容器资源** - 必须为内存和 CPU 定义 `requests` 和 `limits`

### 3. 目录命名规则

- 只允许的字符：`a-z`, `A-Z`, `0-9`, 空格, `. , ! ? ; : ' " -`
- 最大长度：30 个字符
- **不允许使用连字符 (`-`)** - 使用下划线 (`_`) 代替

### 4. PR 提交规则

- **一个 PR = 一个目录** - 不能在单个 PR 中修改多个应用目录
- PR 标题必须与目录名完全一致

## 📖 参考资料

- [Olares 官方文档](https://docs.olares.cn/zh/developer/develop/submit/)
- [官方应用仓库](https://github.com/beclab/apps)
- [OAC 打包指南](https://docs.olares.cn/zh/developer/develop/package/chart.html)

## 🤝 贡献

发现了新的 GitBot 错误？请帮助改进这个技能：

1. Fork 本仓库
2. 将新的错误和解决方案添加到 `references/gitbot-errors.md`
3. 提交 Pull Request

## 📦 在不同 AI 助手中使用此技能

这是一个**通用技能包**，任何 AI 助手都可以使用。方法如下：

### 对于 WorkBuddy 用户

```bash
# 通过 WorkBuddy 安装
/skills
# 搜索 "olares-app-submitter" 并安装
```

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

## 📝 许可证

MIT 许可证 - 欢迎自由使用和修改此技能。

---

## 📊 Actual Test Results / 实际测试结果

**PR Submitted**: [#2185](https://github.com/beclab/apps/pull/2185) (Merged ✅)

**Errors Discovered**: 10 errors found during testing, all documented in `references/gitbot-errors.md`

**Key Value**: This skill saves developers hours of trial-and-error by providing real-world solutions to GitBot validation errors that are not documented in official Olares docs.

---

**提交成功的 PR**: [#2185](https://github.com/beclab/apps/pull/2185)（已合并 ✅）

**发现的错误**: 测试过程中发现 10 个错误，全部记录在 `references/gitbot-errors.md` 中

**核心价值**: 本技能通过提供官方 Olares 文档中未说明的 GitBot 校验错误的实际解决方案，帮助开发者节省数小时的试错时间。
