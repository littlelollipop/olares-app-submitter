# OAC（Olares Application Chart）规范

OAC 是 Olares 官方定义的应用打包格式，基于 Helm Chart 扩展而来。

## 目录结构

标准的 OAC 目录结构如下：

```
your-app/
├── Chart.yaml          # Helm 标准配置文件（必需）
├── OlaresManifest.yaml # Olares 扩展元数据配置（必需）
├── owners              # 应用所有者 GitHub 用户名列表（必需）
├── .suspend            # （可选）暂停应用市场分发标记
├── .remove             # （可选）移除应用市场展示标记
├── values.yaml         # Helm 标准默认值配置（可选）
├── templates/          # Helm 标准模板目录（可选）
├── charts/             # Helm 标准依赖目录（可选）
└── README.md           # 应用说明文档（推荐）
```

## Chart.yaml 规范

`Chart.yaml` 是 Helm Chart 的标准配置文件，必须包含以下字段：

```yaml
apiVersion: v2                  # Helm API 版本，固定为 v2
name: your-app                  # 应用名称，与目录名一致
version: 1.0.0                 # 版本号，必须符合语义化版本规范
description: 应用描述信息        # 应用简短描述
type: application               # 固定为 application
```

**重要要求**：
- `version` 字段必须与 `OlaresManifest.yaml` 中的 `metadata.version` 字段**完全一致**
- 版本号必须符合语义化版本规范（SemVer 2.0.0）：`主版本.次版本.修订号`（如 `1.0.0`、`2.1.3`）
- 每次提交 PR 时，新版本号必须高于仓库中已有的版本号
- Olares 市场不支持版本回滚

## OlaresManifest.yaml 规范

`OlaresManifest.yaml` 是 OAC 扩展的元数据配置文件，包含 Olares 特有的配置项。

### 基本结构

```yaml
metadata:
  name: your-app                # 应用名称，与 Chart.yaml 的 name 一致
  version: 1.0.0               # 版本号，必须与 Chart.yaml 的 version 一致
  title:
    zh: 应用中文名称
    en: App English Name
  description:
    zh: 应用中文描述
    en: App English description
  categories:                   # 应用分类，至少选择一个
    - "AI"
    - "工具"
  tags:                         # 应用标签，用于搜索
    - "ai"
    - "tool"
  promoteImage:                 # 宣传图资产链接列表
    - "https://example.com/screenshot1.png"
  featuredImage: "https://example.com/featured.png"  # 精选图链接（可选）
  icon: "https://example.com/icon.png"                # 应用图标链接（必需）
  source: "https://github.com/yourname/your-app"     # 应用源码地址
  homepage: "https://yourapp.com"                    # 应用主页（可选）
  maintainers:                  # 维护者信息
    - name: Your Name
      email: your.email@example.com
spec:
  # 其他 Olares 特定配置...
```

### 字段详细说明

| 字段路径 | 类型 | 必需 | 说明 |
|-----------|------|------|------|
| `metadata.name` | string | 是 | 应用名称，与 Chart.yaml 的 name 一致 |
| `metadata.version` | string | 是 | 版本号，必须与 Chart.yaml 的 version 一致 |
| `metadata.title.zh` | string | 是 | 应用中文名称 |
| `metadata.title.en` | string | 是 | 应用英文名称 |
| `metadata.description.zh` | string | 是 | 应用中文描述 |
| `metadata.description.en` | string | 是 | 应用英文描述 |
| `metadata.categories` | list | 是 | 应用分类，至少选择一个 |
| `metadata.tags` | list | 否 | 应用标签，用于搜索 |
| `metadata.promoteImage` | list | 是 | 宣传截图链接列表，最多 8 张 |
| `metadata.featuredImage` | string | 否 | 精选图链接，如需上精选位则必须填写 |
| `metadata.icon` | string | 是 | 应用图标链接 |
| `metadata.source` | string | 否 | 应用源码地址 |
| `metadata.homepage` | string | 否 | 应用主页 |
| `metadata.maintainers` | list | 否 | 维护者信息 |

### 应用分类（categories）可选值

- `"AI"`
- `"数据库"`
- `"开发工具"`
- `"文件管理"`
- `"媒体"`
- `"网络"`
- `"安全"`
- `"工具"`
- `"其他"`

## owners 文件规范

`owners` 文件包含应用所有者的 GitHub 用户名列表，每行一个用户名。

**示例**：
```
your-github-username
co-maintainer1
co-maintainer2
```

**重要要求**：
- 新应用提交者必须在 `owners` 列表中
- 修改已有应用的 PR 提交者必须在 `owners` 列表中
- 可以添加多个协作者作为共同所有者

## 应用展示资产规格

在 `OlaresManifest.yaml` 中填写的资产链接必须符合以下规格：

| 资产类型 | 格式要求 | 大小限制 | 尺寸要求 | 数量限制 |
|----------|----------|----------|----------|----------|
| 应用图标（`metadata.icon`） | PNG/WEBP | ≤512KB | 256x256px | 1 个（必填） |
| 宣传截图（`metadata.promoteImage`） | JPEG/PNG/WEBP | ≤8MB/张 | 1440x900px | 最多 8 张，建议至少提供 2 张 |
| 精选图（`metadata.featuredImage`） | JPEG/PNG/WEBP | ≤8MB | 1440x900px | 需上精选位则必须提供 1 张 |

**资产托管建议**：
- 可以使用 GitHub Releases 附件
- 可以使用图床服务（如图壳、SM.MS 等）
- 可以使用云存储服务（如 AWS S3、阿里云 OSS 等）
- **注意**：确保资产链接长期有效，避免失效导致应用审核失败

## 控制文件说明

### .suspend 文件

- 作用：标记应用暂停市场分发
- 效果：新用户无法在市场中找到并安装该应用，但已安装的用户可继续使用
- 使用场景：应用存在严重 Bug，需要暂停新用户安装，等待修复后重新上架
- PR 类型：仅 `SUSPEND` 类型 PR 可包含此文件

### .remove 文件

- 作用：标记应用从市场移除
- 效果：新用户无法在市场中找到并安装该应用，已安装的用户可继续使用
- **重要**：此操作不可逆转，OAC 名称无法复用
- PR 类型：仅 `REMOVE` 类型 PR 可包含此文件

## OAC 扩展字段说明

除了上述基本字段外，`OlaresManifest.yaml` 还支持以下扩展字段（可选）：

| 字段路径 | 类型 | 说明 |
|-----------|------|------|
| `spec.promoteImage` | list | 宣传图资产链接列表（与 `metadata.promoteImage` 功能相同，优先使用 `metadata.promoteImage`） |
| `spec.featuredImage` | string | 精选图链接（与 `metadata.featuredImage` 功能相同，优先使用 `metadata.featuredImage`） |
| `spec.require` | object | 应用运行要求（如最低 Olares 版本、硬件要求等） |
| `spec.dependencies` | list | 应用依赖的其他应用或服务 |

详细扩展字段说明参考官方文档：`https://docs.olares.cn/zh/developer/develop/package/extension.html`

## 版本管理规范

1. **语义化版本**：版本号必须符合 SemVer 2.0.0 规范（`主版本.次版本.修订号`）
   - 主版本号：不兼容的 API 修改
   - 次版本号：向下兼容的功能性新增
   - 修订号：向下兼容的问题修正

2. **版本号递增**：每次提交 PR 时，新版本号必须高于仓库中已有的版本号

3. **版本号一致性**：`Chart.yaml` 的 `version` 和 `OlaresManifest.yaml` 的 `metadata.version` 必须完全一致

4. **不支持版本回滚**：Olares 市场不支持版本回滚，如果应用存在问题，必须提交更高版本进行修复

## 参考资料

- Olares 官方 OAC 打包指南：`https://docs.olares.cn/zh/developer/develop/package/chart.html`
- OlaresManifest.yaml 配置指南：`https://docs.olares.cn/zh/developer/develop/package/manifest.html`
- OAC 扩展字段说明：`https://docs.olares.cn/zh/developer/develop/package/extension.html`
- 语义化版本规范：`https://semver.org/lang/zh-CN/`
