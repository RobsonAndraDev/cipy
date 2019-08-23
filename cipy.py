#!/usr/bin/python
import git, os, shutil, sys, yaml

def main():
  execGitIfNeeded()
  openPipelineFile()

def execGitIfNeeded():
  if hasArgs(2):
    if not os.path.exists('repo'):
      gitclone()
    else:
      repo = git.Repo('repo')
      print('remote url: ' + repo.remotes.origin.url)
      if getRepoUrl() == repo.remotes.origin.url:
        gitfech(repo)
      else:
        shutil.rmtree('repo')
        gitclone()

def gitclone():
  repo = git.Repo.clone_from(getRepoUrl(), 'repo', branch='master')
  gitfech(repo)

def gitfech(repo):
  print('Fetching repository: ' + getRepoUrl())
  for remote in repo.remotes:
    remote.fetch()

def getRepoUrl():
  if hasArgs(2):
    return sys.argv[2]
  return ""

def getFolder():
  if hasArgs(2):
    return "repo"
  return "."

def getPipelineName():
  if hasArgs():
    return sys.argv[1]
  return "all"

def hasArgs(numArgs=1):
  return len(sys.argv) > numArgs


def openPipelineFile():
  with open(getFolder() + '/pipeline.yml', 'r') as stream:
    try:
      ppyml = yaml.load(stream)
      tasks = ppyml['tasks']
      pipelines = ppyml['pipelines']
      if pipelineWasChoosen(pipelines):
        choosenPipeline = pipelines[getPipelineName()]
        runPipeline(choosenPipeline, tasks)
      else:
        runAllPipelines(pipelines, tasks)
    except yaml.YAMLError as exc:
      print(exc)

def pipelineWasChoosen(pipelines):
  return getPipelineName() in pipelines

def runAllPipelines(pipelines, tasks):
  for pipeline in(pipelines):
    runPipeline(pipeline, tasks)

def runPipeline(pipeline, tasks):
  print('')
  print('-------------------------------------------------------------------------------------')
  print('')
  print('Running pipeline: ' + pipeline['name'])
  print('')
  print('-------------------------------------------------------------------------------------')
  print('')
  for task in(pipeline['tasks']):
    print('')
    print('-------------------------------------------------------------------------------------')
    print('')
    print('Running task: ' + task + ': ' + tasks[task] + '. From pipeline: ' + pipeline['name'])
    print('')
    print('-------------------------------------------------------------------------------------')
    print('')
    if not runTask(getFolder(), tasks[task]):
      exit()

def runTask(repoDir, command):
  try:
    return os.system('cd ' + repoDir + ' && ' + command) == 0
  except:
    return False

main()