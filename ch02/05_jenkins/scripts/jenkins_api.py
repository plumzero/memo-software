#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import jenkins

import time, datetime

class Job():
  '''
  @brief 登录到 jenkins 服务器
  @param url 服务器 url
  @param jobname 工作任务名称
  @param user 登录帐号
  @param password 登录口令
  @return 
  '''
  def __init__(self, url, user, password, jobname):
    self.url = url
    self.user = user
    self.password = password
    self.jobname = jobname
    self.server = jenkins.Jenkins(self.url, self.user, self.password)

  '''
  @brief 获取工作任务最近一次的 job id
  @return 
  '''
  def getLastJobId(self):
    return self.server.get_job_info(self.jobname)['lastBuild']['number']

  '''
  @brief 获取 job 名为 jobname, job id 为 jobId 的执行结果状态
  @param jobId
  @return SUCCESS:job执行成功/FAILURE:job执行失败/ABORTED:人为结束构建/None:正在构建中
  '''
  def getJobResultStatus(self, jobId):
    return self.server.get_build_info(self.jobname, jobId)['result']

  '''
  @brief 判断 job 名为 jobname, job id 为 jobId 是否还在构建中
  @return True:正在构建/False:构建结束
  '''
  def isJobBuilding(self, jobId):
    return self.server.get_build_info(self.jobname, jobId)['building']

  def getAllStagesStatus(self, jobId):
    '''
    @brief 获取所有的stage，可用于 Debug 查看信息
    @return 状态信息
    '''
    return self.server.get_build_stages(self.jobname, jobId)
  
  def getGivenStageStatus(self, stage_name, jobId):
    '''
    @brief 获取指定 stage 的状态
    @return None:未知状态/SUCCESS:成功/FAILED:失败/IN_PROGRESS:正在构建
    '''
    stages = self.server.get_build_stages(self.jobname, jobId)['stages']
    for stage in stages:
      if stage["name"] == stage_name:
        return stage["status"]
    return "None"

  def buildJob(self, parameters=None):
    '''
    @brief api 触发 job
    @return queueId : 378956
    '''
    print("build job")
    token=datetime.datetime.now().strftime('%Y%m%d_%H%M%S%f')
    print("token=", token)
    # parameters = {"order_date": 2020071111, "test_locals_id_point_version": 2222}
    parameters = {'branch': 'branch_temp'}
    # if parameters:      # ##带参数构建触发，参数必须是字典类型
      # return self.server.build_job(self.jobname, parameters=parameters, token=token)
    # qid = self.server.build_job(self.jobname, parameters=parameters, token=token)  ## 无参数构建触发
    qid = self.server.build_job(self.jobname, parameters=parameters)  ## 无参数构建触发
    print("qid=", qid)
    info = self.server.get_queue_item(qid)
    print("info=", info)

if __name__=='__main__':
  url = "https://ci.jenkins.net"
  user = "mine"
  password = "dee3f1161b76f1e796f517e0c902bd5c8b"
  jobname = "platform_packsoft"

  jk = Job(url, user, password, jobname)

  jk.buildJob()
  time.sleep(3)  #api出发怕jenkin没来得及响应

  jobid = jk.getLastJobId()

  print("job id:", jobid)
  print("job is building:", jk.isJobBuilding(jobid))
  # print("job result status:", jk.getJobResultStatus(jobid))
  # print("job stages status:", jk.getAllStagesStatus(jobid))
  print("job given stage status:", jk.getGivenStageStatus("Install", jobid))