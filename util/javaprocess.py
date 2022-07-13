# -*- coding: utf-8 -*-

import os

def buildCommandLine(parameterspath):
    
    jarName = 'mapmatcher-1.5-jar-with-dependencies.jar'
    jarPath = os.path.dirname(__file__) + "/../jar/" + jarName
        
    cmds = []
    cmds.append("java")
    cmds.append("-jar")
    cmds.append(jarPath)
    cmds.append(parameterspath)
        
    cmd = " ".join(cmds)
    
    return cmd
    
    
    