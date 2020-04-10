var app = new Vue({
	el:'#orderitemlist',
	data:{
		formlist:[],
		itemform:'<div class="orderitem" onmouseover="overItem(this)" onmouseout="leaveItem(this)" id="1">' +
		'<div class="item" style="text-align:right"><a class="deletelink" onclick="deleteItem(this)"></a></div>' + 
		'<div class="item">&nbsp{{myorderitemform.start_time}}至{{myorderitemform.end_time}}，因{{myorderitemform.place}}{{myorderitemform.cause}}</div>' + 
		'<div class="item">1.&nbsp速度不高于{{myorderitemform.speed_limit}}，{{myorderitemform.speed_note}}</div>' +
		'<div class="item">2.&nbsp<textarea name="pattern" rows="3" class="vTextField" placeholder="行车方式变化" autoHeight="true" id="id_pattern"></textarea></div>' + 
		'<div class="item">3.&nbsp<textarea name="device" rows="3" class="vTextField" placeholder="设备变更" id="id_device"></textarea></div>' +
	'</div>'
	},
	methods:{
		onload: function(){
			this.formlist.push(this.itemform)
			console.log(this.formlist)
		},
		
		append: function(event){
			console.log(this.formlist)
			this.formlist.push(this.itemform)
		},
		
		NoToChinese: function(num) {
		    if (!/^\d*(\.\d*)?$/.test(num)) {
		        alert("Number is wrong!");
		        return "Number is wrong!";
		    }
		    var AA = new Array("零", "一", "二", "三", "四", "五", "六", "七", "八", "九");
		    var BB = new Array("", "十", "百", "千", "万", "亿", "点", "");
		    var a = ("" + num).replace(/(^0*)/g, "").split("."),
		        k = 0,
		        re = "";
		    for (var i = a[0].length - 1; i >= 0; i--) {
		        switch (k) {
		            case 0:
		                re = BB[7] + re;
		                break;
		            case 4:
		                if (!new RegExp("0{4}\\d{" + (a[0].length - i - 1) + "}$").test(a[0]))
		                    re = BB[4] + re;
		                break;
		            case 8:
		                re = BB[5] + re;
		                BB[7] = BB[5];
		                k = 0;
		                break;
		        }
		        if (k % 4 == 2 && a[0].charAt(i + 2) != 0 && a[0].charAt(i + 1) == 0) re = AA[0] + re;
		        if (a[0].charAt(i) != 0) re = AA[a[0].charAt(i)] + BB[k % 4] + re;
		        k++;
		    }
		    if (a.length > 1) //加上小数部分(如果有小数部分) 
		    {
		        re += BB[6];
		        for (var i = 0; i < a[1].length; i++) re += AA[a[1].charAt(i)];
		    }
		    return re;
		}
	}
})

app.onload()
