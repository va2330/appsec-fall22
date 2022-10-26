# How to test

1. Open two terminals
2. In the first terminal, navigate to the assignment 3 folder
3. Type `sudo su` to become super user
4. In the second one, copy the grader folder (and all its content)
5. Navigate to `reader` folder and compile read `gcc read.c -o read` then navigate back to the grader folder (where `grader.py` is).
6. In the first terminal (with superuser prompt) run student's script using `python profiler.py`
7. While their script is running, click on the second terminal and run `python grader.py` which will generate something like this where the expected output is also printed (something similar to this): 
```
pkill: killing pid 114 failed: Operation not permitted
pkill: killing pid 114 failed: Operation not permitted
pkill: killing pid 114 failed: Operation not permitted
pkill: killing pid 114 failed: Operation not permitted
pkill: killing pid 114 failed: Operation not permitted
fd = 3/n
exptected:

stats:
number of non-bash processes: 42
number of SYS folders: 3
number of opened p-files: 4
```

9.  In the first terminal CTRL+C student's script and type `cat stats.txt` which should be similar to this:
```
stats:
number of non-bash processes: 42
number of SYS folders: 3
number of opened p-files: 4
```


## Rubric
#### Part 1: non-bash processes
- If `number of non-bash processes: 42` can be in the range of -+7
#### Part 2: non-bash processes
- If `number of SYS folders: 3` can be in the range of -+1
#### Part 2: non-bash processes
- If `number of opened p-files: 4` can be in the range of -+1