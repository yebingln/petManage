//指定日期增加天数
function addDays(value) {
	var curDate = new Date();
	//var curDate = stringToDate('2014-08-30')
	var date = new Date(Date.parse(curDate) + (86400000 * value));
	return date.toLocaleDateString();
}

//获取option
function getGanttOption(obj) {
	//data
	var legendData = obj.legendData;
	var yAxisData = obj.yAxisData;
	var blankData = obj.blankData;
	var chaFengData = obj.chaFengData;
	var lunHouChaFengData = obj.lunHouChaFengData;
	//option
	var option = {
		tooltip: {
			trigger: 'axis',
			axisPointer: { // 坐标轴指示器，坐标轴触发有效
				type: 'cross', // 默认为直线，可选为：'line' | 'shadow' | 'cross'
				shadowStyle: {
					color: 'rgba(150,150,150,0.1)',
					width: 'auto',
					type: 'default'
				},
			},
			showDelay: 0,
			hideDelay: 50,
			backgroundColor: 'rgba(107,107,107,0.7)',
			textStyle: {
				fontFamily: '微软雅黑',
				fontSize: 13
			},
			formatter: function(params) {
				var tar;
				if (params[1].value != '-') {
					debugger
					tar = params[1];
				} else {
					tar = params[2];
				}
				//浮动信息
				return tar.data.desc;
			}
		},
		//图例
		legend: {
			itemGap: 30,
			x: 'center',
			y: 'top',
			data: legendData
		},
		grid: {
			x: 130,
			borderColor: '#EFEFEF',
		},
		//横坐标
		xAxis: [{
			name: '',
			type: 'value',
			nameLocation: 'start',
			position: 'top',
			axisTick: {
				show: true
			},
			splitArea: {
				show: true,
				areaStyle: {
					color: [
						'rgba(248,248,248,1)',
						'rgba(243,243,243,1)'
					]
				}
			},
			splitLine: {
				lineStyle: {
					color: ['#EEEEEE'],
					width: 1,
					type: 'solid'
				}
			},
			axisLabel: {
				show: true,
				formatter: function(value) {
					//横坐标 显示日期
					return addDays(value);
				}
			}
		}],
		//纵坐标
		yAxis: [{
			type: 'category',
			axisTick: {
				show: false
			},
			splitLine: {
				show: false
			},
			data: yAxisData
		}],
		//series
		series: [
			//1.blankData
			{
				name: '辅助留白',
				type: 'bar',
				barWidth: 16, //条形粗细
				stack: '总量',
				itemStyle: {
					normal: {
						barBorderColor: 'rgba(0,0,0,0)',
						color: 'rgba(0,0,0,0)'
					},
					emphasis: {
						barBorderColor: 'rgba(0,0,0,0)',
						color: 'rgba(0,0,0,0)'
					}
				},
				data: blankData
			},
			//2.chaFengData
			{
				name: '查封',
				type: 'bar',
				stack: '总量',
				itemStyle: {
					normal: {
						barBorderRadius: 5,
						color: '#6CD7D9',
						label: {
							show: true,
							position: 'right',
							formatter: function(params, ticket, callback) {
								return params.data.startDate; //条形图上的文字    
							}
						}
					},
					emphasis: {
						barBorderRadius: 5
					}
				},
				data: chaFengData,
				//虚线
				markLine: {
					itemStyle: {
						normal: {
							label: {
								show: false,
							},
						},
					},
					data: [{type: 'max', name: '自定义名字'}]
				}
			},
			//3.lunHouChaFengData
			{
				name: '轮候查封',
				type: 'bar',
				stack: '总量',
				itemStyle: {
					normal: {
						barBorderRadius: 5,
						color: '#E5CF0D',
						label: {
							show: true,
							position: 'right',
							formatter: function(params, ticket, callback) {
								return params.data.endDate;//条形图上的文字   
							}
						}
					},
					emphasis: {
						barBorderRadius: 5
					}
				},
				data: lunHouChaFengData,
			}
		]
	};
	return option;
}