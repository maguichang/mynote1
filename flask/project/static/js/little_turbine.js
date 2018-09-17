//查询按钮点击事件
$("#search").on('click', function(){	
	//将一般时间格式转换为时间戳
    var startTime = new Date($("#test04").val()).getTime();
    console.log("开始时间：" + startTime);
	var stopTime = new Date($("#enYMDhms").val()).getTime();
	console.log("结束时间：" + stopTime);
	var field_selection = $("#field_selection").val();
	console.log("字段：" + field_selection);
	if(stopTime <= startTime){
		alert("结束时间必须大于开始时间");
		return;
	}

	if(startTime == '' || stopTime == '' || field_selection == ''){
		alert("请选择起止时间和字段");
	}else{
		$("#main").html('');//清空原图表
		//查询数据作图
		$.ajax({
        type:'POST',
        //url:"/ +ads_analysis/{{b_time}}/{{e_time}}/1",
        url:"/ads_analysis/{{" startTime + "}}/{{" + Tistopme + "}}/{{"+ field_selection + "}}/realtime",
        dataType:"json",
        success:function (returnData){
             alert("run");
			if (returnData.status==1)
            {
                var myChart = echarts.init(document.getElementById('main'));
                option = {
                    title : {
                        text: '数据采集',
                        subtext: '实时数据',
                    },
                    tooltip : {
                        trigger: 'axis',
                        textStyle:{
							color:'#ffffff',
						}

                    },
                    legend: {
                        data:['ads_analysis1'],
                    },
                    dataZoom : {
                                    show : true,
                                    realtime : true,
                                    start :1,
                                    end : 30,
                                    bottom: 5
                                },
                    toolbox: {
                        show : true,
                        feature : {
                            mark : {show: true},
                            dataView : {show: true, readOnly: false},
                            magicType : {show: true, type: ['line', 'bar']},
                            restore : {show: true},
                            saveAsImage : {show: true}
                        },
						iconStyle:{
					        	normal:{
					        		color:'#FFDAB9',
					        		<!--borderColor:'#ffffff',-->
					        	},
					        },
                    },
                    calculable : true,
                    xAxis : [
                        {
                            type : 'category',
							axisLine:{
					            	lineStyle:
					            	{
					            		color:'#9400D3',
					            	},
					            },
                            boundaryGap : false,

                            data : returnData.datetime
                        }
                    ],
                    yAxis : [
                        {
                            type : 'value',
                            axisLabel : {
                                formatter: '{value} 值'
                            },
							axisLine:{
					            	lineStyle:
					            	{
					            		<!--color:'#9400D3',-->
					            	},
					            },
                        }
                    ],
                    series : [
                        {
                            name:'实时数据',
                            type:'line',
                            data:returnData.num,
                            markPoint : {
                                data : [
                                    {type : 'max', name: '最大值'},
                                    {type : 'min', name: '最小值'}
                                ]
                            },
                            <!--markLine : {-->
                                <!--data : [-->
                                    <!--{type : 'average', name: '平均值'}-->
                                <!--]-->
                            <!--}-->
                        }
                    ]
                };
                myChart.setOption(option);
            }
        }
        })	
	}
})
					
					
			


