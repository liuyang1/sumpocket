<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="vis.css" type="text/css">
    <title>Pocket Summary</title>
</head>

<body>
    <!-- <div id="main" style="width:1300px; height:650px"></div> -->
    <div id="main" style="width:100%%; height:100%%"></div>
    <script src="http://echarts.baidu.com/build/dist/echarts.js"></script>
    <script type="text/javascript">
require.config({paths: {echarts:'http://echarts.baidu.com/build/dist'}});
require(['echarts', 'echarts/chart/line'],
        function (ec) {
var mychart = ec.init(document.getElementById('main'));
var option = {
    title : {
        text: 'Pocket Summary',
        subtext: '%(username)s',
        x:'middle',
        y:'top'
    },
    tooltip : { trigger: 'axis', },
    legend : { data: ['add', 'del'] },
    toolbox: {
        show: true,
        feature: {
            restore: {show: true},
            dataView : {show: true, type: ['line', 'bar']},
            saveAsImage: {show: true},
            // dataZoom: {show: true,}
        }
    },
    calculable : true,
    xAxis : [
        {
            type: 'category',
            boundaryGap : false,
            data : %(date)s
        }
    ],
    yAxis : [
        {
            type: 'value',
            axisLabel : {
                formatter: '{value}'
            }
        }
    ],
    series : [
        {
            name : 'add',
            type:'line',
            data: %(adddata)s,
            makeLine : {
                data : [ {type: 'average', name: 'average'} ]
            },
            markPoint : {
                data : [ {type : 'max', name: 'max add per day'} ]
            },
        }, {
            name : 'del',
            type: 'line',
            data: %(deldata)s,
            makeLine : {
                data : [ {type: 'average', name: 'average'} ]
            },
            markPoint : {
                data : [ {type : 'min', name: 'max read per day'} ]
            },
        }
    ]
};
            mychart.setOption(option);
            var ecConfig = require('echarts/config');
        }
       );
    </script>
</body>
