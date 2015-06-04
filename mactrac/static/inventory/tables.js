$(document).ready(function() {
	$('table.display').dataTable();
	var barcode = $("#barcode").text()
	$('#barcode').barcode(barcode, "code39", {barHeight:20, fontSize:14});
});