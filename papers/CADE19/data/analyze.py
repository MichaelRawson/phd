#!/usr/bin/env python

import sys, copy, random

import cPickle as pickle
import gzip

def read_strats(data_file_names):

  solvers = {}   # maps solvers to expers where each exper is a {solved_problems:status} dict
  
  # loading
  for name in data_file_names:
    with open(name,"r") as f:
      for line in f:
        prob,solver,config,_,time,_,memory,stat = line.split(",")[:8]

        if ".rm" in prob:
          pass

        solver_name = solver+"_"+config

	if "SMT" in prob:
		logic = prob.split("/")[1]
		solver_name = logic+"_"+solver_name

        if solver_name in solvers:
          exper = solvers[solver_name]
        else:
          exper = {}
          solvers[solver_name] = exper
            
        if prob in exper: # if there were multiple runs of the same strategy, conut
          pass
        else:
          exper[prob] = (stat.strip(),time) 

  return solvers

if __name__ == "__main__":
  
  solvers = read_strats(["others.csv","info_no_baseline.csv"])
  if "solver_configuration" in solvers:
    del solvers["solver_configuration"]
  
  m = max({len(k) for k in solvers.keys()}) 

  # map from problem to solvers that solve it
  solved = {}
  times = {}

  for (solver,exper) in sorted(solvers.items()):
    count = 0
    for (prob,(stat,time)) in exper.items(): 
      if stat=="Refutation" or stat=="Theorem" or stat=="Unsatisfiable" or stat=="Satisfiable" or stat=="CounterSatisfiable": 
        count +=1
        if prob not in solved:
          solved[prob] = set()
        solved[prob].add(solver)
        if prob not in times:
          times[prob] = {} 
        times[prob][solver] = time
    print solver,"\t:",count
             
  #sys.exit(0)

  uniques = {}
  for (prob,solutions) in solved.items():    
    vnew = 0
    other = 0
    for s in solutions:
      if '_awrs' in s or 'baseline' in s:
	vnew = 1 
      else:
        other = other+1
    if (vnew+other) == 1: 
      s = "Vampire (new)"
      if other==1:
	s = solutions.pop()
      if s not in uniques:
        uniques[s] = set()
      uniques[s].add(prob)

  print "Uniques"
  for (solver,u) in sorted(uniques.items()):
    print "\t",solver,":",len(u)
    #for prob in u:
    #  print "\t\t",prob
