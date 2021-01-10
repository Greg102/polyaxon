import os

output_root = os.environ['POLYAXON_RUN_OUTPUTS_PATH']
outpath = os.path.join(output_root, 'demofile3.txt')

f = open(outpath, "w")
f.write("Woops! I have deleted the content!")
f.close()