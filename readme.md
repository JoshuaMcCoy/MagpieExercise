to run this program, open a console in this directory and use this command:
docker-compose up --build

the results will be output to /mount/results

you can delete the existing files before running the command to ensure that you are getting freshly generated results.

the input files are located at /mount, feel free to manipulate them to alter the result files.

I used a docker compose implementation to make this project fully repeatable across platforms with a minimum of tooling. The only requirement is docker, but if you would like to run the scripts in your own environment, they are called etl1.py and etl2.py, they are located in the folder called /mount.