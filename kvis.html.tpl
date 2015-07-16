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
require(['echarts', 'echarts/chart/k'],
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
    legend : { data: ['Pocket Summary'] },
    toolbox: {
        show: true,
        feature: {
            restore: {show: true},
            dataView : {show: true, type: ['line', 'bar']},
            dataZoom: {show: true,},
            saveAsImage: {show: true},
        },
    },
    tooltip : {
        trigger: 'axis',
        formatter: function (params) {
            var res = params[0].name;
            res += '<br> start: ' + params[0].value[0] + ' add: ' + ( + params[0].value[3] - params[0].value[0]);
            res += '<br> end:   ' + params[0].value[1] + ' del: ' + ( - params[0].value[2] + params[0].value[0]);
            return res;
        }
    },
    dataZoom : {
        show : true,
        realtime : true,
        start : 0,
        end : 100,
        realtime : true,
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
            scale: true,
            axisLabel : {
                formatter: '{value}'
            }
        }
    ],
    series : [
        {
            name : 'Pocket Summary',
            type:'k',
            barMaxWidth: 20,
            itemStyle: {
                normal: {
                    color: 'red',
                    color0: 'lightgreen',
                    lineStyle: {
                        width: 2,
                        color: 'orange',
                        color0: 'green',
                    }
                },
                emphasis: {
                    color: 'black',
                    color0: 'white',
                }
            },
            data: %(kdata)s,
        }
    ]
};
            mychart.setOption(option);
            var ecConfig = require('echarts/config');
        }
       );
    </script>
</body>
