#!/bin/bash

# 当前版本号: 1.1

# 说明:
# 1. 版本之间相互独立，高版本不一定兼容低版本

## 版本列表
## 1.0 初始版本
## 1.1 新增功能: 可以指定 commit id 触发构建

usage()
{
	echo "Usage: '<>' 中的选项为可选项"
	echo "  $0 <-s jenkins-server> [-u user-name] [-t api-token] [-j job-name] [-b gitlab-target-branch] <-c commit-id> <-i issue-type>"
    echo "  $0 [-u user-name] [-t api-token] [-j job-name] [-b gitlab-target-branch] <-i issue-type>"
    echo "  $0 [-u user-name] [-t api-token] [-j job-name] [-b gitlab-target-branch]"
	echo "Description:"
    echo " <jenkins-server>: jenkins 服务器名称，默认为 https://ci.jenkins.net"
    echo " [user-name]: 用户名称(英文字符)"
    echo " [api-token]: 用户登录认证字符串"
    echo " [job-name]: 要触发的流水线名称"
    echo " [gitlab-target-branch]: 目标分支名称"
    echo " <commit-id>: 目标分支上的某个提交ID, 要求至少前 8 位，默认为最新"
    echo " <issue-type>: 发版类型(devel 或 production)，默认为 devel"
	exit -1
}

# Jenkins 服务器地址
JENKINS_SERVER="https://ci.jenkins.net"
# 用户名 和 API Token
USERNAME=""
TOKEN=""
# 要触发的流水线名称
JOB_NAME=""
# 目标分支名称
TargetBranch=""
# 目标分支上的 COMMIT ID
COMMIT_ID=""
# 环境变量
IssueType="devel"

while getopts 's:u:t:j:b:c:i:' OPT
do
	case $OPT in
        s) JENKINS_SERVER="$OPTARG";;
        u) USERNAME="$OPTARG";;
		t) TOKEN="$OPTARG";;
		j) JOB_NAME="$OPTARG";;
		b) TargetBranch="$OPTARG";;
        c) COMMIT_ID="$OPTARG";;
        i) IssueType="$OPTARG";;
		h) usage;;
		?) usage;;
	esac
done

if [ ! -n "${USERNAME}" ]; then echo "error: <user-name> is null"; usage; exit -1; fi
if [ ! -n "${TOKEN}" ]; then echo "error: <api-token> is null"; usage; exit -1; fi
if [ ! -n "${JOB_NAME}" ]; then echo "error: <job-name> is null"; usage; exit -1; fi
if [ ! -n "${TargetBranch}" ]; then echo "error: <gitlab-target-branch> is null"; usage; exit -1; fi
if [ "${IssueType}" != "devel" -a "${IssueType}" != "production" ]; then
    echo "error: <issue-type> must be 'devel' or 'production'"
    usage
    exit -1
fi

# 触发
curl -X POST \
    -u ${USERNAME}:${TOKEN} \
    -d "targetBranch=${TargetBranch}" \
    -d "commitID=${COMMIT_ID}" \
    -d "issueType=${IssueType}" \
    -d "userName=${USERNAME}" \
    ${JENKINS_SERVER}/job/${JOB_NAME}/buildWithParameters

echo "========== over =========="
exit 0
