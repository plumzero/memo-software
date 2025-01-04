#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import jenkins
import datetime, time

class Job():
  def __init__(self, jenkins_master, jenkins_job, jenkins_user, jenkins_passwd, jenkins_server):
    '''
    jenkins_master ：master地址
    jenkins_job ：jenkins_job名字
    jenkins_user ：登陆账号
    jenkins_passwd ：登陆密码
    '''
    self.jenkins_master = jenkins_master
    self.jenkins_job = jenkins_job
    self.login_user = jenkins_user
    self.login_passwd = jenkins_passwd
    jkServer = jenkins.Jenkins(self.jenkins_master, self.login_user, self.login_passwd)
    self.jenkins_server = jkServer

  def getLastJobId(self):
    '''
    role : 获取job名为job_name的job的最后次构建号
    '''
    return self.jenkins_server.get_job_info(self.jenkins_job)['lastBuild']['number']

  def getJobResultStatus(self, jobId):
    '''
    role:获取job名为job_name的job的某次构建的执行结果状态
    SUCCESS : job执行成功
    FAILURE ：job执行失败
    ABORTED ：人为结束构建
    None : 正在构建中
    '''
    return self.jenkins_server.get_build_info(self.jenkins_job, jobId)['result']

  def getJobBuilding(self, jobId):
    '''
    role:判断job名为job_name的job的某次构建是否还在构建中
    True:正在构建
    Fase:构建结束
    '''
    return self.jenkins_server.get_build_info(self.jenkins_job, jobId)['building']

  def getBuildStages(self, jobId):
    '''
    获取所有的阶段
    '''
    return self.jenkins_server.get_build_stages(self.jenkins_job, jobId)

if __name__=='__main__':
  jkPath = "https://ci.jenkins.net"
  jkJob = "repo_name"     #jobname
  jkLoginUser = "mine"
  jkLoginPwd = "dee3f1161b76f1e796f517e0c902bd5c8b"

  jk = Job(jkPath, jkJob, jkLoginUser, jkLoginPwd, None)

  jobid = jk.getLastJobId()

  print("job id:", jobid)
  print("job building result:", jk.getJobBuilding(jobid))
  print("job result status:", jk.getJobResultStatus(jobid))
  print("job stages:", jk.getBuildStages(jobid))
