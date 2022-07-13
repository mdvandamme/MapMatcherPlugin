# -*- coding: utf-8 -*-

import csv
from qgis.PyQt.QtCore import QVariant
from qgis.core import (QgsWkbTypes,
                       QgsFields,
                       QgsField,
                       QgsPointXY,
                       QgsGeometry,
                       QgsFeature,
                       QgsFeatureSink
                       )
from . import parameters as param


def createFieldsPointMM():
    
    outFields = QgsFields()
    field1 = QgsField("id_gps", QVariant.String)
    outFields.append(field1)
    field2 = QgsField("timestamp", QVariant.String)
    outFields.append(field2)
    field3 = QgsField("mapmatched", QVariant.String)
    outFields.append(field3)
    field4 = QgsField("rmse", QVariant.Double)
    outFields.append(field4)
    
    return outFields



def createLayerSortie(MapMatchingAlgorithm, parameters, context, crsDest, 
                      resultatpath, gpslayer, networklayer):
    
    #   Création de la couche 'track points'
    (sink, dest_id_pl) = MapMatchingAlgorithm.parameterAsSink(parameters, 
                'pointLayer',
                context, 
                createFieldsPointMM(), 
                QgsWkbTypes.Point, 
                crsDest)
    
    #   Création de la couche 'map matching links'
    (sinkLink, dest_id_ll) = MapMatchingAlgorithm.parameterAsSink(parameters, 
                'linkLayer',
                context, 
                QgsFields(), 
                QgsWkbTypes.LineString, 
                crsDest)
    
    #   Création de la couche 'reseau'
    (sinkNetwork, dest_id_nl) = MapMatchingAlgorithm.parameterAsSink(parameters, 
                'network',
                context, 
                QgsFields(), 
                QgsWkbTypes.LineString, 
                crsDest)
    
    
    
    edges = {}
    networkpath = param.getNetworkMMPath(resultatpath)
    with open(networkpath) as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
        for row in reader:
            #link_id,wkt,source,target,one_way
            if row[0] != 'link_id':
                idEdge = int(row[0])
                wkt = str(row[1])
                src = int(row[2])
                tgt = int(row[3])
                    
                if idEdge not in edges:
                    edges[idEdge] = [src,tgt,wkt]
                        
    
    # ---------------------------------------------------------------------
    #   Remplissage des deux premières couches
        
    # Ouverture des fichiers
    gpsmmpath = param.getGpsMMPath(resultatpath, gpslayer)
    with open(gpsmmpath) as f:
        reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        for row in reader:
            if row[1] != 'timestamp':
                    
                createLink = False
                    
                idTrackPoint = int(row[0])
                tps = str(row[1])
                rmse = float(row[6])
                linkid = int(row[7])
                nodeid = int(row[8])
                   
                xrow = float(row[2])
                yrow = float(row[3])
                pt1 = QgsPointXY(xrow, yrow)
                    
                xmm = float(row[4])
                ymm = float(row[5])                    
                pt2 = QgsPointXY(xmm, ymm)
                    
                if linkid == -1:
                    newPoint = QgsFeature()
                    newPoint.setGeometry(QgsGeometry.fromPointXY(pt1))
                    newPoint.setAttributes([idTrackPoint, tps, 'no', rmse])
                    sink.addFeature(newPoint, QgsFeatureSink.FastInsert)
                elif nodeid == -1:
                    newPoint = QgsFeature()
                    newPoint.setGeometry(QgsGeometry.fromPointXY(pt2))
                    newPoint.setAttributes([idTrackPoint, tps, 'edge', rmse])
                    sink.addFeature(newPoint, QgsFeatureSink.FastInsert)
                    createLink = True
                     
                    tab = edges.get(linkid)
                    newEdge = QgsFeature()
                    newEdge.setGeometry(QgsGeometry.fromWkt(tab[2]))
                    sinkNetwork.addFeature(newEdge, QgsFeatureSink.FastInsert)
                        
                else:
                    newPoint = QgsFeature()
                    newPoint.setGeometry(QgsGeometry.fromPointXY(pt2))
                    newPoint.setAttributes([idTrackPoint, tps, 'node', rmse])
                    sink.addFeature(newPoint, QgsFeatureSink.FastInsert)
                   
                if createLink:
                    # On construit une geometrie de type ligne
                    lineLink = QgsGeometry.fromPolylineXY([pt1, pt2])
                    newLink = QgsFeature()
                    newLink.setGeometry(lineLink)
                    sinkLink.addFeature(newLink, QgsFeatureSink.FastInsert)
                    
                        
    return (dest_id_pl, dest_id_ll, dest_id_nl)


    