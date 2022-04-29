# Cipy
**cipy** is a tool used to execute comands based in a `pipeline.yml` file.

### pipeline.yml syntax

```yml
tasks:
  taskName1: command_1
  taskName2: command_1
  taskName3: command_1
pipelines:
  - name: pipelineName1
    tasks:
      - taskName1
      - taskName2
  - name: pipelineName2
    tasks:
      - taskName3
```
### Running cipy
**cipy** expect that `pipeline.yml` file is on the folder it was called.  
To execute it you just need to run:  
```
cipy
```

if you want to setup one specific peline to run, use:
```
cipy pipelineName1
```
test
