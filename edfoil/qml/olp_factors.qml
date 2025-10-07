import QtQuick 2.15
import QtCharts 2.15

Item {
    id: root
    anchors.fill: parent

    function series(sta, k1, len, k2) {
        var series = [sta1, sta2, sta3, len1, len2, len3]
        for (var i = 0; i < series.length; ++i) {
            series[i].clear()
            series[i].visible = false
        }
        for (var i = 0; i < sta.length; ++i) {
            // console.log("STA point:", sta[i][0], sta[i][1])
            if (i === k1) {
                staSelected.clear()
                staSelected.visible = true
                var series = sta[i]
                for (var j = 0; j < series.length; ++j) {
                    staSelected.append(series[j][0], series[j][1])
                }
            } else if (i === 0) {
                sta1.clear()
                sta1.visible = true
                var series = sta[i]
                for (var j = 0; j < series.length; ++j) {
                    sta1.append(series[j][0], series[j][1])
                }
            } else if (i === 1) {
                sta2.clear()
                sta2.visible = true
                var series = sta[i]
                for (var j = 0; j < series.length; ++j) {
                    sta2.append(series[j][0], series[j][1])
                }
            } else if (i === 2) {
                sta3.clear()
                sta3.visible = true
                var series = sta[i]
                for (var j = 0; j < series.length; ++j) {
                    sta3.append(series[j][0], series[j][1])
                }
            }
            // console.log("Sta plotted.")
        }
        for (var i = 0; i < len.length; ++i) {
            // console.log("LEN point:", len[i][0], len[i][1])
            if (i === k2) {
                lenSelected.clear()
                lenSelected.visible = true
                var series = len[i]
                for (var j = 0; j < series.length; ++j) {
                    lenSelected.append(series[j][0], series[j][1])
                }
            } else if (i === 0) {
                len1.clear()
                len1.visible = true
                var series = len[i]
                for (var j = 0; j < series.length; ++j) {
                    len1.append(series[j][0], series[j][1])
                }
            } else if (i === 1) {
                len2.clear()
                len2.visible = true
                var series = len[i]
                for (var j = 0; j < series.length; ++j) {
                    len2.append(series[j][0], series[j][1])
                }
            } else if (i === 2) {
                len3.clear()
                len3.visible = true
                var series = len[i]
                for (var j = 0; j < series.length; ++j) {
                    len3.append(series[j][0], series[j][1])
                }
            }
        }
        autoRange()
    }

    function autoRange() {
        // Collect all points from visible series
        var xs = []
        var ys = []
        var all = [staSelected, lenSelected, sta1, sta2, sta3, len1, len2, len3]
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

        // Padding for y axis only
        var dy = ymax - ymin
        if (dy <= 0) dy = 1e-6
        // padding
        ymin -= dy * 0.05
        ymax += dy * 0.05

        // Round to nearest 100th
        var xrounder = 500.
        xmin = Math.floor(xmin / xrounder) * xrounder
        xmax = Math.ceil(xmax / xrounder) * xrounder

        axisX.min = xmin
        axisX.max = xmax
        axisY.min = ymin
        axisY.max = ymax
    }

    function scatter(points) {
        stations.clear()
        for (var i = 0; i < points.length; ++i) {
            var p = points[i]
            stations.append(p[0], p[1])
        }
        autoRange()
    }

    Connections {
        target: olplenBridge
        function onUpdateSeries(sta, k1, len, k2) {
            series(sta, k1, len, k2)
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
        animationOptions: ChartView.AllAnimations
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
            titleText: "Factor [-]"
            tickCount: 4
        }

        LineSeries {
            id: staSelected
            name: "Start"
            color: "#1f77b4"
            width: 2
            axisX: axisX
            axisY: axisY
        }

        LineSeries {
            id: lenSelected
            name: "Length"
            color: "#ff7f0e"
            width: 2
            axisX: axisX
            axisY: axisY
        }

        // Interpolation orders not selected
        LineSeries {
            id: sta1
            name: "Start (k = 1)"
            color: "#888"
            width: 1.5
            axisX: axisX
            axisY: axisY
            visible: false
        }

        LineSeries {
            id: sta2
            name: "Start (k = 2)"
            color: "#888"
            width: 1.5
            axisX: axisX
            axisY: axisY
            visible: false
        }

        LineSeries {
            id: sta3
            name: "Start (k = 3)"
            color: "#888"
            width: 1.5
            axisX: axisX
            axisY: axisY
            visible: false
        }

        // Interpolation orders not selected
        LineSeries {
            id: len1
            name: "Length (k = 1)"
            color: "#888"
            width: 1.5
            axisX: axisX
            axisY: axisY
            visible: false
        }

        LineSeries {
            id: len2
            name: "Length (k = 2)"
            color: "#888"
            width: 1.5
            axisX: axisX
            axisY: axisY
            visible: false
        }

        LineSeries {
            id: len3
            name: "Length (k = 3)"
            color: "#888"
            width: 1.5
            axisX: axisX
            axisY: axisY
            visible: false
        }

        ScatterSeries {
            id: stations
            name: "Stations"
            markerSize: 6
            markerShape: ScatterSeries.MarkerShapeRectangle
            borderColor: "#0c0c0c"
            color: "green"
            axisX: axisX
            axisY: axisY
        }
    }
}