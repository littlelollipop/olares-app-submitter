#!/usr/bin/env python3
"""
OAC (Olares Application Chart) 包验证脚本
用于检查 OAC 包是否符合 Olares 应用市场规范

跨平台兼容：仅使用 Python 标准库
"""

import os
import sys
import re
from pathlib import Path

def print_error(msg):
    """打印错误信息"""
    print(f"❌ 错误: {msg}")

def print_warning(msg):
    """打印警告信息"""
    print(f"⚠️  警告: {msg}")

def print_success(msg):
    """打印成功信息"""
    print(f"✅ {msg}")

def print_info(msg):
    """打印信息"""
    print(f"ℹ️  {msg}")

def check_semver(version):
    """
    检查版本号是否符合语义化版本规范 (SemVer 2.0.0)
    返回: (bool, str) - (是否符合规范, 错误信息)
    """
    # SemVer 正则表达式
    pattern = r'^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$'
    
    if not re.match(pattern, version):
        return False, f"版本号 {version} 不符合语义化版本规范 (SemVer 2.0.0)"
    
    # 检查是否有前导零
    parts = version.split('-')[0].split('+')[0].split('.')
    for part in parts:
        if len(part) > 1 and part.startswith('0'):
            return False, f"版本号 {version} 包含前导零 (如 01, 02 等)"
    
    return True, ""

def validate_chart_yaml(chart_file):
    """
    验证 Chart.yaml 文件
    返回: (bool, dict) - (是否通过验证, 解析出的配置)
    """
    print_info(f"检查 {chart_file}...")
    
    if not os.path.exists(chart_file):
        print_error(f"文件不存在: {chart_file}")
        return False, {}
    
    # 读取文件内容（简单解析，不依赖第三方库）
    try:
        with open(chart_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 简单解析 YAML（仅提取必需字段）
        config = {}
        
        # 提取 apiVersion
        match = re.search(r'^apiVersion:\s*(.+)$', content, re.MULTILINE)
        if match:
            config['apiVersion'] = match.group(1).strip()
        
        # 提取 name
        match = re.search(r'^name:\s*(.+)$', content, re.MULTILINE)
        if match:
            config['name'] = match.group(1).strip()
        
        # 提取 version
        match = re.search(r'^version:\s*(.+)$', content, re.MULTILINE)
        if match:
            config['version'] = match.group(1).strip()
        
        # 提取 description
        match = re.search(r'^description:\s*(.+)$', content, re.MULTILINE)
        if match:
            config['description'] = match.group(1).strip()
        
        # 提取 type
        match = re.search(r'^type:\s*(.+)$', content, re.MULTILINE)
        if match:
            config['type'] = match.group(1).strip()
        
        # 验证必需字段
        required_fields = ['apiVersion', 'name', 'version', 'description', 'type']
        missing_fields = [field for field in required_fields if field not in config]
        
        if missing_fields:
            print_error(f"缺少必需字段: {', '.join(missing_fields)}")
            return False, config
        
        # 验证 apiVersion
        if config['apiVersion'] != 'v2':
            print_error(f"apiVersion 必须为 'v2'，当前为 '{config['apiVersion']}'")
            return False, config
        
        # 验证 type
        if config['type'] != 'application':
            print_error(f"type 必须为 'application'，当前为 '{config['type']}'")
            return False, config
        
        # 验证版本号格式
        is_valid, error_msg = check_semver(config['version'])
        if not is_valid:
            print_error(error_msg)
            return False, config
        
        print_success(f"Chart.yaml 验证通过 (version: {config['version']})")
        return True, config
        
    except Exception as e:
        print_error(f"解析文件时出错: {e}")
        return False, {}

def validate_olares_manifest(manifest_file):
    """
    验证 OlaresManifest.yaml 文件
    返回: (bool, dict) - (是否通过验证, 解析出的配置)
    """
    print_info(f"检查 {manifest_file}...")
    
    if not os.path.exists(manifest_file):
        print_error(f"文件不存在: {manifest_file}")
        return False, {}
    
    # 读取文件内容（简单解析，不依赖第三方库）
    try:
        with open(manifest_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 简单解析 YAML（仅提取必需字段）
        config = {}
        
        # 提取 metadata.name
        match = re.search(r'name:\s*(.+)$', content, re.MULTILINE)
        if match:
            config['name'] = match.group(1).strip()
        
        # 提取 metadata.version
        match = re.search(r'version:\s*(.+)$', content, re.MULTILINE)
        if match:
            config['version'] = match.group(1).strip()
        
        # 提取 metadata.title.zh
        match = re.search(r'zh:\s*(.+)$', content, re.MULTILINE)
        if match:
            if 'title' not in config:
                config['title'] = {}
            config['title']['zh'] = match.group(1).strip()
        
        # 提取 metadata.title.en
        match = re.search(r'en:\s*(.+)$', content, re.MULTILINE)
        if match:
            if 'title' not in config:
                config['title'] = {}
            config['title']['en'] = match.group(1).strip()
        
        # 提取 metadata.icon
        match = re.search(r'icon:\s*["\']?(https?://\S+)["\']?', content, re.MULTILINE)
        if match:
            config['icon'] = match.group(1).strip()
        
        # 验证必需字段（简化版，实际应该更严格）
        if 'name' not in config:
            print_error("缺少必需字段: metadata.name")
            return False, config
        
        if 'version' not in config:
            print_error("缺少必需字段: metadata.version")
            return False, config
        
        # 验证版本号格式
        is_valid, error_msg = check_semver(config['version'])
        if not is_valid:
            print_error(error_msg)
            return False, config
        
        # 验证图标链接
        if 'icon' not in config:
            print_warning("未找到 metadata.icon 字段，应用图标是必需项")
        else:
            if not config['icon'].startswith('http'):
                print_error(f"metadata.icon 必须是有效的 URL: {config['icon']}")
                return False, config
        
        print_success(f"OlaresManifest.yaml 验证通过 (version: {config['version']})")
        return True, config
        
    except Exception as e:
        print_error(f"解析文件时出错: {e}")
        return False, {}

def validate_owners_file(owners_file):
    """
    验证 owners 文件
    返回: bool - 是否通过验证
    """
    print_info(f"检查 {owners_file}...")
    
    if not os.path.exists(owners_file):
        print_error(f"文件不存在: {owners_file}")
        return False
    
    try:
        with open(owners_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 检查文件是否为空
        if len(lines) == 0:
            print_error("owners 文件为空，必须至少包含一个 GitHub 用户名")
            return False
        
        # 检查每一行
        for i, line in enumerate(lines, 1):
            line = line.strip()
            
            # 跳过空行
            if not line:
                continue
            
            # 检查是否包含空格
            if ' ' in line:
                print_error(f"第 {i} 行包含空格: '{line}'")
                return False
            
            # 检查是否为有效的 GitHub 用户名格式（简化检查）
            if not re.match(r'^[a-zA-Z\d](?:[a-zA-Z\d]|-(?=[a-zA-Z\d])){0,38}$', line):
                print_warning(f"第 {i} 行可能不是有效的 GitHub 用户名: '{line}'")
        
        print_success("owners 文件验证通过")
        return True
        
    except Exception as e:
        print_error(f"解析文件时出错: {e}")
        return False

def validate_oac_directory(oac_dir):
    """
    验证 OAC 目录
    返回: bool - 是否通过所有验证
    """
    print_info(f"开始验证 OAC 目录: {oac_dir}")
    print("-" * 50)
    
    # 检查目录是否存在
    if not os.path.isdir(oac_dir):
        print_error(f"目录不存在: {oac_dir}")
        return False
    
    # 检查必需文件
    chart_file = os.path.join(oac_dir, 'Chart.yaml')
    manifest_file = os.path.join(oac_dir, 'OlaresManifest.yaml')
    owners_file = os.path.join(oac_dir, 'owners')
    
    # 验证 Chart.yaml
    chart_valid, chart_config = validate_chart_yaml(chart_file)
    print("-" * 50)
    
    # 验证 OlaresManifest.yaml
    manifest_valid, manifest_config = validate_olares_manifest(manifest_file)
    print("-" * 50)
    
    # 验证 owners 文件
    owners_valid = validate_owners_file(owners_file)
    print("-" * 50)
    
    # 检查版本号一致性
    if chart_valid and manifest_valid:
        chart_version = chart_config.get('version', '')
        manifest_version = manifest_config.get('version', '')
        
        if chart_version != manifest_version:
            print_error(f"版本号不一致: Chart.yaml={chart_version}, OlaresManifest.yaml={manifest_version}")
            print("-" * 50)
            return False
        else:
            print_success(f"版本号一致: {chart_version}")
            print("-" * 50)
    
    # 总结
    if chart_valid and manifest_valid and owners_valid:
        print_success("🎉 所有检查通过！OAC 包符合规范")
        return True
    else:
        print_error("❌ 验证失败，请修复上述错误后重新验证")
        return False

def main():
    """主函数"""
    if len(sys.argv) != 2:
        print("用法: python3 validate_oac.py <OAC目录路径>")
        print("示例: python3 validate_oac.py ./my-app")
        sys.exit(1)
    
    oac_dir = sys.argv[1]
    is_valid = validate_oac_directory(oac_dir)
    
    if is_valid:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
