# GitBot 常见错误及解决方案

本文档列出 Olares 应用提交过程中 GitBot 常见的校验错误及解决方案。

## 目录

1. [PR 标题格式错误](#1-pr-标题格式错误)
2. [版本号格式错误](#2-版本号格式错误)
3. [版本号未递增](#3-版本号未递增)
4. [Chart.yaml 和 OlaresManifest.yaml 版本号不一致](#4-chartyaml-和-olaresmanifestyaml-版本号不一致)
5. [owners 文件格式错误](#5-owners-文件格式错误)
6. [owners 文件中不包含提交者用户名](#6-owners-文件中不包含提交者用户名)
7. [资产链接失效或不符合规格](#7-资产链接失效或不符合规格)
8. [OAC 目录结构不完整](#8-oac-目录结构不完整)
9. [存在安全漏洞或恶意代码](#9-存在安全漏洞或恶意代码)
10. [PR 类型与内容不匹配](#10-pr-类型与内容不匹配)
11. [同时存在多个打开的 PR](#11-同时存在多个打开的-pr)
12. [PR 被 GitBot 自动关闭](#12-pr-被-gitbot-自动关闭)
13. [文件夹命名不符合规范](#13-文件夹命名不符合规范)
14. [PR 标题中的应用名称与目录名不匹配](#14-pr-标题中的应用名称与目录名不匹配)
15. [一个 PR 包含多个目录的修改](#15-一个-pr-包含多个目录的修改)
16. [缺少 values.yaml 文件](#16-缺少-valuesyaml-文件)
17. [OlaresManifest.yaml 缺少必需字段](#17-olaresmanifestyaml-缺少必需字段)
18. [templates 中的镜像字段包含模板占位符](#18-templates-中的镜像字段包含模板占位符)
19. [templates 引用了不存在的 Values 字段](#19-templates-引用了不存在的-values-字段)
20. [容器未设置资源限制](#20-容器未设置资源限制)

---

## 1. PR 标题格式错误

**错误信息**：
```
PR title format is invalid. Expected format: [PR类型][应用目录名][版本号] 标题
```

**原因**：
- PR 标题不符合命名规范
- 包含了多个 PR 类型或应用目录名
- 版本号格式不正确
- 标题包含特殊字符

**解决方案**：
1. 检查 PR 标题格式是否为：`[PR类型][应用目录名][版本号] 标题`
2. 确保只包含 1 个 PR 类型、1 个应用目录名、1 个版本号
3. 版本号必须符合语义化版本规范（如 `1.0.0`）
4. 标题不得包含特殊字符（如 `/ \ : * ? " < > |`）
5. 修改后，关闭当前 PR，重新创建符合规范的 PR

**示例**：
```
✅ 正确：[NEW][my-app][1.0.0] 提交我的应用
❌ 错误：[NEW] 提交我的应用（缺少应用目录名和版本号）
❌ 错误：[NEW][my-app] 提交我的应用（缺少版本号）
❌ 错误：[NEW][my-app][1.0.0][extra] 提交我的应用（包含多余字段）
```

## 2. 版本号格式错误

**错误信息**：
```
Version number format is invalid. Must follow SemVer 2.0.0 specification.
```

**原因**：
- 版本号不符合语义化版本规范（SemVer 2.0.0）
- 版本号包含非法字符或格式不正确

**解决方案**：
1. 确保版本号格式为：`主版本.次版本.修订号`（如 `1.0.0`、`2.1.3`）
2. 每个部分只能是数字，不能有前导零（如 `1.0.0` 正确，`1.0.01` 错误）
3. 修改 `Chart.yaml` 和 `OlaresManifest.yaml` 中的版本号，确保两者完全一致
4. 提交新的 commit 触发 GitBot 重新检查

**示例**：
```
✅ 正确：1.0.0、2.1.3、10.20.30
❌ 错误：v1.0.0（不能有前缀 v）
❌ 错误：1.0（缺少修订号）
❌ 错误：1.0.0.1（版本号有四段）
❌ 错误：1.0.01（修订号有前导零）
```

## 3. 版本号未递增

**错误信息**：
```
Version number must be incremented. Current version X.Y.Z is not higher than existing version A.B.C.
```

**原因**：
- 新 PR 中的版本号不高于仓库中已有版本号
- 更新应用时忘记递增版本号

**解决方案**：
1. 查看 `beclab/apps` 仓库中你的应用目录，确认当前版本号
2. 递增版本号（根据修改类型选择递增主版本、次版本或修订号）
   - 不兼容的 API 修改 → 递增主版本号
   - 向下兼容的功能性新增 → 递增次版本号
   - 向下兼容的问题修正 → 递增修订号
3. 修改 `Chart.yaml` 和 `OlaresManifest.yaml` 中的版本号，确保两者完全一致
4. 提交新的 commit 触发 GitBot 重新检查

**注意**：Olares 市场不支持版本回滚，应用问题必须通过提交更高版本修复。

## 4. Chart.yaml 和 OlaresManifest.yaml 版本号不一致

**错误信息**：
```
Version mismatch between Chart.yaml and OlaresManifest.yaml.
```

**原因**：
- `Chart.yaml` 的 `version` 字段与 `OlaresManifest.yaml` 的 `metadata.version` 字段不一致
- 只修改了其中一个文件的版本号，忘记修改另一个

**解决方案**：
1. 打开 `Chart.yaml`，检查 `version` 字段
2. 打开 `OlaresManifest.yaml`，检查 `metadata.version` 字段
3. 确保两个字段的值**完全一致**（包括格式）
4. 提交新的 commit 触发 GitBot 重新检查

**示例**：
```yaml
# Chart.yaml
version: 1.0.1

# OlaresManifest.yaml
metadata:
  version: 1.0.1  # 必须与 Chart.yaml 的 version 完全一致
```

## 5. owners 文件格式错误

**错误信息**：
```
Invalid owners file format.
```

**原因**：
- `owners` 文件不存在
- `owners` 文件格式不正确（如包含空格、特殊字符等）
- `owners` 文件为空

**解决方案**：
1. 确保 `owners` 文件存在
2. 每行一个 GitHub 用户名，不能有空格或特殊字符
3. 确保 `owners` 文件至少包含一个用户名
4. 提交新的 commit 触发 GitBot 重新检查

**示例**：
```
# ✅ 正确格式
your-github-username
co-maintainer1
co-maintainer2

# ❌ 错误格式
your-github-username  # 后面有空格
co-maintainer1
```

## 6. owners 文件中不包含提交者用户名

**错误信息**：
```
PR submitter is not in the owners list.
```

**原因**：
- 修改已有应用的 PR 提交者不在 `owners` 文件中
- 新应用的 `owners` 文件中不包含提交者用户名

**解决方案**：
1. 打开 `owners` 文件
2. 添加你的 GitHub 用户名（每行一个）
3. 如果是修改已有应用，联系现有所有者将你的用户名添加到 `owners` 文件
4. 提交新的 commit 触发 GitBot 重新检查

**注意**：此限制是为了防止未授权人员修改应用。

## 7. 资产链接失效或不符合规格

**错误信息**：
```
Invalid asset URL or asset does not meet specifications.
```

**原因**：
- 应用图标、宣传截图等资产链接失效（返回 404 或其他错误）
- 资产格式不符合要求（如图标使用了 JPEG 格式）
- 资产大小超过限制（如图标超过 512KB）
- 资产尺寸不符合要求（如图标不是 256x256px）

**解决方案**：
1. 检查 `OlaresManifest.yaml` 中的所有资产链接（`metadata.icon`、`metadata.promoteImage`、`metadata.featuredImage`）
2. 在浏览器中打开每个链接，确保可以正常访问
3. 检查资产格式、大小、尺寸是否符合规范（参考 `references/oac-specification.md` 中的应用展示资产规格）
4. 如果资产不符合规格，重新生成符合要求的资产，并更新链接
5. 提交新的 commit 触发 GitBot 重新检查

**资产规格快速参考**：
| 资产类型 | 格式 | 大小 | 尺寸 |
|----------|------|------|------|
| 应用图标 | PNG/WEBP | ≤512KB | 256x256px |
| 宣传截图 | JPEG/PNG/WEBP | ≤8MB/张 | 1440x900px |
| 精选图 | JPEG/PNG/WEBP | ≤8MB | 1440x900px |

## 8. OAC 目录结构不完整

**错误信息**：
```
Missing required files in OAC directory.
```

**原因**：
- OAC 目录中缺少必需文件（`Chart.yaml`、`OlaresManifest.yaml`、`owners`）
- 文件命名错误（如 `chart.yaml` 而不是 `Chart.yaml`）

**解决方案**：
1. 确保 OAC 目录中包含以下必需文件：
   - `Chart.yaml`（注意大小写）
   - `OlaresManifest.yaml`（注意大小写）
   - `owners`
2. 检查文件名是否完全正确（区分大小写）
3. 提交新的 commit 触发 GitBot 重新检查

## 9. 存在安全漏洞或恶意代码

**错误信息**：
```
Security vulnerability detected or malicious code found.
```

**原因**：
- 应用包含已知安全漏洞
- 应用包含恶意代码或可疑行为
- 应用依赖的容器镜像包含安全漏洞

**解决方案**：
1. 检查应用代码，确保不包含恶意代码或可疑行为
2. 更新应用依赖，修复已知安全漏洞
3. 使用官方或受信任的基础镜像构建容器镜像
4. 如果确认误报，可以在 PR 中回复 GitBot，说明情况
5. 提交新的 commit 触发 GitBot 重新检查

## 10. PR 类型与内容不匹配

**错误信息**：
```
PR type does not match content. Expected UPDATE but found NEW.
```

**原因**：
- PR 类型与实际内容不匹配（如应用已存在，但使用了 `NEW` 类型）
- PR 类型与 OAC 目录中的控制文件不匹配（如 `NEW` 类型 PR 包含了 `.suspend` 文件）

**解决方案**：
1. 检查应用是否已存在于 `beclab/apps` 仓库
   - 如果不存在，使用 `NEW` 类型
   - 如果存在，使用 `UPDATE`、`SUSPEND` 或 `REMOVE` 类型
2. 检查 OAC 目录中是否包含错误的控制文件：
   - `NEW` 类型 PR：不得包含 `.suspend` 或 `.remove` 文件
   - `SUSPEND` 类型 PR：必须包含 `.suspend` 文件，不得包含 `.remove` 文件
   - `REMOVE` 类型 PR：必须包含 `.remove` 文件，且目录中无其他文件
3. 关闭当前 PR，重新创建符合规范的 PR

## 11. 同时存在多个打开的 PR

**错误信息**：
```
Multiple open PRs found for the same app directory. Please close all but one.
```

**原因**：
- 同一个应用目录同时存在多个打开的 Draft/正式 PR

**解决方案**：
1. 访问你的 Fork 仓库的 Pull Requests 页面
2. 关闭所有针对同一应用目录的 PR，只保留一个
3. GitBot 会自动重新检查保留的 PR

## 12. PR 被 GitBot 自动关闭

**现象**：
- PR 被 GitBot 自动关闭
- PR 状态标签显示为 `closed`

**原因**：
- 存在不可修复的错误（如 PR 标题格式永远不正确、应用包含恶意代码等）
- GitBot 判定无法自动合并

**解决方案**：
1. **不得重新打开此 PR**
2. 阅读 GitBot 的评论，了解具体原因
3. 修改 OAC 包内容，修复所有问题
4. 创建新的 PR（使用正确的标题格式）
5. 等待 GitBot 重新检查

**注意**：PR 被关闭后，不得尝试重新打开，必须创建新 PR。

## 13. 文件夹命名不符合规范

**错误信息**：
```
invalid folder name: '.../test-hello-world' must match pattern '^[w\s.,!?;:'"-]{1,30}$'
```

**原因**：
- OAC 目录名包含不允许的字符（如 `-` 连字符）
- 目录名长度超过 30 个字符
- 目录名包含空格或其他特殊字符

**解决方案**：
1. 重命名 OAC 目录，只允许使用以下字符：
   - 字母数字：`a-z`, `A-Z`, `0-9`
   - 空格：`\s`
   - 标点符号：`. , ! ? ; : ' " -`
2. 目录名长度必须在 1-30 个字符之间
3. 推荐使用下划线 `_` 代替连字符 `-`

**示例**：
```
❌ 错误：test-hello-world（包含连字符）
❌ 错误：my app（包含空格）
✅ 正确：test_hello_world
✅ 正确：skilltestapp
✅ 正确：myapp_v1
```

## 14. PR 标题中的应用名称与目录名不匹配

**错误信息**：
```
Authorization exceptions. [open /tmp/git.../test-hello-world/owners: no such file or directory]
```

**原因**：
- PR 标题中指定的应用目录名与实际提交的目录名不一致
- 修改了目录名但忘记更新 PR 标题

**解决方案**：
1. 检查 PR 标题中的应用目录名（格式：`[类型][目录名][版本]`）
2. 确保与 Fork 仓库中的实际目录名完全一致
3. 修改 PR 标题或重命名目录，确保两者一致
4. 提交新的 commit 触发 GitBot 重新检查

**示例**：
```
PR 标题：[NEW][skilltestapp][1.0.0] 提交测试应用
实际目录：skilltestapp/  ✅ 匹配

PR 标题：[NEW][test-hello-world][1.0.0] 提交测试应用
实际目录：skilltestapp/  ❌ 不匹配
```

## 15. 一个 PR 包含多个目录的修改

**错误信息**：
```
Invalid change. Change in multiple directory detected
```

**原因**：
- 一个 PR 中提交了多个应用的修改
- 一个 PR 包含了多个 OAC 目录的变更

**解决方案**：
1. **一个 PR 只能修改一个应用目录**
2. 如果有多个应用需要提交，为每个应用创建单独的 PR
3. 关闭当前 PR，重新创建只包含一个目录修改的 PR

**示例**：
```
❌ 错误：一个 PR 同时包含 app1/ 和 app2/ 的修改
✅ 正确：PR #1 只包含 app1/ 的修改
✅ 正确：PR #2 只包含 app2/ 的修改
```

## 16. 缺少 values.yaml 文件

**错误信息**：
```
missing values.yaml in folder
```

**原因**：
- OAC 目录中缺少 `values.yaml` 文件
- `values.yaml` 是 Helm Chart 的必需文件

**解决方案**：
1. 在 OAC 目录中创建 `values.yaml` 文件
2. 至少包含基本的结构（即使是空配置）
3. 参考已有应用的 `values.yaml` 作为模板

**最小示例**：
```yaml
# values.yaml 最小配置
replicaCount: 1

image:
  repository: nginx
  pullPolicy: IfNotPresent
  tag: "1.25"

service:
  type: ClusterIP
  port: 80

resources: {}
```

## 17. OlaresManifest.yaml 缺少必需字段

**错误信息**：
```
"validation failed: Metadata.Icon","msg": "invalid parameter: ;icon must satisfy the expr: len($)>0"
"validation failed: Entrances","msg": "invalid parameter: [];entrances must satisfy the expr: len($)>0 && len($)<=10"
```

**原因**：
- `OlaresManifest.yaml` 缺少 `metadata.icon` 字段（GitBot 校验需要，但官方文档未明确说明）
- `OlaresManifest.yaml` 缺少 `entrances` 字段（GitBot 校验需要，但官方文档未明确说明）
- 这些字段在官方文档的 OlaresManifest.yaml 模板中不存在，是 GitBot 的隐藏要求

**解决方案**：
1. 在 `OlaresManifest.yaml` 中添加 `metadata.icon` 字段：
   ```yaml
   metadata:
     name: your-app
     description: Your app description
     icon: https://app.cdn.olares.com/appstore/your-app/icon.png  # 必须添加
     # ... 其他字段
   ```

2. 在 `OlaresManifest.yaml` 中添加 `entrances` 字段（定义应用入口）：
   ```yaml
   entrances:
   - name: yourapp
     port: 80
     host: yourapp
     title: Your App Title
     icon: https://app.cdn.olares.com/appstore/your-app/icon.png
     openMethod: window
   ```

3. 确保 `metadata.icon` 的 URL 可访问（返回 200 状态码）
4. 提交新的 commit 触发 GitBot 重新检查

**重要提示**：这些字段在 Olares 官方文档的模板中不存在，但是 GitBot 校验的隐藏必需字段。必须添加才能通过校验。

## 18. templates 中的镜像字段包含模板占位符

**错误信息**：
```
templates/deployment.yaml line 29: image field must not contain template placeholders
```

**原因**：
- `templates/deployment.yaml` 中的 `image` 字段使用了 Helm 模板占位符（如 `{{ .Values.image.tag }}`）
- GitBot 要求镜像字段必须是硬编码的具体镜像地址

**解决方案**：
1. 打开 `templates/deployment.yaml`
2. 将 `image` 字段从模板占位符改为硬编码的具体镜像地址
3. 如果需要在 values.yaml 中配置镜像，可以在 containers 环境变量中使用，但 `image` 字段必须硬编码

**示例**：
```yaml
# ❌ 错误：包含模板占位符
containers:
- name: {{ .Chart.Name }}
  image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
  # GitBot 会报错

# ✅ 正确：硬编码镜像地址
containers:
- name: {{ .Chart.Name }}
  image: "nginx:1.25"
  # 必须通过校验
```

## 19. templates 引用了不存在的 Values 字段

**错误信息**：
```
template: ... at <.Values.autoscaling.enabled>: nil pointer evaluating interface {}.enabled
```

**原因**：
- `templates/` 中的文件引用了 `values.yaml` 中不存在的字段
- 使用了标准的 Helm 模板但 `values.yaml` 中没有定义对应的配置项
- 从 Helm 官方模板复制代码时，忘记在 `values.yaml` 中添加对应的配置

**解决方案**：
1. 检查错误信息中提到的字段（如 `.Values.autoscaling.enabled`）
2. 在 `values.yaml` 中添加对应的配置项，或
3. 删除 `templates/` 中对这些字段的引用

**示例**：
```yaml
# values.yaml 中添加缺失的字段
autoscaling:
  enabled: false
  minReplicas: 1
  maxReplicas: 100
  targetCPUUtilizationPercentage: 80
```

或者：
```yaml
# templates/deployment.yaml 中删除对 autoscaling 的引用
# ❌ 删除以下代码
{{- if .Values.autoscaling.enabled }}
...
{{- end }}
```

## 20. 容器未设置资源限制

**错误信息**：
```
container: skilltestapp must set memory request/cpu request/memory limit/cpu limit
```

**原因**：
- `templates/deployment.yaml` 中的容器未设置资源请求（requests）和限制（limits）
- GitBot 要求所有容器必须明确设置内存和 CPU 的 requests/limits

**解决方案**：
1. 打开 `templates/deployment.yaml`
2. 在 `containers` 部分添加 `resources` 字段
3. 必须同时设置 `requests`（资源请求）和 `limits`（资源限制）
4. 值必须与 `OlaresManifest.yaml` 中的 `requiredMemory`、`limitedMemory`、`requiredCpu`、`limitedCpu` 一致或更小

**示例**：
```yaml
# templates/deployment.yaml
containers:
- name: {{ .Chart.Name }}
  image: "nginx:1.25"
  resources:
    requests:
      memory: "128Mi"
      cpu: "100m"
    limits:
      memory: "256Mi"
      cpu: "500m"
```

**对应关系**：
```yaml
# OlaresManifest.yaml
spec:
  requiredMemory: 128Mi    # 对应 resources.requests.memory
  limitedMemory: 256Mi     # 对应 resources.limits.memory
  requiredCpu: 0.1         # 对应 resources.requests.cpu (100m = 0.1)
  limitedCpu: 0.5          # 对应 resources.limits.cpu (500m = 0.5)
```

---

## 通用排查建议

1. **仔细阅读 GitBot 评论**：GitBot 会在 PR 中添加评论，说明具体错误原因和修复建议
2. **检查拼写和格式**：YAML 文件对格式要求严格，确保缩进、冒号后空格等格式正确
3. **使用 YAML 校验工具**：使用在线 YAML 校验工具检查 `Chart.yaml` 和 `OlaresManifest.yaml` 格式是否正确
4. **本地测试**：在提交 PR 前，本地测试应用是否能在 Olares OS 中正常运行
5. **参考已有应用**：查看 `beclab/apps` 仓库中其他应用的 OAC 包，学习正确格式

## 参考资料

- Olares 官方提交指南：`https://docs.olares.cn/zh/developer/develop/submit/`
- 官方应用仓库：`https://github.com/beclab/apps`
- OAC 打包指南：`https://docs.olares.cn/zh/developer/develop/package/chart.html`
- YAML 在线校验工具：`https://www.yamllint.com/`
