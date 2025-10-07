import QtGraphs
import QtQuick

Item {
    id: mainView
    width: 800
    height: 600

    // Bridge comes from Python (context property "graphBridge")
    // points passed as: [{x: <float>, y: <float>}, ...]
    function updateLine(points, name) {
        lineseries.clear()
        if (name) lineseries.name = name
        for (var i = 0; i < points.length; ++i) {
            var p = points[i]
            lineseries.append(p.x, p.y)
        }
    }

    Connections {
        target: graphBridge
        function onUpdateSeriesRequested(points, name) {
            updateLine(points, name)
        }
        function onClearRequested() {
            lineseries.clear()
        }
        function onUpdateAxesRequested(minX, maxX, tickX, minY, maxY, tickY) {
            xAxis.min = minX
            xAxis.max = maxX
            xAxis.tickInterval = tickX
            yAxis.min = minY
            yAxis.max = maxY
            yAxis.tickInterval = tickY
            // console.log(graph.plotArea)
            plotBorder.requestPaint()

        }
        function onUpdateLE(x, y) {
            leMarker.clear()
            leMarker.append(x, y)
        }
    }

    // property alias lower: lineseries

    GraphsView {
        id: graph
        anchors.fill: parent
        antialiasing: true
        
        marginBottom: 0
        marginLeft: 0
        marginTop: 10
        marginRight: 10

        theme: GraphsTheme {
            backgroundVisible: false
            plotAreaBackgroundVisible: false
            grid.mainColor: "#888"
            grid.subColor: "transparent"
            axisX.mainColor: "transparent"
            axisY.mainColor: "transparent"
            axisX.subColor: "transparent"
            axisY.subColor: "transparent"
            axisX.labelTextColor: "black"
            axisY.labelTextColor: "black"
            seriesColors: ["#1f77b4"]
        }

        axisX: ValueAxis {
            id: xAxis
            min: 0
            max: 1
            tickInterval: 0.2
            gridVisible: true
            labelsVisible: true
            lineVisible: false
        }

        axisY: ValueAxis {
            id: yAxis
            min: -0.1
            max: 0.1
            tickInterval: 0.02
            gridVisible: true
            labelsVisible: true
            lineVisible: false
        }

        LineSeries {
            id: lineseries
            name: "Airfoil"
        }

        ScatterSeries {
            id: leMarker
            name: "Leading Edge"
            pointDelegate: Rectangle {
                width: 12
                height: 12
                color: "green"
                radius: width * 0.5
                border.width: 2
                border.color: "black"
            }
        }

    }
    Canvas {
        id: plotBorder
        anchors.fill: parent
        antialiasing: true
        z: 100
        onPaint: {
            var ctx = getContext("2d")
            ctx.reset()

            // plotArea expected to have x,y,width,height
            var pa = graph.plotArea
            // console.log(pa)

            var x = pa.x
            var y = pa.y
            var w = pa.width
            var h = pa.height

            ctx.lineWidth = 1
            ctx.strokeStyle = "#000001"
            ctx.beginPath()
            ctx.rect(x,y,w,h)
            ctx.stroke()
        }
    }
}