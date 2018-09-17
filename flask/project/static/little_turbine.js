alert("running");
//查询按钮点击事件
$("#search").on('click', function(){	
	//将一般时间格式转换为时间戳
    var startTime = new Date($("#test04").val()).getTime();
    console.log("开始时间：" + startTime);
    alert(startTime);
	var stopTime = new Date($("#enYMDhms").val()).getTime();
	console.log("结束时间：" + stopTime);
	alert(stopTime);
	var field_selection = $("#field_selection").val();
	console.log("字段：" + field_selection);
	alert(field_selection);
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
        //url:"/ads_analysis/{{b_time}}/{{e_time}}/1",
//        url:"/ads_analysis/{{" + startTime + "}}/{{" + stopTime + "}}/{{"+ field_selection + "}}/realtime",
        url:"http://127.0.0.1:5001/ads_analysis/data",
//        url:'{{url_for("ads_analysis/data")}}',
        dataType:"json",
        data:JSON.stringify({'start':startTime,'stop':stopTime}),
            })
        }
        })	


					
					
			


