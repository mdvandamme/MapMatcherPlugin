# -*- coding: utf-8 -*-

from qgis.PyQt.QtGui import QColor
from qgis.core import (QgsProcessingUtils,
                       QgsMarkerSymbol,
                       QgsLineSymbol,
                       QgsRendererCategory,
                       QgsCategorizedSymbolRenderer,
                       QgsSingleSymbolRenderer,
                       QgsSimpleLineSymbolLayer
                       )

def stylePointsMM(dest_id_pl, context):
    categories = []
        
    # categorie 1
    symbolEdge = QgsMarkerSymbol.createSimple({'name': 'square', 'color_border': '255,255,255'})
    symbolEdge.setColor(QColor.fromRgb(31, 120, 180))
    symbolEdge.setSize(1.8)
    categoryEdge = QgsRendererCategory("edge", symbolEdge, "mm")
    categories.append(categoryEdge)
        
    # categorie 2
    symbolNode = QgsMarkerSymbol.createSimple({'name': 'square', 'color_border': '255,255,255'})
    symbolNode.setColor(QColor.fromRgb(68, 174, 240))
    symbolNode.setSize(1.8)
    symbolNode = QgsRendererCategory("node", symbolNode, "node")
    categories.append(symbolNode)

    # categorie 3
    symbolNone = QgsMarkerSymbol.createSimple({'name': 'square', 'color_border': '255,255,255'})
    symbolNone.setColor(QColor.fromRgb(216,7,96))
    symbolNone.setSize(1.8)
    symbolNone = QgsRendererCategory("no", symbolNone, "--")
    categories.append(symbolNone)

    # On construit une expression pour appliquer les categories
    expression = 'mapmatched' # field name
    renderer = QgsCategorizedSymbolRenderer(expression, categories)
    trackpointLayer = QgsProcessingUtils.mapLayerFromString(dest_id_pl, context)
    trackpointLayer.setRenderer(renderer)
    
    
def styleLinkMM(dest_id_ll, context):
    
    symbolL = QgsLineSymbol.createSimple({'penstyle':'solid', 'width':'0.6','line_style':'dash'})
    symbolL.setColor(QColor.fromRgb(255, 127, 0))
    linkLayer = QgsProcessingUtils.mapLayerFromString(dest_id_ll, context)
    linkLayer.renderer().setSymbol(symbolL)
    
    # -----
        
        #symbolL = QgsLineSymbol.createSimple({'penstyle':'solid', 'width':'0.6','line_style':'dash'})
        #symbolL.setColor(QColor.fromRgb(255, 127, 0))
        #linkLayer = QgsProcessingUtils.mapLayerFromString(dest_id_ll, context)
        #linkLayer.renderer().setSymbol(symbolL)
        
        
def styleNetworkConstruct(idlayer, context):
    
    symbol = QgsLineSymbol.createSimple ({'color':'red', 'width':'0.8', 'line_style':'solid'})    
    symbol_l2 = QgsSimpleLineSymbolLayer.create ({'color':'white', 'width':'0.2', 'line_style':'solid'})    
    symbol.appendSymbolLayer (symbol_l2)

    renderer = QgsSingleSymbolRenderer (symbol)  
    renderer.setUsingSymbolLevels(True)
    
    networkLayer = QgsProcessingUtils.mapLayerFromString(idlayer, context)
    networkLayer.setRenderer(renderer)    
    
    
    
       