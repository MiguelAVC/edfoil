import QtQuick 2.15
import QtCharts 2.15

Item {
    id: root
    anchors.fill: parent

    // Called from Python via signals
    function rebuild(sta, end, le, te) {
        leMarker.clear()
        teMarker.clear()
        olpSta.clear()
        olpEnd.clear()

        for (var i = 0; i < le.length; ++i) {
            // console.log("LE point:", le[i][0], le[i][1])
            leMarker.append(le[i][0], le[i][1])
            teMarker.append(te[i][0], te[i][1])
            olpSta.append(sta[i][0], sta[i][1])
            olpEnd.append(end[i][0], end[i][1])
        }

        autoRange()
    }

    function scatter(points) {
        stations.clear()
        for (var i = 0; i < points.length; ++i) {
            var p = points[i]
            stations.append(p[0], p[1])
        }
        autoRange()
    }

    function clearAll() {
        while (chart.seriesCount > 0)
            chart.removeSeries(chart.series(0))
    }

    function autoRange() {
        // Collect all points from visible series
        var xs = []
        var ys = []
        var all = [leMarker, teMarker, olpSta, olpEnd]
        for (var i = 0; i < all.length; ++i) {
            var s = all[i]
            var c = s.count
            for (var k = 0; k < c; ++k) {
                var p = s.at(k)
                xs.push(p.x); ys.push(p.y)
            }
        }
        if (!xs.length) return
        var xmin = Math.min.apply(Math, xs)
        var xmax = Math.max.apply(Math, xs)
        var ymin = Math.min.apply(Math, ys)
        var ymax = Math.max.apply(Math, ys)

        // var dx = xmax - xmin
        // var dy = ymax - ymin
        // if (dx <= 0) dx = 1e-6
        // if (dy <= 0) dy = 1e-6
        // // padding
        // xmin -= dx * 0.05
        // xmax += dx * 0.05
        // ymin -= dy * 0.05
        // ymax += dy * 0.05

        // Round to nearest 100th
        var xrounder = 500.
        var yrounder = 100.
        xmin = Math.floor(xmin / xrounder) * xrounder
        xmax = Math.ceil(xmax / xrounder) * xrounder
        ymin = Math.floor(ymin / yrounder) * yrounder
        ymax = Math.ceil(ymax / yrounder) * yrounder

        // number of ticks
        // var dx = xmax - xmin
        // var dy = ymax - ymin

        axisX.min = xmin
        axisX.max = xmax
        axisY.min = ymin
        axisY.max = ymax
    }

    Connections {
        target: olpstaBridge
        function onUpdateSeries(sta, end, le, te) {
            rebuild(sta, end, le, te)
        }
        function onUpdateScatter(points) {
            scatter(points)
        }
        function onClear() {
            clearAll()
        }
    }

    ChartView {
        id: chart
        anchors.fill: parent
        antialiasing: true
        legend.alignment: Qt.AlignTop
        theme: ChartView.ChartThemeLight
        animationOptions: ChartView.SeriesAnimations
        margins.bottom: 0
        margins.left: 0
        margins.top: 0
        margins.right: 0

        ValueAxis {
            id: axisX
            titleText: "Blade length [d]"
            tickCount: 8 
        }

        ValueAxis {
            id: axisY
            titleText: "x [d]"
            tickCount: 4
        }

        LineSeries {
            id: leMarker
            name: "LE"
            color: "#888"
            width: 2
            axisX: axisX
            axisY: axisY
        }

        LineSeries {
            id: teMarker
            name: "TE"
            color: "#888"
            width: 2
            axisX: axisX
            axisY: axisY
        }

        LineSeries {
            id: olpSta
            name: "Start"
            color: "#1f77b4"
            width: 1.5
            axisX: axisX
            axisY: axisY
        }

        LineSeries {
            id: olpEnd
            name: "End"
            color: "#ff7f0e"
            width: 1.5
            axisX: axisX
            axisY: axisY
        }

        // ScatterSeries {
        //     id: stations
        //     name: "Stations"
        //     markerSize: 10
        //     markerShape: ScatterSeries.MarkerShapeRectangle
        //     borderColor: "black"
        //     axisX: axisX
        //     axisY: axisY
        // }
    }
}