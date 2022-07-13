# -*- coding: utf-8 -*-

from datetime import datetime
import os
from pathlib import Path


def getResultPath(resultatpath):
    return resultatpath + '/'


def getGpsMMPath(resultatpath, gpsPath):
    chemin = getResultPath(resultatpath)
    gpsmmpath = chemin + Path(gpsPath).stem + "_mm.dat"
    return gpsmmpath


def createParamFile(resultatpath, networkpath, gpspath):
    
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    fp = open(os.path.dirname(__file__) + "/../tmp/parameters.txt", "w")
    fp.write("# ----------------------------------------------\n")
    fp.write("# Parameter file for map-matching               \n")
    fp.write("# ----------------------------------------------\n")
    fp.write("# User : " + os.getlogin() + "\n")
    fp.write("# Date : " + dt_string + "\n")
    fp.write("# ----------------------------------------------\n")
    fp.write("\n")
    
    fp.write("# Input files\n")
    fp.write('input.network.path = "' + networkpath.strip() + '"\n')
    fp.write('input.track.path = "' + gpspath + '"\n')
    fp.write("\n")
    
    fp.write("# Network format\n")
    fp.write("network.header = true\n")
    fp.write('network.delimiter = ","\n')
    fp.write('network.geom.name = ""wkt""\n')
    fp.write('network.source.name = ""source""\n')
    fp.write('network.target.name = ""target""\n')
    fp.write('network.edge.name = ""link_id""\n')
    fp.write('network.oneway.name = ""\n')
    fp.write("\n")
    
    fp.write('# Track format \n')
    fp.write('track.header = false\n')
    fp.write('track.delimiter = ","\n')
    fp.write('track.columns.x.id = 2\n')
    fp.write('track.columns.y.id = 3\n')
    fp.write('track.columns.t.id = -1\n')
    fp.write('track.error.code = "-1"\n')
    fp.write('track.date.fmt = "yyyy-mm-dd hh:mm:ss"\n')
    fp.write("\n")
    
    fp.write('# Computation parameters \n')
    fp.write('computation.sigma = 4.0\n')
    fp.write('computation.beta = 0.2\n')
    fp.write('computation.radius = 35.0\n')
    fp.write('computation.transition = 0.0\n')
    fp.write('computation.limit.speed = 1.7976931348623157E308\n')
    fp.write('computation.autocorrelation = 60.0\n')
    fp.write('computation.scope = 100.0\n')
    fp.write('computation.angle = 0.0\n')
    fp.write('computation.distribution = normal\n')
    fp.write("\n")

    fp.write('# Additional options \n')
    fp.write('option.max.candidates = -1\n')
    fp.write('option.failure.skip = true\n')
    fp.write('option.confidence.ratio = false\n')
    fp.write('option.projection = false\n')
    fp.write('option.precompute.distances = true\n')
    fp.write('option.buffer.type = full_network\n')
    fp.write('option.buffer.radius = 300.0\n')
    fp.write('option.make.topology = false\n')
    fp.write('option.sort.nodes = false\n')
    fp.write('option.simplify = false\n')
    fp.write('option.ref.network = false\n')
    fp.write('bias.x = 0.0\n')
    fp.write('bias.y = 0.0\n')
    fp.write('topology.tolerance = 0.01\n')
    fp.write('network.rmse = 0.0\n')
    fp.write('confidence.ratio = 0.0\n')
    fp.write('network.inaccuracies = false\n')
    fp.write("\n")

    fp.write('# Output \n')
    fp.write('output.path = "' + getResultPath(resultatpath) + '"\n')
    fp.write('output.clear = true\n')
    fp.write('output.report = true\n')
    fp.write('output.graphics = false\n')
    fp.write('output.debug = false\n')
    fp.write('output.suffix = "_mm.dat"\n')
    fp.write('output.delimiter = ","\n')
    fp.write('output.mute = false\n')
    fp.write('output.errors = true\n')
    fp.write('output.parameters = true\n')
    fp.write('output.index = true\n')
    fp.write('output.rmse = true\n')
    fp.write('output.abs.type = from_source_m\n')
    fp.write('output.confidence = false\n')
    fp.write('output.index.all.edge = false\n')
    fp.write('output.index.coords = false\n')
    fp.write('output.index.format.csv = true\n')
    fp.write('output.rmse.type = after\n')
    fp.write("\n")

    return (fp, os.path.realpath(fp.name))


