from PyQt5.QtCore import Qt
from qgis._core import *
from qgis.gui import *

from gui.preview.functions.file_func import *
from gui.preview.functions.button_func import *
from gui.preview.functions.coords_func import *
from gui.preview.functions.menu_func import *
from customFunc.custom_func import *


def load_preview(main):

    declaring_variable(main)

    init_preview(main)

    init_qgis_map(main)

    init_vector_tools(main)
    
    init_custom_tools(main)

    init_rightMenu(main)

    bind_func(main)

    bind_label(main)


def declaring_variable(main):
    main.preview_canvas = None
    main.preview_tool_pan = None
    main.preview_tool_zoom_in = None
    main.preview_tool_zoom_out = None


def init_preview(main):
    main.ui.splitter.setStretchFactor(0, 3)
    main.ui.splitter.setStretchFactor(1, 5)


def init_qgis_map(main):
    main.preview_canvas = QgsMapCanvas()
    main.preview_canvas.setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:4326"))
    main.preview_canvas.setCanvasColor(Qt.white)
    main.preview_canvas.enableAntiAliasing(True)
    main.preview_canvas.setFocus()
    main.preview_canvas.setParallelRenderingEnabled(True)

    main.ui.preview_qgis_map.addWidget(main.preview_canvas)

    main.preview_tool_pan = QgsMapToolPan(main.preview_canvas)
    main.preview_tool_zoom_in = QgsMapToolZoom(main.preview_canvas, False)
    main.preview_tool_zoom_out = QgsMapToolZoom(main.preview_canvas, True)

    main.preview_canvas.setMapTool(main.preview_tool_pan)

    main.layerTreeView = QgsLayerTreeView(main)
    main.ui.layout_prev_layers.addWidget(main.layerTreeView)

    main.model = QgsLayerTreeModel(QgsProject.instance().layerTreeRoot(), main)
    main.model.setFlag(QgsLayerTreeModel.AllowNodeRename)  # 允许图层节点重命名
    main.model.setFlag(QgsLayerTreeModel.AllowNodeReorder)  # 允许图层拖拽排序
    main.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)  # 允许改变图层节点可视性
    main.model.setFlag(QgsLayerTreeModel.ShowLegendAsTree)  # 展示图例
    main.model.setAutoCollapseLegendNodes(10)  # 当节点数大于等于10时自动折叠
    main.layerTreeView.setModel(main.model)
    main.layerTreeBridge = QgsLayerTreeMapCanvasBridge(QgsProject.instance().layerTreeRoot(), main.preview_canvas, main)
    main.ui.label_coords_name.setText("坐标系(默认): WGS 84 / EPSG:4326")


def init_rightMenu(main):
    main.rightMenu = menu_provider(main)
    main.layerTreeView.setMenuProvider(main.rightMenu)

def init_custom_tools(main):
    main.ui.button_tool_access_analysis.clicked.connect(lambda: open_accessibility_analysis_widget(main))
    main.ui.button_tool_isochronous_circle.clicked.connect(lambda: open_isochronous_circle_dialog(main))


def init_vector_tools(main):
    main.ui.button_feature_editor.setEnabled(False)
    main.ui.button_feature_select.setEnabled(False)
    main.ui.button_delete_feature_select.setEnabled(False)
    main.editTempLayer: QgsVectorLayer = None
    main.layerTreeView.clicked.connect(lambda self: layer_clicked(main))
    main.ui.button_feature_editor.clicked.connect(lambda: feature_editor(main))
    main.ui.button_feature_select.clicked.connect(lambda: feature_selected(main))
    main.ui.button_delete_feature_select.clicked.connect(lambda: feature_delete_selected(main))


def bind_func(main):
    _ui = main.ui
    _ui.button_add_raster.clicked.connect(lambda self: open_raster_file(main))
    _ui.button_add_vector.clicked.connect(lambda self: open_vector_file(main))
    _ui.button_move.clicked.connect(lambda self: slot_set_map_tool(main.preview_canvas, main.preview_tool_pan))
    _ui.button_zoom_in.clicked.connect(lambda self: slot_set_map_tool(main.preview_canvas, main.preview_tool_zoom_in))
    _ui.button_zoom_out.clicked.connect(lambda self: slot_set_map_tool(main.preview_canvas, main.preview_tool_zoom_out))
    _ui.button_refresh.clicked.connect(lambda self: slot_refresh_canvas(main.preview_canvas))
    _ui.button_prev_clear.clicked.connect(lambda self: clear_all_layer(main))
    _ui.button_prev_remove.clicked.connect(lambda self: delete_selected_layer(main))


def bind_label(main):
    main.preview_canvas.xyCoordinates.connect(lambda point: showXY(main, point))
    main.preview_canvas.destinationCrsChanged.connect(lambda: showCrs(main))
