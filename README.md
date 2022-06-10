# N-Queens v1.1.0
N-queens is a solver for the N queens problem, which is how can one position N queens on a chess board so that none of them are able to attack another.

N-Queens will given a visual representation of all solutions to the n-queens problem. By default it does the 8x8 version with 8 queens. Each of the solutions will have a number with it, so that you can see the total number of solutions. 
 
## Running n-queens.py

```console
$ chmod +x n-queens.py
$ ./n-queens.py
``` 
or
```console
$ python3 n-queens.py
```

If using the first option, chmod will only need to be run once, in order to make ./n-queens executable by the shell, after that it doens't need to be run again at all.

## Command line options
Multiple command line options can be applied to change the behaviour of N-Queens.

### Board size options

`--width=X` or `-W=X` will set the width of the board to X.

`--height=Y` or `-H=Y` will set the height of the board to Y.

By default the width and height of the board are both 8.
Changing the width or height does not change the number of queens, so you will need to use the -N option for that.

```console
$ ./n-queens.py --width=4 --height=4 -N=4
...
```

### N option

`-N=n` will set the number of queens to n. By default the number of queens is 8.

```console
$ ./n-queens.py -N=7
...
```

### Silent option

`--silent` or `-S` will stop n-queens from printing each solution, only showing the total number of solutions.

```console
$ ./n-queens.py --silent
92 solutions
```

### Version option

`--version`, `-V`, or `-v` will show the version number and stop the program.

```console
$ ./n-queens.py --version
v1.1.0
```

### Help option

`--help` or `-h` will show the usage of n-queens.py and stop the program.

```console
$ ./n-queens.py --help
usage: ./n-queens.py [--width=<width>] [-W=<width>] [--height=<height>] [-H=<height>] [-N=<N>] [--silent] [-S] [--version] [-V|v] [--help] [-h]
```

### Multiple options

When multiple options are used, they will act independently and one after another. Some, like --version and --help, will cause the program to stop running after their correspoinding action, and any options after them will not be run.
